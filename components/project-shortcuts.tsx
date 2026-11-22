import Image from "next/image";
import { projects } from "@/lib/portfolio-data";
import { StoryDialog } from "@/components/story-dialog";

const shortcuts = [
  { id: "soundbuddy", name: "SoundBuddy", logo: "/assets/journey/soundbuddy-logo.png" },
  { id: "buildsy", name: "Buildsy", logo: null },
  { id: "clario", name: "Clario", logo: "/assets/clario.png" },
  { id: "lyvo", name: "Lyvo AI", logo: null },
];

export function ProjectShortcuts() {
  return (
    <div className="project-shortcuts" aria-label="Explore my projects">
      {shortcuts.map(({ id, name, logo }) => {
        const story = projects.find((project) => project.id === id)!;
        return (
          <StoryDialog key={id} story={story} returnTo="projects">
            <button type="button" className="project-shortcut" aria-label={`Explore ${name}`}>
              <span className="project-shortcut-art">
                {logo ? <Image src={logo} alt="" width={100} height={70} /> : <span className="project-shortcut-placeholder" aria-hidden="true">{name}</span>}
              </span>
              <span className="project-shortcut-label">{name}<span aria-hidden="true">↗</span></span>
            </button>
          </StoryDialog>
        );
      })}
    </div>
  );
}
