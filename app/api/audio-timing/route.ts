import {z} from 'zod';
import {identity,json,sameOrigin,getCatalog,isAdmin} from '../../../lib/server';
import prepared from '../../../lib/a0/audio-timings.json';
const input=z.object({bookId:z.literal('manhaj-a0'),page:z.number().int().min(1).max(112),audioId:z.string().max(150)});
type Track={key:string;page:number;duration:number;words:{word:string;start:number;end:number;wordId?:string;rect?:{x:number;y:number;w:number;h:number}}[]};
/** Book audio timings are prepared once from original recordings; playback never calls an AI API. */
export async function POST(req:Request){
 if(!sameOrigin(req))return json({error:'So‘rov manbasi mos emas.'},403);const user=await identity();if(!user)return json({error:'Hisobingizga kiring.'},401);
 try{const p=input.safeParse(await req.json());if(!p.success)return json({error:'Audio tanlovini tekshiring.'},400);const a=p.data,b=(await getCatalog(isAdmin(user.userId))).find(b=>b.id===a.bookId),q=b?.units.flatMap(u=>u.pages).find(p=>p.number===a.page)?.qrAudio?.find(q=>q.id===a.audioId&&!q.folder&&q.key);if(!q?.key)return json({error:'Audio shu sahifaga tegishli emas.'},404);
 const track=(prepared.tracks as Record<string,Track>)[a.audioId];if(!track||track.key!==q.key||track.page!==a.page)return json({error:'Bu audioning vaqt belgilari hali tayyorlanmagan.',code:'timing_not_prepared'},404);
 return json({words:track.words,matched:track.words.filter(w=>w.rect).length,duration:track.duration,source:'prepared'});
 }catch{return json({error:'Audio belgilarini yuklab bo‘lmadi.',code:'timing_failed'},503);}
}
