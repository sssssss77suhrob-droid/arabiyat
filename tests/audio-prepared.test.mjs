import assert from 'node:assert/strict';import {readFile} from 'node:fs/promises';
const book=JSON.parse(await readFile('lib/a0/book.json')),data=JSON.parse(await readFile('lib/a0/audio-timings.json')),assets=JSON.parse(await readFile('lib/a0/assets.json'));const qs=book.units.flatMap(u=>u.pages.flatMap(p=>(p.qrAudio??[]).filter(q=>q.key).map(q=>({...q,page:p.number}))));
assert.equal(qs.length,82);assert.equal(Object.keys(data.tracks).length,82);let mapped=0;
for(const q of qs){const t=data.tracks[q.id];assert(t,q.id);assert.equal(t.page,q.page);assert.equal(t.key,q.key);assert.equal(t.sha256,assets.find(a=>a.key===q.key).sha256);assert(t.duration>0);assert(t.words.length>0);let previous=-1;
 for(const w of t.words){assert(w.start>=0&&w.end>w.start&&w.end<=t.duration+.1,q.id+':'+JSON.stringify(w));assert(w.start>=previous,q.id+':nonchronological');previous=w.start;if(w.rect){mapped++;const r=w.rect;assert(r.x>=0&&r.y>=0&&r.w>0&&r.h>0&&r.x+r.w<=1.001&&r.y+r.h<=1.001,q.id+':rect');}}
 assert(t.words.some(w=>w.rect),q.id+':no mapped content');
}
const route=await readFile('app/api/audio-timing/route.ts','utf8');assert(!route.includes('openAI'));assert(!route.includes('takeAITurn'));
console.log(`PASS API-free timing assets:82 original source hashes, chronological real intervals, duration bounds and ${mapped} printed targets; no paid API adapter.`);
