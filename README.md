# md2wechat

将 Markdown 文件转换为微信公众号兼容的 HTML，通过 CSS inlining 确保样式在微信中正常显示。

## 特性

- 支持表格、围栏代码块、目录等 GFM 扩展语法
- **代码语法高亮**，基于 Pygments，支持 Python、JavaScript 等 500+ 语言
- **多种样式主题**：`default`（微信绿）和 `github`（GitHub 风格），通过 `-s` 参数切换
- 自动将 `<style>` 标签中的 CSS 内联为 `style=""` 属性，兼容微信文章编辑器
- 自动提取第一个一级标题作为页面标题
- 响应式图片、代码块横向滚动、表格斑马条纹

## 安装

需要 Python >= 3.12，使用 [uv](https://docs.astral.sh/uv/) 管理依赖：

```bash
uv sync
```

## 使用方法

```bash
# 基础用法，默认使用 default 样式
uv run python main.py input.md

# 指定输出路径
uv run python main.py input.md -o output.html

# 使用 GitHub 风格样式
uv run python main.py input.md -s github

# 查看可用样式
uv run python main.py --help
```

## 工作流程

```
Markdown 文件
    │
    ▼
读取 UTF-8 文本 → 提取标题（首个 H1 或文件名）
    │
    ▼
markdown.markdown() 转换 → 表格 + 代码块 + 代码高亮 + 目录
    │
    ▼
嵌入 HTML 模板 → <style> 包含完整 CSS
    │
    ▼
css_inline.CSSInliner() → CSS 规则转为内联 style="" 属性
    │
    ▼
输出 WeChat 兼容的 HTML 文件
```

微信文章编辑器会丢弃 `<style>` 标签和外部样式表，只有内联样式才能生效，因此 CSS inlining 是核心步骤。

## 项目结构

```
├── main.py           # 主程序（CLI + 转换逻辑）
├── styles/           # 样式主题包
│   ├── __init__.py   # 样式注册表
│   ├── default.py    # 微信绿色主题
│   └── github.py     # GitHub 风格主题
├── pyproject.toml    # 项目配置与依赖声明
└── uv.lock           # 锁定依赖版本
```

## 依赖

| 依赖 | 说明 |
|------|------|
| [markdown](https://python-markdown.github.io/) | Markdown 转 HTML，启用 tables / fenced_code / codehilite / toc 扩展 |
| [css-inline](https://github.com/Stranger6667/css-inline) | 基于 Rust 的 CSS 内联引擎 |
| [pygments](https://pygments.org/) | 代码语法高亮，通过 codehilite 扩展集成 |

## 未来规划

- 支持加载外部 CSS 文件作为自定义样式

