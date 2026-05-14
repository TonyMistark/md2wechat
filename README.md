# md2wechat

[中文](README.zh-CN.md)

Convert Markdown files to WeChat Official Account (微信公众号) compatible HTML, with CSS inlining so styles survive WeChat's editor.

## Features

- GFM extensions: tables, fenced code blocks, TOC
- **Syntax highlighting** via Pygments (500+ languages)
- **Style themes**: `default` (WeChat green) and `github` — switch with `-s`
- **CSS inlining** via css-inline (Rust) — WeChat strips `<style>` tags, only inline styles work
- Auto-extracts first H1 as page title
- Responsive images, code block horizontal scroll, zebra-striped tables

## Requirements

Python >= 3.12. Uses [uv](https://docs.astral.sh/uv/) for dependency management.

## Installation

### Install as a global CLI tool

```bash
uv tool install git+https://github.com/liuliqiu/md2wechat
# or from a local clone:
uv tool install .
```

After install, `md2wechat` is available anywhere:

```bash
md2wechat input.md
md2wechat input.md -o output.html -s github
```

### Install for development

```bash
git clone https://github.com/liuliqiu/md2wechat
cd md2wechat
uv sync
uv pip install -e .
```

## CLI usage

```bash
md2wechat input.md                 # default style → input.html
md2wechat input.md -o output.html  # custom output path
md2wechat input.md -s github       # GitHub theme
md2wechat --help                   # list all options
```

## Claude Code skill

Claude Code custom skills are defined as markdown files in `.claude/skills/` (project) or `~/.claude/skills/` (global). This repo includes the skill file at `.claude/skills/md2wechat.md`.

### Setup

**If you cloned the repo**, the skill is ready automatically — just open this directory as a Claude Code workspace.

**If you installed via `uv tool install`**, download the skill file separately:

```bash
mkdir -p ~/.claude/skills
curl -o ~/.claude/skills/md2wechat.md \
  https://raw.githubusercontent.com/liuliqiu/md2wechat/main/.claude/skills/md2wechat.md
```

Then restart Claude Code, and `/md2wechat` will be available in all projects:

```
/md2wechat article.md
```

Claude will run `md2wechat` with the right arguments based on context.

## OpenCode skill

The skill definition lives in `.opencode/skills/md2wechat.md`. OpenCode picks it up automatically when this project is opened as workspace.

### Setup

1. Install `md2wechat` as a global tool (see Installation above)

2. Open this project in OpenCode — the skill registers automatically

3. Ask Claude to convert:

> Convert this markdown article to WeChat HTML

Claude will run `md2wechat` with the right arguments based on context.

## How it works

```
Markdown file
    │
    ▼
Read UTF-8 text → Extract title (first H1 or filename)
    │
    ▼
markdown.markdown() → tables, fenced_code, codehilite, TOC
    │
    ▼
Embed HTML template → <style> with full CSS + Pygments theme
    │
    ▼
css_inline.CSSInliner() → CSS rules → inline style="" attributes
    │
    ▼
WeChat-compatible HTML file
```

WeChat's article editor strips `<style>` tags and external stylesheets — only inline styles survive, so CSS inlining is the critical step.

## Project structure

```
├── md2wechat/
│   ├── __init__.py       # package entry, re-exports CLI
│   ├── cli.py            # CLI + conversion logic
│   └── styles/
│       ├── __init__.py   # style registry
│       ├── default.py    # WeChat green theme
│       └── github.py     # GitHub theme
├── .claude/
│   └── skills/
│       └── md2wechat.md  # Claude Code skill definition
├── .opencode/
│   └── skills/
│       └── md2wechat.md  # OpenCode skill definition
├── pyproject.toml
└── uv.lock
```

## Dependencies

| Package | Role |
|---------|------|
| [markdown](https://python-markdown.github.io/) | Markdown → HTML (tables, fenced_code, codehilite, toc) |
| [css-inline](https://github.com/Stranger6667/css-inline) | Rust-powered CSS inlining |
| [pygments](https://pygments.org/) | Syntax highlighting (via codehilite) |
