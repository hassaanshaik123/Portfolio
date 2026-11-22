"use client";

import Image from "next/image";
import { ArrowUpRight } from "lucide-react";
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import type { Story } from "@/lib/portfolio-data";

export function StoryDialog({
  story,
  children,
  returnTo,
}: {
  story: Story;
  returnTo?: "experiments" | "projects";
  children: React.ReactNode;
}) {
  return (
    <Dialog>
      <DialogTrigger asChild>{children}</DialogTrigger>
      <DialogContent
        className="portfolio-story"
        aria-describedby={`description-${story.id}`}
      >
        <header className="story-header">
          {story.image ? (
            <Image
              src={story.image}
              alt={`${story.name} logo`}
              width={110}
              height={110}
              className="object-contain"
            />
          ) : null}
          <div>
            <DialogTitle className="story-title">{story.name}</DialogTitle>
            <DialogDescription
              id={`description-${story.id}`}
              className="story-role"
            >
              {story.role || story.category}
            </DialogDescription>
            {story.url ? (
              <Button asChild className="button small mb-3">
                <a href={story.url} target="_blank" rel="noopener noreferrer">
                  Visit {story.name}
                  <ArrowUpRight className="size-4" />
                </a>
              </Button>
            ) : null}
            {story.date ? <p className="story-date">{story.date}</p> : null}
          </div>
        </header>
        <div className="story-columns">
          <section>
            <h3>{story.originTitle}</h3>
            <p>{story.origin}</p>
          </section>
          <section>
            <h3>What I did</h3>
            <p>{story.work}</p>
          </section>
        </div>
        {story.metrics ? (
          <div className="story-metrics">
            {story.metrics.map(([number, text]) => (
              <div key={text}>
                <strong>{number}</strong>
                <span>{text}</span>
              </div>
            ))}
          </div>
        ) : null}
        <section className="story-ending">
          <h3>{story.endTitle}</h3>
          <p>{story.end}</p>
        </section>
        <DialogClose asChild>
          <Button variant="ghost" className="back-story justify-self-start">
            Back to {returnTo || (story.image ? "experiments" : "projects")}
          </Button>
        </DialogClose>
      </DialogContent>
    </Dialog>
  );
}
