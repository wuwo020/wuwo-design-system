#!/bin/bash
# wuwo-design-system — 列出本 skill 的可用资产（组件包 / 参考层 / 模板）
# 用法：bash scripts/list-assets.sh
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "组件包 (bundles/)"
for d in "$ROOT"/bundles/*/; do
  [ -d "$d" ] || continue
  echo "  - $(basename "$d")  $(head -1 "$d/README.md" 2>/dev/null | sed 's/^# *//')"
done

echo
echo "参考层 (references/)"
for f in "$ROOT"/references/*.md; do
  printf '  - %-26s %s\n' "$(basename "$f")" "$(grep -m1 '^#' "$f" | sed 's/^# *//')"
done
for d in "$ROOT"/references/*/; do
  [ -d "$d" ] || continue
  printf '  - %-26s %s\n' "$(basename "$d")/" "$(ls "$d" | wc -l) 个文件"
done

echo
echo "模板 (templates/)"
for d in "$ROOT"/templates/*/; do
  [ -d "$d" ] || continue
  printf '  - %-26s %s\n' "$(basename "$d")/" "$(ls "$d" | head -3 | tr '\n' ' ')"
done
