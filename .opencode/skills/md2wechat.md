---
name: md2wechat
description: Convert Markdown files to WeChat-compatible HTML with inline CSS. Use this skill when the user wants to convert a Markdown article to HTML suitable for publishing on WeChat Official Account (微信公众号).
---

# md2wechat

Convert Markdown to WeChat-compatible HTML with inline CSS styles.

## When to use

- User wants to publish a Markdown article on WeChat Official Account
- User needs to convert `.md` files to WeChat-compatible HTML
- User asks about WeChat article formatting or 微信公众号排版

## How it works

1. Parses Markdown with GFM extensions (tables, fenced code blocks, TOC, syntax highlighting)
2. Applies a CSS theme (`default` WeChat green or `github` style)
3. Inlines all CSS via css-inline (Rust) — essential because WeChat strips `<style>` tags
4. Outputs a self-contained HTML file ready to paste into WeChat editor

## Usage

```bash
md2wechat input.md                     # default style, output to input.html
md2wechat input.md -o output.html      # custom output path
md2wechat input.md -s github           # GitHub-themed style
md2wechat --help                       # see all options
```

Run the command, then copy the HTML content into WeChat's article editor.
