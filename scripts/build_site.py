#!/usr/bin/env python3
"""Build the ARB static docs site into site/ — minimal: workflows + mermaid maps."""
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
  --bg:#0b0d12;--raised:#14161c;--paper:#f4efe6;--ink:#111318;--muted:#5b554c;
  --line:#23262f;--coral:#f07545;--tint:#f3a884;--ok:#8fb389;
  --w85:rgba(255,255,255,.88);--w72:rgba(255,255,255,.72);--w55:rgba(255,255,255,.55);
  --w40:rgba(255,255,255,.4);--w12:rgba(255,255,255,.12);--w06:rgba(255,255,255,.06);
}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:var(--bg);color:#fff;font-family:system-ui,-apple-system,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased;line-height:1.55}}
.shell{{max-width:860px;margin:0 auto;padding:2rem 1.4rem 4rem}}
/* single back link on workflow pages */
.back{{display:inline-block;margin-bottom:1.6rem;color:var(--w55);text-decoration:none;font-size:.85rem}}
.back:hover{{color:var(--tint)}}
/* content */
h1{{font-size:clamp(1.8rem,4.5vw,2.5rem);letter-spacing:-.025em;line-height:1.08;margin-bottom:.5rem}}
.sub{{color:var(--w55);font-size:1rem;margin-bottom:2rem;max-width:60ch}}
h2{{font-size:1.1rem;margin:2rem 0 .7rem;color:var(--tint);display:flex;align-items:center;gap:.55rem}}
h2::before{{content:"";width:10px;height:10px;border-radius:3px;background:var(--coral);display:inline-block;flex:none}}
h3{{font-size:1.02rem;margin:1.2rem 0 .4rem;color:var(--w85)}}
p{{margin:.6rem 0;color:var(--w72)}}
strong{{color:#fff}}
a{{color:var(--tint);text-decoration:none;border-bottom:1px solid rgba(240,117,69,.35)}}
a:hover{{color:#fff;border-color:var(--coral)}}
ul,ol{{margin:.6rem 0 .6rem 1.25rem;color:var(--w72)}}
li{{margin:.4rem 0}}
hr{{border:0;border-top:1px solid var(--w12);margin:2rem 0}}
/* loop map — the main thing on the page */
.mermaid-holder{{margin:1.4rem 0;background:var(--raised);border:1px solid var(--line);border-radius:16px;padding:1.3rem;overflow:auto}}
.mermaid-holder svg{{width:100%!important;height:auto!important;max-width:100%!important}}
/* callouts */
.reply{{background:var(--paper);color:var(--ink);border-radius:16px;padding:1rem 1.2rem;margin:1.2rem 0;position:relative;max-width:52ch;box-shadow:0 10px 30px rgba(0,0,0,.35)}}
.reply::before{{content:"";position:absolute;left:22px;bottom:-9px;width:18px;height:18px;background:var(--paper);border-radius:3px;transform:rotate(45deg)}}
.reply p{{color:var(--ink)!important;font-size:1rem;margin:0!important}}
.callout{{border-radius:14px;padding:1rem 1.15rem;margin:1.2rem 0;background:var(--card,var(--raised));border:1px solid var(--line)}}
.callout.human{{border-left:4px solid var(--ok)}}
.callout.human h2{{margin:0 0 .5rem;color:var(--ok);font-size:.78rem;text-transform:uppercase;letter-spacing:.1em}}
.callout.human h2::before{{display:none}}
.callout.human ul{{margin:.2rem 0 .2rem 1.15rem;color:var(--w72)}}
.callout.runs{{border-left:4px solid var(--coral)}}
.callout.runs h2{{margin:0 0 .5rem;color:var(--tint);font-size:.78rem;text-transform:uppercase;letter-spacing:.1em}}
.callout.runs h2::before{{display:none}}
.callout.runs p{{margin:0;color:var(--w72)}}
.honest{{border-left:4px solid var(--coral);background:rgba(240,117,69,.08);padding:.8rem 1rem;border-radius:0 12px 12px 0;margin:1.6rem 0;color:var(--w85);font-size:.92rem}}
/* home: one list, no cards */
.niche{{margin-top:2.2rem}}
.niche h2{{margin-bottom:.8rem}}
.wf{{display:block;padding:.7rem .2rem;border-bottom:1px solid var(--w06);color:var(--w72);text-decoration:none;font-size:1rem}}
.wf:hover{{color:var(--tint)}}
.wf .n{{color:var(--coral);font-family:ui-monospace,Menlo,monospace;font-size:.8rem;margin-right:.6rem}}
/* prev/next on workflow pages */
.pager{{display:flex;justify-content:space-between;gap:1rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--w12);font-size:.9rem}}
.pager a{{color:var(--w55);text-decoration:none}}
.pager a:hover{{color:var(--tint)}}
.pager .next{{margin-left:auto;text-align:right}}
code{{font-family:ui-monospace,Menlo,monospace;font-size:.86em;background:var(--w06);border:1px solid var(--w12);border-radius:6px;padding:.1rem .35rem;color:var(--tint)}}
pre{{background:var(--raised);border:1px solid var(--line);border-radius:12px;padding:.9rem 1rem;overflow:auto;margin:.8rem 0}}
pre code{{background:none;border:0;padding:0;color:var(--w72)}}
.foot{{margin-top:3rem;padding-top:1.2rem;border-top:1px solid var(--w12);font-size:.85rem;color:var(--w55)}}
.foot a{{color:var(--tint)}}
</style>
</head>
<body><div class="shell">
{back}
{content}
<div class="foot">
  Free workflow maps by <a href="https://yodalai.xyz">Yo-Da Lai</a> — no tech knowledge needed.
  Want this for your business? Free 15-min build review at <a href="https://yodalai.xyz">yodalai.xyz</a>.
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
      var svg=h.querySelector('svg');
      if(svg){{svg.setAttribute('width','100%');svg.removeAttribute('height');svg.style.maxWidth='100%';svg.style.width='100%';svg.style.height='auto';}}
      el.closest('pre').replaceWith(h);
    }}).catch(function(e){{console.warn('mermaid fail',e);}});
  }});
}});
</script>
</body></html>
"""


def md_to_html(md_text):
    MD.reset()
    html = MD.convert(md_text)
    html = re.sub(r'href="([^"#]+?)\.md(#?[^"]*)"', r'href="\1.html\2"', html)
    html = re.sub(r'href="(workflows/[^"#]+)(#?[^"]*)"', r'href="\1.html\2"', html)
    html = re.sub(r'href="((?:0[0-9]-[^"#]+)/)(#?[^"]*)"', r'href="\1index.html\2"', html)
    return html


def wrap_callouts(html):
    pat = re.compile(r'<h2>What a reply looks like</h2>\s*<p>(.*?)</p>', re.S)
    html = pat.sub(r'<div class="reply"><p>\1</p></div>', html)
    pat = re.compile(r'<h2>What a human still does</h2>(.*?)(?=<h2>|<hr|$)', re.S)
    def human(m):
        return f'<div class="callout human"><h2>What a human still does</h2>{m.group(1).strip()}</div>'
    html = pat.sub(human, html)
    pat = re.compile(r'<h2>What it runs on</h2>\s*<p>(.*?)</p>', re.S)
    html = pat.sub(r'<div class="callout runs"><h2>What it runs on</h2><p>\1</p></div>', html)
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


pages = []

def add_page(slug, label, text):
    fm, body = title_from_frontmatter(text)
    t = (fm or {}).get('title', label)
    if t == label and body.startswith('#'):
        t = body.split('\n', 1)[0].lstrip('# ').strip()
        t = re.sub(r'^Ep \d+ — ', '', t)
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
            add_page(f'{niche}/workflows/{wf.stem}.html', wf.stem, wf.read_text())


NICE = {
    '01-property-management': 'Property management',
    '02-student-inquiries': 'Migration & education agency',
    '03-tradie': 'Tradie',
    '04-short-stay-host': 'Short-stay host',
    '05-allied-health-clinic': 'Allied health clinic',
    '06-accountant-bookkeeper': 'Accountant & bookkeeper',
    '07-real-estate-sales': 'Real estate sales agent',
}

# ordered niches with their workflow slugs
NICHE_ORDER = ['01-property-management', '02-student-inquiries', '03-tradie',
               '04-short-stay-host', '05-allied-health-clinic',
               '06-accountant-bookkeeper', '07-real-estate-sales']


def home_html():
    parts = ['<h1>Automating Real Businesses</h1>',
             '<p class="sub">Free, plain-English AI workflow maps for small businesses — one business, one real workflow, per episode. No tech knowledge needed.</p>']
    for niche in NICHE_ORDER:
        wf_pages = [p for p in pages if p[0].startswith(f'{niche}/workflows/')]
        parts.append(f'<div class="niche"><h2>{NICE.get(niche, niche)}</h2>')
        if wf_pages:
            for i, (slug, label, title, body) in enumerate(wf_pages, 1):
                parts.append(f'<a class="wf" href="{slug}"><span class="n">{i:02d}</span>{title}</a>')
        else:
            idx_slug = f'{niche}/index.html'
            t = next((t for s, l, t, _ in pages if s == idx_slug), niche)
            parts.append(f'<a class="wf" href="{idx_slug}">{t}</a>')
        parts.append('</div>')
    return '\n'.join(parts)


def back_link_for(slug):
    if slug == 'index.html':
        return ''
    if slug == 'pattern.html':
        return '<a class="back" href="index.html">← All workflows</a>'
    if '/workflows/' in slug:
        return '<a class="back" href="../index.html">← All workflows</a>'
    return '<a class="back" href="../index.html">← All workflows</a>'


def pager_for(slug):
    if '/workflows/' not in slug:
        return ''
    niche = slug.split('/')[0]
    wfs = [p for p in pages if p[0].startswith(f'{niche}/workflows/')]
    idx = next((i for i, p in enumerate(wfs) if p[0] == slug), None)
    if idx is None:
        return ''
    prev = wfs[idx - 1] if idx > 0 else None
    nxt = wfs[idx + 1] if idx < len(wfs) - 1 else None
    p = []
    if prev:
        p.append(f'<a class="prev" href="./{prev[0].split("/")[-1]}">← {prev[2]}</a>')
    if nxt:
        p.append(f'<a class="next" href="./{nxt[0].split("/")[-1]}">{nxt[2]} →</a>')
    return f'<div class="pager">{"".join(p)}</div>' if p else ''


for slug, label, title, body in pages:
    if slug == 'index.html':
        html_body = home_html()
    else:
        html_body = md_to_html(body)
        if '/workflows/' in slug:
            html_body = wrap_callouts(html_body)
            html_body += pager_for(slug)
    page = HEAD.format(title=title, back=back_link_for(slug), content=html_body)
    dest = OUT / slug
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(page)
    print(f'wrote {slug}')

print(f'total pages: {len(pages)}')
