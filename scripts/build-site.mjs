import { mkdir, readFile, writeFile, cp } from 'node:fs/promises';
import { projects } from '../js/portfolio-data.js';
const html = await readFile('index.html', 'utf8');
const routes = ['', 'work', 'human', 'experience', ...projects.map(p => `work/${p.id}`)];
const labels = {work:'Work', human:'Human', experience:'Experience'};
await mkdir('dist', {recursive:true});
for (const folder of ['css', 'js']) await cp(folder, `dist/${folder}`, {recursive:true});
await mkdir('dist/assets', {recursive:true});
for (const file of ['hero-burning-sky.webp', 'scene-sky.webp', 'scene-mountain.webp', 'scene-trio.webp', 'scene-ledge.webp', 'scene-cloud.webp', 'h-logo.png', 'fonts', 'portraits']) {
  await cp(`assets/${file}`, `dist/assets/${file}`, {recursive:true});
}
for (const route of routes) {
  const prefix = '../'.repeat(route ? route.split('/').length : 0);
  const project = projects.find(p => route === `work/${p.id}`);
  const title = project?.title || labels[route];
  let output = html.replace(/(href|src)="(assets\/|css\/|js\/)/g, `$1="${prefix}$2`);
  if (title) output = output.replaceAll('Muhammad Hassaan — Business Developer', `${title} — Muhammad Hassaan`);
  if (project) output = output.replace('Business development, consultative sales, and venture building. Explore Muhammad Hassaan’s work, experience, and academic projects.', project.description);
  await mkdir(`dist/${route}`, {recursive:true});
  await writeFile(`dist/${route ? route + '/' : ''}index.html`, output);
}
await writeFile('dist/404.html', html.replace(/(href|src)="(assets\/|css\/|js\/)/g, '$1="/$2'));
console.log(`Built ${routes.length} pages into dist/`);
