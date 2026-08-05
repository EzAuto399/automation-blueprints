# Site build

This folder is generated — do not hand-edit. Source of truth is the markdown in
the repo root (index.md, pattern.md, `0X-*/index.md`, `0X-*/workflows/*.md`).

Rebuild locally:

```bash
python3 scripts/build_site.py
```

Then commit. The GitHub Actions workflow deploys `site/` to Pages as static files.
