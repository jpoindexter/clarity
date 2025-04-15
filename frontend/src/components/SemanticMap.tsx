"use client";

import { useEffect, useRef } from "react";

export default function SemanticMap() {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "#4ade80";
    ctx.beginPath();
    ctx.arc(canvas.width / 2, canvas.height / 2, 50, 0, 2 * Math.PI);
    ctx.fill();
  }, []);

  return (
    <div className="w-full h-[600px] border border-zinc-800 rounded bg-black">
      <canvas ref={canvasRef} width={800} height={600} className="block" />
    </div>
  );
}
