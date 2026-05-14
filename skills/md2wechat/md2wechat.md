---
name: md2wechat
description: Convert Markdown files to WeChat-compatible HTML with inline CSS. Use when the user wants to convert Markdown articles for WeChat Official Account (微信公众号).
---

# md2wechat

Convert Markdown to WeChat Official Account compatible HTML.

## How it works

1. Parses Markdown with GFM extensions (tables, fenced code blocks, TOC, syntax highlighting)
2. Applies a CSS theme (`default` WeChat green or `github` style)
3. Inlines all CSS via css-inline (Rust) — WeChat strips `<style>` tags
4. Outputs self-contained HTML ready to paste into WeChat article editor

## Usage

Run the CLI tool directly:

```bash
md2wechat input.md                     # default style → input.html
md2wechat input.md -o output.html      # custom output path
md2wechat input.md -s github           # GitHub-themed style
```

- `-s default` — WeChat green accent theme
- `-s github` — GitHub-flavored markdown theme