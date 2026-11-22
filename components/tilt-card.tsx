"use client";
import {
  motion,
  useMotionValue,
  useReducedMotion,
} from "motion/react";
import type { PointerEvent, ReactNode } from "react";

export function TiltCard({
  children,
  className,
}: {
  children: ReactNode;
  className?: string;
}) {
  const reduced = useReducedMotion();
  const x = useMotionValue(0);
  const y = useMotionValue(0);
  function reset() {
    x.set(0);
    y.set(0);
  }
  function move(event: PointerEvent<HTMLElement>) {
    if (reduced || event.pointerType !== "mouse") return;
    const rect = event.currentTarget.getBoundingClientRect();
    x.set(-((event.clientY - rect.top) / rect.height - 0.5) * 5);
    y.set(((event.clientX - rect.left) / rect.width - 0.5) * 5);
  }
  return (
    <motion.article
      className={`tilt-card ${className || ""}`}
      style={{ rotateX: x, rotateY: y, transformPerspective: 1000 }}
      onPointerMove={move}
      onPointerLeave={reset}
      onPointerCancel={reset}
    >
      {children}
    </motion.article>
  );
}
