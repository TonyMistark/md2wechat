#!/usr/bin/env python3
"""Convert Markdown files to WeChat-compatible HTML with inline CSS."""

import argparse
import sys
from pathlib import Path

import css_inline
import markdown
from pygments.formatters import HtmlFormatter

from md2wechat.styles import DEFAULT_STYLE, get_style, list_styles

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
{css}
</style>
</head>
<body>
{content}
</body>
</html>
"""


def convert_md_to_wechat(
    md_path: str, output_path: str | None = None, style_name: str = DEFAULT_STYLE,
) -> str:
    md_file = Path(md_path)
    if not md_file.exists():
        print(f"Error: File not found: {md_path}")
        sys.exit(1)

    style = get_style(style_name)
    pygments_css = HtmlFormatter(style=style.PYGMENTS_STYLE).get_style_defs(".codehilite")
    full_css = style.CSS_STYLES + "\n" + pygments_css

    md_text = md_file.read_text(encoding="utf-8")

    title = md_file.stem
    for line in md_text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            break

    md_content = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "toc", "codehilite"],
        extension_configs={
            "codehilite": {
                "guess_lang": False,
                "use_pygments": True,
                "noclasses": False,
            }
        },
    )

    html = HTML_TEMPLATE.format(title=title, css=full_css, content=md_content)

    inliner = css_inline.CSSInliner()
    html_inlined = inliner.inline(html)

    if output_path is None:
        output_path = str(md_file.with_suffix(".html"))

    Path(output_path).write_text(html_inlined, encoding="utf-8")

    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert Markdown to WeChat-compatible HTML",
    )
    parser.add_argument("input", help="Input Markdown file path")
    parser.add_argument(
        "-o", "--output",
        help="Output HTML file path (default: same name with .html extension)",
    )
    parser.add_argument(
        "-s", "--style",
        default=DEFAULT_STYLE,
        choices=[n for n, _ in list_styles()],
        help=f"Output style theme (default: {DEFAULT_STYLE})",
    )

    args = parser.parse_args()
    output = convert_md_to_wechat(args.input, args.output, style_name=args.style)
    print(f"Converted: {args.input} -> {output}")


if __name__ == "__main__":
    main()
