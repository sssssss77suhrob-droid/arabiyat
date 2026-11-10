'use client';
import {useEffect,useRef} from 'react';
export function useLongPress(delay=500){
 const timer=useRef<ReturnType<typeof setTimeout>|null>(null),origin=useRef<{x:number;y:number}|null>(null),fired=useRef(false);
 const cancel=()=>{if(timer.current)clearTimeout(timer.current);timer.current=null;origin.current=null;};
 useEffect(()=>cancel,[]);
 function bind(action:(point:{x:number;y:number;rect:DOMRect;target:HTMLElement})=>void,quickTap?:()=>void){return {
  onPointerDown:(ev:React.PointerEvent<HTMLElement>)=>{cancel();fired.current=false;if(!ev.isPrimary||ev.button!==0)return;const x=ev.clientX,y=ev.clientY,target=ev.currentTarget;origin.current={x,y};timer.current=setTimeout(()=>{fired.current=true;timer.current=null;action({x,y,rect:target.getBoundingClientRect(),target});},delay);},
  onPointerMove:(ev:React.PointerEvent<HTMLElement>)=>{if(origin.current&&Math.hypot(ev.clientX-origin.current.x,ev.clientY-origin.current.y)>10)cancel();},
  onPointerUp:cancel,onPointerCancel:cancel,onPointerLeave:cancel,
  onContextMenu:(ev:React.MouseEvent<HTMLElement>)=>ev.preventDefault(),
  onClick:(ev:React.MouseEvent<HTMLElement>)=>{ev.stopPropagation();if(fired.current){ev.preventDefault();fired.current=false;return;}quickTap?.();},
  onKeyDown:(ev:React.KeyboardEvent<HTMLElement>)=>{if(ev.key==='Enter'||ev.key===' '){ev.preventDefault();const target=ev.currentTarget,r=target.getBoundingClientRect();action({x:r.x+r.width/2,y:r.y+r.height/2,rect:r,target});}}
 };}
 return {bind,cancel};
}
