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
            className={`experiment-card experiment-${story.id} ${story.id === "hustlers" ? "orange-card" : ""}`}
          >
            <h3>{story.id === "hustlers" ? "Hustlers’ Edge" : story.name}</h3>
            <p className="date">{story.date || story.role}</p>
            {story.image ? (
              <Image
                src={story.image}
                alt={`${story.name} logo`}
                width={500}
                height={300}
                sizes="(max-width: 700px) 85vw, 45vw"
              />
            ) : (
              <div className={`project-art experiment-art ${story.id}`} aria-label={`${story.name} artwork`}>
                <span>{story.name}</span>
              </div>
            )}
            <p>{story.preview}</p>
            <div className="story-link" aria-hidden="true">
              <span>The story</span>
              <span className="circle">↗</span>
            </div>
            <StoryDialog story={story} returnTo="experiments">
              <button className="experiment-open" type="button" aria-label={`Read the story of ${story.name}`} />
            </StoryDialog>
          </TiltCard>
        </Reveal>
      ))}
    </div>
  );
}
