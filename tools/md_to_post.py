#!/usr/bin/env python3
"""Convert one clean digest markdown file into a Jekyll post for the public site.

Usage:
  python tools/md_to_post.py --src <digest.md> --date YYYY-MM-DD --slug <slug> [--title "..."]

Transforms each item block
    **Headline**
    description
    https://url · source · date
into a clickable post line
    **[Headline](url)**
    description
    *source · date*
and writes _posts/<date>-<slug>.md with Jekyll front matter.

IMPORTANT: only ever point this at the CLEAN reader digest (the same content that was
emailed). Never at outbox receipts, run-logs, or anything containing an email address.
"""
import re, os, argparse

POSTS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_posts")
URL = re.compile(r'^(https?://\S+)(.*)$')

def transform(raw_text):
    lines = raw_text.split('\n')
    # drop everything up to and including the first '# ' title line
    while lines and not lines[0].startswith('# '):
        lines.pop(0)
    if lines:
        lines.pop(0)
    text = "\n".join(lines).strip()
    out = []
    for b in re.split(r'\n\s*\n', text):
        bl = b.strip()
        if not bl:
            continue
        if bl.startswith('## ') or bl == '---':
            out.append(bl)
            continue
        rows = bl.split('\n')
        if rows[0].startswith('**') and URL.match(rows[-1].strip()):
            head = rows[0].strip().strip('*').strip()
            m = URL.match(rows[-1].strip())
            url = m.group(1).rstrip('.,')
            meta = rows[-1].strip()[len(m.group(1)):].lstrip(' ·').strip()
            desc = ' '.join(r.strip() for r in rows[1:-1]).strip()
            item = f"**[{head}]({url})**  \n{desc}"
            if meta:
                item += f"  \n*{meta}*"
            out.append(item)
        else:
            out.append(bl)
    return "\n\n".join(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', required=True)
    ap.add_argument('--date', required=True, help='YYYY-MM-DD')
    ap.add_argument('--slug', required=True)
    ap.add_argument('--title', default=None)
    a = ap.parse_args()
    raw = open(a.src, encoding='utf-8').read()
    if 'chanduonline@gmail.com' in raw or 'alticelabs' in raw.lower():
        raise SystemExit("REFUSING: source contains an email address — point at the clean digest, not a receipt.")
    # Refuse any non-newsletter (internal-jargon) digest: only clean reader copy gets published.
    low = raw.lower()
    jargon = ['harvest ledger', 'recency line', 'seen_urls', 'breadth floor', 'vocab fan-out',
              'vocabulary fan-out', 'rubric', '`listed`', '`opened`', 'mode b', 'mode e', 'mode f',
              'candidate pool', 'dedupe', 'auto-email']
    hits = [w for w in jargon if w in low] + (['<n>/8 score'] if re.search(r'\b\d(?:\.\d)?/8\b', raw) else [])
    if hits:
        raise SystemExit(f"REFUSING: source isn't newsletter-clean (internal markers: {', '.join(hits[:4])}). "
                         "Publish only the reader digest, not a run-log/verification file.")
    title = a.title or next((l[2:].strip() for l in raw.split('\n') if l.startswith('# ')), a.slug)
    body = transform(raw)
    os.makedirs(POSTS, exist_ok=True)
    path = os.path.join(POSTS, f"{a.date}-{a.slug}.md")
    fm = f'---\nlayout: post\ntitle: "{title}"\ndate: {a.date}\n---\n\n'
    open(path, 'w', encoding='utf-8').write(fm + body + "\n")
    print(path)

if __name__ == '__main__':
    main()
