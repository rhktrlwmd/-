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
assets=()
for lab in labs/lab*; do
  assets+=(
    "$lab/report/report.docx"
    "$lab/report/report.pdf"
    "$lab/presentation/presentation.html"
    "$lab/presentation/presentation.pdf"
    "$lab/presentation/presentation.md"
    "$lab/report/report.md"
    "$lab/release/"*.zip
  )
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
