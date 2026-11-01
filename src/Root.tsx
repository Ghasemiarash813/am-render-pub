import React from "react";
import { Composition } from "remotion";
import { Doc, DOC_TOTAL } from "./Doc";
export const RemotionRoot: React.FC = () => (<Composition id="Doc" component={Doc} durationInFrames={DOC_TOTAL} fps={30} width={1920} height={1080} />);
