#!/usr/bin/env python3
"""AI dub for Ancient Machines episodes (kokoro-onnx).
usage:
  dub.py tts  EP_DIR LANG VOICE LINES_JSON [ids...]  -> EP_DIR/dub/<lang>/sNN.wav + fit report
  dub.py mix  EP_DIR LANG                             -> EP_DIR/dub/<Name>-<lang>.wav/.m4a (loudnorm -14)
  dub.py mix  EP_DIR en                               -> rebuild English mix from audio/sNN.mp3 (validation)
Mix replicates Doc.tsx: music.wav vol 0.30 / 0.13 while speaking (line start-4f .. end+4f),
voice 1.0, whoosh 0.35 at chapter shots (ch), beeps 0.25 on score shots #2/#3, whoosh 0.5 after title shot.
Each dubbed line must fit its slot = next line start - this start - GAP frames.
"""
import sys, json, os, subprocess, re
R = '/workspace/projects/135872d5-70e2-46c7-af0f-bc6c101de728'
sys.path.insert(0, R + '/voice_lab/.lib')
import numpy as np, soundfile as sf

FPS = 30; SR = 48000; GAP = 8; MAXSPD = 1.15
PUB = R + '/pipeline/pyramid-ai/public'
FIX = {
 'es': {"Xesspe": "Jéspe", "Däniken": "Déniken", "Reiche": "Ráije", "Erich": "Érij", "Paul": "Pol",
        "Joe Nickell": "Yóu Níquel", "Nickell": "Níquel", "Gerald Hawkins": "Yérald Jókins", "Anthony": "Ántoni",
        "Johan Reinhard": "Yójan Ráinjard", "David Johnson": "Déivid Yónson", "IBM Research": "I B M Ríserch",
        "PNAS": "P N A S", "Ancient Machines": "Éinshent Mashíns", "la IA": "la I A", "La IA": "La I A",
        "Kosok": "Kósok", "Maussan": "Mósan", "Oumuamua": "Oumuamúa", "Tres I Atlas": "Tres I Átlas", "Weryk": "Uérik", "Haleakala": "Jaleakalá", "Pan-STARRS": "Pan Stars", "Loeb": "Loub", "Statler": "Státler", "Jason Wright": "Yéison Ráit", "Wright": "Ráit", "Mawangdui": "Mawangduí", "Very Large Telescope": "Véri Larch Télescop", "Allen Telescope Array": "Álen Télescop Arréi", "Breakthrough Listen": "Bréiktru Lísen", "Green Bank": "Grin Bank", "Robert": "Róbert", "Arthur C. Clarke": "Árthur Si Clark", "Astronomy and Astrophysics": "Astronomy and Astrophysics"},
 'pt-br': {"Xesspe": "Réspi", "Däniken": "Déniken", "Reiche": "Ráiche", "Erich": "Érich", "Paul": "Pól",
        "Joe Nickell": "Djôu Níquel", "Nickell": "Níquel", "Gerald Hawkins": "Djérald Róquins", "Anthony": "Ântoni",
        "Johan Reinhard": "Iôran Ráinrard", "David Johnson": "Dêivid Djônson", "IBM Research": "I B M Ríserch",
        "PNAS": "P N A S", "Ancient Machines": "Êinchent Machíns", "a IA": "a I A", "A IA": "A I A",
        "Maussan": "Môssan", "Oumuamua": "Oumuamúa", "Três I Atlas": "Três I Átlas", "Weryk": "Uérik", "Haleakala": "Raleakalá", "Pan-STARRS": "Pan Stars", "Loeb": "Lôub", "Statler": "Státler", "Jason Wright": "Djêison Ráit", "Wright": "Ráit", "Mawangdui": "Mawangduí", "Very Large Telescope": "Véri Lardj Télescop", "Allen Telescope Array": "Álen Télescop Arrêi", "Breakthrough Listen": "Brêiktru Lissen", "Green Bank": "Grin Bénk", "Arthur C. Clarke": "Árthur Ci Clark"},
}

def tl(ep): return json.load(open(f'{ep}/timeline.json'))

def lines(ep):
    t = tl(ep); L = []
    for s in t['shots']:
        for l in s['lines']: L.append(dict(id=s['id'], start=l['start'], end=l['end'], file=l['file']))
    for i, l in enumerate(L):
        nxt = L[i + 1]['start'] if i + 1 < len(L) else t['total'] - 45
        l['slot'] = (nxt - l['start'] - GAP) / FPS
    return t, L

def tts(ep, lang, voice, lj, ids):
    from kokoro_onnx import Kokoro
    k = Kokoro(R + '/voice_lab/kokoro-v1.0.onnx', R + '/voice_lab/voices-v1.0.bin')
    tx = json.load(open(lj)); t, L = lines(ep)
    od = f'{ep}/dub/{lang}'; os.makedirs(od, exist_ok=True)
    rep = json.load(open(f'{od}/fit.json')) if os.path.exists(f'{od}/fit.json') else {}
    base = 1.0
    for l in L:
        if ids and str(l['id']) not in ids: continue
        txt = tx[str(l['id'])]
        for a, b in FIX.get(lang, {}).items(): txt = txt.replace(a, b)
        spd = base
        for attempt in range(3):
            a, sr = k.create(txt, voice=voice, speed=spd, lang=lang)
            a = np.trim_zeros(a, 'b'); d = len(a) / sr
            if d <= l['slot'] or spd >= base * MAXSPD: break
            spd = min(base * MAXSPD, spd * d / l['slot'] * 1.02)
        sf.write('/tmp/dub_raw_b2.wav', a, sr)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', '/tmp/dub_raw_b2.wav', '-af',
                        'highpass=f=70,acompressor=threshold=-20dB:ratio=2.5:attack=10:release=150',
                        '-ar', str(SR), '-ac', '1', f"{od}/s{l['id']:02d}.wav"], check=True)
        ok = d <= l['slot'] + 0.05
        rep[str(l['id'])] = dict(dur=round(d, 2), slot=round(l['slot'], 2), speed=round(spd, 3), fits=ok)
        print(l['id'], round(d, 2), '/', round(l['slot'], 2), 'spd', round(spd, 3), 'OK' if ok else 'LONG', flush=True)
        json.dump(rep, open(f'{od}/fit.json', 'w'), indent=1)

def load(path, sr=SR):
    raw = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', path, '-f', 'f32le', '-ac', '1', '-ar', str(sr), '-'])
    return np.frombuffer(raw, np.float32).copy()

def mix(ep, lang):
    t, L = lines(ep); total = t['total']; N = int(total / FPS * SR)
    out = np.zeros(N, np.float32)
    def add(sig, at_frame, maxframes=None, vol=1.0):
        s0 = int(at_frame / FPS * SR)
        if maxframes: sig = sig[:int(maxframes / FPS * SR)]
        e = min(N, s0 + len(sig)); out[s0:e] += sig[:e - s0] * vol
    # voices + speaking windows
    spk = np.zeros(total + 1, bool)
    for l in L:
        f = f"{ep}/{l['file'][3:]}" if lang == 'en' else f"{ep}/dub/{lang}/s{l['id']:02d}.wav"
        v = load(f)
        if lang == 'en':
            add(v, l['start'], l['end'] - l['start'] + 15); end = l['end']
        else:
            add(v, l['start']); end = l['start'] + int(round(len(v) / SR * FPS))
        spk[max(0, l['start'] - 4):min(total, end + 4)] = True
    # music with ducking (per-frame gain, smoothed 2 frames)
    m = load(f'{ep}/music.wav')[:N]
    g = np.where(spk[:total], 0.13, 0.30).astype(np.float32)
    gs = np.repeat(g, SR // FPS)[:N]
    gs = np.pad(gs, (0, max(0, N - len(gs))), mode='edge')
    out[:len(m)] += m * gs[:len(m)]
    # sfx
    shots = t['shots']; score = [s['id'] for s in shots if s.get('fx') == 'score']
    wh = load(PUB + '/whoosh.wav'); bp = load(PUB + '/beep.wav')
    for s in shots:
        if s.get('ch'): add(wh, s['start'], 45, 0.35)
        k = score.index(s['id']) if s['id'] in score else -1; ln = s['end'] - s['start']
        if k == 1:
            for i in range(4): add(bp, s['start'] + round(30 + (i * (ln - 90)) / 4), 45, 0.25)
        if k == 2:
            for j in range(3): add(bp, s['start'] + round(30 + (j * (ln - 90)) / 3), 45, 0.25)
    s2 = next(s for s in shots if s['id'] == t['titleAfter'])
    add(wh, s2['lines'][-1]['end'] + 6, 45, 0.5)
    od = f'{ep}/dub'; os.makedirs(od, exist_ok=True)
    tag = {'es': 'es', 'pt-br': 'pt-BR', 'en': 'en-rebuild'}[lang]
    raw = f'/tmp/dubmix_b2_{lang}.wav'; sf.write(raw, np.stack([out, out], 1), SR, subtype='FLOAT')
    short={'es':'es','pt-br':'pt','en':'en-rebuild'}[lang]; w = f'/tmp/dubb2_{short}.wav'; a = f'{od}/{short}.m4a'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', raw, '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11',
                    '-ar', str(SR), '-c:a', 'pcm_s16le', w], check=True)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', w, '-c:a', 'aac', '-b:a', '192k', a], check=True)
    print(w, a)

if __name__ == '__main__':
    c = sys.argv[1]
    if c == 'tts': tts(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6:])
    elif c == 'mix': mix(sys.argv[2], sys.argv[3])
