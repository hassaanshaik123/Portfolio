# Scene asset generation

Tool: built-in image generation, edit mode. Reference: the user-supplied “Heroic Trio Beneath a Burning Sky.png”. All five originals remain in the Codex generated-images directory; project outputs are optimized WebP files below. Alpha is preserved on the four transparent assets. The supplied source image is unchanged.

## `assets/scene-trio.webp`

Use case: background-extraction. Edit target: the supplied Heroic Trio Beneath a Burning Sky illustration. Produce a clean, high resolution genuinely transparent-background PNG cutout of ONLY the full standing young man, adult lion at his left, and lion cub at his right, keeping the exact original face, hair, glasses, black shirt, beige trousers, shoes, animal appearances, poses, proportions, and painterly sunset lighting. Preserve every subject fully, including feet and paws; do not crop heads or feet. Remove ALL sky, clouds, lights and ALL rocky ground. No rock at all, no floor, no shadow backdrop, no text. Keep the three subjects arranged exactly as in the original with transparent space around them. This is a foreground sprite for a scroll-zoom mountain scene.

## `assets/scene-mountain.webp`

Use case: precise-object-edit. Input image is the style and lighting reference. Create a genuinely transparent-background isolated tall mountain for a layered illustrated portfolio homepage. One dramatic, slender jagged rocky mountain with a narrow flat-ish summit at 15% from the top of the image, widening toward the bottom to a massive broad base extending to both lower corners, like a steep alpine pyramid. Show the full mountain silhouette, no sky anywhere. Match the input illustration's dark charcoal angular rocks, warm bright orange sunset rim light on RIGHT-facing rock planes, shaded dark purple/black LEFT-facing face, subtle moss. Summit should have space for a tiny standing person and two lions to be composited later. Mountain centered, sharp silhouette edges, tall portrait composition. Upper 10% transparent. Entire area outside mountain transparent. No people, no animals, no paths, no flags, no vegetation silhouettes, no text. This must be a standalone mountain sprite, not a whole scene.

## `assets/scene-sky.webp`

Use case: precise-object-edit. Edit target: supplied Heroic Trio Beneath a Burning Sky illustration. Create a 16:9 wide seamless-looking landscape SKY BACKPLATE for a layered website hero. Remove the man, lion, cub, and ALL rocks/ground/mountain completely and reconstruct only the painterly sky behind them. Match the exact original style: deep cobalt blue and purple sky, luminous burning orange sunset cumulus clouds rising from left and lower right, very subtle warm haze on horizon. Sky and clouds only, edge-to-edge, wide landscape 16:9 composition. No people, animals, mountains, silhouettes, ground, text, frame or watermark. Do not add stars or sun/moon. Keep open blue sky at upper right, dramatic orange cloud mass toward left, original image's brushwork and colors.

## `assets/scene-ledge.webp`

Use case: background-extraction. Create a transparent foreground ROCK LEDGE sprite for the provided illustrated scene. Only a wide dark angular rocky platform, like the foreground rocky ground in the input, no people, no lion, no cub, no sky. Composition: very broad, low, almost level top ridge suitable for three standing figures across the entire width; craggy detailed charcoal rock with subtle warm orange light on right edges and deep purple shadows. Shape like a low wide irregular trapezoid/mound with nearly flat top, 3:1 width:height. Fill most of image width. Real transparent outside its silhouette. No tall summit, no triangular pyramid, no dramatic central peak. No text. Exact input painterly geological style and colors. This is the level ledge immediately beneath the characters' feet.

## `assets/scene-cloud.webp`

Use case: background-extraction. Asset type: small foreground cloud for a website portrait composition. Generate ONLY a single elongated, wispy luminous orange and coral sunset cloud, matching the original illustration's burning clouds. Genuine transparent background, nothing else. Cloud horizontal roughly 3:1 width-to-height, organically ragged fine vapor edges and uneven puffy wisps, not an oval, not a capsule, no hard border. Deep red-purple shadows at left bottom, bright orange illuminated billows on top and at right. No sky backdrop, blue background, people, rocks, text, stars or watermark. Soft painterly sunset texture, keep all wisps inside canvas.
