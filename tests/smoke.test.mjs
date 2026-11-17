import test from "node:test";
import assert from "node:assert/strict";

const base = process.env.BASE_URL || "http://127.0.0.1:3000";

test("homepage delivers the approved content as server-rendered HTML", async () => {
  const response = await fetch(`${base}/`);
  assert.equal(response.status, 200);
  const html = await response.text();
  for (const text of ["Sales &amp; Business Developer", "Listen to the Problem", "Stroque Consulting", "hassaan-about-black-original.png", "Resume"])
    assert.ok(html.includes(text), `Missing homepage content: ${text}`);
  const resumeLink = html.match(/<a\b[^>]*href="\/assets\/Muhammad-Hassaan-Resume\.pdf"[^>]*>Resume<\/a>/)?.[0];
  assert.ok(resumeLink, "Resume should link directly to the PDF");
  assert.ok(!/\bdownload(?:=|\s|>)/.test(resumeLink), "Resume should open rather than force a download");
  assert.ok(!html.includes('src="js/main.js'), "Legacy DOM scripts must not be loaded");
});

test("projects route renders all four projects", async () => {
  const response = await fetch(`${base}/projects`);
  assert.equal(response.status, 200);
  const html = await response.text();
  for (const project of ["SoundBuddy", "Clario AI", "Buildsy", "LYVO"])
    assert.ok(html.includes(`Read ${project} story`));
});

for (const [legacy, destination] of [["index.html", "/"], ["projects.html", "/projects"]]) {
  test(`legacy ${legacy} redirects to ${destination}`, async () => {
    const response = await fetch(`${base}/${legacy}`, { redirect: "manual" });
    assert.equal(response.status, 308);
    assert.equal(response.headers.get("location"), destination);
  });
}

test("resume and original portraits are publicly served", async () => {
  for (const [file, type] of [["Muhammad-Hassaan-Resume.pdf", "application/pdf"], ["hassaan-about-black-original.png", "image/png"], ["hassaan-hero-suit.png", "image/png"]]) {
    const response = await fetch(`${base}/assets/${file}`);
    assert.equal(response.status, 200, file);
    assert.ok(response.headers.get("content-type")?.includes(type), file);
  }
});

test("unknown routes return a useful 404", async () => {
  const response = await fetch(`${base}/this-page-does-not-exist`);
  assert.equal(response.status, 404);
  assert.ok((await response.text()).includes("That page wandered off."));
});
