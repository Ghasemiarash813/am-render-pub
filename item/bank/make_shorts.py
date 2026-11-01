"""Cut 5 vertical clip Shorts from Puma-Punku.mp4 (ffmpeg only). Run under flock render.lock.
usage: python3 make_shorts.py [n ...]"""
import json, re, subprocess, sys, os
E = os.path.dirname(os.path.abspath(__file__))
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
tl = json.load(open(f'{E}/timeline.json')); FPS = tl['fps']
S = {s['id']: s for s in tl['shots']}
CLIPS = {
 1: dict(a=1, b=4, hook="LASER CUT STONE?", title="Puma Punku's 'laser-cut' H-blocks: we measured the claim #Shorts"),
 2: dict(a=15, b=18, hook="131 TONS, NOT 800", title="Puma Punku's biggest stone: 131 tons, not 800 #Shorts"),
 3: dict(a=25, b=28, hook="ARE THEY IDENTICAL?", title="Are Puma Punku's H-blocks identical? The survey says no #Shorts"),
 4: dict(a=43, b=46, hook="STONE TOOLS ONLY?", title="Can stone tools carve Puma Punku precision? One experiment #Shorts"),
 5: dict(a=54, b=56, hook="WHERE ARE THE LASER MARKS?", title="If Puma Punku was laser-cut, where are the laser marks? #Shorts"),
}


def t2s(t):
    h, m, r = t.split(':'); s, ms = r.split(','); return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000

def ass_time(x):
    x = max(0, x); h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def wrap(txt, n=26):
    w = txt.split(); L = []; cur = ''
    for x in w:
        if len(cur) + len(x) + 1 > n and cur: L.append(cur); cur = x
        else: cur = (cur + ' ' + x).strip()
    L.append(cur); return '\\N'.join(L)

cues = []
for blk in open(f'{E}/captions.srt').read().strip().split('\n\n'):
    ln = blk.split('\n')
    if len(ln) >= 3:
        a, b = ln[1].split(' --> '); cues.append((t2s(a), t2s(b), ' '.join(ln[2:])))

def build(n):
    c = CLIPS[n]; sa = S[c['a']]; sb = S[c['b']]
    t0 = sa['lines'][0]['start'] / FPS - 0.4
    t1 = sb['lines'][-1]['end'] / FPS + 0.6
    dur = t1 - t0
    od = f'{E}/shorts/{n}'; os.makedirs(od, exist_ok=True)
    ass = ['[Script Info]', 'ScriptType: v4.00+', 'PlayResX: 1080', 'PlayResY: 1920', '',
           '[V4+ Styles]',
           'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding',
           'Style: Cap,DejaVu Sans,62,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,1,0,0,0,100,100,0,0,1,5,2,8,60,60,1330,1',
           'Style: Hook,DejaVu Sans,86,&H005AE0FF,&H005AE0FF,&H00000000,&H80000000,1,0,0,0,100,100,0,0,1,6,3,8,50,50,330,1',
           'Style: End,DejaVu Sans,64,&H00FFFFFF,&H00FFFFFF,&H00000000,&HC0000000,1,0,0,0,100,100,0,0,3,18,0,5,60,60,0,1',
           '', '[Events]', 'Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text']
    ass.append(f"Dialogue: 1,{ass_time(0)},{ass_time(min(3.0, dur))},Hook,,0,0,0,,{{\\fad(0,250)}}{wrap(c['hook'], 18)}")
    for a, b, txt in cues:
        if b <= t0 or a >= t1: continue
        ass.append(f"Dialogue: 0,{ass_time(a - t0)},{ass_time(min(b, t1) - t0)},Cap,,0,0,0,,{wrap(txt)}")
    ass.append(f"Dialogue: 2,{ass_time(dur - 3.2)},{ass_time(dur)},End,,0,0,0,,{{\\fad(200,0)}}FULL CASE \u2192\\NANCIENT MACHINES")
    open(f'{od}/caps.ass', 'w').write('\n'.join(ass))
    vf = ("[0:v]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=28,eq=brightness=-0.18[bg];"
          "[b]scale=1080:-2,crop=1080:608[fg];[bg][fg]overlay=0:656,"
          f"ass={od}/caps.ass[v]")
    tmp = f'/tmp/pp_short_{n}.mp4'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', f'{t0:.3f}', '-t', f'{dur:.3f}', '-i', f'{E}/Puma-Punku.mp4',
                    '-filter_complex', vf, '-map', '[v]', '-map', '0:a', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20',
                    '-c:a', 'aac', '-b:a', '160k', '-af', 'afade=t=out:st=%.2f:d=0.6' % (dur - 0.6), '-movflags', '+faststart', tmp], check=True)
    subprocess.run(['cp', tmp, f'{od}/clip.mp4'], check=True); os.remove(tmp)
    m, s = divmod(int(t0), 60)
    open(f'{od}/publish.md', 'w').write(f"""# Short {n} — clip from "Puma Punku: Laser-Cut Stones or Tiwanaku Genius?" (bank B5)
File: clip.mp4 (1080x1920, {dur:.1f} s) — cut from Puma-Punku.mp4 at {m}:{s:02d}
Title: {c['title']}
Description: {c['hook'].title()} The full engineer's site survey of Puma Punku (Tiwanaku, Bolivia) is on Ancient Machines. Facts labelled, theories labelled THEORY. Visuals are AI-generated reconstructions; narration is a synthetic voice.
Hashtags: #PumaPunku #Tiwanaku #Bolivia #AncientMysteries #AncientTechnology #Shorts
Related video: the long "Puma Punku" episode once it is uploaded (paste its URL in Studio > Related video).
Pinned comment: Full site survey (measurements, quarries, tool test, scorecard) on the channel. Laser-cut or Tiwanaku genius? 👇
""")
    print(n, round(dur, 1), 'ok')

if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS): build(n)
