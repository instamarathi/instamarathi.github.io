"""Publish due drafts from _drafts/ into blog/.

Each draft starts with a header comment:

<!--
publish: 2026-11-09
tag: mindset            (clients | mindset | content | case-studies | niche | tools)
category: Mindset & Creativity
title: Card title
summary: Card summary
-->

For every draft whose publish date is today or earlier (India time), this:
  1. moves it to blog/<same-name>.html (header removed)
  2. adds its card at the top of the blog feed in blog/index.html
  3. adds it to sitemap.xml
  4. reveals any <!--scheduled:<slug> ... --> blocks in other pages
     (use these to link to a post before it is live)
"""
import datetime as dt
import html
import pathlib
import re
import sys
import zoneinfo

ROOT = pathlib.Path(__file__).resolve().parents[2]
DRAFTS = ROOT / "_drafts"
BLOG = ROOT / "blog"
INDEX = BLOG / "index.html"
SITEMAP = ROOT / "sitemap.xml"
SITE = "https://instamarathi.github.io"
TAGS = {"clients", "mindset", "content", "case-studies", "niche", "tools"}
MONTHS = "जानेवारी फेब्रुवारी मार्च एप्रिल मे जून जुलै ऑगस्ट सप्टेंबर ऑक्टोबर नोव्हेंबर डिसेंबर".split()
HEADER = re.compile(r"\A\s*<!--(.*?)-->\s*", re.S)
FEED_OPEN = '<div class="blog-grid" id="blog-feed">\n'


def parse(path):
    text = path.read_text(encoding="utf-8")
    m = HEADER.match(text)
    if not m:
        sys.exit(f"{path.name}: missing header comment")
    meta = {}
    for line in m.group(1).strip().splitlines():
        key, _, val = line.partition(":")
        meta[key.strip()] = val.strip()
    for key in ("publish", "tag", "category", "title", "summary"):
        if not meta.get(key):
            sys.exit(f"{path.name}: header is missing '{key}'")
    if meta["tag"] not in TAGS:
        sys.exit(f"{path.name}: tag must be one of {sorted(TAGS)}")
    meta["date"] = dt.date.fromisoformat(meta["publish"])
    return meta, text[m.end():]


def card(slug, meta):
    d = meta["date"]
    esc = lambda s: html.escape(s, quote=False)
    return (
        f'      <a href="/blog/{slug}.html" class="blog-card" data-tag="{meta["tag"]}" data-date="{d.isoformat()}">\n'
        f'        <span class="blog-category">{esc(meta["category"])}</span>\n'
        f'        <div class="blog-meta"><time datetime="{d.isoformat()}">{d.day} {MONTHS[d.month - 1]} {d.year}</time></div>\n'
        f'        <h3>{esc(meta["title"])}</h3>\n'
        f'        <p>{esc(meta["summary"])}</p>\n'
        f'      </a>\n'
    )


def main():
    today = dt.datetime.now(zoneinfo.ZoneInfo("Asia/Kolkata")).date()
    drafts = sorted(DRAFTS.glob("*.html")) if DRAFTS.exists() else []
    due = []
    for path in drafts:
        meta, body = parse(path)  # validates every draft, not just due ones
        status = "due" if meta["date"] <= today else f"waiting for {meta['date']}"
        print(f"{path.name}: {status}")
        if meta["date"] <= today:
            due.append((path, meta, body))
    if not due:
        print("Nothing to publish.")
        return

    index = INDEX.read_text(encoding="utf-8")
    sitemap = SITEMAP.read_text(encoding="utf-8")
    for path, meta, body in sorted(due, key=lambda x: x[1]["date"]):
        slug = path.stem
        target = BLOG / path.name
        if target.exists():
            sys.exit(f"{target} already exists; refusing to overwrite")
        target.write_text(body, encoding="utf-8")
        path.unlink()
        if f'href="/blog/{slug}.html" class="blog-card"' not in index:
            index = index.replace(FEED_OPEN, FEED_OPEN + card(slug, meta), 1)
        url = f"{SITE}/blog/{slug}.html"
        if url not in sitemap:
            sitemap = sitemap.replace(
                "</urlset>",
                f"  <url><loc>{url}</loc><lastmod>{meta['date'].isoformat()}</lastmod></url>\n</urlset>",
            )
        block = re.compile(rf"<!--scheduled:{re.escape(slug)}\s*(.*?)\s*-->", re.S)
        for page in ROOT.rglob("*.html"):
            if "_drafts" in page.parts or ".git" in page.parts:
                continue
            text = page.read_text(encoding="utf-8")
            new = block.sub(lambda m: m.group(1), text)
            if new != text:
                page.write_text(new, encoding="utf-8")
                print(f"  revealed link in {page.relative_to(ROOT)}")
        print(f"Published {slug}")
    if FEED_OPEN not in index:
        sys.exit("blog feed marker not found in blog/index.html")
    INDEX.write_text(index, encoding="utf-8")
    SITEMAP.write_text(sitemap, encoding="utf-8")


if __name__ == "__main__":
    main()
