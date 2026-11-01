"""Shared clip-Short builder (same look as serapeum-boxes/make_shorts.py: 1080x1920, blurred bg, 16:9 fg,
burned DejaVu captions, hook 0-3 s, end card), plus support for NON-contiguous shot lists so each Short keeps
the claim + the payoff under 60 s. Parts are joined with 80 ms audio fades.
Used by <item>/make_shorts.py:  build(E, MASTER, LONG_TITLE, CLIPS, TAGS, n)
CLIPS[n] = dict(shots=[...ids...], hook="...", title="... #Shorts")"""
import json, subprocess, os

FPS = 30

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

def runs(ids):
    ids = sorted(ids); out = [[ids[0], ids[0]]]
    for i in ids[1:]:
        if i == out[-1][1] + 1: out[-1][1] = i
        else: out.append([i, i])
    return out

def build(E, MASTER, LONG_TITLE, CLIPS, TAGS, n, PIN=None):
    tl = json.load(open(f'{E}/timeline.json')); S = {s['id']: s for s in tl['shots']}
    cues = []
    for blk in open(f'{E}/captions.srt').read().strip().split('\n\n'):
        ln = blk.split('\n')
        if len(ln) >= 3:
            a, b = ln[1].split(' --> '); cues.append((t2s(a), t2s(b), ' '.join(ln[2:])))
    c = CLIPS[n]; parts = []
    R = runs(c['shots'])
    for k, (a, b) in enumerate(R):
        t0 = S[a]['lines'][0]['start'] / FPS - (0.4 if k == 0 else 0.25)
        t1 = S[b]['lines'][-1]['end'] / FPS + (0.6 if k == len(R) - 1 else 0.35)
        parts.append((t0, t1))
    dur = sum(t1 - t0 for t0, t1 in parts)
    od = f'{E}/shorts/{n}'; os.makedirs(od, exist_ok=True)
    ass = ['[Script Info]', 'ScriptType: v4.00+', 'PlayResX: 1080', 'PlayResY: 1920', '',
           '[V4+ Styles]',
           'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding',
           'Style: Cap,DejaVu Sans,62,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,1,0,0,0,100,100,0,0,1,5,2,8,60,60,1330,1',
           'Style: Hook,DejaVu Sans,86,&H005AE0FF,&H005AE0FF,&H00000000,&H80000000,1,0,0,0,100,100,0,0,1,6,3,8,50,50,330,1',
           'Style: End,DejaVu Sans,64,&H00FFFFFF,&H00FFFFFF,&H00000000,&HC0000000,1,0,0,0,100,100,0,0,3,18,0,5,60,60,0,1',
           '', '[Events]', 'Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text']
    ass.append(f"Dialogue: 1,{ass_time(0)},{ass_time(min(3.0, dur))},Hook,,0,0,0,,{{\\fad(0,250)}}{wrap(c['hook'], 18)}")
    off = 0.0
    for t0, t1 in parts:
        for a, b, txt in cues:
            if b <= t0 + 0.05 or a >= t1 - 0.05: continue
            ass.append(f"Dialogue: 0,{ass_time(max(a, t0) - t0 + off)},{ass_time(min(b, t1) - t0 + off)},Cap,,0,0,0,,{wrap(txt)}")
        off += t1 - t0
    ass.append(f"Dialogue: 2,{ass_time(dur - 3.2)},{ass_time(dur)},End,,0,0,0,,{{\\fad(200,0)}}FULL CASE \u2192\\NANCIENT MACHINES")
    open(f'{od}/caps.ass', 'w').write('\n'.join(ass))
    fc = []; vl = ''; al = ''
    for k, (t0, t1) in enumerate(parts):
        d = t1 - t0
        fc.append(f"[0:v]trim=start={t0:.3f}:end={t1:.3f},setpts=PTS-STARTPTS[v{k}]")
        fc.append(f"[0:a]atrim=start={t0:.3f}:end={t1:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.08,afade=t=out:st={d - 0.08:.3f}:d=0.08[a{k}]")
        vl += f"[v{k}]"; al += f"[a{k}]"
    fc.append(f"{vl}concat=n={len(parts)}:v=1:a=0[vc]")
    fc.append(f"{al}concat=n={len(parts)}:v=0:a=1,afade=t=out:st={dur - 0.6:.2f}:d=0.6[ac]")
    fc.append("[vc]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=28,eq=brightness=-0.18[bg];"
              f"[b]scale=1080:-2,crop=1080:608[fg];[bg][fg]overlay=0:656,ass={od}/caps.ass[v]")
    tmp = f'/tmp/short_{os.path.basename(E)}_{n}.mp4'
    ss = max(0, parts[0][0] - 1); pe = parts[-1][1] + 1
    # input-seek near the first part to keep it fast; shift part times accordingly
    fcs = ';'.join(fc)
    for t0, t1 in parts:
        fcs = fcs.replace(f"start={t0:.3f}:end={t1:.3f}", f"start={t0 - ss:.3f}:end={t1 - ss:.3f}")
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', f'{ss:.3f}', '-t', f'{pe - ss:.3f}', '-i', f'{E}/{MASTER}',
                    '-filter_complex', fcs, '-map', '[v]', '-map', '[ac]', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20',
                    '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', tmp], check=True)
    subprocess.run(['cp', tmp, f'{od}/clip.mp4'], check=True); os.remove(tmp)
    m, s = divmod(int(parts[0][0]), 60)
    pin = PIN or "Full case file (sources, tests, verdict) on the channel. What do you think it really shows? \U0001F447"
    open(f'{od}/publish.md', 'w').write(f"""# Short {n} — clip from "{LONG_TITLE}"
File: clip.mp4 (1080x1920, {dur:.1f} s) — cut from {MASTER} starting {m}:{s:02d} (shots {', '.join(map(str, c['shots']))})
Title: {c['title']}
Description: {c['hook'].title()} The full investigation is on Ancient Machines. Facts labelled, theories labelled THEORY. Visuals are AI-generated reconstructions; narration is a synthetic voice.
Hashtags: {TAGS} #Shorts
Related video: the long "{LONG_TITLE}" once it is uploaded (paste its URL in Studio > Related video).
Pinned comment: {pin}
""")
    print(n, round(dur, 1), 'ok')
