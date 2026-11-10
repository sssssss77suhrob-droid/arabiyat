import {readFile} from 'node:fs/promises';
import assert from 'node:assert/strict';
import ts from 'typescript';
import {createRequire} from 'node:module';
import {pathToFileURL} from 'node:url';
const require=createRequire(import.meta.url);
async function module(path,replacements={}){let source=await readFile(path,'utf8');if(path==='lib/catalog.ts'){source=source.replace("import a0BookData from './a0/book.json';",'const a0BookData='+await readFile('lib/a0/book.json','utf8')+';');}for(const [a,b] of Object.entries(replacements))source=source.replace(a,b);const out=ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;return import('data:text/javascript;base64,'+Buffer.from(out).toString('base64'));}
const l=await module('lib/learning.ts'),{defaultBooks}=await module('lib/catalog.ts');
const {bookSchema}=await module('lib/content-schema.ts',{"'zod'":JSON.stringify(pathToFileURL(require.resolve('zod')).href)});
const book=defaultBooks.find(b=>b.id==='manhaj-a2'),unit=book.units[0],word=book.words[0],now=Date.now();
let state=l.emptyState(now);
for(let i=0;i<4;i++)state.attempts.push({id:String(i),unitId:unit.id,wordId:word.id,mode:'write',correct:true,assisted:false,createdAt:now,seconds:2,answer:word.ar});
assert.equal(l.unitStats(state,unit).mastered,1);assert.equal(l.unitStats(state,unit).progress,8);assert.equal(l.bookStats(state,book).progress,4);
state.attempts.push({id:'flash',unitId:unit.id,wordId:'teacher',mode:'flashcard',correct:true,assisted:true,createdAt:now,seconds:0,answer:'known'});
state.attempts.push({id:'help',unitId:unit.id,wordId:'teacher',mode:'write',correct:true,assisted:true,createdAt:now,seconds:2,answer:'x'});
assert.equal(l.unitStats(state,unit).mastered,1);
for(const b of defaultBooks)assert.equal(bookSchema.safeParse(b).success,true,b.id);
for(const u of book.units)for(const id of u.wordIds){const w=book.words.find(w=>w.id===id);for(const mode of ['choice','write','dictation','cloze','shuffle',...(w.forms?['forms']:[])]){for(const w of book.words){assert(w.reteachExample&&w.reteachExample!==w.example,w.id);assert(w.reteachExample.includes(w.ar));}
const q=l.makeQuestion(book,u,w,mode);assert(l.gradeAnswer(q,q.answer[0],true),id+':'+mode);if(mode==='cloze')assert(q.promptAr.includes('______'),id);assert(q.options.every(o=>u.wordIds.some(id=>book.words.find(w=>w.id===id)?.ar===o)));}}
const q=l.makeQuestion(book,unit,word,'write');assert(l.gradeAnswer(q,'طالب'));assert(!l.gradeAnswer(q,'طالب',true));assert(!l.gradeAnswer(q,'طليب'));assert.notEqual(l.normalizeArabic('أَمَلٌ'),l.normalizeArabic('عَمَلٌ'));
assert.equal(l.membership(now-9*86400000).canAnalyze,false);assert.equal(l.membership(now).trialDaysLeft,7);assert.equal(l.membership(now,'premium',now-1).canAnalyze,false);assert.equal(l.membership(now,'premium',now+86400000).canAnalyze,true);
assert.equal(l.nextReview(undefined,false,now).dueAt,now+600000);assert.equal(l.nextReview(undefined,true,now).dueAt,now+86400000);
assert.equal(bookSchema.safeParse({...book,units:[unit,{...unit,id:'other'}]}).success,false);
assert.equal(bookSchema.safeParse({...book,words:[...book.words,{...book.words[8],id:'bad-verb',forms:undefined}]}).success,false);
console.log('PASS domain: scope, six modes, grading, harakat, independent unique mastery, weighted book progress, review intervals, trial, invalid content.');
