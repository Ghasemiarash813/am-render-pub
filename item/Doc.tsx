import React from "react";
import {
  AbsoluteFill,
  Audio,
  Img,
  Sequence,
  interpolate,
  staticFile,
  useCurrentFrame,
  Easing,
} from "remotion";
import tl from "./doc_timeline.json";

type LineT = { who: string; text: string; file: string; start: number; end: number };
type ShotT = { ch?: string[] | null; q?: string[] | null; tag?: string; id: number; fx: string; motion: string; img: string; start: number; end: number; lines: LineT[] };
const shots = tl.shots as ShotT[];
export const DOC_TOTAL = tl.total;
const XF = tl.xf;
const TAGS: Record<string, { t: string; c: string }> = { T: { t: "THEORY", c: "#F2D696" }, E: { t: "EVIDENCE", c: "#7FF6FF" }, R: { t: "RETRACTED", c: "#FF5A4E" }, V: { t: "VERDICT", c: "#FFFFFF" }, P: { t: "PARTIAL", c: "#FFB347" }, D: { t: "DEBUNKED", c: "#FF5A4E" }, U: { t: "UNVERIFIED", c: "#FFB347" }, M: { t: "METAPHOR", c: "#C9A0FF" }, L: { t: "LEGEND", c: "#C9A0FF" }, O: { t: "OBJECTION", c: "#FF8A3D" } };
const CH_IDS = shots.filter((s) => s.ch).map((s) => s.id);
const WP_LABELS = ["BOX", "P1", "P2", "P3", "P4", "P5", "P6", "FIT", "\u2605"];
const STAGE: Record<string, string> = { BOX: "THE BOX LID", FIT: "REASSEMBLY", "\u2605": "SCORECARD" };
const PIECE: Record<string, string> = { P1: "THE MAKER'S SIGNATURE", P2: "PIRI'S SOURCE LIST", P3: "A COLUMBUS MAP c. 1495", P4: "PORTUGUESE CHARTS", P5: "THE 'ANTARCTICA' EDGE", P6: "THE CAIRO LENS" };
const ROWS: [string, string, string][] = [
  ["Drawn by Piri Reis, Gallipoli, 1513", "EVIDENCE", "#7FF6FF"],
  ["Compiled from ~20 older charts", "EVIDENCE", "#7FF6FF"],
  ["Preserves a lost Columbus map", "EVIDENCE", "#7FF6FF"],
  ["South edge = bent Brazil + Terra Australis", "MOST LIKELY", "#FFB347"],
  ["Ice-free Antarctic coastline", "DEBUNKED", "#FF5A4E"],
  ["Photo 'from space' above Cairo", "DEBUNKED", "#FF5A4E"],
  ["Aliens or a lost Ice-Age civilisation", "NOT NEEDED", "#FF5A4E"],
];
const SCORE_IDS = shots.filter((s) => s.fx === "score").map((s) => s.id);

const allLines = shots.flatMap((s) => s.lines);
const speaking = (f: number) => allLines.some((l) => f >= l.start - 4 && f < l.end + 4);

// deterministic pseudo random
const rnd = (i: number) => {
  const x = Math.sin(i * 12.9898 + 78.233) * 43758.5453;
  return x - Math.floor(x);
};

const Dust: React.FC<{ f: number; warm?: boolean }> = ({ f, warm = true }) => (
  <AbsoluteFill style={{ pointerEvents: "none" }}>
    <svg width={1920} height={1080}>
      {new Array(45).fill(0).map((_, i) => {
        const x = (rnd(i) * 1920 + f * (0.3 + rnd(i + 3) * 0.6)) % 1920;
        const y = (rnd(i + 7) * 1080 - f * (0.15 + rnd(i + 9) * 0.3) + 2000) % 1080;
        const r = 1 + rnd(i + 11) * 3.2;
        const o = 0.15 + 0.45 * Math.abs(Math.sin(f / (25 + rnd(i) * 30) + i));
        return <circle key={i} cx={x} cy={y} r={r} fill={warm ? "#FFE3B0" : "#BFF8FF"} opacity={o} />;
      })}
    </svg>
  </AbsoluteFill>
);

const Sand: React.FC<{ f: number }> = ({ f }) => (
  <AbsoluteFill style={{ pointerEvents: "none" }}>
    <svg width={1920} height={1080}>
      {new Array(30).fill(0).map((_, i) => {
        const x = (rnd(i) * 2200 + f * (3 + rnd(i + 1) * 4)) % 2200 - 200;
        const y = 650 + rnd(i + 5) * 430 + Math.sin(f / 20 + i) * 8;
        const w = 30 + rnd(i + 2) * 90;
        return <rect key={i} x={x} y={y} width={w} height={1.6} rx={1} fill="#FFE6B8" opacity={0.18 + rnd(i + 4) * 0.25} />;
      })}
    </svg>
  </AbsoluteFill>
);

const Glow: React.FC<{ f: number }> = ({ f }) => {
  const p = 0.5 + 0.5 * Math.sin(f / 18);
  return (
    <>
      <AbsoluteFill
        style={{
          background: "radial-gradient(circle at 50% 45%, rgba(63,243,255,0.22) 0%, rgba(63,243,255,0) 55%)",
          mixBlendMode: "screen",
          opacity: 0.4 + 0.6 * p,
        }}
      />
      <Dust f={f} warm={false} />
    </>
  );
};

const Stars: React.FC<{ f: number }> = ({ f }) => (
  <AbsoluteFill style={{ pointerEvents: "none" }}>
    <svg width={1920} height={1080}>
      {new Array(28).fill(0).map((_, i) => {
        const x = rnd(i + 20) * 1920;
        const y = rnd(i + 40) * 480;
        const o = Math.max(0, Math.sin(f / (10 + rnd(i) * 20) + i * 3)) ** 3;
        const s = 6 + rnd(i + 2) * 8;
        return (
          <g key={i} transform={`translate(${x},${y})`} opacity={o * 0.9}>
            <rect x={-s} y={-0.8} width={s * 2} height={1.6} fill="white" />
            <rect x={-0.8} y={-s} width={1.6} height={s * 2} fill="white" />
            <circle r={1.8} fill="white" />
          </g>
        );
      })}
    </svg>
  </AbsoluteFill>
);

const Scorecard: React.FC<{ s: ShotT; frame: number }> = ({ s, frame }) => {
  const k = SCORE_IDS.indexOf(s.id);
  const len = s.end - s.start;
  const ap = (t: number) => interpolate(frame, [t, t + 15], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const shown = (i: number) => {
    if (k === 0) return 0;
    if (k === 1) return i > 3 ? 0 : ap(30 + (i * (len - 90)) / 4);
    if (i <= 3) return 1;
    return ap(30 + ((i - 4) * (len - 90)) / 3);
  };
  const o = k === 0 ? interpolate(frame, [10, 35], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }) : 1;
  return (
    <div style={{ position: "absolute", left: 110, top: 150, width: 1150, padding: "28px 40px", background: "rgba(4,10,16,0.80)", border: "2px solid rgba(127,246,255,0.5)", borderRadius: 18, fontFamily: "Georgia, serif", opacity: o, boxShadow: "0 0 60px rgba(63,243,255,0.15)" }}>
      <div style={{ fontFamily: "'Courier New', monospace", fontSize: 24, letterSpacing: 6, color: "#7FF6FF" }}>THE JIGSAW {"\u00b7"} SCORECARD</div>
      <div style={{ fontSize: 50, fontWeight: 700, color: "#F2D696", margin: "6px 0 16px" }}>The Piri Reis Map: What Fits?</div>
      {ROWS.map((r, i) => (
        <div key={i} style={{ display: "flex", justifyContent: "space-between", alignItems: "center", height: 64, borderTop: "1px solid rgba(255,255,255,0.12)", opacity: shown(i), transform: `translateX(${(1 - shown(i)) * -30}px)` }}>
          <div style={{ fontSize: 32, color: "#F4F1EA" }}>{r[0]}</div>
          <div style={{ fontFamily: "'Courier New', monospace", fontSize: 28, fontWeight: 700, letterSpacing: 4, color: r[2], border: `2px solid ${r[2]}`, padding: "4px 14px", minWidth: 210, textAlign: "center" }}>{r[1]}</div>
        </div>
      ))}
    </div>
  );
};

const Piece: React.FC<{ on: boolean; cur: boolean; n: number }> = ({ on, cur, n }) => {
  const col = on ? "#F2D696" : "rgba(255,255,255,0.35)";
  return (
    <svg width={58} height={58} viewBox="0 0 58 58">
      <path
        d="M6 6 H22 a7 7 0 0 1 14 0 H52 V22 a7 7 0 0 1 0 14 V52 H36 a7 7 0 0 0 -14 0 H6 V36 a7 7 0 0 0 0 -14 Z"
        fill={cur ? "#F2D696" : on ? "rgba(242,214,150,0.35)" : "rgba(0,0,0,0.5)"}
        stroke={col}
        strokeWidth={2}
      />
      <text x={29} y={35} textAnchor="middle" fontFamily="'Courier New', monospace" fontSize={18} fontWeight={700} fill={cur ? "#111" : "#F4F1EA"}>{n}</text>
    </svg>
  );
};

const Hud: React.FC<{ s: ShotT; frame: number }> = ({ s, frame }) => {
  const idx = CH_IDS.filter((c) => c <= s.id).length - 1;
  const lb = idx >= 0 ? WP_LABELS[idx] : "";
  const placed = Math.max(0, Math.min(6, idx));
  const o = interpolate(frame, [XF, XF + 20, 175, 200], [0, 1, 1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  return (
    <div style={{ position: "absolute", top: 84, right: 70, opacity: o, fontFamily: "'Courier New', monospace", color: "#BFF8FF", display: "flex", flexDirection: "column", alignItems: "flex-end" }}>
      <div style={{ fontSize: 20, letterSpacing: 5, marginBottom: 10, color: "#E8FDFF", textShadow: "0 0 8px rgba(0,0,0,1), 0 2px 12px rgba(0,0,0,0.9)" }}>ANCIENT MACHINES {"\u00b7"} THE JIGSAW</div>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 58px)", gap: 2, padding: 8, background: "rgba(0,0,0,0.45)", border: "1px solid rgba(242,214,150,0.4)", borderRadius: 8 }}>
        {[1, 2, 3, 4, 5, 6].map((n) => (
          <Piece key={n} n={n} on={n <= placed || lb === "FIT" || lb === "\u2605"} cur={lb === "P" + n} />
        ))}
      </div>
      <div style={{ marginTop: 8, fontSize: 18, letterSpacing: 3, color: "#F2D696", textShadow: "0 0 8px rgba(0,0,0,1)" }}>
        {STAGE[lb] ? STAGE[lb] : "PIECES PLACED " + placed + " / 6"}
      </div>
    </div>
  );
};

const Quote: React.FC<{ q: string[]; frame: number; len: number }> = ({ q, frame, len }) => {
  const o = interpolate(frame, [XF + 25, XF + 45, len - 30, len - 10], [0, 1, 1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  return (
    <div style={{ position: "absolute", left: 70, bottom: 92, width: 1080, padding: "20px 28px", background: "rgba(10,8,4,0.78)", borderLeft: "4px solid #F2D696", borderRadius: 6, opacity: o, transform: `translateY(${(1 - o) * 14}px)`, boxShadow: "0 6px 40px rgba(0,0,0,0.6)" }}>
      <div style={{ fontFamily: "Georgia, serif", fontStyle: "italic", fontSize: 34, lineHeight: 1.3, color: "#F7EBD0" }}>{q[0]}</div>
      <div style={{ marginTop: 12, fontFamily: "'Courier New', monospace", fontSize: 19, letterSpacing: 2, color: "#7FF6FF" }}>{"\u2014 " + q[1]}</div>
    </div>
  );
};

const Shot: React.FC<{ s: ShotT }> = ({ s }) => {
  const frame = useCurrentFrame(); // local to sequence
  const len = s.end - s.start;
  const p = interpolate(frame, [0, len], [0, 1], { easing: Easing.inOut(Easing.sin) });
  let scale = 1.08,
    tx = 0,
    ty = 0;
  switch (s.motion) {
    case "in":
      scale = 1.02 + 0.08 * p;
      break;
    case "out":
      scale = 1.10 - 0.08 * p;
      break;
    case "left":
      scale = 1.1;
      tx = 2 - 4 * p;
      break;
    case "right":
      scale = 1.1;
      tx = -2 + 4 * p;
      break;
    case "up":
      scale = 1.1;
      ty = 2 - 4 * p;
      break;
  }
  const fadeIn = interpolate(frame, [0, XF], [0, 1], { extrapolateRight: "clamp" });
  return (
    <AbsoluteFill style={{ opacity: s.id === 1 ? interpolate(frame, [0, 30], [0, 1], { extrapolateRight: "clamp" }) : fadeIn }}>
      <AbsoluteFill style={{ overflow: "hidden" }}>
        <Img
          src={staticFile(s.img)}
          style={{
            width: "100%",
            height: "100%",
            objectFit: "cover",
            transform: `scale(${scale}) translate(${tx}%, ${ty}%)`,
          }}
        />
      </AbsoluteFill>
      {s.fx === "dust" && <Dust f={frame} />}
      {s.fx === "sand" && <Sand f={frame} />}
      {s.fx === "glow" && <Glow f={frame} />}
      {s.fx === "stars" && <Stars f={frame} />}
      {s.tag && TAGS[s.tag] && s.fx !== "score" && (
        <div style={{ position: "absolute", top: 86, left: 70, padding: "8px 18px", border: `2px solid ${TAGS[s.tag].c}`, color: TAGS[s.tag].c, fontFamily: "Georgia, serif", fontSize: 30, letterSpacing: 6, background: "rgba(0,0,0,0.55)", opacity: interpolate(frame, [XF, XF + 15], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }) }}>{TAGS[s.tag].t}</div>
      )}
      {(() => {
        const ci = CH_IDS.filter((c) => c <= s.id).length - 1;
        const lb = ci >= 0 ? WP_LABELS[ci] : "";
        if (s.fx === "score" || !PIECE[lb]) return null;
        const col = "#F2D696";
        return (
          <div style={{ position: "absolute", bottom: 78, right: 70, padding: "6px 14px", border: `2px solid ${col}`, color: col, fontFamily: "'Courier New', monospace", fontSize: 22, letterSpacing: 4, background: "rgba(0,0,0,0.55)", opacity: interpolate(frame, [XF, XF + 15], [0, 0.9], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }) }}>
            {"PIECE " + lb.slice(1) + " \u00b7 " + PIECE[lb]}
          </div>
        );
      })()}
      {s.q && s.fx !== "score" && <Quote q={s.q} frame={frame} len={len} />}
      {s.fx === "score" && <Scorecard s={s} frame={frame} />}
      {s.ch && s.fx !== "score" && <Hud s={s} frame={frame} />}
      {s.ch && s.fx !== "score" && (
        <div style={{ position: "absolute", bottom: 110, left: 70, fontFamily: "Georgia, serif", opacity: interpolate(frame, [XF, XF + 20, 175, 200], [0, 1, 1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }) }}>
          <div style={{ fontSize: 26, letterSpacing: 8, color: "#7FF6FF" }}>{s.ch[0]}</div>
          <div style={{ width: 420, height: 2, background: "linear-gradient(90deg, #F2D696, transparent)", margin: "10px 0" }} />
          <div style={{ fontSize: 56, fontWeight: 700, color: "#F2D696", textShadow: "0 4px 20px rgba(0,0,0,0.9)" }}>{s.ch[1]}</div>
          <div style={{ marginTop: 10, fontFamily: "'Courier New', monospace", fontSize: 22, letterSpacing: 3, color: "#BFF8FF", textShadow: "0 2px 10px rgba(0,0,0,0.9)" }}>{s.ch[2]}</div>
        </div>
      )}
    </AbsoluteFill>
  );
};


const TitleCard: React.FC = () => {
  const frame = useCurrentFrame();
  const o = interpolate(frame, [0, 25, 100, 125], [0, 1, 1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const sp = interpolate(frame, [0, 125], [14, 26]);
  return (
    <AbsoluteFill style={{ justifyContent: "center", alignItems: "center", opacity: o, background: "rgba(0,0,0,0.55)" }}>
      <div style={{ textAlign: "center", fontFamily: "Georgia, 'Times New Roman', serif" }}>
        <div style={{ fontSize: 120, fontWeight: 700, letterSpacing: sp, color: "#F2D696", textShadow: "0 6px 30px rgba(0,0,0,0.9)" }}>ANCIENT MACHINES</div>
        <div style={{ width: 520, height: 2, background: "linear-gradient(90deg, transparent, #7FF6FF, transparent)", margin: "26px auto" }} />
        <div style={{ fontSize: 44, letterSpacing: 4, color: "#BFF8FF" }}>CASE FILE · THE PIRI REIS MAP, TAKEN APART</div>
      </div>
    </AbsoluteFill>
  );
};

export const Doc: React.FC = () => {
  const s2 = shots.find((s) => s.id === (tl as any).titleAfter)!;
  const s2LastEnd = s2.lines[s2.lines.length - 1].end;
  const sfx: { at: number; file: string; vol: number }[] = [];
  shots.forEach((s) => {
    if (s.ch) sfx.push({ at: s.start, file: "whoosh.wav", vol: 0.35 });
    const k = SCORE_IDS.indexOf(s.id);
    const len = s.end - s.start;
    if (k === 1) [0, 1, 2, 3].forEach((i) => sfx.push({ at: s.start + Math.round(30 + (i * (len - 90)) / 4), file: "beep.wav", vol: 0.25 }));
    if (k === 2) [0, 1, 2].forEach((j) => sfx.push({ at: s.start + Math.round(30 + (j * (len - 90)) / 3), file: "beep.wav", vol: 0.25 }));
  });
  sfx.push({ at: s2LastEnd + 6, file: "whoosh.wav", vol: 0.5 });
  return (
    <AbsoluteFill style={{ backgroundColor: "black" }}>
      {shots.map((s) => (
        <Sequence key={s.id} from={s.start} durationInFrames={s.end - s.start}>
          <Shot s={s} />
        </Sequence>
      ))}
      <Sequence from={s2LastEnd + 6} durationInFrames={125}>
        <TitleCard />
      </Sequence>
      {/* film look: vignette + subtle warm grade */}
      <AbsoluteFill
        style={{
          background: "radial-gradient(ellipse at center, rgba(0,0,0,0) 55%, rgba(0,0,0,0.5) 100%)",
          pointerEvents: "none",
        }}
      />
      <AbsoluteFill style={{ background: "rgba(255,170,90,0.04)", mixBlendMode: "overlay", pointerEvents: "none" }} />
      <AbsoluteFill style={{ pointerEvents: "none" }}>
        <div style={{ position: "absolute", top: 0, left: 0, right: 0, height: 56, background: "black" }} />
        <div style={{ position: "absolute", bottom: 0, left: 0, right: 0, height: 56, background: "black" }} />
      </AbsoluteFill>
      {/* fade out end */}
      <AbsoluteFill
        style={{ background: "black", opacity: interpolate(useCurrentFrame(), [DOC_TOTAL - 50, DOC_TOTAL - 5], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }) }}
      />

      <Audio src={staticFile("ep/music.wav")} volume={(f) => (speaking(f) ? 0.13 : 0.3)} />
      {allLines.map((l, i) => (
        <Sequence key={i} from={l.start} durationInFrames={l.end - l.start + 15}>
          <Audio src={staticFile(l.file)} />
        </Sequence>
      ))}
      {sfx.map((x, i) => (
        <Sequence key={`sfx${i}`} from={x.at} durationInFrames={45}>
          <Audio src={staticFile(x.file)} volume={x.vol} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
