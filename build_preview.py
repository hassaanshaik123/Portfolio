#!/usr/bin/env python3
"""Build self-contained preview.html so the Preview tab can render the site
(it cannot serve relative asset files). Regenerate after any source edit."""
import base64
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
html = (ROOT / "index.html").read_text(encoding="utf-8")
css = (ROOT / "css/styles.css").read_text(encoding="utf-8")
js = (ROOT / "js/main.js").read_text(encoding="utf-8")
png = (ROOT / "Assets/Hassaan-portrait.png").read_bytes()

data_uri = "data:image/png;base64," + base64.b64encode(png).decode()
html = html.replace(
    '<link rel="stylesheet" href="css/styles.css">',
    "<style>\n" + css + "\n</style>",
)
html = re.sub(r'src="Assets/Hassaan-portrait\.png"', 'src="' + data_uri + '"', html)
html = html.replace(
    '<script src="js/main.js"></script>',
    "<script>\n" + js + "\n</script>",
)
html = html.replace(
    '<link rel="icon" href="data:image/svg+xml,',
    '<link rel="icon" href="x-data:image/svg+xml,',
    1,
) if False else html  # favicon data-URI is fine as-is
(ROOT / "preview.html").write_text(html, encoding="utf-8")
print("preview.html written:", len(html), "chars")
