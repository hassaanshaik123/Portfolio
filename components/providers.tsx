"use client";

import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useState,
} from "react";
import { usePathname } from "next/navigation";
import { ThemeProvider } from "next-themes";
import {
  AnimatePresence,
  motion,
  MotionConfig,
  useReducedMotion,
} from "motion/react";

const EntranceContext = createContext(true);
export const useEntranceReady = () => useContext(EntranceContext);

function OpeningSequence({ onComplete }: { onComplete: () => void }) {
  const [progress, setProgress] = useState(0);
  const reduced = useReducedMotion();
  useEffect(() => {
    if (reduced || (window.location.hash && window.location.hash !== "#home")) {
      onComplete();
      return;
    }
    const previous = document.documentElement.style.overflow;
    document.documentElement.style.overflow = "hidden";
    const start = performance.now();
    const timer = window.setInterval(() => {
      const value = Math.min(100, Math.floor((performance.now() - start) / 55));
      setProgress(value);
      if (value >= 100) {
        window.clearInterval(timer);
        onComplete();
      }
    }, 50);
    return () => {
      window.clearInterval(timer);
      document.documentElement.style.overflow = previous;
    };
  }, [onComplete, reduced]);
  return (
    <motion.div
      className="opening-overlay fixed inset-0 z-[100] grid place-items-center"
      initial={{ opacity: 1 }}
      exit={{ opacity: 0, y: -12 }}
      transition={{ duration: 0.4 }}
    >
      <div className="w-[min(340px,calc(100vw-64px))] text-center">
        <span className="text-[15px] font-bold tracking-[0.22em]">
          HASSAAN<span className="text-[var(--orange)]">.</span>
        </span>
        <div className="my-8 grid h-44 place-items-center" aria-hidden="true">
          <motion.div
            className="size-12 bg-[var(--orange)]"
            animate={{
              borderRadius: ["6%", "50%", "6%"],
              rotate: [0, 180, 360],
            }}
            transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
          />
        </div>
        <div className="mb-4 flex items-center justify-between gap-3">
          <span className="text-sm text-[var(--muted)]">
            {progress < 95 ? "Loading portfolio" : "Let’s get started"}
          </span>
          <span className="text-[33px] font-bold tabular-nums">
            {progress}
            <span className="ml-1 text-base text-[var(--orange)]">%</span>
          </span>
        </div>
        <div
          className="h-[3px] overflow-hidden rounded bg-[var(--gray)]"
          role="progressbar"
          aria-label="Opening portfolio"
          aria-valuemin={0}
          aria-valuemax={100}
          aria-valuenow={progress}
        >
          <div
            className="h-full origin-left bg-[var(--orange)]"
            style={{ transform: `scaleX(${progress / 100})` }}
          />
        </div>
        <p className="sr-only" role="status">
          Opening Hassaan’s portfolio.
        </p>
      </div>
    </motion.div>
  );
}

export function Providers({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const [complete, setComplete] = useState(false);
  const finish = useCallback(() => setComplete(true), []);
  const ready = pathname !== "/" || complete;
  return (
    <ThemeProvider
      attribute="data-theme"
      defaultTheme="system"
      enableSystem
      disableTransitionOnChange
      storageKey="portfolio-theme"
    >
      <MotionConfig reducedMotion="user">
        <EntranceContext.Provider value={ready}>
          <AnimatePresence>
            {!ready ? (
              <OpeningSequence key="opening" onComplete={finish} />
            ) : null}
          </AnimatePresence>
          <div
            inert={!ready ? true : undefined}
            aria-hidden={!ready ? true : undefined}
          >
            {children}
          </div>
        </EntranceContext.Provider>
      </MotionConfig>
    </ThemeProvider>
  );
}
