import {createRequire} from 'node:module';
import {readFile,readdir} from 'node:fs/promises';
import {resolve} from 'node:path';
import assert from 'node:assert/strict';
import {randomUUID} from 'node:crypto';
const require=createRequire(import.meta.url),wranglerRequire=createRequire(require.resolve('wrangler/package.json'));
const {Miniflare}=await import(wranglerRequire.resolve('miniflare'));
const files=(await readdir('dist/server',{recursive:true})).filter(p=>p.endsWith('.js')&&p!=='index.js');
const modules=await Promise.all(['index.js',...files].map(async p=>({type:'ESModule',path:resolve('dist/server',p),contents:await readFile(resolve('dist/server',p),'utf8')})));
const mf=new Miniflare({modules,modulesRoot:resolve('dist/server'),compatibilityDate:'2026-05-15',compatibilityFlags:['nodejs_compat'],d1Databases:['DB'],r2Buckets:['BUCKET'],bindings:{ADMIN_USER_IDS:'qa-admin'},cf:false,inspectorPort:0});
const who='qa-'+randomUUID();
function headers(user=who){return user?{'oai-authenticated-user-id':user,'oai-authenticated-user-email':'qa@example.test'}:{};}
async function upload(form){const req=new Request('http://arabiyat.test/api/admin/upload',{method:'POST',body:form});return mf.dispatchFetch(req.url,{method:'POST',headers:{...headers('qa-admin'),'Content-Type':req.headers.get('content-type')},body:await req.arrayBuffer()});}
async function call(path,body,user=who,method=body?'POST':'GET',extra={}){const r=await mf.dispatchFetch('http://arabiyat.test'+path,{method,headers:{...headers(user),...(body?{'Content-Type':'application/json'}:{}),...extra},body:body?JSON.stringify(body):undefined});const text=await r.text();let data;try{data=JSON.parse(text);}catch{throw new Error(`Non-JSON ${r.status}: ${text.slice(0,200)}`);}return {status:r.status,data};}
try{
 const db=await mf.getD1Database('DB');for(const file of (await readdir('drizzle')).filter(f=>f.endsWith('.sql')).sort()){const migration=await readFile('drizzle/'+file,'utf8');for(const sql of migration.replaceAll('--> statement-breakpoint','').split(';').map(s=>s.trim()).filter(Boolean))await db.prepare(sql).run();}
 assert.equal((await call('/api/learning',{},null)).status,401);
 let content=await call('/api/content');assert.equal(content.status,200,JSON.stringify(content));assert.equal(content.data.state.attempts.length,0);assert.equal(content.data.isAdmin,false);
 assert.equal((await call('/api/admin/books')).status,403);
 assert.equal((await call('/api/admin/books',undefined,'qa-admin')).status,200);
 const answer={type:'answer',id:randomUUID(),bookId:'manhaj-a2',unitId:'a2-sample-1',wordId:'student',mode:'write',answer:'طالب',direction:'ar',formIndex:0,strict:false,assisted:false,seconds:4};
 let r=await call('/api/learning',answer);assert.equal(r.status,200,JSON.stringify(r));assert.equal(r.data.result.correct,true);assert.equal(r.data.state.reviews[0].stage,1);
 assert.equal((await call('/api/learning',answer)).data.state.attempts.length,1);
 assert.equal((await call('/api/learning',{...answer,id:randomUUID(),wordId:'water'})).status,400);
 r=await call('/api/learning',{...answer,id:randomUUID(),answer:'ماء'});assert.equal(r.data.result.correct,false);assert.equal(r.data.state.reviews[0].unknown,true);
 r=await call('/api/learning',{...answer,id:randomUUID(),assisted:true});assert.equal(r.data.state.reviews[0].unknown,true);assert.equal(r.data.state.reviews[0].stage,0);
 r=await call('/api/learning',{type:'flashcard',id:randomUUID(),bookId:'manhaj-a2',unitId:'a2-sample-1',wordId:'teacher',rating:'hard'});assert.equal(r.status,200);assert(r.data.state.reviews.find(r=>r.wordId==='teacher').unknown);
 assert.equal((await call('/api/learning',{...answer,id:randomUUID(),wordId:'book',strict:true,answer:'كتاب'})).data.result.correct,false);
 assert.equal((await call('/api/learning',{...answer,id:randomUUID(),wordId:'read',mode:'forms',formIndex:2,answer:'اقرأ'})).data.result.correct,true);
 assert.equal((await call('/api/learning',{type:'profile',displayName:'Suhrob',dailyGoal:25})).status,200);
 assert.equal((await call('/api/learning',{type:'reading',bookId:'manhaj-a2',unitId:'a2-sample-1',page:3})).status,400);
 assert.equal((await call('/api/learning',{type:'reading',bookId:'manhaj-a2',unitId:'a2-sample-1',page:2})).status,200);
 assert.equal((await call('/api/learning',{type:'save',key:'a2-sample-1:student',done:true})).status,200);assert.equal((await call('/api/learning',{type:'save',key:'a2-sample-1:water',done:true})).status,400);
 const note={bookId:'manhaj-a2',page:1,expectedVersion:0,document:{strokes:[{id:'ink',tool:'pen',color:'#32623f',width:3,points:[{x:.1,y:.2},{x:.3,y:.4}]}],texts:[{id:'text',x:.8,y:.3,text:'Tarjima qaydi',color:'#32623f'}]}};
 assert.equal((await call('/api/notes',note,who,'PUT')).data.version,1);
 assert.equal((await call('/api/notes',note,who,'PUT')).status,409);
 assert.equal((await call('/api/notes?bookId=manhaj-a2&page=1')).data.document.texts[0].text,'Tarjima qaydi');
 assert.equal((await call('/api/notes?bookId=manhaj-a2&page=1',undefined,who+'-other')).data.version,0);
 assert.equal((await call('/api/notes',{...note,expectedVersion:1,document:{...note.document,strokes:[{...note.document.strokes[0],points:[{x:2,y:.2}]}]}},who,'PUT')).status,400);
 const analyze={bookId:'manhaj-a2',unitId:'a2-sample-1',page:1,text:'طَالِبٌ',context:'أَنَا طَالِبٌ.',kind:'nahv'};
 assert.equal((await call('/api/analyze',analyze)).status,403);
 assert.equal((await call('/api/analyze',{...analyze,kind:'translation'})).data.answer.translation,'talaba');
 assert.equal((await call('/api/analyze',{...analyze,bookId:'at-tanal',unitId:'tanal-sample-1'})).status,400);
 assert.equal((await call('/api/learning',answer,who,'POST',{Origin:'https://elsewhere.test'})).status,403);
 // Upload → R2 → ranged read; content type is checked against the actual bytes.
 let form=new FormData();form.set('file',new File(['fake data'],'bad.pdf',{type:'application/pdf'}));let response=await upload(form);assert.equal(response.status,400);
 const pdf='%PDF-1.4\n1 0 obj<</Type/Catalog>>endobj\n%%EOF';form=new FormData();form.set('file',new File([pdf],'qa.pdf',{type:'application/pdf'}));response=await upload(form);assert.equal(response.status,200);const asset=await response.json();
 response=await mf.dispatchFetch('http://arabiyat.test/api/assets?key='+asset.asset.key,{headers:{...headers(),Range:'bytes=0-4'}});assert.equal(response.status,206);assert.equal(await response.text(),'%PDF-');
 const book=content.data.books.find(b=>b.id==='manhaj-a2');r=await call('/api/admin/books',{...book,pdfKey:asset.asset.key,status:'published'},'qa-admin','PUT');assert.equal(r.status,200,JSON.stringify(r));
 assert.equal((await call('/api/admin/books',{...book,id:'other-book'},'qa-admin','PUT')).status,400);
 assert.equal((await call('/api/content')).data.state.profile.displayName,'Suhrob');assert.equal((await call('/api/content')).data.state.profile.lastPage,2);
 assert.equal((await call('/api/content',undefined,who+'-other')).data.state.attempts.length,0);
 // Original A0 exercises: draft/check, optimistic version and user isolation.
 const p20=await call('/api/book-page?bookId=manhaj-a0&page=20');assert.equal(p20.status,200);assert.equal(p20.data.exercises[0].slots.length,12);
 const workBody={bookId:'manhaj-a0',page:20,exerciseId:'a0-p020-e1',expectedVersion:0,document:{answers:{s0:p20.data.exercises[0].slots[0].accepted[0]},checked:true,manualDone:false}};
 r=await call('/api/book-work',workBody,who,'PUT');assert.equal(r.status,200,JSON.stringify(r));assert.equal(r.data.record.grade.correct,1);assert.equal(r.data.record.grade.complete,false);assert.equal(r.data.record.version,1);
 assert.equal((await call('/api/book-work',workBody,who,'PUT')).status,409);
 assert.equal((await call('/api/book-work',{...workBody,page:21},who,'PUT')).status,404);
 assert.equal((await call('/api/book-work?bookId=manhaj-a0',undefined,who+'-other')).data.records.length,0);
 const completeAnswers=Object.fromEntries(p20.data.exercises[0].slots.map(s=>[s.id,s.accepted[0]]));
 r=await call('/api/book-work',{...workBody,expectedVersion:1,document:{...workBody.document,answers:completeAnswers}},who,'PUT');assert.equal(r.data.record.grade.complete,true);assert.equal(r.data.record.grade.correct,12);
 assert((await call('/api/content')).data.activityProgress.some(x=>x.exerciseId==='a0-p020-e1'&&x.complete));
 assert.equal((await call('/api/content')).data.state.attempts.length,6,'book worksheet must not inflate vocabulary mastery');
 assert.equal((await call('/api/book-work',{...workBody,expectedVersion:2,document:{...workBody.document,answers:{fake:'x'}}},who,'PUT')).status,400);
 // Saving a scanned word is authenticated, catalog-scoped, trusted and isolated.
 const scanPage=await call('/api/book-page?bookId=manhaj-a0&page=34');const scan=scanPage.data.words.find(w=>w.ar==='دَجَاجَةٌ');assert(scan?.id);assert.equal(scan.uz,'tovuq');
 const selection={type:'save-selection',bookId:'manhaj-a0',unitId:'manhaj-a0-v1-unit-04',page:34,scanId:scan.id,done:true,ar:'forged',uz:'forged'};
 assert.equal((await call('/api/learning',selection,null)).status,401);
 assert.equal((await call('/api/learning',{...selection,page:35})).status,400);
 assert.equal((await call('/api/learning',{...selection,unitId:'manhaj-a0-v1-unit-03'})).status,400);
 assert.equal((await call('/api/learning',selection)).status,200);
 assert.equal((await call('/api/learning',selection)).data.state.savedSelections.length,1);
 const stored=(await call('/api/content')).data.state.savedSelections[0];assert.equal(stored.ar,scan.ar);assert.equal(stored.uz,'tovuq');assert.equal(stored.page,34);
 assert.equal((await call('/api/content',undefined,who+'-other')).data.state.savedSelections.length,0);
 assert.equal((await call('/api/learning',{...selection,done:false})).data.state.savedSelections.length,0);
 // The bounded, checksummed streaming importer accepts only owner-authorized, exact manifest assets.
 assert.equal((await call('/api/admin/import')).status,403);
 // Optional original-media importer integration remains in the ingestion workflow.
 // Core R2 upload/range checks above use a self-contained fixture.
 const persisted=await db.prepare('SELECT count(*) AS n FROM attempts WHERE user_id=?').bind(who).first();assert.equal(persisted.n,6);
 console.log('PASS API: authenticated learning → D1 → reload, scope isolation, idempotency, reviews, harakat, verb forms, notes/409 conflict, admin guards, R2 upload/range, prepared-content gates, origin validation.');
}finally{await mf.dispose();}
