'use client';
import {createContext,useContext} from 'react';
import type {Book,Bootstrap,LearningState,Forms,ActivityProgress} from '../lib/types';
export type View='home'|'library'|'book'|'reader'|'games'|'flashcards'|'vocabulary'|'phrases'|'review'|'results'|'profile'|'admin';
export type Selection={bookId:string;unitId:string;page:number;rect?:{x:number;y:number;w:number;h:number};anchor?:{x:number;y:number;width:number;height:number};lookup?:{x:number;y:number;image:string};pageLookup?:{x:number;y:number;image:string};contextVerified?:boolean;hasSentence?:boolean;scanId?:string;wordId?:string;ar:string;uz?:string;nahv?:string;context:string;analysis?:string;wholeSentence?:boolean;formsNote?:string;forms?:Forms};
export type Scope={bookId:string;unitIds:string[];filter:'all'|'unknown'|'due'|'saved'};
export type AppContextValue={data:Bootstrap;highlightRequest:{id:string;selection:Selection}|null;highlightWord:(s:Selection)=>void;clearHighlight:()=>void;setActivityProgress:(p:ActivityProgress)=>void;ready:boolean;saving:boolean;scope:Scope;setScope:(s:Scope)=>void;view:View;go:(v:View)=>void;bookId:string;openBook:(id:string)=>void;openReader:(bookId:string,unitId:string,page?:number)=>void;reader:{bookId:string;unitId:string;page:number};setReaderPage:(n:number)=>void;select:(s:Selection|null)=>void;notify:(s:string)=>void;mutate:(action:Record<string,any>,previewCorrect?:boolean)=>Promise<{ok:boolean;result?:any}>;reload:()=>Promise<void>;openSubscription:()=>void;startLearning:(view:'games'|'flashcards',bookId:string,unitIds:string[],filter?:Scope['filter'])=>void};
export const AppContext=createContext<AppContextValue|null>(null);
export const useApp=()=>{const x=useContext(AppContext);if(!x)throw new Error('Missing app context');return x;};
