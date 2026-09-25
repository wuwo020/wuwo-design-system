#!/usr/bin/env python3
"""双端验收截图 + 基础检查（手机网页 / PC 网页）

用法：
    python3 scripts/dual-screenshot.py <文件或URL> [输出目录]

做四件事：
  1. 手机 390×844（isMobile / hasTouch / dpr3）与 PC 1440×900 各截 4 张（0% / 30% / 60% / 90% 滚动位置）
  2. 收集 console 错误与页面异常（JS 报错、资源 404）
  3. 检查横向溢出（scrollWidth > innerWidth 是手机网页最常见事故）
  4. 打印每张截图路径，供人眼复核（不允许只靠几何断言交付）

依赖：playwright（本机已装 chromium）。国内访问 CDN 时先 export https_proxy。
"""
import asyncio, json, pathlib, sys
from playwright.async_api import async_playwright

MOBILE = {"viewport": {"width": 390, "height": 844}, "device_scale_factor": 3,
          "is_mobile": True, "has_touch": True}
DESKTOP = {"viewport": {"width": 1440, "height": 900}, "device_scale_factor": 1}
CHECKPOINTS = [0.0, 0.33, 0.66, 1.0]   # 100% 必须看：底边安全区/页脚常出事故


async def run(target: str, outdir: pathlib.Path):
    outdir.mkdir(parents=True, exist_ok=True)
    url = target if target.startswith("http") else pathlib.Path(target).resolve().as_uri()
    report = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=["--no-sandbox", "--font-render-hinting=none"])
        for name, dev in (("mobile", MOBILE), ("pc", DESKTOP)):
            ctx = await browser.new_context(**dev)
            page = await ctx.new_page()
            errors, failed = [], []
            page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.on("requestfailed", lambda r: failed.append(f"{r.url} {r.failure}"))
            await page.goto(url, wait_until="domcontentloaded")
            try:                                                    # 等 CDN 脚本（挂了不算失败）
                await page.wait_for_function("typeof window.gsap !== 'undefined'", timeout=8000)
            except Exception:
                pass
            await page.wait_for_timeout(900)
            has_gsap = await page.evaluate("typeof window.gsap !== 'undefined'")
            rail_ok = await page.evaluate(
                "() => { const el=document.querySelector('.gallery-rail');"
                "return el ? el.scrollWidth > el.clientWidth : null; }")
            shots = []
            for i, frac in enumerate(CHECKPOINTS):
                await page.evaluate("f => window.scrollTo(0, (document.body.scrollHeight - innerHeight) * f)",
                                    frac)
                await page.wait_for_timeout(700)
                overflow = await page.evaluate(
                    "() => document.documentElement.scrollWidth - window.innerWidth")
                path = outdir / f"{name}-{i}-{int(frac*100)}.png"
                await page.screenshot(path=str(path))
                shots.append({"at": f"{int(frac*100)}%", "file": str(path), "overflow_px": overflow})
                # 手机端：验证横向画廊可横滑（拇指天然手势）
            report[name] = {"gsap_loaded": has_gsap, "gallery_overflows": rail_ok,
                            "console_errors": errors, "failed_requests": failed, "shots": shots}
            await ctx.close()
        await browser.close()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    bad = [f"{k}:{s['at']} +{s['overflow_px']}px" for k, v in report.items()
           for s in v["shots"] if s["overflow_px"] > 1]
    if bad:
        print("\n!! 横向溢出（必须修）:", ", ".join(bad))
    for k, v in report.items():
        if v["console_errors"]:
            print(f"!! {k} console 错误:", v["console_errors"][:5])
        if v["failed_requests"]:
            print(f":: {k} 资源失败:", v["failed_requests"][:5])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    target = sys.argv[1]
    out = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else pathlib.Path("shots")
    asyncio.run(run(target, out))
