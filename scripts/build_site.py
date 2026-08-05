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
  --bg:#0b0d12;--raised:#14161c;--card:#101217;--paper:#f4efe6;--ink:#111318;--muted:#5b554c;
  --line:#23262f;--coral:#f07545;--tint:#f3a884;--deep:#a64f2f;--ok:#8fb389;
  --w85:rgba(255,255,255,.88);--w72:rgba(255,255,255,.72);--w55:rgba(255,255,255,.55);
  --w40:rgba(255,255,255,.4);--w12:rgba(255,255,255,.12);--w06:rgba(255,255,255,.06);
}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:var(--bg);color:#fff;font-family:system-ui,-apple-system,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased;line-height:1.55}}
.shell{{max-width:1080px;margin:0 auto;padding:1.5rem 1.4rem 4rem}}
/* top bar */
.bar{{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:.9rem;margin-bottom:2rem}}
.brand{{display:flex;align-items:center;gap:.6rem;font-family:ui-monospace,Menlo,monospace;font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:var(--tint)}}
.brand b{{color:var(--paper);font-weight:700}}
.nav{{display:flex;flex-wrap:wrap;gap:.3rem}}
.nav a{{color:var(--w55);text-decoration:none;font-size:.8rem;font-weight:600;padding:.44rem .8rem;border-radius:999px;border:1px solid var(--w12)}}
.nav a:hover{{color:var(--tint);border-color:rgba(240,117,69,.4)}}
.nav a.on{{background:var(--coral);color:#0b0d12;border-color:var(--coral)}}
/* crumbs */
.crumbs{{display:flex;flex-wrap:wrap;align-items:center;gap:.35rem;font-size:.78rem;color:var(--w40);margin-bottom:1.2rem}}
.crumbs a{{color:var(--w55);text-decoration:none}}
.crumbs a:hover{{color:var(--tint)}}
.crumbs .sep{{color:var(--w12)}}
/* layout */
.grid{{display:grid;grid-template-columns:230px 1fr;gap:2rem;align-items:start}}
.side{{position:sticky;top:1.2rem;display:flex;flex-direction:column;gap:.35rem;font-size:.85rem}}
.side details{{border-bottom:1px solid var(--w06);padding:.4rem 0}}
.side summary{{cursor:pointer;list-style:none;display:flex;align-items:center;justify-content:space-between;padding:.3rem .4rem;border-radius:8px;color:var(--w72);font-weight:600;font-size:.82rem}}
.side summary::-webkit-details-marker{{display:none}}
.side summary:hover{{color:var(--tint)}}
.side summary::after{{content:"▸";font-size:.7rem;color:var(--w40);transition:transform .15s}}
.side details[open] summary::after{{transform:rotate(90deg)}}
.side details[open] summary{{color:var(--tint)}}
.side a{{display:block;color:var(--w55);text-decoration:none;padding:.3rem .4rem .3rem 1.1rem;border-radius:8px;border-left:2px solid transparent}}
.side a:hover{{color:var(--tint);background:var(--w06)}}
.side a.on{{color:#fff;background:rgba(240,117,69,.12);border-left-color:var(--coral)}}
.side .home{{display:block;color:var(--w55);text-decoration:none;padding:.35rem .4rem;border-radius:8px;font-weight:600}}
.side .home:hover{{color:var(--tint)}}
.side .home.on{{color:#fff;background:rgba(240,117,69,.12)}}
@media(max-width:860px){{.grid{{grid-template-columns:1fr}}.side{{position:static;display:none}}}}
/* content */
.content{{min-width:0}}
.content h1{{font-size:clamp(1.8rem,4vw,2.6rem);letter-spacing:-.025em;line-height:1.08;margin-bottom:.6rem}}
.content .sub{{color:var(--w55);font-size:1.02rem;margin-bottom:1.4rem;max-width:62ch}}
.content h2{{font-size:1.15rem;margin:2rem 0 .7rem;color:var(--tint);display:flex;align-items:center;gap:.55rem}}
.content h2::before{{content:"";width:10px;height:10px;border-radius:3px;background:var(--coral);display:inline-block;flex:none}}
.content h3{{font-size:1.02rem;margin:1.2rem 0 .4rem;color:var(--w85)}}
.content p{{margin:.6rem 0;color:var(--w72)}}
.content strong{{color:#fff}}
.content a{{color:var(--tint);text-decoration:none;border-bottom:1px solid rgba(240,117,69,.35)}}
.content a:hover{{color:#fff;border-color:var(--coral)}}
.content ul,.content ol{{margin:.6rem 0 .6rem 1.25rem;color:var(--w72)}}
.content li{{margin:.4rem 0}}
.content hr{{border:0;border-top:1px solid var(--w12);margin:2rem 0}}
/* loop map */
.mermaid-holder{{margin:1.2rem 0;background:var(--raised);border:1px solid var(--line);border-radius:16px;padding:1.2rem;overflow:auto}}
.mermaid-holder svg{{width:100%!important;height:auto!important;max-width:100%!important}}
/* callouts */
.reply{{background:var(--paper);color:var(--ink);border-radius:16px;padding:1rem 1.2rem;margin:1.1rem 0;position:relative;max-width:52ch;box-shadow:0 10px 30px rgba(0,0,0,.35)}}
.reply::before{{content:"";position:absolute;left:22px;bottom:-9px;width:18px;height:18px;background:var(--paper);border-radius:3px;transform:rotate(45deg)}}
.reply p{{color:var(--ink)!important;font-size:1rem;margin:0!important}}
.callout{{border-radius:14px;padding:1rem 1.15rem;margin:1.1rem 0;background:var(--card);border:1px solid var(--line)}}
.callout.human{{border-left:4px solid var(--ok)}}
.callout.human h2{{margin:0 0 .5rem;color:var(--ok);font-size:.8rem;text-transform:uppercase;letter-spacing:.1em}}
.callout.human h2::before{{display:none}}
.callout.human ul{{margin:.2rem 0 .2rem 1.15rem;color:var(--w72)}}
.callout.runs{{border-left:4px solid var(--coral)}}
.callout.runs h2{{margin:0 0 .5rem;color:var(--tint);font-size:.8rem;text-transform:uppercase;letter-spacing:.1em}}
.callout.runs h2::before{{display:none}}
.callout.runs p{{margin:0;color:var(--w72)}}
.honest{{border-left:4px solid var(--coral);background:rgba(240,117,69,.08);padding:.8rem 1rem;border-radius:0 12px 12px 0;margin:1.4rem 0;color:var(--w85);font-size:.92rem}}
/* home cards */
.card-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1rem;margin:1.6rem 0}}
.niche-card{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:1.15rem 1.2rem;display:flex;flex-direction:column;gap:.45rem;transition:border-color .15s,transform .15s}}
.niche-card:hover{{border-color:rgba(240,117,69,.45);transform:translateY(-2px)}}
.niche-card h3{{font-size:1.02rem;color:var(--paper);display:flex;align-items:center;gap:.5rem}}
.niche-card h3::before{{content:"";width:8px;height:8px;border-radius:2px;background:var(--coral);flex:none}}
.niche-card p{{font-size:.9rem;color:var(--w55);margin:0;flex:1}}
.niche-card a{{font-size:.88rem;font-weight:700;color:var(--tint);text-decoration:none;border:0}}
.niche-card a:hover{{color:#fff}}
code{{font-family:ui-monospace,Menlo,monospace;font-size:.86em;background:var(--w06);border:1px solid var(--w12);border-radius:6px;padding:.1rem .35rem;color:var(--tint)}}
pre{{background:var(--raised);border:1px solid var(--line);border-radius:12px;padding:.9rem 1rem;overflow:auto;margin:.8rem 0}}
pre code{{background:none;border:0;padding:0;color:var(--w72)}}
.foot{{margin-top:3rem;padding-top:1.2rem;border-top:1px solid var(--w12);font-size:.86rem;color:var(--w55);display:flex;flex-wrap:wrap;gap:.5rem;justify-content:space-between}}
.foot a{{color:var(--tint)}}
</style>
</head>
<body><div class="shell">
<div class="bar">
  <span class="brand">Automating Real Businesses <b>· by Yo-Da Lai</b></span>
  <div class="nav">
    <a href="{pfx}index.html">Home</a>
    <a href="{pfx}pattern.html">The pattern</a>
    <a href="https://www.youtube.com/@yodalaihq" target="_blank">YouTube</a>
    <a href="https://yodalai.xyz" target="_blank">yodalai.xyz</a>
  </div>
</div>
{crumbs}
<div class="grid">
  <nav class="side">{sidebar}</nav>
  <main class="content">{content}</main>
</div>
<div class="foot">
  <span>Free workflow maps — no tech knowledge needed.</span>
  <span>Want this for your business? <a href="https://yodalai.xyz">yodalai.xyz</a> · free 15-min build review</span>
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
    """Convert markdown; then rewrite relative links to static targets."""
    MD.reset()
    html = MD.convert(md_text)
    html = re.sub(r'href="([^"#]+?)\.md(#?[^"]*)"', r'href="\1.html\2"', html)
    html = re.sub(r'href="(workflows/[^"#]+)(#?[^"]*)"', r'href="\1.html\2"', html)
    html = re.sub(r'href="((?:0[0-9]-[^"#]+)/)(#?[^"]*)"', r'href="\1index.html\2"', html)
    return html


def wrap_callouts(html):
    """Post-process: .reply for 'What a reply looks like', .callout for human/runs sections."""
    # What a reply looks like -> cream chat bubble
    pat = re.compile(
        r'<h2>What a reply looks like</h2>\s*<p>(.*?)</p>', re.S)
    html = pat.sub(
        r'<div class="reply"><p>\1</p></div>', html)
    # What a human still does -> callout.human
    pat = re.compile(
        r'<h2>What a human still does</h2>(.*?)(?=<h2>|<hr|$)',
        re.S)
    def human(m):
        inner = m.group(1).strip()
        return f'<div class="callout human"><h2>What a human still does</h2>{inner}</div>'
    html = pat.sub(human, html)
    # What it runs on -> callout.runs
    pat = re.compile(
        r'<h2>What it runs on</h2>\s*<p>(.*?)</p>', re.S)
    html = pat.sub(
        r'<div class="callout runs"><h2>What it runs on</h2><p>\1</p></div>', html)
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


pages = []  # (slug, label, title, body_md)

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


def prefix_for(slug):
    depth = slug.count('/')
    return '../' * depth if depth else ''


def sidebar_for(current):
    pfx = prefix_for(current)
    out = [f'<a class="home {"on" if current == "index.html" else ""}" href="{pfx}index.html">Home</a>']
    groups = {}
    # all niches in series order; details-group when they have workflows
    for slug, label, title, _ in pages[2:]:
        if '/workflows/' in slug:
            niche_slug, _, wf = slug.split('/')
            groups.setdefault(niche_slug, []).append((slug, wf))
    for niche_slug, wfs in groups.items():
        idx_slug = f'{niche_slug}/index.html'
        nicetitle = next((t for s, l, t, _ in pages if s == idx_slug), niche_slug)
        open_attr = ' open' if current == idx_slug or current.startswith(niche_slug + '/') else ''
        out.append(f'<details{open_attr}><summary>{nicetitle}</summary>')
        for slug, wf in wfs:
            t = next((t for s, l, t, _ in pages if s == slug), wf)
            on = 'on' if current == slug else ''
            out.append(f'<a href="{pfx}{slug}" class="{on}">{t}</a>')
        out.append('</details>')
    # niches without workflows (01/02) -> plain links
    short_names = {'01-property-management': 'Property management',
                   '02-student-inquiries': 'Migration & education agency'}
    for niche_slug in ['01-property-management', '02-student-inquiries']:
        idx_slug = f'{niche_slug}/index.html'
        nicetitle = short_names.get(niche_slug, niche_slug)
        on = 'on' if current == idx_slug else ''
        out.append(f'<a href="{pfx}{idx_slug}" class="home {"on" if on else ""}">{nicetitle}</a>')
    return '\n'.join(out)


def crumbs_for(slug, title):
    pfx = prefix_for(slug)
    parts = [f'<a href="{pfx}index.html">Home</a>']
    if slug == 'index.html':
        return ''
    if slug == 'pattern.html':
        parts.append('<span class="sep">/</span><span>The pattern</span>')
        return f'<div class="crumbs">{" ".join(parts)}</div>'
    if '/workflows/' in slug:
        niche_slug, _, wf = slug.split('/')
        niche_title = next((t for s, l, t, _ in pages if s == f'{niche_slug}/index.html'), niche_slug)
        parts.append(f'<span class="sep">/</span><a href="{pfx}{niche_slug}/index.html">{niche_title}</a>')
        parts.append(f'<span class="sep">/</span><span>{title}</span>')
    else:
        niche_title = title
        parts.append(f'<span class="sep">/</span><span>{niche_title}</span>')
    return f'<div class="crumbs">{" ".join(parts)}</div>'


for slug, label, title, body in pages:
    html_body = md_to_html(body)
    if '/workflows/' in slug:
        html_body = wrap_callouts(html_body)
    page = HEAD.format(title=title, pfx=prefix_for(slug),
                       sidebar=sidebar_for(slug), content=html_body,
                       crumbs=crumbs_for(slug, title))
    dest = OUT / slug
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(page)
    print(f'wrote {slug}')

print(f'total pages: {len(pages)}')
