#!/usr/bin/env python3
"""Build the ARB static docs site into site/ — brand style + mermaid via CDN."""
import markdown
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'site'
OUT.mkdir(exist_ok=True)

MD = markdown.Markdown(extensions=['extra', 'tables', 'fenced_code', 'sane_lists'])

HEAD = """<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{title} · Automating Real Businesses</title>
<style>
:root{{
  --bg:#0b0d12;--raised:#111318;--paper:#f4efe6;--ink:#111318;--muted:#5b554c;
  --line:#d8d0c2;--coral:#f07545;--tint:#f3a884;--deep:#a64f2f;
  --w85:rgba(255,255,255,.88);--w72:rgba(255,255,255,.72);--w55:rgba(255,255,255,.55);
  --w40:rgba(255,255,255,.4);--w12:rgba(255,255,255,.12);--w06:rgba(255,255,255,.06);
}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:var(--bg);color:#fff;font-family:system-ui,-apple-system,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased;line-height:1.5}}
.shell{{max-width:1120px;margin:0 auto;padding:1.25rem 1.25rem 3rem}}
.bar{{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:.75rem;margin-bottom:1.5rem}}
.brand{{font-family:ui-monospace,Menlo,monospace;font-size:.68rem;letter-spacing:.16em;text-transform:uppercase;color:var(--tint)}}
.nav{{display:flex;flex-wrap:wrap;gap:.25rem}}
.nav a{{color:var(--w55);text-decoration:none;font-size:.8rem;font-weight:600;padding:.42rem .7rem;border-radius:999px;border:1px solid transparent}}
.nav a:hover{{color:var(--tint);border-color:var(--w12)}}
.nav a.on{{background:var(--coral);color:#0b0d12;border-color:var(--coral)}}
.grid{{display:grid;grid-template-columns:250px 1fr;gap:1.5rem;align-items:start}}
.side{{position:sticky;top:1rem;display:flex;flex-direction:column;gap:.15rem;font-size:.86rem}}
.side a{{color:var(--w55);text-decoration:none;padding:.32rem .55rem;border-radius:8px}}
.side a:hover{{color:var(--tint);background:var(--w06)}}
.side a.on{{color:#fff;background:rgba(240,117,69,.14);border-left:2px solid var(--coral)}}
.side .grp{{font-family:ui-monospace,Menlo,monospace;font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;color:var(--w40);padding:.5rem .55rem .15rem}}
.content{{min-width:0}}
.content h1{{font-size:clamp(1.7rem,3.6vw,2.4rem);letter-spacing:-.02em;line-height:1.05;margin-bottom:.8rem}}
.content h2{{font-size:1.25rem;margin:1.6rem 0 .6rem;color:var(--tint)}}
.content h3{{font-size:1.05rem;margin:1.2rem 0 .4rem;color:var(--w85)}}
.content p{{margin:.55rem 0;color:var(--w72)}}
.content strong{{color:#fff}}
.content a{{color:var(--tint);text-decoration:none;border-bottom:1px solid rgba(240,117,69,.35)}}
.content a:hover{{color:#fff;border-color:var(--coral)}}
.content ul,.content ol{{margin:.55rem 0 .55rem 1.3rem;color:var(--w72)}}
.content li{{margin:.3rem 0}}
.content blockquote{{border-left:3px solid var(--coral);padding:.2rem 0 .2rem 1rem;color:var(--w55);margin:1rem 0}}
.content hr{{border:0;border-top:1px solid var(--w12);margin:1.6rem 0}}
.mermaid-holder{{margin:1.1rem 0;background:var(--raised);border:1px solid var(--w12);border-radius:14px;padding:1.1rem;overflow:auto}}
.mermaid-holder svg{{width:100%!important;height:auto;max-width:100%}}
code{{font-family:ui-monospace,Menlo,monospace;font-size:.86em;background:var(--w06);border:1px solid var(--w12);border-radius:6px;padding:.1rem .35rem;color:var(--tint)}}
pre{{background:var(--raised);border:1px solid var(--w12);border-radius:12px;padding:.9rem 1rem;overflow:auto;margin:.8rem 0}}
pre code{{background:none;border:0;padding:0;color:var(--w72)}}
.foot{{margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--w12);font-size:.86rem;color:var(--w55)}}
.foot a{{color:var(--tint)}}
.honest{{border-left:4px solid var(--coral);background:rgba(240,117,69,.09);padding:.7rem .9rem;border-radius:0 10px 10px 0;margin:1.1rem 0;color:var(--w85)}}
@media(max-width:860px){{.grid{{grid-template-columns:1fr}}.side{{position:static}}}}
</style>
</head>
<body><div class="shell">
<div class="bar">
  <span class="brand">Automating Real Businesses · by Yo-Da Lai</span>
  <div class="nav">
    <a href="{pfx}index.html">Home</a>
    <a href="{pfx}pattern.html">The pattern</a>
    <a href="https://www.youtube.com/@yodalaihq" target="_blank">YouTube</a>
    <a href="https://yodalai.xyz" target="_blank">yodalai.xyz</a>
  </div>
</div>
<div class="grid">
  <nav class="side">{sidebar}</nav>
  <main class="content">{content}</main>
</div>
<div class="foot">
  Free workflow maps — no tech knowledge needed. Want this for your business?
  <a href="https://yodalai.xyz">yodalai.xyz</a> · free 15-min build review.
</div>
</div>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>
mermaid.initialize({{startOnLoad:false,theme:'base',themeVariables:{{
  primaryColor:'#fdf3ee',primaryBorderColor:'#f07545',primaryTextColor:'#111318',
  lineColor:'#5b554c',fontFamily:'system-ui, sans-serif',fontSize:'19px'}},
  flowchart:{{nodeSpacing:55,rankSpacing:75,curve:'basis'}}}});
document.addEventListener('DOMContentLoaded',function(){{
  document.querySelectorAll('pre code.language-mermaid').forEach(function(el){{
    var id='mmd'+Math.random().toString(36).slice(2,9);
    mermaid.render(id,(el.textContent||'').trim()).then(function(r){{
      var h=document.createElement('div');h.className='mermaid-holder';h.innerHTML=r.svg;
      el.closest('pre').replaceWith(h);
    }}).catch(function(e){{console.warn('mermaid fail',e);}});
  }});
}});
</script>
</body></html>
"""


def md_to_html(md_text):
    """Convert markdown; then rewrite relative links to static targets."""
    MD.reset()
    html = MD.convert(md_text)
    # link.md -> link.html ; bare path without ext -> path.html if it looks like a page ref
    html = re.sub(r'href="([^"#]+?)\.md(#?[^"]*)"', r'href="\1.html\2"', html)
    html = re.sub(r'href="(workflows/[^"#]+)(#?[^"]*)"', r'href="\1.html\2"', html)
    html = re.sub(r'href="((?:0[0-9]-[^"#]+)/)(#?[^"]*)"', r'href="\1index.html\2"', html)
    return html


def title_from_frontmatter(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        return None, text
    fm = {}
    for line in m.group(1).splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm, text[m.end():]


# Collect pages: (slug, label, title, body_md, is_workflow_parent)
pages = []

def add_page(slug, label, text):
    fm, body = title_from_frontmatter(text)
    t = (fm or {}).get('title', label)
    pages.append((slug, label, t, body))

add_page('index.html', 'Home', (ROOT / 'index.md').read_text())
add_page('pattern.html', 'The pattern', (ROOT / 'pattern.md').read_text())

for niche in ['01-property-management', '02-student-inquiries', '03-tradie',
              '04-short-stay-host', '05-allied-health-clinic',
              '06-accountant-bookkeeper', '07-real-estate-sales']:
    idx = ROOT / niche / 'index.md'
    if not idx.exists():
        idx = ROOT / niche / 'README.md'
    if not idx.exists():
        continue
    add_page(f'{niche}/index.html', niche, idx.read_text())
    wf_dir = ROOT / niche / 'workflows'
    if wf_dir.exists():
        for wf in sorted(wf_dir.glob('*.md')):
            rel = f'{niche}/workflows/{wf.stem}.html'
            add_page(rel, wf.stem, wf.read_text())

# Build sidebar
def prefix_for(slug):
    depth = slug.count('/')
    return '../' * depth if depth else ''


def sidebar_for(current):
    pfx = prefix_for(current)
    out = ['<a class="grp">Series</a>',
           f'<a href="{pfx}index.html" class="{"on" if current == "index.html" else ""}">Home</a>',
           f'<a href="{pfx}pattern.html" class="{"on" if current == "pattern.html" else ""}">The pattern</a>']
    groups = {}
    for slug, label, title, _ in pages[2:]:
        if '/workflows/' in slug:
            niche_slug, _, wf = slug.split('/')
            groups.setdefault(niche_slug, []).append((slug, wf))
        else:
            pass
    for niche_slug, wfs in groups.items():
        out.append(f'<a class="grp">{niche_slug.replace("-", " ").title()}</a>')
        idx_slug = f'{niche_slug}/index.html'
        nicetitle = next((t for s, l, t, _ in pages if s == idx_slug), niche_slug)
        out.append(f'<a href="{pfx}{idx_slug}" class="{"on" if current == idx_slug else ""}">{nicetitle}</a>')
        for slug, wf in wfs:
            t = next((t for s, l, t, _ in pages if s == slug), wf)
            on = 'on' if current == slug else ''
            out.append(f'<a href="{pfx}{slug}" class="{on}">· {t}</a>')
    return '\n'.join(out)

for slug, label, title, body in pages:
    html_body = md_to_html(body)
    page = HEAD.format(title=title, pfx=prefix_for(slug), sidebar=sidebar_for(slug), content=html_body)
    dest = OUT / slug
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(page)
    print(f'wrote {slug}')

print(f'total pages: {len(pages)}')
