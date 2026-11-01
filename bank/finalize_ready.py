#!/usr/bin/env python3
"""Write/refresh READY.md for a finished bank long. usage: finalize_ready.py <slug>"""
import sys, os, re, json, subprocess, glob
B = os.path.dirname(os.path.abspath(__file__))
slug = sys.argv[1]; E = f'{B}/{slug}'
MASTER = {'dendera-zodiac': 'Dendera-Zodiac', 'serapeum-boxes': 'Serapeum-Boxes',
          'fermi-paradox': 'Fermi-Paradox', 'oumuamua-atlas': 'Oumuamua-vs-3I-ATLAS', 'puma-punku': 'Puma-Punku', 'simulation': 'Simulation-Hypothesis', 'vimanas': 'Vimanas-vs-UAP-Files', 'dendera-lightbulbs': 'Dendera-Light-Bulbs', 'gobekli-vulture': 'Gobekli-Tepe-Vulture-Stone', 'ufo-art': 'UFOs-in-Ancient-Art'}.get(slug) or open(f'{E}/MASTER_NAME').read().strip()
UPLOAD = {'serapeum-boxes': 'serapeum-boxes-upload.mp4', 'puma-punku': 'puma-punku-upload.mp4', 'simulation': 'simulation-upload.mp4', 'vimanas': 'vimanas-upload.mp4', 'dendera-lightbulbs': 'dendera-lightbulbs-upload.mp4', 'gobekli-vulture': 'gobekli-vulture-upload.mp4', 'ufo-art': 'ufo-art-upload.mp4'}.get(slug, f'{MASTER}-upload.mp4')

def probe(f):
    if not os.path.exists(f): return None, None
    d = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]))
    return d, os.path.getsize(f)
def mmss(d): return f"{int(d//60)}:{int(round(d%60)):02d}"
def mb(s): return f"{s/1e6:.0f} MB"

md, ms = probe(f'{E}/{MASTER}.mp4'); ud, us = probe(f'{E}/{UPLOAD}')
# srt copy
if os.path.exists(f'{E}/captions.srt') and not os.path.exists(f'{E}/{MASTER}.srt'):
    subprocess.run(['cp', f'{E}/captions.srt', f'{E}/{MASTER}.srt'])
shorts = []
for p in sorted(glob.glob(f'{E}/shorts/*/clip.mp4')):
    d, s = probe(p); pub = os.path.join(os.path.dirname(p), 'publish.md')
    t = ''
    if os.path.exists(pub):
        m = re.search(r'^TITLE:\s*(.+)$', open(pub).read(), re.M) or re.search(r'^#\s*(.+)$', open(pub).read(), re.M)
        t = m.group(1).strip() if m else ''
    shorts.append(f"- shorts/{os.path.basename(os.path.dirname(p))}/clip.mp4 — {d:.1f}s — {t}")
dubs = [f"- dub/{os.path.basename(f)} — {mmss(probe(f)[0])}" for f in sorted(glob.glob(f'{E}/dub/*.m4a'))]

rp = f'{E}/READY.md'
if slug == 'dendera-zodiac' and os.path.exists(rp):
    s = open(rp).read()
    s = s.replace('__DUR__', f"{mmss(md)} ({md:.1f} s), {mb(ms)}" if md else 'NOT BUILT')
    s = s.replace('__USIZE__', f"{mb(us)}, {mmss(ud)}" if us else 'NOT BUILT')
else:
    meta = open(f'{E}/youtube_metadata.txt').read()
    titles = re.findall(r'^\s*([123])\)\s*(.+?)\s*(?:\[.*\])?\s*$', meta, re.M)[:3]
    ch = re.search(r'CHAPTERS\s*\n(.*?)\n\s*\n', meta, re.S)
    s = f"# READY — {slug} (bank item, NOT uploaded)\nFinished 2026-10-31/11-01 by bank finisher. Arash uploads later (free plan).\n\n"
    s += f"## Files (folder pipeline/bank/{slug}/)\n"
    s += f"- {MASTER}.mp4 — master 1920x1080 H.264 + AAC 48k, loudnorm -14 LUFS — {mmss(md) if md else 'NOT BUILT'} ({md:.1f} s), {mb(ms) if ms else ''}\n" if md else f"- {MASTER}.mp4 — NOT BUILT\n"
    s += f"- {UPLOAD} — re-encoded upload copy — {mb(us)}\n" if us else f"- {UPLOAD} — NOT BUILT\n"
    s += f"- {MASTER}.srt — English captions (copy of captions.srt)\n- thumbnail.jpg, thumb_b.jpg, thumb_c.jpg — 1280x720\n"
    s += "- youtube_metadata.txt — 3 titles, description with chapters + sources, tags, pinned comment, ES/PT title + description\n"
    s += "- facts.md — sourced facts; shots_src.py / timeline.json / Doc.tsx / build.sh — reproducible source\n\n"
    s += "## Metadata summary\n" + ''.join(f"- Title {n}: {t}\n" for n, t in titles)
    if ch: s += "- Chapters:\n" + ''.join(f"  {l.strip()}\n" for l in ch.group(1).strip().split('\n'))
    s += "- Set Altered content = Yes (AI visuals + synthetic voice). Education, English, not for kids.\n\n"
s = re.sub(r'\n## EXTRA \(clip Shorts \+ dubs\).*', '', s, flags=re.S)
s += "\n## EXTRA (clip Shorts + dubs)\n"
s += ("### Clip Shorts (1080x1920, burned captions, hook 0-3 s, end card)\n" + '\n'.join(shorts) + "\n") if shorts else "### Clip Shorts: NOT BUILT yet\n"
s += ("### Dub audio tracks (Kokoro em_alex / pm_alex, aligned to timeline, -14 LUFS) — add via Studio Languages > Audio\n" + '\n'.join(dubs) + "\nES/PT title + description: see youtube_metadata.txt.\n") if dubs else "### Dubs: NOT BUILT yet\n"
open(rp, 'w').write(s)
print(slug, md, ms, us, len(shorts), len(dubs))
