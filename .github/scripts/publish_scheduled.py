"""Publish due drafts from _drafts/ into blog/.

Each draft starts with a header comment:

<!--
publish: 2026-11-09        (goes live at 9:00 AM India time; or add a time: 2026-11-09 18:30)
tag: mindset            (clients | mindset | content | case-studies | niche | tools)
category: Mindset & Creativity
title: Card title
summary: Card summary
path: marketing/seo.html   (optional; where the page goes. Default: blog/<same-name>.html)
card: no                   (optional; "no" = don't add a card to the blog feed)
-->

The job runs every hour. A draft goes live on the first run after its publish
time (India time). This:
  1. moves it to blog/<same-name>.html, or to `path:` if given (header removed)
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
IST = zoneinfo.ZoneInfo("Asia/Kolkata")
DEFAULT_TIME = dt.time(9, 0)
TAGS = {"clients", "mindset", "content", "case-studies", "niche", "tools", "marketing"}
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
    day, _, clock = meta["publish"].partition(" ")
    try:
        meta["date"] = dt.date.fromisoformat(day)
        at = dt.time.fromisoformat(clock.strip()) if clock.strip() else DEFAULT_TIME
    except ValueError:
        sys.exit(f"{path.name}: publish must look like 2026-11-09 or 2026-11-09 18:30")
    meta["at"] = dt.datetime.combine(meta["date"], at, IST)
    rel = meta.get("path") or f"blog/{path.name}"
    if rel.startswith("/") or ".." in rel or not rel.endswith(".html"):
        sys.exit(f"{path.name}: path must be relative like marketing/seo.html")
    meta["rel"] = rel
    meta["href"] = "/" + (rel[: -len("index.html")] if rel.endswith("index.html") else rel)
    meta["card"] = meta.get("card", "yes").lower() != "no"
    return meta, text[m.end():]


def card(slug, meta):
    d = meta["date"]
    esc = lambda s: html.escape(s, quote=False)
    return (
        f'      <a href="{meta["href"]}" class="blog-card" data-tag="{meta["tag"]}" data-date="{d.isoformat()}">\n'
        f'        <span class="blog-category">{esc(meta["category"])}</span>\n'
        f'        <div class="blog-meta"><time datetime="{d.isoformat()}">{d.day} {MONTHS[d.month - 1]} {d.year}</time></div>\n'
        f'        <h3>{esc(meta["title"])}</h3>\n'
        f'        <p>{esc(meta["summary"])}</p>\n'
        f'      </a>\n'
    )


def main():
    now = dt.datetime.now(IST)
    drafts = sorted(DRAFTS.glob("*.html")) if DRAFTS.exists() else []
    due = []
    for path in drafts:
        meta, body = parse(path)  # validates every draft, not just due ones
        due_now = meta["at"] <= now
        print(f"{path.name}: {'due' if due_now else 'waiting for ' + meta['at'].strftime('%Y-%m-%d %H:%M IST')}")
        if due_now:
            due.append((path, meta, body))
    if not due:
        print("Nothing to publish.")
        return

    index = INDEX.read_text(encoding="utf-8")
    sitemap = SITEMAP.read_text(encoding="utf-8")
    published = []
    for path, meta, body in sorted(due, key=lambda x: x[1]["at"]):
        slug = path.stem
        target = ROOT / meta["rel"]
        if target.exists():
            sys.exit(f"{target} already exists; refusing to overwrite")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body, encoding="utf-8")
        path.unlink()
        if meta["card"] and f'href="{meta["href"]}" class="blog-card"' not in index:
            index = index.replace(FEED_OPEN, FEED_OPEN + card(slug, meta), 1)
        url = SITE + meta["href"]
        if f"<loc>{url}</loc>" not in sitemap:
            sitemap = sitemap.replace(
                "</urlset>",
                f"  <url><loc>{url}</loc><lastmod>{meta['date'].isoformat()}</lastmod></url>\n</urlset>",
            )
        published.append(slug)
        print(f"Published {slug} -> {meta['rel']}")
    if FEED_OPEN not in index:
        sys.exit("blog feed marker not found in blog/index.html")
    INDEX.write_text(index, encoding="utf-8")
    SITEMAP.write_text(sitemap, encoding="utf-8")
    # Reveal links only after every due page is written, so pages published
    # in the same run (e.g. a section index and its first lesson) see each other.
    pages = [p for p in ROOT.rglob("*.html") if "_drafts" not in p.parts and ".git" not in p.parts]
    for slug in published:
        block = re.compile(rf"<!--scheduled:{re.escape(slug)}\s*(.*?)\s*-->", re.S)
        for page in pages:
            text = page.read_text(encoding="utf-8")
            new = block.sub(lambda m: m.group(1), text)
            if new != text:
                page.write_text(new, encoding="utf-8")
                print(f"  revealed {slug} link in {page.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
