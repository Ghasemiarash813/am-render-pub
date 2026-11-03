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
type ShotT = { ch?: string[] | null; tag?: string; id: number; fx: string; motion: string; img: string; start: number; end: number; lines: LineT[] };
const shots = tl.shots as ShotT[];
export const DOC_TOTAL = tl.total;
const XF = tl.xf;
const TAGS: Record<string, { t: string; c: string }> = { T: { t: "THEORY", c: "#F2D696" }, E: { t: "EVIDENCE", c: "#7FF6FF" }, R: { t: "RETRACTED", c: "#FF5A4E" }, V: { t: "VERDICT", c: "#FFFFFF" }, P: { t: "PARTIAL", c: "#FFB347" }, D: { t: "DEBUNKED", c: "#FF5A4E" }, U: { t: "UNVERIFIED", c: "#FFB347" }, M: { t: "MODERN MYTH", c: "#FF8A5C" }, L: { t: "LEGEND", c: "#C9A0FF" }, X: { t: "EXPERIMENT", c: "#9CFF8A" }, C: { t: "CHRONICLE", c: "#E8C3FF" }, A: { t: "ANALYSIS", c: "#9CFF8A" }, N: { t: "UNPROVEN", c: "#FFB347" } };
const CH_IDS = shots.filter((s) => s.ch).map((s) => s.id);
const WP_LABELS = ["INT", "PRS", "INV", "PAT", "CRB", "SOL", "FOR", "ALN", "DEBRIEF"];
const ITEM: Record<string, string> = { INT: "PAGE 1 \u00b7 THE INTERCEPT", PRS: "PAGE 2 \u00b7 THE PRESS", INV: "PAGE 3 \u00b7 INVENTORY", PAT: "PAGE 4 \u00b7 PATTERNS", CRB: "PAGE 5 \u00b7 CRIBS", SOL: "PAGE 6 \u00b7 SOLUTIONS", FOR: "PAGE 7 \u00b7 COUNTERFEIT", ALN: "PAGE 8 \u00b7 ALIEN HYPOTHESIS" };
const CODE = ["PAGE 1", "PAGE 2", "PAGE 3", "PAGE 4", "PAGE 5", "PAGE 6", "PAGE 7", "PAGE 8"];
const ROWS: [string, string, string][] = [
  ["Genuine Minoan object, c. 1700 BC", "EVIDENCE", "#7FF6FF"],
  ["Stamped with 45 punches (early printing)", "EVIDENCE", "#7FF6FF"],
  ["A real script, probably syllabic", "LIKELY", "#9CFF8A"],
  ["A hymn or prayer", "OPEN", "#FFB347"],
  ["\u201cDeciphered\u201d by any claimant", "UNPROVEN", "#FF5A4E"],
  ["A modern forgery (1908)", "UNLIKELY", "#FF5A4E"],
  ["Alien message or star map", "NO EVIDENCE", "#FF5A4E"],
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
      <div style={{ fontFamily: "'Courier New', monospace", fontSize: 24, letterSpacing: 6, color: "#7FF6FF" }}>CODEBREAKER’S NOTEBOOK {"\u00b7"} DEBRIEF</div>
      <div style={{ fontSize: 50, fontWeight: 700, color: "#F2D696", margin: "6px 0 16px" }}>Phaistos Disc: Message or Mystery?</div>
      {ROWS.map((r, i) => (
        <div key={i} style={{ display: "flex", justifyContent: "space-between", alignItems: "center", height: 64, borderTop: "1px solid rgba(255,255,255,0.12)", opacity: shown(i), transform: `translateX(${(1 - shown(i)) * -30}px)` }}>
          <div style={{ fontSize: 34, color: "#F4F1EA" }}>{r[0]}</div>
          <div style={{ fontFamily: "'Courier New', monospace", fontSize: 28, fontWeight: 700, letterSpacing: 4, color: r[2], border: `2px solid ${r[2]}`, padding: "4px 14px", minWidth: 230, textAlign: "center" }}>{r[1]}</div>
        </div>
      ))}
    </div>
  );
};

const Hud: React.FC<{ s: ShotT; frame: number }> = ({ s, frame }) => {
  const idx = Math.max(0, CH_IDS.filter((c) => c <= s.id).length - 1);
  const o = interpolate(frame, [XF, XF + 20, 175, 200], [0, 1, 1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  // a codebreaker's notebook: 8 page tabs (finished pages ticked, current one fills gold), a spiral that draws itself,
  // and a "DECODED" meter that never moves past 0%
  const N = 8;
  const W = 470;
  const bw = 44;
  const gap = (W - 44 - N * bw) / (N - 1);
  const bx = (i: number) => 22 + i * (bw + gap);
  const k = interpolate(frame, [XF, XF + 70], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.inOut(Easing.cubic) });
  const blink = Math.floor(frame / 12) % 2 === 0 ? 1 : 0.3;
  const turns = 3.2;
  const pts: string[] = [];
  const steps = Math.max(2, Math.round(80 * k));
  for (let i = 0; i <= steps; i++) {
    const t = (i / 80) * turns * 2 * Math.PI;
    const r = 22 - (i / 80) * 20;
    pts.push(`${250 + r * Math.cos(-t + frame / 40)},${38 + r * Math.sin(-t + frame / 40)}`);
  }
  const flick = Math.floor(frame / 6) % 7 === 0 ? 1 : 0;
  return (
    <div style={{ position: "absolute", top: 84, right: 70, opacity: o, fontFamily: "'Courier New', monospace", color: "#BFF8FF" }}>
      <div style={{ fontSize: 20, letterSpacing: 5, textAlign: "right", marginBottom: 10, color: "#E8FDFF", textShadow: "0 0 8px rgba(0,0,0,1), 0 2px 12px rgba(0,0,0,0.9)" }}>ANCIENT MACHINES {"\u00b7"} CODEBREAKER{"\u2019"}S NOTEBOOK</div>
      <svg width={W} height={170} style={{ display: "block", marginLeft: "auto", background: "rgba(0,0,0,0.6)", borderRadius: 12 }}>
        <circle cx={30} cy={36} r={7} fill="#FF5A4E" opacity={blink} />
        <text x={46} y={44} fontFamily="'Courier New', monospace" fontSize={19} fontWeight={700} fill="#FF8A5C">DECODED {flick ? "?" : "0"}%</text>
        <polyline points={pts.join(" ")} fill="none" stroke="#F2D696" strokeWidth={2} strokeLinecap="round" />
        <circle cx={250} cy={38} r={24} fill="none" stroke="rgba(242,214,150,0.35)" strokeWidth={1.5} />
        <rect x={W - 150} y={14} width={132} height={44} rx={6} fill="rgba(10,20,26,0.9)" stroke="#F2D696" strokeWidth={1.5} />
        <text x={W - 84} y={45} textAnchor="middle" fontFamily="'Courier New', monospace" fontSize={24} fontWeight={700} fill="#F2D696">{CODE[Math.min(idx, N - 1)]}</text>
        {WP_LABELS.slice(0, N).map((l, i) => {
          const x = bx(i);
          const done = i < idx;
          const cur = i === idx;
          const fill = cur ? k : done ? 1 : 0;
          return (
            <g key={i}>
              <rect x={x} y={82} width={bw} height={34} rx={4} fill="rgba(255,255,255,0.06)" stroke={cur ? "#F2D696" : done ? "#7FF6FF" : "rgba(255,255,255,0.35)"} strokeWidth={cur ? 2.5 : 1.5} />
              <rect x={x + 2} y={84} width={(bw - 4) * fill} height={30} rx={3} fill={cur ? "rgba(242,214,150,0.55)" : "rgba(127,246,255,0.22)"} />
              {done && <polyline points={`${x + 12},${99} ${x + 19},${107} ${x + 32},${90}`} fill="none" stroke="#7FF6FF" strokeWidth={3} strokeLinecap="round" />}
              <text x={x + bw / 2} y={142} textAnchor="middle" fontFamily="Georgia, serif" fontSize={15} fontWeight={700} fill={cur ? "#F2D696" : "#F4F1EA"} style={{ paintOrder: "stroke", stroke: "rgba(0,0,0,0.9)", strokeWidth: 4 }}>{l}</text>
            </g>
          );
        })}
      </svg>
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
        if (s.fx === "score" || !ITEM[lb]) return null;
        const col = "#F2D696";
        return (
          <div style={{ position: "absolute", bottom: 78, right: 70, padding: "6px 14px", border: `2px solid ${col}`, color: col, fontFamily: "'Courier New', monospace", fontSize: 22, letterSpacing: 4, background: "rgba(0,0,0,0.55)", opacity: interpolate(frame, [XF, XF + 15], [0, 0.9], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }) }}>
            {"NOTEBOOK \u00b7 " + ITEM[lb]}
          </div>
        );
      })()}
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
        <div style={{ fontSize: 44, letterSpacing: 4, color: "#BFF8FF" }}>CASE FILE · THE CODEBREAKER’S NOTEBOOK</div>
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
