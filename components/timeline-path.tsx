"use client";
import { motion, useReducedMotion } from "motion/react";
export function TimelinePath() {
  const reduced = useReducedMotion();
  return (
    <svg
      className="journey-path"
      viewBox="0 0 1200 400"
      preserveAspectRatio="none"
      aria-hidden="true"
    >
      <path
        className="black-path"
        d="M55 180 C220 110 310 300 490 240 S750 100 890 190 S1080 280 1155 240"
      />
      <motion.path
        className="orange-path"
        d="M55 195 C220 125 310 315 490 255 S750 115 890 205 S1080 295 1155 255"
        initial={reduced ? false : { pathLength: 0 }}
        whileInView={{ pathLength: 1 }}
        viewport={{ once: true, amount: 0.2 }}
        transition={{ duration: 1.6, ease: "easeInOut" }}
      />
      <circle cx="155" cy="170" r="6" />
      <circle cx="485" cy="241" r="6" />
      <circle cx="790" cy="157" r="6" />
      <circle cx="1055" cy="251" r="6" />
    </svg>
  );
}
