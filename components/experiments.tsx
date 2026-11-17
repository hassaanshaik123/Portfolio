import Image from "next/image";
import { experiments } from "@/lib/portfolio-data";
import { StoryDialog } from "@/components/story-dialog";
import { Reveal } from "@/components/motion";
import { TiltCard } from "@/components/tilt-card";

export function Experiments() {
  return (
    <div id="experiment-cards" className="experiment-grid">
      {experiments.map((story, index) => (
        <Reveal key={story.id} delay={index * 0.1}>
          <TiltCard
            className={`experiment-card ${index === 1 ? "orange-card" : ""}`}
          >
            <h3>{index === 1 ? "Hustlers’ Edge" : story.name}</h3>
            <p className="date">{story.date}</p>
            <Image
              src={story.image!}
              alt={`${story.name} logo`}
              width={500}
              height={300}
              sizes="(max-width: 700px) 85vw, 30vw"
            />
            <p>{story.preview}</p>
            <StoryDialog story={story}>
              <button className="story-link" type="button">
                <span>
                  The story<span className="sr-only"> of {story.name}</span>
                </span>
                <span className="circle" aria-hidden="true">
                  ↗
                </span>
              </button>
            </StoryDialog>
          </TiltCard>
        </Reveal>
      ))}
    </div>
  );
}
