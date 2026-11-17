"use client";

import { useRef } from "react";
import {
  motion,
  useReducedMotion,
  useScroll,
  useSpring,
  useTransform,
} from "motion/react";
import { useEntranceReady } from "@/components/providers";
import { cn } from "@/lib/utils";

const tags = {
  div: motion.div,
  section: motion.section,
  article: motion.article,
  header: motion.header,
  h1: motion.h1,
  h2: motion.h2,
  p: motion.p,
  footer: motion.footer,
};
export function Reveal({
  children,
  className,
  id,
  as = "div",
  direction = "up",
  delay = 0,
  parallax = 0,
}: {
  children: React.ReactNode;
  className?: string;
  id?: string;
  as?: keyof typeof tags;
  direction?: "up" | "down";
  delay?: number;
  parallax?: number;
}) {
  const ready = useEntranceReady();
  const reduced = useReducedMotion();
  const Tag = tags[as];
  return (
    <Tag
      id={id}
      className={cn("reveal-motion", className)}
      initial={reduced ? false : "hidden"}
      whileInView={ready ? "visible" : "hidden"}
      viewport={{ once: true, amount: 0.08, margin: "0px 0px -12px 0px" }}
      variants={{
        hidden: { opacity: 0, y: direction === "down" ? -24 : 36 },
        visible: { opacity: 1, y: 0 },
      }}
      transition={{ duration: 0.8, delay, ease: [0.22, 1, 0.36, 1] }}
    >
      {parallax ? (
        <ParallaxLayer amount={parallax}>{children}</ParallaxLayer>
      ) : (
        children
      )}
    </Tag>
  );
}

function ParallaxLayer({
  children,
  amount,
}: {
  children: React.ReactNode;
  amount: number;
}) {
  const ref = useRef<HTMLDivElement>(null);
  const reduced = useReducedMotion();
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start end", "end start"],
  });
  const drift = useTransform(scrollYProgress, [0, 1], [amount, -amount]);
  const y = useSpring(drift, { stiffness: 90, damping: 26 });
  return (
    <motion.div
      ref={ref}
      className="parallax-layer"
      style={{ y: reduced ? 0 : y }}
    >
      {children}
    </motion.div>
  );
}

export function ScrollProgress() {
  const { scrollYProgress } = useScroll();
  const scaleX = useSpring(scrollYProgress, { stiffness: 130, damping: 30 });
  const reduced = useReducedMotion();
  if (reduced) return null;
  return (
    <motion.div
      aria-hidden="true"
      className="pointer-events-none fixed inset-x-0 top-0 z-[80] h-[3px] origin-left bg-[var(--orange)]"
      style={{ scaleX }}
    />
  );
}
