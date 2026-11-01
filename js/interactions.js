const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
const clamp = (v, min=0, max=1) => Math.min(max, Math.max(min,v));
const ease = t => t*t*(3-2*t);
const mix = (a,b,t) => a+(b-a)*t;

export function initMountainScene(url) {
  const section = document.querySelector('.scene-scroll');
  if (!section) return;
  const stage = section.querySelector('.scene-stage');
  const world = section.querySelector('.scene-world');
  const card = section.querySelector('.destination-card');
  const trail = section.querySelector('.mountain-trail');
  const stops = [...section.querySelectorAll('.trail-stop')];
  const copy = section.querySelector('.scene-copy');
  const cue = section.querySelector('.scene-scroll-button');
  const destinations = {
    work: {title:'Work',note:'Strategy. Questions. Possibilities.',path:'work/',art:'work'},
    human: {title:'About',note:'The person behind the work.',path:'human/',art:'human'},
    experience: {title:'Experience',note:'Ventures built from zero.',path:'experience/',art:'experience'},
    resume: {title:'Resume',note:'Coming soon.',path:null,art:'resume'}
  };
  const select = id => {
    const item = destinations[id];
    if (card.dataset.destination === id) return;
    card.dataset.destination=id;
    card.querySelector('.destination-title').textContent=item.title;
    card.querySelector('.destination-note').textContent=item.note;
    card.classList.remove('card-changing');
    requestAnimationFrame(()=>card.classList.add('card-changing'));
    card.setAttribute('aria-label',item.path?`Explore ${item.title}`:'Resume — coming soon');
    if(item.path){card.href=url(item.path);card.removeAttribute('aria-disabled');}
    else{card.removeAttribute('href');card.setAttribute('aria-disabled','true');}
    stops.forEach(s=>s.classList.toggle('selected',s.dataset.destination===id));
  };
  stops.forEach(stop=>{
    stop.addEventListener('pointerenter',()=>select(stop.dataset.destination));
    stop.addEventListener('focus',()=>select(stop.dataset.destination));
    stop.addEventListener('click',event=>{if(stop.hasAttribute('aria-disabled'))event.preventDefault();});
  });
  card.addEventListener('click',event=>{if(card.hasAttribute('aria-disabled'))event.preventDefault();});
  select('work');
  cue.addEventListener('click',()=>{cue.blur();const goal=section.offsetHeight-stage.clientHeight;window.scrollTo({top:goal,behavior:'instant'});});
  let target=0, current=0, frame=0, width=innerWidth, height=innerHeight;
  let renderer;
  const render = () => {
    frame=0;
    const mobile=width<=760;
    current = reducedMotion.matches?1:Math.abs(target-current)<.0008?target:mix(current,target,.13);
    if(Math.abs(target-current)<.001)current=target;
    const p=ease(current),scale=mix(mobile?7:8,1,p);
    const dx=(mobile?-.3:-.2)*width*(1-p);
    const dy=(mobile?.4768:.625)*height*(1-p);
    world.style.transform=current===1?'none':`translate(${dx}px,${dy}px) scale(${scale})`;
    world.style.willChange=current>0&&current<1?'transform':'auto';
    section.style.setProperty('--progress',p);
    section.querySelector('.scene-mountain').style.opacity=clamp(p*4);
    section.querySelector('.scene-ledge').style.opacity=1-ease(clamp((p-.1)/.65));
    const revealed=clamp((p-.61)/.28);
    copy.style.opacity=revealed;
    copy.style.transform=`translateY(${(1-revealed)*24}px)`;
    copy.querySelector('a').inert=revealed<.7;
    const showTrail=p>.94;
    trail.inert=!showTrail;
    card.inert=!showTrail;
    trail.style.opacity=clamp((p-.83)/.14);
    card.style.opacity=clamp((p-.86)/.13);
    card.style.transform=`translateY(${(1-clamp((p-.86)/.13))*25}px)`;
    cue.style.opacity=clamp(1-current*5);
    cue.inert=current>.1;
    section.querySelector('.lion-hello').inert=current>.1;
    document.body.classList.toggle('scene-wide',p>.94);
    renderer?.draw(current);
    if(Math.abs(current-target)>.0008)frame=requestAnimationFrame(render);
  };
  const schedule=()=>{if(!frame)frame=requestAnimationFrame(render);};
  const update=()=>{width=innerWidth;height=stage.clientHeight;target=clamp(scrollY/Math.max(1,section.offsetHeight-height));if(reducedMotion.matches)target=1;schedule();};
  window.addEventListener('scroll',update,{passive:true});
  window.addEventListener('resize',update);
  reducedMotion.addEventListener('change',update);
  Promise.all([...stage.querySelectorAll('img')].map(i=>i.decode().catch(()=>{}))).then(()=>{
    if(!reducedMotion.matches)renderer=createSceneTransition(stage);
    update();
  });
  update();
}

function createSceneTransition(stage) {
  const canvas=stage.querySelector('.scene-transition');
  const gl=canvas.getContext('webgl',{alpha:false,antialias:false,premultipliedAlpha:false});
  if(!gl)return null;
  const vertex=`attribute vec2 position; varying vec2 uv; void main(){uv=(position+1.0)*.5;gl_Position=vec4(position,0.,1.);}`;
  const fragment=`precision highp float;
  varying vec2 uv; uniform vec2 resolution; uniform float progress; uniform float rockOpacity; uniform float ledgeOpacity;
  uniform sampler2D sky,mountain,trio,ledge; uniform vec4 skyBox,mountainBox,trioBox,ledgeBox;
  float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
  vec4 layer(sampler2D image,vec4 box,vec2 p){vec2 q=(p-box.xy)/box.zw;if(q.x<0.||q.y<0.||q.x>1.||q.y>1.)return vec4(0.);return texture2D(image,q);}
  void main(){
    vec2 p=vec2(uv.x,1.-uv.y)*resolution;
    float diagonal=length(resolution),amplitude=sin(progress*3.14159265);
    float distanceFromCentre=length(p-resolution*vec2(.5,.47));
    float wave=progress*diagonal*.94;
    float band=exp(-pow((distanceFromCentre-wave)/(diagonal*.16),2.))*amplitude;
    float cell=2.+band*10.; vec2 grid=floor(p/cell);
    vec2 samplePoint=mix(p,(grid+.5)*cell,band*.85);
    samplePoint+=vec2(hash(grid),hash(grid+23.))*.005*diagonal*band;
    vec4 background=layer(sky,skyBox,samplePoint);
    vec3 color=background.rgb;
    vec4 figures=layer(trio,trioBox,samplePoint);color=mix(color,figures.rgb,figures.a);
    vec4 rock=layer(mountain,mountainBox,samplePoint);color=mix(color,rock.rgb,rock.a*rockOpacity);
    vec4 platform=layer(ledge,ledgeBox,samplePoint);color=mix(color,platform.rgb,platform.a*ledgeOpacity);
    float grain=(hash(floor(p/1.8))-0.5)*band*.27;
    color+=grain;
    color+=vec3(.25,.16,.08)*band;
    float speck=step(.987,hash(floor(p/4.)))*band;
    color+=vec3(1.,.8,.35)*speck*.6;
    gl_FragColor=vec4(color,1.);
  }`;
  const compile=(type,source)=>{const shader=gl.createShader(type);gl.shaderSource(shader,source);gl.compileShader(shader);if(!gl.getShaderParameter(shader,gl.COMPILE_STATUS))throw new Error('Scene shader compilation failed');return shader;};
  let program;
  try{program=gl.createProgram();gl.attachShader(program,compile(gl.VERTEX_SHADER,vertex));gl.attachShader(program,compile(gl.FRAGMENT_SHADER,fragment));gl.linkProgram(program);if(!gl.getProgramParameter(program,gl.LINK_STATUS))return null;}catch{return null;}
  gl.useProgram(program);
  const buffer=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,buffer);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,-1,1,1,-1,1,1]),gl.STATIC_DRAW);
  const position=gl.getAttribLocation(program,'position');gl.enableVertexAttribArray(position);gl.vertexAttribPointer(position,2,gl.FLOAT,false,0,0);
  const images=[stage.querySelector('.scene-sky'),stage.querySelector('.scene-mountain'),stage.querySelector('.scene-trio'),stage.querySelector('.scene-ledge')];
  const names=['sky','mountain','trio','ledge'];
  images.forEach((image,i)=>{
    gl.activeTexture(gl.TEXTURE0+i);const texture=gl.createTexture();gl.bindTexture(gl.TEXTURE_2D,texture);
    gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_S,gl.CLAMP_TO_EDGE);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_T,gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MIN_FILTER,gl.LINEAR);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MAG_FILTER,gl.LINEAR);
    gl.texImage2D(gl.TEXTURE_2D,0,gl.RGBA,gl.RGBA,gl.UNSIGNED_BYTE,image);gl.uniform1i(gl.getUniformLocation(program,names[i]),i);
  });
  const box = image => {
    const r=image.getBoundingClientRect(),base=stage.getBoundingClientRect();
    if(image.classList.contains('scene-sky')){
      const scale=Math.max(r.width/image.naturalWidth,r.height/image.naturalHeight),w=image.naturalWidth*scale,h=image.naturalHeight*scale;
      return [(r.width-w)/2,(r.height-h)/2,w,h];
    }
    return [r.left-base.left,r.top-base.top,r.width,r.height];
  };
  let lost=false;canvas.addEventListener('webglcontextlost',()=>{lost=true;canvas.style.opacity=0;});
  return {draw(p){
    if(lost)return;
    const active=p>.005&&p<.995;
    canvas.style.opacity=active?1:0;
    canvas.style.display=active?'block':'none';
    if(!active)return;
    const w=stage.clientWidth,h=stage.clientHeight,dpr=Math.min(devicePixelRatio,1.5);
    if(canvas.width!==Math.round(w*dpr)||canvas.height!==Math.round(h*dpr)){canvas.width=Math.round(w*dpr);canvas.height=Math.round(h*dpr);gl.viewport(0,0,canvas.width,canvas.height);}
    gl.uniform2f(gl.getUniformLocation(program,'resolution'),w,h);
    gl.uniform1f(gl.getUniformLocation(program,'progress'),p);
    gl.uniform1f(gl.getUniformLocation(program,'rockOpacity'),Number(images[1].style.opacity));
    gl.uniform1f(gl.getUniformLocation(program,'ledgeOpacity'),Number(images[3].style.opacity));
    names.forEach((n,i)=>gl.uniform4fv(gl.getUniformLocation(program,n+'Box'),box(images[i])));
    gl.drawArrays(gl.TRIANGLES,0,6);
  }};
}

export function initProjectGalleries() {
  const rows=[...document.querySelectorAll('.expandable-project')];
  if(!rows.length)return;
  const hover=matchMedia('(hover: hover) and (pointer: fine)');
  let active=null,closeTimer;
  const open=row=>{
    rows.forEach(item=>{
      const expanded=item===row;
      item.classList.toggle('expanded',expanded);
      item.querySelector('.project-disclosure').setAttribute('aria-expanded',String(expanded));
      item.querySelector('.project-gallery-collapse').inert=!expanded;
    });
    active=row;
  };
  rows.forEach(row=>{
    const disclosure=row.querySelector('.project-disclosure');
    row.addEventListener('pointerenter',()=>{clearTimeout(closeTimer);if(hover.matches)open(row);});
    row.addEventListener('pointerleave',()=>{if(hover.matches&&!row.contains(document.activeElement))closeTimer=setTimeout(()=>open(null),240);});
    row.addEventListener('focusin',event=>{clearTimeout(closeTimer);if(!event.target.closest('.project-disclosure'))open(row);});
    disclosure.addEventListener('click',()=>open(active===row?null:row));
    const track=row.querySelector('.gallery-track');
    const prev=row.querySelector('.gallery-prev'),next=row.querySelector('.gallery-next');
    const step=direction=>track.scrollBy({left:direction*track.clientWidth*.65,behavior:reducedMotion.matches?'instant':'smooth'});
    prev.addEventListener('click',()=>step(-1));next.addEventListener('click',()=>step(1));
    const refresh=()=>{prev.disabled=track.scrollLeft<=2;next.disabled=track.scrollLeft+track.clientWidth>=track.scrollWidth-2;};
    track.addEventListener('scroll',refresh,{passive:true});window.addEventListener('resize',refresh);refresh();
    track.addEventListener('keydown',event=>{if(event.target!==track)return;if(['ArrowRight','ArrowLeft'].includes(event.key)){event.preventDefault();step(event.key==='ArrowRight'?1:-1);}});
    let drag=null,moved=false;
    track.addEventListener('pointerdown',event=>{if(event.pointerType==='touch'||event.button!==0)return;drag={x:event.clientX,start:track.scrollLeft,id:event.pointerId};moved=false;});
    track.addEventListener('pointermove',event=>{if(!drag)return;const delta=event.clientX-drag.x;if(Math.abs(delta)>5){moved=true;track.setPointerCapture(drag.id);track.classList.add('dragging');track.scrollLeft=drag.start-delta;event.preventDefault();}});
    const end=()=>{drag=null;track.classList.remove('dragging');};track.addEventListener('pointerup',end);track.addEventListener('pointercancel',end);
    track.addEventListener('click',event=>{if(moved){event.preventDefault();event.stopPropagation();moved=false;}},true);
    track.addEventListener('dragstart',event=>event.preventDefault());
  });
  open(rows[0]);
}

export function initPortraits(url) {
  const image=document.querySelector('#portrait');
  if(!image)return;
  const wrap=image.closest('.portrait-wrap'),canvas=wrap.querySelector('.portrait-transition');
  const dots=[...document.querySelectorAll('[data-photo]')];
  const context=canvas.getContext('2d');
  let selected=0,animating=false,queued=null,visible=true,timer;
  const pictures=[1,2,3].map(i=>{const im=new Image();im.src=url(`assets/portraits/portrait-${i}.webp`);return im;});
  const prepared=Promise.all(pictures.map(p=>p.decode().catch(()=>{})));
  const cover=(ctx,p,w,h)=>{const scale=Math.max(w/p.naturalWidth,h/p.naturalHeight),iw=p.naturalWidth*scale,ih=p.naturalHeight*scale;ctx.drawImage(p,(w-iw)/2,(h-ih)*.45,iw,ih);};
  const show=async next=>{
    if(next===selected)return;
    if(animating){queued=next;return;}
    await prepared;
    dots.forEach((d,i)=>{d.classList.toggle('active',i===next);d.setAttribute('aria-pressed',String(i===next));});
    if(reducedMotion.matches||!context){image.src=pictures[next].src;selected=next;return;}
    animating=true;
    const w=Math.round(wrap.clientWidth),h=Math.round(wrap.clientHeight);
    canvas.width=w;canvas.height=h;
    const before=document.createElement('canvas'),after=document.createElement('canvas');before.width=after.width=w;before.height=after.height=h;
    cover(before.getContext('2d'),pictures[selected],w,h);cover(after.getContext('2d'),pictures[next],w,h);
    canvas.style.opacity=1;
    const start=performance.now(),cell=9;
    const draw=now=>{
      const t=clamp((now-start)/760);context.drawImage(before,0,0);
      for(let y=0;y<h;y+=cell)for(let x=0;x<w;x+=cell){
        const noise=((Math.sin(x*12.9898+y*78.233)*43758.5453)%1+1)%1;
        const threshold=.48*(x/w+y/h)+noise*.36-.16;
        if(t>threshold)context.drawImage(after,x,y,cell,cell,x,y,cell,cell);
        if(Math.abs(t-threshold)<.06){context.fillStyle=`rgba(242,230,189,${.18*Math.sin(Math.PI*t)})`;context.fillRect(x,y,cell,cell);}
      }
      if(t<1)requestAnimationFrame(draw);else{image.src=pictures[next].src;selected=next;canvas.style.opacity=0;animating=false;if(queued!==null){const n=queued;queued=null;show(n);}}
    };
    requestAnimationFrame(draw);
  };
  const resetTimer=()=>{clearInterval(timer);if(!reducedMotion.matches)timer=setInterval(()=>{if(visible&&!document.hidden&&!wrap.contains(document.activeElement))show((selected+1)%3);},5200);};
  dots.forEach((dot,i)=>dot.addEventListener('click',()=>{show(i);resetTimer();}));
  wrap.querySelector('.portrait-advance').addEventListener('click',()=>{show((selected+1)%3);resetTimer();});
  new IntersectionObserver(([entry])=>{visible=entry.isIntersecting;}).observe(wrap);
  reducedMotion.addEventListener('change',resetTimer);resetTimer();
}
