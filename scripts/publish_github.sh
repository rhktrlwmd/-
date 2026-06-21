#!/bin/zsh
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

echo "Checking GitHub auth..."
gh auth status

echo "Pushing branch..."
git push -u origin main --force-with-lease

echo "Pushing tag..."
git push origin v1.0.0

echo "Collecting release assets..."
tmpdir="$(mktemp -d)"
trap 'rm -rf "$tmpdir"' EXIT
assets=()
for lab in labs/lab*; do
  lab_name="$(basename "$lab")"
  cp "$lab/report/report.docx" "$tmpdir/${lab_name}-report.docx"
  cp "$lab/report/report.pdf" "$tmpdir/${lab_name}-report.pdf"
  cp "$lab/report/report.md" "$tmpdir/${lab_name}-report.md"
  cp "$lab/presentation/presentation.html" "$tmpdir/${lab_name}-presentation.html"
  cp "$lab/presentation/presentation.pdf" "$tmpdir/${lab_name}-presentation.pdf"
  cp "$lab/presentation/presentation.md" "$tmpdir/${lab_name}-presentation.md"
  cp "$lab/release/"*.zip "$tmpdir/"
done
for asset in "$tmpdir"/*; do
  assets+=("$asset")
done

echo "Creating or updating release..."
if gh release view v1.0.0 >/dev/null 2>&1; then
  gh release upload v1.0.0 "${assets[@]}" --clobber
else
  gh release create v1.0.0 "${assets[@]}" \
    --title "v1.0.0" \
    --notes "Первичная публикация лабораторных работ и презентаций по курсу 'Имитационное моделирование'."
fi

echo "Done."
