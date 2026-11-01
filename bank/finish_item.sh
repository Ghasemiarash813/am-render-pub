#!/bin/bash
# Idempotent, restart-safe finisher for one bank long. usage: finish_item.sh <slug>
# Renders the frames not yet covered in ~1400-frame segments (c s<START>.mp4) under render.lock,
# then audio -> mux (/tmp then cp) -> <200MB upload copy -> 5 clip Shorts -> READY.md
set -u
B=/workspace/projects/135872d5-70e2-46c7-af0f-bc6c101de728/pipeline/bank; L=$B/render.lock
slug=$1; E=$B/$slug; cd $E
# CLOUD_RENDER marker: item is rendered on GitHub Actions (see bank/CLOUD_RENDER.md). Local finisher skips it;
# the cloud puller runs this script with CLOUD_OK=1 after placing the cloud segments (cs<START>.mp4) here.
if [ -f CLOUD_RENDER ] && [ -z "${CLOUD_OK:-}" ]; then echo "$slug skipped: CLOUD_RENDER marker $(date +%T)"; exit 0; fi
case $slug in
 dendera-zodiac) M=Dendera-Zodiac; U=Dendera-Zodiac-upload.mp4; LEG="1:0:4210 2:4211:8421 3:8422:12632";;
 serapeum-boxes) M=Serapeum-Boxes; U=serapeum-boxes-upload.mp4; LEG="";;
 fermi-paradox)  M=Fermi-Paradox; U=Fermi-Paradox-upload.mp4; LEG="";;
 oumuamua-atlas) M=Oumuamua-vs-3I-ATLAS; U=Oumuamua-vs-3I-ATLAS-upload.mp4; LEG="";;
 puma-punku) M=Puma-Punku; U=puma-punku-upload.mp4; LEG="";;
 simulation) M=Simulation-Hypothesis; U=simulation-upload.mp4; LEG="";;
 vimanas) M=Vimanas-vs-UAP-Files; U=vimanas-upload.mp4; LEG="";;
 dendera-lightbulbs) M=Dendera-Light-Bulbs; U=dendera-lightbulbs-upload.mp4; LEG="";;
 gobekli-vulture) M=Gobekli-Tepe-Vulture-Stone; U=gobekli-vulture-upload.mp4; LEG="";;
 ufo-art) M=UFOs-in-Ancient-Art; U=ufo-art-upload.mp4; LEG="";;
 *) [ -s MASTER_NAME ] || { echo "$slug: no MASTER_NAME file (master basename, e.g. Bronze-Ring)"; exit 1; }; M=$(head -1 MASTER_NAME | tr -d "[:space:]"); U=$slug-upload.mp4; LEG="";;
esac
nf(){ ffprobe -v error -count_packets -select_streams v:0 -show_entries stream=nb_read_packets -of csv=p=0 "$1" 2>/dev/null || echo 0; }
TOT=$(python3 -c "import json;print(json.load(open('timeline.json'))['total'])")
: > list.txt; pos=0
for l in $LEG; do IFS=: read n a b <<< "$l"; [ "$(nf c$n.mp4)" = "$((b-a+1))" ] || { echo "legacy c$n bad"; break; }; echo "file 'c$n.mp4'" >> list.txt; pos=$((b+1)); done
SEG=1400
while [ $pos -lt $TOT ]; do
  a=$pos; b=$((a+SEG-1)); [ $((TOT-b)) -lt 400 ] && b=$((TOT-1)); [ $b -ge $TOT ] && b=$((TOT-1))
  tag=$(printf "s%06d" $a); f=c$tag.mp4
  if [ "$(nf $f)" != "$((b-a+1))" ]; then
    echo "$slug seg $a-$b start $(date +%T)"
    flock $L bash build.sh chunk $tag $a $b > c$tag.log 2>&1
    echo "$slug seg $a-$b end $(date +%T) frames=$(nf $f)"
    [ "$(nf $f)" = "$((b-a+1))" ] || { echo "$slug seg $a FAILED"; exit 1; }
  fi
  echo "file '$f'" >> list.txt; pos=$((b+1))
done
# audio: Python re-creation of the Doc.tsx mix (dub script "mix en", validated vs Remotion mix on Ep4) — fast & restart-safe
if [ ! -s audio_mix.wav ]; then
  echo "$slug audio (python mix en) start $(date +%T)"
  mkdir -p dub; [ -n "$(ls dub/dub_*.py 2>/dev/null)" ] || cp $B/oumuamua-atlas/dub/dub_b2.py dub/dub_gen.py
  DS=$(ls dub/dub_*.py | head -1); python3 $DS mix $E en > audio.log 2>&1
  W=$(ls dub/*en-rebuild*.wav /tmp/dub*en-rebuild*.wav 2>/dev/null | head -1)
  [ -z "$W" ] && { A=$(ls dub/*en-rebuild*.m4a | head -1); ffmpeg -y -loglevel error -i "$A" -c:a pcm_s16le /tmp/en_$slug.wav; W=/tmp/en_$slug.wav; }
  cp "$W" /tmp/am_$slug.wav && cp /tmp/am_$slug.wav audio_mix.wav; rm -f dub/*en-rebuild*; echo "$slug audio end $(date +%T)"
fi
[ -s audio_mix.wav ] || { echo "$slug audio FAILED"; exit 1; }
if [ ! -s $M.mp4 ] || [ "$(nf $M.mp4)" != "$TOT" ]; then
  echo "$slug mux $(date +%T)"
  flock $L ffmpeg -y -loglevel error -f concat -safe 0 -i list.txt -i audio_mix.wav -map 0:v -map 1:a -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11 -ar 48000 -c:a aac -b:a 192k -movflags +faststart /tmp/fin_$slug.mp4 && cp /tmp/fin_$slug.mp4 $M.mp4 && rm -f /tmp/fin_$slug.mp4
  echo "$slug mux frames=$(nf $M.mp4)/$TOT"
fi
[ -s $M.srt ] || cp captions.srt $M.srt
if [ ! -s $U ]; then
  echo "$slug upload copy $(date +%T)"
  DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $M.mp4); VB=$(python3 -c "print(min(1800,int(188e6*8/$DUR/1000-192-15)))"); MR=$((VB*22/18)); echo "$slug upload vbitrate ${VB}k"
  flock $L ffmpeg -y -loglevel error -i $M.mp4 -c:v libx264 -preset veryfast -b:v ${VB}k -maxrate ${MR}k -bufsize 4000k -c:a copy -movflags +faststart /tmp/up_$slug.mp4 && cp /tmp/up_$slug.mp4 $U && rm -f /tmp/up_$slug.mp4
  ls -la $U
fi
[ -f make_shorts.py ] || echo "$slug no make_shorts.py (clips pending)"
for n in 1 2 3 4 5; do [ -f make_shorts.py ] || break; [ -s shorts/$n/clip.mp4 ] && continue; echo "$slug short $n $(date +%T)"; flock $L python3 make_shorts.py $n >> shorts.log 2>&1 || echo "$slug short $n FAIL"; done
python3 $B/finalize_ready.py $slug
echo "$slug ITEM DONE $(date +%T)"
