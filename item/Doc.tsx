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
const TAGS: Record<string, { t: string; c: string }> = { T: { t: "THEORY", c: "#F2D696" }, E: { t: "EVIDENCE", c: "#7FF6FF" }, R: { t: "RETRACTED", c: "#FF5A4E" }, V: { t: "VERDICT", c: "#FFFFFF" }, P: { t: "PARTIAL", c: "#FFB347" }, D: { t: "DEBUNKED", c: "#FF5A4E" }, U: { t: "UNVERIFIED", c: "#FFB347" }, M: { t: "METAPHOR", c: "#C9A0FF" }, L: { t: "LEGEND", c: "#C9A0FF" }, C: { t: "CONTESTED", c: "#FF9F5A" } };
const CH_IDS = shots.filter((s) => s.ch).map((s) => s.id);
const WP_LABELS = ["B", "L1", "L2", "L3", "L4", "L5", "L6", "\u2605"];
const LAYERS: [string, string, string][] = [
  ["BRIEFING", "THE CLAIM", "#BFF8FF"],
  ["LAYER 1", "MODERN SKIN \u00b7 1817\u2013TODAY", "#E9D9B0"],
  ["LAYER 2", "ROMAN \u00b7 SAITE", "#D9BC86"],
  ["LAYER 3", "NEW KINGDOM \u00b7 c.1400 BC", "#C99A5B"],
  ["LAYER 4", "OLD KINGDOM \u00b7 c.2500 BC", "#B47A3E"],
  ["LAYER 5", "THE ROCK \u00b7 50 MILLION YRS", "#93602F"],
  ["LAYER 6", "BEDROCK ZERO \u00b7 10,500 BC?", "#7A4A2A"],
  ["CORE", "SCORECARD & VERDICT", "#F2D696"],
];
const ROWS: [string, string, string][] = [
  ["Enclosure walls are deeply weathered", "EVIDENCE", "#7FF6FF"],
  ["Only centuries of rain could do it", "CONTESTED", "#FF9F5A"],
  ["Heavy rain ended before 3000 BC", "DEBUNKED", "#FF5A4E"],
  ["Sphinx + temples cut in one quarry project", "EVIDENCE", "#7FF6FF"],
  ["Carved in 10,500 BC to face Leo", "DEBUNKED", "#FF5A4E"],
  ["Lost or alien builders", "NO EVIDENCE", "#FF5A4E"],
  ["Which 4th-dynasty king (Khafre/Khufu)", "OPEN", "#FFB347"],
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
      <div style={{ fontFamily: "'Courier New', monospace", fontSize: 24, letterSpacing: 6, color: "#7FF6FF" }}>CORE SAMPLE {"\u00b7"} 6 LAYERS</div>
      <div style={{ fontSize: 50, fontWeight: 700, color: "#F2D696", margin: "6px 0 16px" }}>The Sphinx Age Scorecard</div>
      {ROWS.map((r, i) => (
        <div key={i} style={{ display: "flex", justifyContent: "space-between", alignItems: "center", height: 64, borderTop: "1px solid rgba(255,255,255,0.12)", opacity: shown(i), transform: `translateX(${(1 - shown(i)) * -30}px)` }}>
          <div style={{ fontSize: 34, color: "#F4F1EA" }}>{r[0]}</div>
          <div style={{ fontFamily: "'Courier New', monospace", fontSize: 28, fontWeight: 700, letterSpacing: 4, color: r[2], border: `2px solid ${r[2]}`, padding: "4px 14px", minWidth: 190, textAlign: "center" }}>{r[1]}</div>
        </div>
      ))}
    </div>
  );
};

const Hud: React.FC<{ s: ShotT; frame: number }> = ({ s, frame }) => {
  const idx = CH_IDS.filter((c) => c <= s.id).length - 1;
  const o = interpolate(frame, [XF, XF + 20, 175, 200], [0, 1, 1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  return (
    <div style={{ position: "absolute", top: 80, right: 70, opacity: o, fontFamily: "'Courier New', monospace", color: "#BFF8FF", width: 400 }}>
      <div style={{ fontSize: 19, letterSpacing: 5, textAlign: "right", marginBottom: 10, color: "#E8FDFF", textShadow: "0 0 8px rgba(0,0,0,1), 0 2px 12px rgba(0,0,0,0.9)" }}>ANCIENT MACHINES {"\u00b7"} CORE SAMPLE</div>
      <div style={{ border: "2px solid rgba(242,214,150,0.6)", borderRadius: 10, overflow: "hidden", background: "rgba(0,0,0,0.55)" }}>
        {LAYERS.map((l, i) => (
          <div key={i} style={{ display: "flex", alignItems: "center", height: 34, background: i === idx ? l[2] : i < idx ? "rgba(255,255,255,0.06)" : "transparent", borderTop: i ? `2px solid ${l[2]}55` : "none", color: i === idx ? "#111" : i < idx ? "rgba(244,241,234,0.55)" : "#F4F1EA" }}>
            <div style={{ width: 8, alignSelf: "stretch", background: l[2] }} />
            <div style={{ width: 120, paddingLeft: 10, fontSize: 16, fontWeight: 700, letterSpacing: 2 }}>{l[0]}</div>
            <div style={{ flex: 1, fontSize: 14, letterSpacing: 1, whiteSpace: "nowrap" }}>{l[1]}</div>
            <div style={{ width: 26, fontSize: 18, fontWeight: 700 }}>{i === idx ? "\u25c0" : ""}</div>
          </div>
        ))}
      </div>
    </div>
  );
};

const DepthGauge: React.FC<{ s: ShotT; frame: number }> = ({ s, frame }) => {
  const idx = CH_IDS.filter((c) => c <= s.id).length - 1;
  if (idx < 0) return null;
  const top = 230, h = 620, step = h / (LAYERS.length - 1);
  const y = top + idx * step;
  const o = interpolate(frame, [XF, XF + 15], [0, 0.85], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  return (
    <div style={{ position: "absolute", left: 0, top: 0, width: 80, height: 1080, opacity: o, pointerEvents: "none" }}>
      <div style={{ position: "absolute", left: 34, top, width: 3, height: h, background: "linear-gradient(180deg, #E9D9B0, #7A4A2A)" }} />
      {LAYERS.map((l, i) => (
        <div key={i} style={{ position: "absolute", left: 26, top: top + i * step - 1, width: 19, height: 3, background: l[2] }} />
      ))}
      <div style={{ position: "absolute", left: 22, top: y - 13, width: 0, height: 0, borderTop: "13px solid transparent", borderBottom: "13px solid transparent", borderLeft: "20px solid #F2D696", filter: "drop-shadow(0 0 6px rgba(242,214,150,0.9))" }} />
      <div style={{ position: "absolute", left: 14, top: top - 40, fontFamily: "'Courier New', monospace", fontSize: 15, letterSpacing: 2, color: "#E9D9B0", textShadow: "0 2px 6px #000" }}>DEPTH</div>
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
        if (s.fx === "score" || ci < 1 || ci > 6) return null;
        const col = LAYERS[ci][2];
        return (
          <div style={{ position: "absolute", bottom: 78, right: 70, padding: "6px 14px", border: `2px solid ${col}`, color: col, fontFamily: "'Courier New', monospace", fontSize: 22, letterSpacing: 4, background: "rgba(0,0,0,0.6)", opacity: interpolate(frame, [XF, XF + 15], [0, 0.9], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }) }}>
            CORE {"\u25bc"} {LAYERS[ci][0]} {"\u00b7"} {LAYERS[ci][1]}
          </div>
        );
      })()}
      {s.fx !== "score" && <DepthGauge s={s} frame={frame} />}
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
        <div style={{ fontSize: 44, letterSpacing: 4, color: "#BFF8FF" }}>CORE SAMPLE · HOW OLD IS THE SPHINX?</div>
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
