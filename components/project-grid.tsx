import Image from "next/image";
import { projects } from "@/lib/portfolio-data";
import { Reveal } from "@/components/motion";
import { StoryDialog } from "@/components/story-dialog";
import { TiltCard } from "@/components/tilt-card";
export function ProjectGrid() {
  return (
    <div className="project-grid">
      {projects.map((story, index) => (
        <Reveal key={story.id} delay={(index % 2) * 0.12}>
          <TiltCard className="project-card">
            <div
              className={`project-art ${story.id}`}
              aria-label={`${story.name} artwork`}
            >
              {story.image ? (
                <Image src={story.image} alt={`${story.name} cover`} width={500} height={300} sizes="(max-width: 700px) 85vw, 45vw" className="project-cover" />
              ) : <span>{story.name}</span>}
            </div>
            <div className="project-copy">
              <p className="eyebrow">{story.category}</p>
              <h2>{story.name}</h2>
              <p>{story.preview}</p>
              <div className="project-bottom">
                <small>
                  {story.role ? `My role: ${story.role}` : story.note}
                </small>
                <StoryDialog story={story} returnTo="projects">
                  <button
                    type="button"
                    className="circle"
                    aria-label={`Read ${story.name} story`}
                  >
                    ↗
                  </button>
                </StoryDialog>
              </div>
            </div>
          </TiltCard>
        </Reveal>
      ))}
    </div>
  );
}
