import type {Book,PreparedAnswer} from './types';
import {normalizeArabic} from './learning';
import {sentenceText} from './catalog';
export const analysisEnabled=(book:Book)=>book.id!=='manhaj-a0'&&book.analysisMode!=='none';
export function preparedAnswer(book:Book,unitId:string,page:number,text:string,context:string,kind:string):PreparedAnswer|null{
 const unit=book.units.find(u=>u.id===unitId),p=unit?.pages.find(p=>p.number===page);if(!unit||!p)return null;
 const word=book.words.find(w=>normalizeArabic(w.ar)===normalizeArabic(text)&&unit.wordIds.includes(w.id)),target=p.wordTargets?.find(w=>normalizeArabic(w.ar)===normalizeArabic(text));
 const base:PreparedAnswer={translation:'',explanation:'',arabicExample:'',exampleTranslation:'',past:'',present:'',command:'',masdar:'',isVerb:false,parts:[],verbs:[]};
 if(kind==='translation'){const uz=target?.uz??word?.uz,forms=target?.forms??word?.forms;return uz?{...base,translation:uz,...forms,isVerb:!!forms}:null;}
 const s=p.sentences.find(s=>normalizeArabic(sentenceText(s))===normalizeArabic(context));
 if(kind==='sentence')return s?{...base,translation:s.uz}:null;
 if(!analysisEnabled(book))return null;
 if(kind==='rule')return p.rule?{...base,explanation:p.rule}:null;
 if(!s)return null;if(s.prepared)return {...base,...s.prepared,translation:s.uz,explanation:kind==='sarf'?s.prepared.sarf:s.prepared.nahv};
 if(book.sample)return {...base,translation:s.uz,explanation:s.analysis,parts:s.tokens.map(t=>{const w=book.words.find(w=>w.id===t.wordId);return {ar:t.ar,uz:t.uz??w?.uz??'',sarf:w?.sarf??'',nahv:t.nahv??w?.nahv??''};}),verbs:s.tokens.flatMap(t=>{const w=book.words.find(w=>w.id===t.wordId);return w?.forms?[{...w.forms,uz:w.uz}]:[];})};return null;
}
