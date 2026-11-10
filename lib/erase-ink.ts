import type {Point,Stroke} from './types';
/** Cut polyline segments at a circular eraser boundary; never paint over the page. */
export function eraseInk(strokes:Stroke[],center:Point,radius:number,height:number,newId:()=>string):Stroke[]{
 const result:Stroke[]=[];
 for(const s of strokes){
  const r=radius+s.width/2,c={x:center.x*1000,y:center.y*height};let touched=false;const runs:Point[][]=[];let run:Point[]=[];
  const flush=()=>{if(run.length)runs.push(run);run=[];};
  if(s.points.length===1){const p=s.points[0];if(Math.hypot(p.x*1000-c.x,p.y*height-c.y)>r)result.push(s);continue;}
  for(let i=1;i<s.points.length;i++){
   const a=s.points[i-1],b=s.points[i],dx=(b.x-a.x)*1000,dy=(b.y-a.y)*height,ox=a.x*1000-c.x,oy=a.y*height-c.y,A=dx*dx+dy*dy,B=2*(ox*dx+oy*dy),C=ox*ox+oy*oy-r*r,D=B*B-4*A*C;
   let lo=0,hi=0,hit=false;
   if(A===0){hit=C<=0;hi=1;}else if(D>0){lo=Math.max(0,(-B-Math.sqrt(D))/(2*A));hi=Math.min(1,(-B+Math.sqrt(D))/(2*A));hit=hi>lo;}
   const at=(t:number)=>({x:a.x+(b.x-a.x)*t,y:a.y+(b.y-a.y)*t});
   if(!hit){if(!run.length)run.push(a);run.push(b);continue;}
   touched=true;
   if(lo>0){if(!run.length)run.push(a);run.push(at(lo));}flush();
   if(hi<1)run=[at(hi),b];
  }
  flush();if(!touched)result.push(s);else for(const points of runs)if(points.length>1)result.push({...s,id:newId(),points});
 }
 return result;
}
