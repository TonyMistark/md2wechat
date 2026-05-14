---
name: md2wechat
description: Convert Markdown files to WeChat-compatible HTML with inline CSS
---

# md2wechat

Convert Markdown files to WeChat Official Account (微信公众号) compatible HTML.

## Usage

When the user asks to convert a Markdown file to WeChat HTML, run the `md2wechat` CLI tool:

```bash
md2wechat <input.md>              # default style → input.html
md2wechat <input.md> -o <output>  # custom output path
md2wechat <input.md> -s github    # GitHub theme
```

- `-s default` — WeChat green accent theme
- `-s github` — GitHub-flavored markdown theme

The tool inlines all CSS automatically so the output works in WeChat's article editor.