import {readFile} from 'node:fs/promises';import ts from 'typescript';import assert from 'node:assert/strict';
const source=await readFile('lib/erase-ink.ts','utf8');const {eraseInk}=await import('data:text/javascript;base64,'+Buffer.from(ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.ESNext}}).outputText).toString('base64'));
let n=0;const id=()=>`piece-${++n}`,line={id:'original',tool:'pen',color:'#123456',width:2,points:[{x:.1,y:.5},{x:.9,y:.5}]};
const original=JSON.stringify(line),cut=eraseInk([line],{x:.5,y:.5},20,1000,id);assert.equal(cut.length,2);assert(cut[0].points.at(-1).x<.48);assert(cut[1].points[0].x>.52);assert.equal(cut[0].color,line.color);assert.equal(JSON.stringify(line),original);
assert.equal(eraseInk([line],{x:.5,y:.8},20,1000,id)[0],line);
assert.deepEqual(eraseInk([{...line,points:[{x:.5,y:.5}]}],{x:.5,y:.5},20,1000,id),[]);
const marker={...line,tool:'highlighter',width:18};assert.equal(eraseInk([marker],{x:.5,y:.5},20,1500,id).length,2);
const end=eraseInk([line],{x:.1,y:.5},20,1000,id);assert.equal(end.length,1);assert(end[0].points[0].x>.12);
console.log('PASS eraser: partial cut across sparse segments, preserved style, immutable undo source, missed stroke, dots, marker and endpoint.');
