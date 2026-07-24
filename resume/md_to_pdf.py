#!/usr/bin/env python3
"""Minimal, dependency-free Markdown -> styled HTML -> PDF (via headless Chrome).
Tailored to the resume Markdown structure. Leaves .md files untouched."""
import html
import re
import subprocess
import sys
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Simple Icons monochrome paths (24x24 viewBox); rendered as clickable inline SVG.
ICONS = {
    "github": '<path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/>',
    "linkedin": '<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>',
    "scholar": '<path d="M5.242 13.769L0 9.5 12 0l12 9.5-5.242 4.269C17.548 11.249 14.978 9.5 12 9.5c-2.977 0-5.548 1.748-6.758 4.269zM12 10a7 7 0 1 0 0 14 7 7 0 0 0 0-14z"/>',
}

CSS = """
@page { size: Letter; margin: 0.38in 0.5in; }
* { box-sizing: border-box; }
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 9.15pt; line-height: 1.24; color: #1a1a1a; margin: 0;
  -webkit-print-color-adjust: exact;
}
h1 { font-size: 20pt; margin: 0 0 1px 0; letter-spacing: 0.3px; }
.subtitle { font-size: 10.5pt; font-weight: 600; color: #333; margin: 0 0 2px 0; }
.contact { font-size: 8.6pt; color: #444; margin: 0 0 4px 0; }
.contact a { color: #1155cc; text-decoration: none; }
.contact a.icon { vertical-align: -2px; margin: 0 1px; }
.contact a.icon svg { width: 11px; height: 11px; fill: #333; }
h2 {
  font-size: 10.5pt; text-transform: uppercase; letter-spacing: 0.6px;
  color: #111; border-bottom: 1.1px solid #999;
  padding-bottom: 1px; margin: 7px 0 3px 0;
}
h2 .note { text-transform: none; letter-spacing: 0; font-weight: 400; font-size: 8pt; color: #666; }
p { margin: 1px 0 2px 0; }
.role { margin: 4px 0 1px 0; font-size: 9.5pt; }
ul { margin: 1px 0 3px 0; padding-left: 15px; }
li { margin: 0 0 1.5px 0; }
a { color: #1155cc; text-decoration: none; }
strong { font-weight: 700; }
em { color: #555; }
hr { border: none; margin: 0; }
"""


def _icon(m):
    name, url = m.group(1), m.group(2)
    svg = ICONS.get(name, "")
    return (f'<a class="icon" href="{url}" title="{name}">'
            f'<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">{svg}</svg></a>')


def inline(t: str) -> str:
    t = html.escape(t)
    # protect backslash-escaped chars (e.g. \* equal-contribution markers)
    t = re.sub(r"\\(.)", lambda m: f"\x00{ord(m.group(1))}\x00", t)
    # icon tokens {{icon:name|url}} (before other markup)
    t = re.sub(r"\{\{icon:([a-z]+)\|([^}]+)\}\}", _icon, t)
    # links [text](url)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    # bold then italic
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", t)
    # restore escaped chars as literals
    t = re.sub(r"\x00(\d+)\x00", lambda m: chr(int(m.group(1))), t)
    return t


def convert(md: str) -> str:
    lines = md.split("\n")
    out, in_list = [], False
    # header block: first h1 + following bold subtitle + contact line
    i = 0
    n = len(lines)

    def close_list():
        nonlocal in_list
        if in_list:
            out.append("</ul>")
            in_list = False

    # Title
    while i < n and not lines[i].startswith("# "):
        i += 1
    if i < n:
        out.append(f"<h1>{inline(lines[i][2:].strip())}</h1>")
        i += 1
    # subtitle + contact: next two non-empty non-hr lines
    header_lines = []
    while i < n and len(header_lines) < 2:
        s = lines[i].strip()
        i += 1
        if not s or s == "---":
            if s == "---":
                break
            continue
        header_lines.append(s)
    if header_lines:
        out.append(f'<div class="subtitle">{inline(header_lines[0].strip("*"))}</div>')
    if len(header_lines) > 1:
        out.append(f'<div class="contact">{inline(header_lines[1])}</div>')

    for line in lines[i:]:
        s = line.rstrip()
        st = s.strip()
        if st == "---" or st == "":
            close_list()
            continue
        if st.startswith("### "):
            close_list()
            out.append(f'<p class="role"><strong>{inline(st[4:].strip())}</strong></p>')
            continue
        if st.startswith("## "):
            close_list()
            # split trailing italic note like *(full list: ...)*
            body = st[3:].strip()
            m = re.search(r"\*\(([^)]*)\)\*\s*$", body)
            if m:
                head = body[: m.start()].strip()
                note = m.group(1)
                out.append(f'<h2>{inline(head)} <span class="note">({inline(note)})</span></h2>')
            else:
                out.append(f"<h2>{inline(body)}</h2>")
            continue
        if st.startswith("- "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(st[2:])}</li>")
            continue
        # bold role/company line or plain paragraph
        close_list()
        cls = ' class="role"' if st.startswith("**") else ""
        out.append(f"<p{cls}>{inline(st)}</p>")
    close_list()

    return (
        "<!doctype html><html><head><meta charset='utf-8'>"
        f"<style>{CSS}</style></head><body>" + "\n".join(out) + "</body></html>"
    )


def main():
    for md_path in sys.argv[1:]:
        p = Path(md_path)
        htmlp = p.with_suffix(".html")
        pdfp = p.with_suffix(".pdf")
        htmlp.write_text(convert(p.read_text()), encoding="utf-8")
        subprocess.run(
            [CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
             f"--print-to-pdf={pdfp}", htmlp.resolve().as_uri()],
            check=True, capture_output=True,
        )
        print(f"{p.name} -> {pdfp.name}")
        htmlp.unlink()  # keep only .md and .pdf


if __name__ == "__main__":
    main()
