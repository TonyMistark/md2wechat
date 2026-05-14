NAME = "github"
DESCRIPTION = "GitHub-flavored markdown theme"
PYGMENTS_STYLE = "default"

CSS_STYLES = """
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans",
                 Helvetica, Arial, sans-serif;
    font-size: 16px;
    line-height: 1.6;
    color: #1f2328;
    padding: 20px 16px;
    word-wrap: break-word;
    overflow-wrap: break-word;
    background-color: #ffffff;
}

h1 {
    font-size: 2em;
    font-weight: 600;
    color: #1f2328;
    margin: 24px 0 16px;
    padding-bottom: 0.3em;
    border-bottom: 1px solid #d0d7de;
    line-height: 1.25;
}

h2 {
    font-size: 1.5em;
    font-weight: 600;
    color: #1f2328;
    margin: 24px 0 16px;
    padding-bottom: 0.3em;
    border-bottom: 1px solid #d0d7de;
    line-height: 1.25;
}

h3 {
    font-size: 1.25em;
    font-weight: 600;
    color: #1f2328;
    margin: 24px 0 16px;
    line-height: 1.25;
}

h4 {
    font-size: 1em;
    font-weight: 600;
    color: #1f2328;
    margin: 24px 0 16px;
    line-height: 1.25;
}

p {
    margin: 0 0 16px;
}

strong {
    font-weight: 600;
    color: #1f2328;
}

em {
    font-style: italic;
    color: #1f2328;
}

a {
    color: #0969da;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

ul, ol {
    padding-left: 2em;
    margin: 0 0 16px;
}

li {
    margin: 4px 0;
    line-height: 1.6;
}

blockquote {
    margin: 0 0 16px;
    padding: 0 1em;
    border-left: 4px solid #d0d7de;
    color: #656d76;
}

code {
    font-family: "SF Mono", Menlo, Monaco, Consolas, "Courier New", monospace;
    font-size: 0.875em;
    background-color: #f6f8fa;
    padding: 2px 6px;
    border-radius: 6px;
    color: #1f2328;
}

pre {
    margin: 0 0 16px;
    padding: 16px;
    background-color: #f6f8fa;
    border-radius: 6px;
    overflow-x: auto;
    font-size: 0.85em;
    line-height: 1.45;
}

pre code {
    background: none;
    padding: 0;
    color: #1f2328;
    font-size: inherit;
}

img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 8px auto;
    border-radius: 6px;
}

hr {
    border: none;
    border-top: 1px solid #d0d7de;
    margin: 24px 0;
    height: 1px;
    padding: 0;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 0 0 16px;
    font-size: 14px;
}

th, td {
    border: 1px solid #d0d7de;
    padding: 6px 13px;
    text-align: left;
}

th {
    background-color: #f6f8fa;
    font-weight: 600;
    color: #1f2328;
}

tr:nth-child(even) {
    background-color: #f6f8fa;
}
"""
