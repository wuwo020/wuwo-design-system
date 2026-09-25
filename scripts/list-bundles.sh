#!/bin/bash
# ui-component-bundles - List available UI component bundles
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUNDLES_DIR="$SCRIPT_DIR/bundles"

if [ ! -d "$BUNDLES_DIR" ]; then
  echo "Error: Bundles directory not found"
  exit 1
fi

echo "🎨 Available UI Component Bundles"
echo "================================"
echo ""

for bundle in "$BUNDLES_DIR"/*; do
  if [ -d "$bundle" ]; then
    name=$(basename "$bundle")
    # Try to get description from README or SKILL.md
    desc=""
    for f in "$bundle/README.md" "$bundle/SKILL.md" "$bundle/README"; do
      if [ -f "$f" ]; then
        desc=$(head -5 "$f" | grep -v '^#' | sed 's/^[-*] //') || desc="No description available"
        break
      fi
    done
    echo "  📦 $name"
    echo "     ${desc}"
    echo ""
  fi
done

echo "Usage:!"bundle <bundle-name>" to view details of a specific bundle"
echo "Example: !bundle landing-kit"
