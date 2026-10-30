#!/usr/bin/env python3
import os

BASE_DIR = "/Users/muhammadhassaan/Documents/GitHub/Portfolio"
BUILD_SCRIPT = os.path.join(BASE_DIR, "scripts", "build_portfolio.py")

with open(BUILD_SCRIPT, "r", encoding="utf-8") as f:
    code = f.read()

# -----------------------------------------------------------------------------
# 1. Update SPLICE_1: Loader safety, getBBox try/catch, whoosh try/catch, fallback timer
# -----------------------------------------------------------------------------
old_splice_1_start = 'SPLICE_1 = r"""wh=[.22,1,.36,1],Th=[.76,0,.24,1],Eh='
old_splice_1_end = '\n\n# ============================================================================\n# SPLICE 2:'
s1_pos = code.find(old_splice_1_start)
s1_end = code.find(old_splice_1_end)
if s1_pos == -1 or s1_end == -1:
    raise RuntimeError(f"SPLICE_1 markers not found: {s1_pos}, {s1_end}")

new_splice_1 = '''SPLICE_1 = r"""wh=[.22,1,.36,1],Th=[.76,0,.24,1],Eh=[`h`,`a`,`s`,`s`,`a`,`a`,`n`],Dh=2.5,Oh=[{d:`M20 280H980`,delay:.05},{d:`M60 172H940`,delay:.16},{d:`M100 350H760`,delay:.28},{d:`M110 70V380`,delay:.2},{d:`M452 100V372`,delay:.32},{d:`M788 110V400`,delay:.44},{d:`M110 372L580 84`,delay:.38}],kh=[{x:22,y:272,text:`baseline`,delay:.5},{x:62,y:164,text:`x-height`,delay:.6},{x:102,y:342,text:`descender`,delay:.7}];function Ah(){let e=um(),[t,n]=(0,v.useState)(`wait`),r=(0,v.useRef)(null),i=(0,v.useRef)(null),[a,o]=(0,v.useState)({dotX:886,shift:0}),s=nm(0),c=am(s,e=>`${String(Math.round(e)).padStart(3,`0`)}%`);return(0,v.useEffect)(()=>(`scrollRestoration`in history&&(history.scrollRestoration=`manual`),window.scrollTo(0,0),document.documentElement.classList.add(`is-loading`),r.current=setInterval(()=>Vm()?.stop(),50),()=>{r.current&&clearInterval(r.current)}),[]),(0,v.useEffect)(()=>{let safety=setTimeout(()=>{r.current&&clearInterval(r.current);r.current=null;document.documentElement.classList.remove(`is-loading`);try{let vm=Vm();if(!document.querySelector(`.case-overlay[open]`)){vm?.start()}}catch(err){}},2800);return()=>clearTimeout(safety)},[]),(0,v.useEffect)(()=>{let e=!1,t=()=>!e&&n(e=>e===`wait`?`draw`:e),r=setTimeout(t,700);return document.fonts?.ready.then(()=>{clearTimeout(r),t()}).catch(()=>{clearTimeout(r),t()}),()=>{e=!0,clearTimeout(r)}},[]),(0,v.useLayoutEffect)(()=>{if(t!==`draw`||!i.current)return;try{let e=typeof i.current.getBBox===`function`?i.current.getBBox():{x:110,width:680};let n=(e.x||110)+(e.width||680)+22;o({dotX:n,shift:500-((e.x||110)+n+30)/2})}catch(err){o({dotX:886,shift:0})}},[t]),(0,v.useEffect)(()=>{if(t!==`draw`)return;let r=Fm(s,100,{duration:e?.3:2.3,ease:[.4,0,.2,1]}),timer=setTimeout(()=>{try{Ch.whoosh()}catch(err){}n(`done`)},e?400:Dh*1e3);return()=>{r.stop(),clearTimeout(timer)}},[t,s,e]),(0,G.jsx)(cf,{onExitComplete:()=>{r.current&&clearInterval(r.current),r.current=null,document.documentElement.classList.remove(`is-loading`);try{let e=Vm();if(document.querySelector(`.case-overlay[open]`)){e?.stop();return}e?.start(),e?.scrollTo(0,{immediate:!0})}catch(err){}},children:t!==`done`&&(0,G.jsxs)(K.div,{className:`loader`,role:`status`,"aria-label":`Loading Muhammad Hassaan's portfolio`,initial:{y:0},exit:e?{opacity:0,transition:{duration:.3}}:{y:`-100%`,transition:{duration:.9,ease:Th}},children:[(0,G.jsx)(`div`,{className:`loader-texture`,style:{backgroundImage:`url(${zm})`},"aria-hidden":!0}),(0,G.jsxs)(`div`,{className:`loader-corner loader-corner--tl`,children:[(0,G.jsx)(`span`,{children:`muhammad hassaan`}),(0,G.jsx)(`span`,{children:`listening closely, solving problems`})]}),(0,G.jsxs)(`div`,{className:`loader-corner loader-corner--tr`,children:[(0,G.jsx)(`span`,{children:`visitor no. 01`}),(0,G.jsx)(`span`,{children:`glad you dropped by`})]}),t===`draw`&&(0,G.jsx)(K.svg,{className:`loader-mark`,viewBox:`0 0 1000 420`,fill:`none`,"aria-hidden":!0,exit:{opacity:0,y:-40,transition:{duration:.5,ease:wh}},children:(0,G.jsxs)(`g`,{transform:`translate(${a.shift} 0)`,children:[(0,G.jsx)(`text`,{ref:i,x:`110`,y:`280`,className:`loader-word`,opacity:`0`,children:`hassaan`}),(0,G.jsxs)(`g`,{className:`loader-guides`,children:[Oh.map(e=>(0,G.jsx)(K.path,{d:e.d,initial:{pathLength:0,opacity:0},animate:{pathLength:1,opacity:[0,1,1,.4]},transition:{pathLength:{duration:.9,delay:e.delay,ease:wh},opacity:{duration:2.1,delay:e.delay,times:[0,.1,.65,1]}}},e.d)),(0,G.jsx)(K.circle,{cx:a.dotX,cy:`252`,r:`30`,initial:{pathLength:0},animate:{pathLength:1},transition:{duration:.8,delay:.55,ease:wh}})]}),kh.map(e=>(0,G.jsx)(K.text,{x:e.x,y:e.y,className:`loader-spec`,initial:{opacity:0},animate:{opacity:[0,1,1,.5]},transition:{duration:1.8,delay:e.delay,times:[0,.15,.7,1]},children:e.text},e.text)),(0,G.jsx)(K.text,{x:`110`,y:`280`,className:`loader-word loader-word--outline`,initial:{strokeDashoffset:1400,opacity:1},animate:{strokeDashoffset:0,opacity:[1,1,0]},transition:{strokeDashoffset:{duration:1.05,delay:.5,ease:`easeInOut`},opacity:{duration:1.8,delay:.5,times:[0,.8,1]}},children:`hassaan`}),(0,G.jsx)(`text`,{x:`110`,y:`280`,className:`loader-word`,children:Eh.map((e,t)=>(0,G.jsx)(K.tspan,{initial:{fillOpacity:0},animate:{fillOpacity:1},transition:{duration:.3,delay:1.2+t*.08,ease:`easeOut`},children:e},t))}),(0,G.jsx)(K.circle,{cx:a.dotX,cy:`252`,r:`25`,className:`loader-dot`,initial:{scale:0,y:-90},animate:{scale:1,y:0},transition:{type:`spring`,stiffness:420,damping:15,delay:1.8},style:{transformBox:`fill-box`,transformOrigin:`center`}})]})}),(0,G.jsx)(`div`,{className:`loader-corner loader-corner--bl`,children:(0,G.jsx)(K.span,{className:`loader-count`,children:c})}),(0,G.jsx)(`div`,{className:`loader-corner loader-corner--br`,children:(0,G.jsx)(`span`,{children:`entrepreneurship · consultative sales · growth`})})]},`loader`)})}"""'''

code = code[:s1_pos] + new_splice_1 + code[s1_end:]

# -----------------------------------------------------------------------------
# 2. Update SPLICE_5: SafeCanvas for 3D door + synchronous WebGL check
# -----------------------------------------------------------------------------
old_splice_5_start = 'SPLICE_5 = r"""var _B=``;'
old_splice_5_end = '\n\n# ============================================================================\n# SPLICE 6:'
s5_pos = code.find(old_splice_5_start)
s5_end = code.find(old_splice_5_end)
if s5_pos == -1 or s5_end == -1:
    raise RuntimeError(f"SPLICE_5 markers not found: {s5_pos}, {s5_end}")

new_splice_5 = '''SPLICE_5 = r"""var _B=``;
class SafeCanvas extends v.Component{
  constructor(props){super(props);this.state={hasError:!1}}
  static getDerivedStateFromError(){return{hasError:!0}}
  componentDidCatch(err){console.warn(`3D canvas fallback:`,err)}
  render(){if(this.state.hasError)return this.props.fallback||null;return this.props.children}
}
function bB({clone:e=!1,openProgress:t=0,hingeRef:n}){
  return(0,G.jsxs)(`group`,{scale:1.15,children:[
    (0,G.jsx)(`mesh`,{position:[0,0,-0.08],children:[(0,G.jsx)(`boxGeometry`,{args:[1.62,2.62,0.14]}),(0,G.jsx)(`meshStandardMaterial`,{color:`#242620`,roughness:0.45,metalness:0.15})]}),
    (0,G.jsx)(`mesh`,{position:[0,0,-0.05],children:[(0,G.jsx)(`planeGeometry`,{args:[1.34,2.36]}),(0,G.jsx)(`meshBasicMaterial`,{color:`#141212`})]}),
    (0,G.jsx)(`mesh`,{position:[0,0,-0.03],children:[(0,G.jsx)(`planeGeometry`,{args:[1.24,2.24]}),(0,G.jsx)(`meshBasicMaterial`,{color:`#e25531`,transparent:!0,opacity:0.22})]}),
    (0,G.jsxs)(`group`,{ref:n,position:[-0.67,0,0.01],rotation:[0,-t*Math.PI*0.74,0],children:[
      (0,G.jsx)(`mesh`,{position:[0.67,0,0],children:[(0,G.jsx)(`boxGeometry`,{args:[1.34,2.36,0.09]}),(0,G.jsx)(`meshStandardMaterial`,{color:`#b53c1f`,roughness:0.38,metalness:0.12})]}),
      (0,G.jsx)(`mesh`,{position:[0.67,0.56,0.052],children:[(0,G.jsx)(`boxGeometry`,{args:[1.02,0.82,0.025]}),(0,G.jsx)(`meshStandardMaterial`,{color:`#8f2d15`,roughness:0.48,metalness:0.08})]}),
      (0,G.jsx)(`mesh`,{position:[0.67,-0.56,0.052],children:[(0,G.jsx)(`boxGeometry`,{args:[1.02,0.82,0.025]}),(0,G.jsx)(`meshStandardMaterial`,{color:`#8f2d15`,roughness:0.48,metalness:0.08})]}),
      (0,G.jsx)(`mesh`,{position:[1.16,-0.04,0.08],children:[(0,G.jsx)(`sphereGeometry`,{args:[0.065,24,24]}),(0,G.jsx)(`meshStandardMaterial`,{color:`#ead56f`,roughness:0.2,metalness:0.85})]}),
      (0,G.jsx)(`mesh`,{position:[1.16,-0.04,0.05],children:[(0,G.jsx)(`cylinderGeometry`,{args:[0.035,0.035,0.06,16]}),(0,G.jsx)(`meshStandardMaterial`,{color:`#ead56f`,roughness:0.25,metalness:0.8})]})
    ]})
  ]})
}
function CB({progress:e,onTriggerOpen:t}){
  let r=(0,v.useRef)(null),hinge=(0,v.useRef)(null),n=dI(e=>e.invalidate);
  return(0,v.useEffect)(()=>(n(),e.on(`change`,()=>n())),[e,n]),fI(()=>{
    if(!r.current)return;
    let p=e.get(),
        approach=Math.min(p/.25,1),
        swing=Math.min(Math.max((p-.12)/.5,0),1),
        enter=Math.min(Math.max((p-.52)/.38,0),1),
        ease=x=>1-(1-x)**3,
        sc=.92+ease(approach)*0.65+ease(enter)*2.6;
    r.current.scale.setScalar(sc);
    r.current.rotation.y=(1-ease(approach))*0.28-ease(swing)*0.08;
    r.current.rotation.x=.06*(1-ease(swing));
    r.current.position.y=-.18*(1-ease(approach))+.12*ease(enter);
    r.current.position.z=ease(enter)*1.65;
    r.current.visible=p<.995;
    if(hinge.current){
      hinge.current.rotation.y=-ease(swing)*Math.PI*0.76;
    }
  }),(0,G.jsx)(`group`,{ref:r,onClick:t,children:(0,G.jsx)(bB,{hingeRef:hinge})})
}
function wB({progress:e,onTriggerOpen:t}){
  return(0,G.jsx)(SafeCanvas,{children:(0,G.jsxs)(RL,{frameloop:`demand`,camera:{position:[0,0,6],fov:32},dpr:[1,1.6],gl:{antialias:!0,alpha:!0},children:[
    (0,G.jsx)(`ambientLight`,{intensity:.85,color:`#ffffff`}),
    (0,G.jsx)(`hemisphereLight`,{args:[`#fff8f0`,`#242620`,.65]}),
    (0,G.jsx)(`directionalLight`,{position:[3,4,5],intensity:1.8,color:`#ffffff`}),
    (0,G.jsx)(`directionalLight`,{position:[-4,2,-3],intensity:.75,color:`#d8631f`}),
    (0,G.jsx)(`pointLight`,{position:[0,0,1.2],intensity:1.2,color:`#ead56f`}),
    (0,G.jsx)(CB,{progress:e,onTriggerOpen:t})
  ]})})
}
function TB(){try{let e=document.createElement(`canvas`);return!!(e.getContext(`webgl`)||e.getContext(`experimental-webgl`))}catch{return!1}}
var EB=[{at:0,text:`Click the door (or scroll) to open & enter my workstation.`},{at:.25,text:`Opening the door — let's go look inside.`}];
function DB(){
  let e=(0,v.useRef)(null),{scrollYProgress:t}=bg(e),n=um(),[r,i]=(0,v.useState)(()=>TB());
  (0,v.useEffect)(()=>{i(TB())},[]);
  let a=am(t,e=>Math.max(0,Math.min((e-.78)/.12,1))*3.4),
      o=am(t,[0,.15,.68,.84,1],[1,1,1,0,0]),
      [s,c]=(0,v.useState)(EB[0].text),
      openDoorAndEnter=(0,v.useCallback)(()=>{
        Ch.clunk();
        setTimeout(()=>Ch.whoosh(),260);
        let workEl=document.getElementById(`work`);
        if(!workEl)return;
        let lenis=Vm();
        if(lenis){
          lenis.scrollTo(workEl,{duration:2.2});
        }else{
          workEl.scrollIntoView({behavior:`smooth`});
        }
      },[]);
  return(0,v.useEffect)(()=>t.on(`change`,e=>{let t=[...EB].reverse().find(t=>e>=t.at);t&&c(t.text)}),[t]),n||!r?(0,G.jsxs)(`section`,{className:`paper-grain flex min-h-[70vh] flex-col items-center justify-center gap-6 bg-[var(--color-paper)] px-6 py-24 text-center`,children:[(0,G.jsx)(`p`,{className:`max-w-sm text-lg text-[var(--color-ink-dim)]`,children:`Open the Door — heading straight into Entrepreneurship Experiments.`}),(0,G.jsx)(`a`,{href:`#work`,className:`text-sm font-medium text-[var(--color-ink)] underline decoration-[var(--color-accent)] decoration-2 underline-offset-4`,children:`Open the Door →`})]}):(0,G.jsx)(`div`,{ref:e,className:`headset-wrapper`,children:(0,G.jsxs)(`div`,{"data-scroll-stage":!0,className:`headset-stage overflow-hidden bg-[var(--color-paper)]`,children:[(0,G.jsx)(`div`,{className:`absolute inset-0`,style:{cursor:`var(--cursor-pointer)`},onClick:openDoorAndEnter,children:(0,G.jsx)(wB,{progress:t,onTriggerOpen:openDoorAndEnter})}),(0,G.jsxs)(K.div,{style:{opacity:o},className:`pointer-events-none absolute inset-x-0 bottom-[9%] flex flex-col items-center gap-3 text-center`,children:[(0,G.jsxs)(`button`,{type:`button`,onClick:openDoorAndEnter,className:`door-stage-cta`,children:[(0,G.jsx)(`span`,{className:`door-stage-cta-dot`,"aria-hidden":!0}),(0,G.jsx)(`span`,{children:`Open the Door`}),(0,G.jsx)(`span`,{"aria-hidden":!0,children:`→`})]}),(0,G.jsx)(`p`,{className:`text-base text-[var(--color-ink-dim)] sm:text-lg`,children:s})]}),(0,G.jsx)(`a`,{href:`#work`,className:`tabular absolute bottom-8 right-6 z-20 text-[11px] text-[var(--color-ink-dim)] underline decoration-[var(--color-line)] underline-offset-4 transition-colors hover:text-[var(--color-ink)] sm:right-10`,children:`SKIP TO WORKSTATION →`}),(0,G.jsx)(K.div,{"aria-hidden":!0,"data-progress-iris":!0,style:{scale:a},className:`pointer-events-none absolute left-1/2 top-1/2 h-[60vmax] w-[60vmax] -translate-x-1/2 -translate-y-1/2 rounded-full bg-[var(--color-void)]`})]})})
}"""'''

code = code[:s5_pos] + new_splice_5 + code[s5_end:]

# -----------------------------------------------------------------------------
# 3. Update SPLICE_6: Safe tV and guarded hV & _V
# -----------------------------------------------------------------------------
code = code.replace(
    'cat_sprite_to_vv_code = src[pos_nv_cat:pos_vv].replace("Samay\'s cat", "Hassaan\'s cat")',
    '''cat_sprite_to_vv_code = src[pos_nv_cat:pos_vv].replace("Samay's cat", "Hassaan's cat")
# Guard hV against missing entries
cat_sprite_to_vv_code = cat_sprite_to_vv_code.replace(
    "function hV(e,t){let n=e[t],r=e.body/(UB.right-UB.left)*n.scale;",
    "function hV(e,t){if(!e||!e[t])return{scale:1,left:0,top:0,width:0,height:0};let n=e[t],r=e.body/(UB.right-UB.left)*(n.scale||1);"
)
# Guard _V layout effect transform
cat_sprite_to_vv_code = cat_sprite_to_vv_code.replace(
    "e&&a&&!p.current&&(e.style.transform=gV(hV(a,d.current)))",
    "e&&a&&!p.current&&(()=>{try{let pos=hV(a,d.current);if(pos)e.style.transform=gV(pos)}catch(err){}})()"
)'''
)

old_tv = r"""function tV(e,t){let n=e.firstChild,r=e.querySelector(`.hero-wordmark-baseline`);if(!n||n.nodeType!==Node.TEXT_NODE||!r)return null;let i=getComputedStyle(e),a=Number.parseFloat(i.fontSize),o=`${i.fontStyle} ${i.fontWeight} ${WB}px ${i.fontFamily}`,s=`${o}|${[...document.fonts].map(e=>e.status).join(``)}`;YB.has(s)||YB.set(s,QB(o));let c=YB.get(s);if(!c)return null;let{bowl:u}=c,d=u.bottom-u.top,f=Math.max(...[...u.rows.values()].map(e=>e.right-e.left)),m=Math.max(GB/(a/WB),f*1.02),g=a/WB,_=t.getBoundingClientRect(),v=r.getBoundingClientRect().top-_.top,y=e=>{let t=document.createRange();return t.setStart(n,e),t.setEnd(n,e+1),t.getBoundingClientRect().left-_.left},b=(e,t,n)=>({x:e+(t-qB)*g,bottom:v+(n-JB)*g}),x=(n.textContent??``).toLowerCase(),S=x.lastIndexOf(`a`),C=x.indexOf(`a`);if(S<0||C<0)return null;let w=u.bottom-d*.04;return{body:m*g,shelf:v-c.xHeight*g,y:{id:`y`,scale:.92,...b(y(S),eV(u,u.top+d*.55),w)},a:{id:`a`,scale:.84,...b(y(C),eV(u,u.top+d*.55),w)}}}"""

new_tv = r"""function tV(e,t){
  try{
    let n=e.firstChild,r=e.querySelector(`.hero-wordmark-baseline`);
    if(!n||n.nodeType!==Node.TEXT_NODE||!r)return null;
    let i=getComputedStyle(e),a=Number.parseFloat(i.fontSize)||184,o=`${i.fontStyle} ${i.fontWeight} ${WB}px ${i.fontFamily}`;
    let fontsStatus;
    try{fontsStatus=document.fonts?[...document.fonts].map(e=>e.status).join(``):`ready`}catch{fontsStatus=`ready`}
    let s=`${o}|${fontsStatus}`;
    YB.has(s)||YB.set(s,QB(o));
    let c=YB.get(s);
    if(!c||!c.bowl||!c.bowl.rows)return null;
    let{bowl:u}=c,d=u.bottom-u.top,f=Math.max(...[...u.rows.values()].map(e=>e.right-e.left)),m=Math.max(GB/(a/WB),f*1.02),g=a/WB,_=t.getBoundingClientRect(),v=r.getBoundingClientRect().top-_.top,y=e=>{let t=document.createRange();return t.setStart(n,e),t.setEnd(n,e+1),t.getBoundingClientRect().left-_.left},b=(e,t,n)=>({x:e+(t-qB)*g,bottom:v+(n-JB)*g}),x=(n.textContent??``).toLowerCase(),S=x.lastIndexOf(`a`),C=x.indexOf(`a`);
    if(S<0||C<0)return null;
    let w=u.bottom-d*.04;
    return{body:m*g,shelf:v-c.xHeight*g,y:{id:`y`,scale:.92,...b(y(S),eV(u,u.top+d*.55),w)},a:{id:`a`,scale:.84,...b(y(C),eV(u,u.top+d*.55),w)}}
  }catch(err){
    return null;
  }
}"""

code = code.replace(old_tv, new_tv)

# -----------------------------------------------------------------------------
# 4. Update SPLICE_8: AppErrorBoundary around createRoot
# -----------------------------------------------------------------------------
old_render = r"""(0,b.createRoot)(document.getElementById(`root`)).render((0,G.jsx)(v.StrictMode,{children:(0,G.jsx)(Sn,{children:(0,G.jsx)($K,{})})}));"""
new_render = r"""class AppErrorBoundary extends v.Component{
  constructor(props){super(props);this.state={hasError:!1,error:null}}
  static getDerivedStateFromError(err){return{hasError:!0,error:err}}
  componentDidCatch(err,info){console.error(`Portfolio Error caught:`,err,info)}
  render(){
    if(this.state.hasError){
      return(0,G.jsxs)(`div`,{style:{minHeight:`100vh`,padding:`48px 24px`,background:`#f1f0eb`,color:`#242620`,fontFamily:`system-ui,sans-serif`,display:`flex`,flexDirection:`column`,alignItems:`center`,justifyContent:`center`,textAlign:`center`},children:[
        (0,G.jsx)(`h1`,{style:{fontSize:`36px`,fontFamily:`serif`,marginBottom:`14px`},children:`Hey! I'm Hassaan.`}),
        (0,G.jsx)(`p`,{style:{fontSize:`18px`,color:`#6f7168`,maxWidth:`540px`,marginBottom:`28px`,lineHeight:1.6},children:`I listen to people & solve their problems by giving them tailored solutions.`}),
        (0,G.jsx)(`a`,{href:`/`,onClick:()=>window.location.reload(),style:{padding:`12px 26px`,borderRadius:`999px`,background:`#242620`,color:`#f1f0eb`,textDecoration:`none`,fontWeight:`600`},children:`Reload Portfolio`})
      ]});
    }
    return this.props.children;
  }
}
(0,b.createRoot)(document.getElementById(`root`)).render((0,G.jsx)(v.StrictMode,{children:(0,G.jsx)(AppErrorBoundary,{children:(0,G.jsx)(Sn,{children:(0,G.jsx)($K,{})})})}));"""

code = code.replace(old_render, new_render)

# Write updated build_portfolio.py
with open(BUILD_SCRIPT, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated build_portfolio.py successfully!")
