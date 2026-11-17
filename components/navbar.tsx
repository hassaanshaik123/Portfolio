"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useState, useRef } from "react";
import { useTheme } from "next-themes";
import { motion, useScroll, useMotionValueEvent, useReducedMotion, useTransform, useSpring, useMotionValue } from "motion/react";
import { ArrowUpRight, Menu, Moon, Sun } from "lucide-react";
import { Button } from "@/components/ui/button";
import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet";
import { Reveal } from "@/components/motion";

const links = [
  ["About", "about"],
  ["Experiments", "experiments"],
  ["Projects", "projects"],
  ["Timeline", "timeline"],
] as const;
export function Navbar() {
  const pathname = usePathname();
  const { resolvedTheme, setTheme } = useTheme();
  const [mounted, setMounted] = useState(false);
  const [open, setOpen] = useState(false);
  const lastScroll = useRef(0);
  const travel = useRef(0);
  const [collapsed, setCollapsed] = useState(false);
  const [controlsHidden, setControlsHidden] = useState(false);
  const reduced = useReducedMotion();
  const { scrollY } = useScroll();
  const progress = useMotionValue(0);
  useMotionValueEvent(scrollY, "change", value => {
    const delta = value - lastScroll.current;
    lastScroll.current = value;
    if (open || Math.abs(delta) < 0.1) return;
    if (Math.sign(delta) !== Math.sign(travel.current)) travel.current = 0;
    travel.current += delta;
    if (Math.abs(travel.current) >= 6) {
      if (delta > 0) setControlsHidden(true);
      progress.set(delta > 0 ? 1 : 0);
      travel.current = 0;
    }
  });
  const eased = useSpring(progress, { stiffness: 840, damping: 60, restDelta: 0.001 });
  const collapse = reduced ? progress : eased;
  const width = useTransform(collapse, value => `calc(${100 * (1 - value)}% + ${59 * value}px)`);
  const height = useTransform(collapse, [0, 1], [64, 22]);
  const paddingInline = useTransform(collapse, [0, 1], [24, 6]);
  const opacity = useTransform(collapse, [0, 1], [1, 0.6]);
  useMotionValueEvent(collapse, "change", value => {
    setCollapsed(value > 0.4);
    if (value < 0.005 && progress.get() === 0) setControlsHidden(false);
  });
  useEffect(() => {
    progress.set(0);
    setControlsHidden(false);
    lastScroll.current = window.scrollY;
    travel.current = 0;
  }, [pathname, progress]);
  useEffect(() => setMounted(true), []);
  function closeAndNavigate(id: string) {
    setOpen(false);
    window.setTimeout(() => document.getElementById(id)?.scrollIntoView({ behavior: reduced ? "instant" : "smooth" }), 350);
  }
  const dark = mounted && resolvedTheme === "dark";
  const home = pathname === "/" ? "" : "/";
  const href = (id: string) =>
    pathname === "/projects" && id === "projects"
      ? "/projects"
      : `${home}#${id}`;
  const themeToggle = (
    <Button
      variant="ghost"
      size="icon"
      className="theme-toggle"
      aria-label={dark ? "Switch to day mode" : "Switch to night mode"}
      aria-pressed={dark}
      onClick={() => setTheme(dark ? "light" : "dark")}
    >
      {dark ? (
        <Sun className="size-[22px]" />
      ) : (
        <Moon className="size-[22px]" />
      )}
    </Button>
  );
  return (
    <Reveal as="header" className="nav-wrap" direction="down">
      <motion.nav
        id="site-nav"
        aria-label="Main navigation"
        className={collapsed ? "nav-notch" : undefined}
        style={{ width, height, paddingInline, opacity, backgroundColor: "#1e1d1c" }}
      >
        {collapsed ? (
          <button className="brand notch-home" aria-label="Open navigation" aria-expanded={open} onClick={() => setOpen(true)}>
            <span className="notch-dots" aria-hidden="true"><i /><i /><i /></span>
          </button>
        ) : (
          <div className="brand">
            <span className="monogram" aria-hidden="true">H</span>
            <Link className="brand-name" href={`${home}#home`} aria-label="Hassaan home">
              Hassaan
            </Link>
          </div>
        )}
        <div className="nav-links desktop-navigation">
          {links.map(([label, id]) => (
            <Link
              key={id}
              href={href(id)}
              aria-current={
                pathname === "/projects" && id === "projects"
                  ? "page"
                  : undefined
              }
            >
              {label}
            </Link>
          ))}
          <Button asChild className="button small">
            <Link href={`${home}#connect`}>
              Connect <ArrowUpRight className="size-4" />
            </Link>
          </Button>
          {themeToggle}
        </div>
        <div className={`mobile-nav-actions${controlsHidden ? " controls-hidden" : ""}`} inert={controlsHidden ? true : undefined} aria-hidden={controlsHidden ? true : undefined}>
          {themeToggle}
          <Sheet open={open} onOpenChange={setOpen}>
            <SheetTrigger asChild>
              <Button
                variant="ghost"
                size="icon"
                className="size-11 text-white hover:bg-white/10"
                aria-label={collapsed ? "Open notch navigation" : "Open navigation"}
              >
                <Menu className="size-6" />
              </Button>
            </SheetTrigger>
            <SheetContent className="mobile-sheet" side="right">
              <SheetHeader>
                <SheetTitle>Explore the portfolio</SheetTitle>
              </SheetHeader>
              <div className="flex flex-col gap-2 px-5 py-8">
                <Button variant="outline" onClick={() => setTheme(dark ? "light" : "dark")}>
                  {dark ? "Switch to day mode" : "Switch to night mode"}
                </Button>
                <Link className="rounded-xl px-4 py-3 text-xl font-medium" href="/#home" onClick={() => closeAndNavigate("home")}>Home</Link>
                {links.map(([label, id]) => (
                  <Link
                    className="rounded-xl px-4 py-3 text-xl font-medium hover:bg-[var(--gray)]"
                    key={id}
                    href={href(id)}
                    onClick={() => closeAndNavigate(id)}
                  >
                    {label}
                  </Link>
                ))}
                <Button asChild className="button mt-4">
                  <Link href={`${home}#connect`} onClick={() => closeAndNavigate("connect")}>
                    Let’s connect <ArrowUpRight className="size-4" />
                  </Link>
                </Button>
              </div>
            </SheetContent>
          </Sheet>
        </div>
      </motion.nav>
    </Reveal>
  );
}
