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
const TAGS: Record<string, { t: string; c: string }> = { T: { t: "THEORY", c: "#F2D696" }, E: { t: "EVIDENCE", c: "#7FF6FF" }, R: { t: "RETRACTED", c: "#FF5A4E" }, V: { t: "VERDICT", c: "#FFFFFF" }, P: { t: "PARTIAL", c: "#FFB347" }, D: { t: "DEBUNKED", c: "#FF5A4E" }, U: { t: "UNVERIFIED", c: "#FFB347" }, M: { t: "METAPHOR", c: "#C9A0FF" }, L: { t: "LEGEND", c: "#C9A0FF" }, X: { t: "EXPERIMENT", c: "#9CFF8A" }, C: { t: "CHRONICLE", c: "#E8C3FF" } };
const CH_IDS = shots.filter((s) => s.ch).map((s) => s.id);
const WP_LABELS = ["I", "II", "III", "IV", "V", "VI", "VII", "L"];
const STATION: Record<string, string> = { I: "SITE SURVEY", II: "GROUND REPORT", III: "THE WALLS", IV: "THE BASEMENT", V: "THE WIRING", VI: "DATE STAMP", VII: "REAL TENANTS" };
// result stamp shown against each finished inspection item
const RESULT: Record<string, [string, string]> = { I: ["NATURAL", "#7FF6FF"], II: ["NATURAL", "#7FF6FF"], III: ["NATURAL", "#7FF6FF"], IV: ["OPEN", "#FFB347"], V: ["FAIL", "#FF5A4E"], VI: ["FAIL", "#FF5A4E"], VII: ["MEDIEVAL", "#9CFF8A"] };
const ROWS: [string, string, string][] = [
  ["Same lake-bed layers as the hills around it", "EVIDENCE", "#7FF6FF"],
  ["Block size matches natural layer thickness", "EVIDENCE", "#7FF6FF"],
  ["Medieval Visoki & Roman remains on the summit", "EVIDENCE", "#7FF6FF"],
  ["\u201cTerraces\u201d carved by the digs themselves", "LIKELY", "#9CFF8A"],
  ["World\u2019s largest pyramid, 12\u201334,000 yrs old", "DEBUNKED", "#FF5A4E"],
  ["28 kHz energy beam / alien links", "NO EVIDENCE", "#FF5A4E"],
  ["Who dug the Ravne tunnels, and when", "OPEN", "#FFB347"],
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
      <div style={{ fontFamily: "'Courier New', monospace", fontSize: 24, letterSpacing: 6, color: "#7FF6FF" }}>THE BUILDING INSPECTION {"\u00b7"} CERTIFICATE</div>
      <div style={{ fontSize: 50, fontWeight: 700, color: "#F2D696", margin: "6px 0 16px" }}>Visoko: Pyramid or Natural Hill?</div>
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
  // an inspection checklist: finished items get their result stamp, the current item gets a stamp that thumps down
  const items = WP_LABELS.map((l) => (l === "L" ? "CERTIFICATE" : STATION[l]));
  const stampIn = interpolate(frame, [XF + 30, XF + 42], [2.2, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.back(2)) });
  const stampO = interpolate(frame, [XF + 30, XF + 36], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  return (
    <div style={{ position: "absolute", top: 84, right: 70, opacity: o, fontFamily: "'Courier New', monospace", color: "#BFF8FF" }}>
      <div style={{ fontSize: 20, letterSpacing: 5, textAlign: "right", marginBottom: 10, color: "#E8FDFF", textShadow: "0 0 8px rgba(0,0,0,1), 0 2px 12px rgba(0,0,0,0.9)" }}>ANCIENT MACHINES {"\u00b7"} BUILDING INSPECTION</div>
      <div style={{ width: 430, marginLeft: "auto", background: "rgba(0,0,0,0.62)", borderRadius: 12, padding: "12px 16px", border: "1px solid rgba(242,214,150,0.35)" }}>
        {items.map((t, i) => {
          const done = i < idx;
          const cur = i === idx;
          const lb = WP_LABELS[i];
          const r = RESULT[lb];
          return (
            <div key={i} style={{ display: "flex", alignItems: "center", height: 26, fontSize: 17, letterSpacing: 2, color: cur ? "#F2D696" : done ? "#F4F1EA" : "rgba(255,255,255,0.45)", fontWeight: cur ? 700 : 400 }}>
              <div style={{ width: 18, height: 18, border: `2px solid ${cur ? "#F2D696" : done ? "#D9B97A" : "rgba(255,255,255,0.4)"}`, marginRight: 12, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 14, color: "#F2D696" }}>{done ? "\u2713" : ""}</div>
              <div style={{ width: 44 }}>{lb === "L" ? "" : lb}</div>
              <div style={{ flex: 1 }}>{t}</div>
              {done && r && <div style={{ fontSize: 13, letterSpacing: 2, color: r[1], border: `1.5px solid ${r[1]}`, padding: "0 6px", transform: "rotate(-4deg)" }}>{r[0]}</div>}
              {cur && <div style={{ fontSize: 13, letterSpacing: 2, color: "#F2D696", border: "2px solid #F2D696", padding: "0 6px", opacity: stampO, transform: `rotate(-6deg) scale(${stampIn})` }}>{lb === "L" ? "SIGNING" : "CHECKING"}</div>}
            </div>
          );
        })}
      </div>
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
        if (s.fx === "score" || !STATION[lb]) return null;
        const col = "#F2D696";
        return (
          <div style={{ position: "absolute", bottom: 78, right: 70, padding: "6px 14px", border: `2px solid ${col}`, color: col, fontFamily: "'Courier New', monospace", fontSize: 22, letterSpacing: 4, background: "rgba(0,0,0,0.55)", opacity: interpolate(frame, [XF, XF + 15], [0, 0.9], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }) }}>
            {"INSPECTION " + lb + " \u00b7 " + STATION[lb]}
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
        <div style={{ fontSize: 44, letterSpacing: 4, color: "#BFF8FF" }}>CASE FILE · THE BUILDING INSPECTION</div>
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
