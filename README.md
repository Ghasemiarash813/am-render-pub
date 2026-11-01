# am-render
Parallel Remotion renderer for Ancient Machines bank long-forms (GitHub Actions).
- main: Remotion project (same package-lock as pipeline/pyramid-ai), fonts replicating the sandbox, workflow.
- item/<slug>: per-item inputs (Doc.tsx, timeline.json, audio/*.mp3, music.wav, img/*.jpg).
- Dispatch `render` with slug; segments (c s<START>.mp4, 1400 frames, crf 18, H.264, muted) land on release out-<slug>-<run_id>.
