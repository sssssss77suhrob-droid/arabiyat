"""Build API-free, source-pinned word timings from local original-audio alignment.
Usage: python scripts/prepare-a0-timings.py <audio-work-directory>
Model artifacts/audio stay outside Git. Intervals are measured, never uniformly divided.
"""
import csv,json,pathlib,re,sys,unicodedata,difflib
root=pathlib.Path(__file__).resolve().parents[1];work=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else root/'scripts/a0-timing-inputs';pages={p['page']:p for p in json.load(open(root/'lib/a0/worksheets.json'))};book=json.load(open(root/'lib/a0/book.json'));assets={a['key']:a for a in json.load(open(root/'lib/a0/assets.json'))}
manual={p['page']:p['words'] for p in json.load(open(work/'manual-words-extra.json'))}
if (work/'manual-vowel-words.json').exists():
 for p in json.load(open(work/'manual-vowel-words.json')):manual.setdefault(p['page'],[]).extend(p['words'])
if (work/'manual-owner-words.json').exists():
 for p in json.load(open(work/'manual-owner-words.json')):manual.setdefault(p['page'],[]).extend(p['words'])
def norm(t):return ''.join(c for c in unicodedata.normalize('NFD',t.replace('ى','ي').replace('ـ','')) if '\u0621'<=c<='\u064a' and not unicodedata.combining(c))
ocr_path=root/'scripts/a0-timing-inputs/ocr-words.json'
ocr_candidates=json.load(open(ocr_path)) if ocr_path.exists() else {}
def candidates(page):
 result=[]
 for i,w in enumerate(manual.get(page,[])+pages[page]['words']):
  if norm(w['ar']):result.append(dict(w,id=w.get('id',f'audio-p{page}-{i}')))
 tsv=work.parent/'tmp/ocr'/f'{page:03}.tsv'
 if tsv.exists():
  rows=list(csv.DictReader(open(tsv),delimiter='\t'));
  if not rows:return sorted(result,key=lambda w:(round(w['rect']['y']/.025),-w['rect']['x']))
  width=int(rows[0]['width']);height=int(rows[0]['height'])
  for i,row in enumerate(rows):
   t=row['text'].strip();key=norm(t)
   if len(key)<2 or len(key)>30 or float(row['conf'])<15:continue
   rect={k:round(int(row[v])/den,6) for k,v,den in [('x','left',width),('y','top',height),('w','width',width),('h','height',height)]}
   if any(norm(w['ar'])==key and abs(w['rect']['x']-rect['x'])<.035 and abs(w['rect']['y']-rect['y'])<.03 for w in result):continue
   result.append({'id':f'audio-ocr-{page}-{i}','ar':t,'rect':rect})
 if not tsv.exists():result.extend(ocr_candidates.get(str(page),[]))
 return sorted(result,key=lambda w:(round(w['rect']['y']/.025),-w['rect']['x']))
def choose(key,items,last):
 exact=[(i,w) for i,w in enumerate(items) if key in [norm(w['ar']),*[norm(a) for a in w.get('aliases',[])]]]
 if not exact and key.endswith('ن'):
  exact=[(i,w) for i,w in enumerate(items) if any(h in w['ar'] for h in 'ًٌٍ') and norm(w['ar'])==key[:-1]]
 if not exact:return None
 if last<0:return exact[0]
 # Prefer the next occurrence for dialogue turns; allow a recorded repetition.
 following=[c for c in exact if c[0]>last]
 if following and following[0][0]-last<12:return following[0]
 current=[c for c in exact if c[0]==last]
 if current:return current[0]
 return min(exact,key=lambda c:abs(c[0]-last))
source_transcripts=json.load(open(root/'scripts/a0-timing-inputs/transcripts.json'));tracks={};report=[]
for unit in book['units']:
 for page in unit['pages']:
  number=page['number'];items=candidates(number)
  for q in page.get('qrAudio',[]):
   if not q.get('key'):continue
   file=work/'transcripts'/f'{q["id"]}.json'
   if not file.exists() and q['id'] not in source_transcripts:report.append({'id':q['id'],'missing':True});continue
   data=json.load(open(file)) if file.exists() else source_transcripts[q['id']];words=[];last=-1
   # Two separate dialogues on one page stay in their own printed region.
   if len([x for x in page.get('qrAudio',[]) if x.get('key')])==2 and number!=12:
    index=page['qrAudio'].index(q);split=page['qrAudio'][1]['rect']['y']-.02;itemsq=[w for w in items if (w['rect']['y']<split if index==0 else w['rect']['y']>=split)]
   else:itemsq=items
   flat=[w for s in data['segments'] for w in s['words'] if w['end']>w['start']]
   pos=0
   while pos<len(flat):
    w=flat[pos];key=norm(w['word']);found=None;take=1
    for n in [3,2,1]:
     group=flat[pos:pos+n]
     if len(group)!=n or group[-1]['end']-group[0]['start']>5:continue
     k=''.join(norm(t['word']) for t in group)
     f=choose(k,itemsq,last)
     if f:found=f;take=n;break
    token={'word':w['word'],'start':round(w['start'],3),'end':round(flat[pos+take-1]['end'],3)}
    if found:
     last,c=found;token.update(word=c['ar'],wordId=c['id'],rect=c['rect'])
    words.append(token);pos+=take
   tracks[q['id']]={'key':q['key'],'page':number,'duration':round(data['duration'],3),'sha256':assets[q['key']]['sha256'],'words':words}
   report.append({'id':q['id'],'page':number,'words':len(words),'matched':sum('rect' in w for w in words),'duration':round(data['duration'],1),'unmatched':[w['word'] for w in words if 'rect' not in w]})
override=work/'phonetic-overrides.json'
if override.exists():
 for id,record in json.load(open(override)).items():
  if id in tracks and record.get('verified'):tracks[id]['words']=record['words'];tracks[id]['method']='measured-speech-intervals'
output={'version':1,'method':'local-original-audio-alignment','notes':'Prepared offline, no API at playback. Only mapped printed words receive underline. OCR/automatic alignment may require editorial correction.','tracks':tracks}
(root/'lib/a0/audio-timings.json').write_text(json.dumps(output,ensure_ascii=False,separators=(',',':'))+'\n')
(work/'alignment-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('tracks',len(tracks),'mapped',sum('rect' in w for t in tracks.values() for w in t['words']),'events',sum(len(t['words']) for t in tracks.values()))
