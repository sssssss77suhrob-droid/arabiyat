import {normalizeArabic} from './learning';
import type {Rect,ScanWord} from './book-work';

export type TimedWord={start:number;end:number;word:string;wordId?:string;rect?:Rect};
export function popoverPosition(anchor:{x:number;y:number;width:number;height:number},width:number,height:number,viewport:{width:number;height:number}){
 const left=Math.max(8,Math.min(viewport.width-width-8,anchor.x+anchor.width/2-width/2));
 const below=anchor.y+anchor.height+12;
 const top=below+height<=viewport.height-8?below:Math.max(8,anchor.y-height-12);
 return {left,top};
}
export function swipePage(dx:number,dy:number,elapsed:number){return elapsed<900&&Math.abs(dx)>75&&Math.abs(dx)>Math.abs(dy)*1.8?(dx>0?1:-1):0;}
const normalize=(s:string)=>normalizeArabic(s).replace(/[أإآ]/g,'ا').replace(/[^\u0621-\u064a]/g,'');
export function alignTranscript(transcript:TimedWord[],words:ScanWord[]):TimedWord[]{
 const sorted=[...words].sort((a,b)=>Math.round(a.rect.y/.025)-Math.round(b.rect.y/.025)||b.rect.x-a.rect.x);
 let cursor=-1,previous='';
 return transcript.map(t=>{const key=normalize(t.word);if(!key)return t;
  let index=key===previous&&cursor>=0&&normalize(sorted[cursor].ar)===key?cursor:sorted.findIndex((w,i)=>i>cursor&&normalize(w.ar)===key);
  if(index<0)index=sorted.findIndex(w=>normalize(w.ar)===key);
  previous=key;if(index<0)return t;cursor=index;return {...t,wordId:sorted[index].id,rect:sorted[index].rect};
 });
}
export function currentTimedWord(words:TimedWord[],seconds:number){return words.find(w=>seconds>=w.start&&seconds<w.end);}
export function centeredBookPopover(book:{x:number;y:number;width:number;height:number}|null,width:number,height:number,viewport:{width:number;height:number;x?:number;y?:number}){const x=viewport.x??0,y=viewport.y??0,l=Math.max(x,book?.x??x),r=Math.min(x+viewport.width,(book?.x??x)+(book?.width??viewport.width)),t=Math.max(y,book?.y??y),b=Math.min(y+viewport.height,(book?.y??y)+(book?.height??viewport.height));return {left:Math.max(x+10,Math.min(x+viewport.width-width-10,(l+r)/2-width/2)),top:Math.max(y+10,Math.min(y+viewport.height-height-10,(t+b)/2-height/2))};}
export function wordProgress(word:TimedWord,time:number){return Math.max(0,Math.min(1,(time-word.start)/Math.max(.001,word.end-word.start)));}

/** Use the nearest printed word when finger-sized hit areas overlap. */
export function findScanWord(words:ScanWord[],x:number,y:number,padding:{x:number;y:number}={x:0,y:0}){
 return words.filter(w=>w.uz&&x>=w.rect.x-padding.x&&x<=w.rect.x+w.rect.w+padding.x&&y>=w.rect.y-padding.y&&y<=w.rect.y+w.rect.h+padding.y).sort((a,b)=>Math.hypot(x-a.rect.x-a.rect.w/2,(y-a.rect.y-a.rect.h/2)*1.334)-Math.hypot(x-b.rect.x-b.rect.w/2,(y-b.rect.y-b.rect.h/2)*1.334))[0];
}
