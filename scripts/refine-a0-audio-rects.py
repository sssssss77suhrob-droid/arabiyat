"""Keep measured intervals; attach reviewed printed word boxes for exact-width underlines.
Run after compile-a0-review.py. No audio generation, speech API or network.
"""
import json,pathlib,unicodedata,math,collections
root=pathlib.Path(__file__).resolve().parents[1]
original=root/'scripts/a0-timing-inputs/timing-intervals.json'
if not original.exists():original.write_bytes((root/'lib/a0/audio-timings.json').read_bytes())
data=json.load(open(original));pages={p['page']:p for p in json.load(open(root/'lib/a0/worksheets.json'))}
def norm(s):return ''.join(c for c in unicodedata.normalize('NFD',s.replace('ـ','').replace('ى','ي')) if '\u0621'<=c<='\u064a' and not unicodedata.combining(c))
def vocal(s):return ''.join(c for c in s if '\u0621'<=c<='\u065f' and c!='ـ')
def distance(a,b):return math.hypot(a['x']+a['w']/2-b['x']-b['w']/2,(a['y']+a['h']/2-b['y']-b['h']/2)*1.334)
changed=added=0;unresolved=[]
for id,t in data['tracks'].items():
 targets=pages[t['page']]['words']
 for index,event in enumerate(t['words']):
  key=norm(event['word']);matches=[w for w in targets if key and norm(w['ar'])==key]
  # Phonetic rows require the printed vowel too, not just the consonant.
  if len(key)==1:
   exact=[w for w in matches if vocal(w['ar'])==vocal(event['word'])]
   if exact:matches=exact
  previous=event.get('rect');chosen=None
  if previous and matches:
   chosen=min(matches,key=lambda w:distance(w['rect'],previous))
   if distance(chosen['rect'],previous)>.15:chosen=None
  elif not previous and len(matches)==1 and len(key)>=2:chosen=matches[0]
  if chosen:
   event.update(wordId=chosen['id'],rect=chosen['rect']);changed+=bool(previous);added+=not bool(previous)
  elif previous:unresolved.append({'track':id,'index':index,'word':event['word']})
overrides=json.load(open(root/'scripts/a0-review/audio-rect-overrides.json'))
bytrack=collections.defaultdict(list)
for patch in overrides:bytrack[patch['track']].append(patch)
for id,patches in bytrack.items():
 t=data['tracks'][id]
 # Apply from the end so original event indexes stay valid after splits.
 for patch in sorted(patches,key=lambda p:p['index'],reverse=True):
  old=t['words'][patch['index']]
  if patch.get('unresolved'):
   old.pop('rect',None);old.pop('wordId',None);continue
  replacement=patch.get('split') or [{**old,**{k:v for k,v in patch.items() if k in ['word','rect']}}]
  if patch.get('split'):
   assert abs(replacement[0]['start']-old['start'])<.001 and abs(replacement[-1]['end']-old['end'])<.001,'Split envelope changed'
  for event in replacement:
   candidates=[w for w in pages[t['page']]['words'] if norm(w['ar'])==norm(event['word'])]
   if candidates:
    chosen=min(candidates,key=lambda w:distance(w['rect'],event['rect']))
    if distance(chosen['rect'],event['rect'])<.035:event['wordId']=chosen['id']
    else:event.pop('wordId',None)
   else:event.pop('wordId',None)
  t['words'][patch['index']:patch['index']+1]=replacement
handled={(p['track'],p['index']) for p in overrides}
unresolved=[v for v in unresolved if (v['track'],v['index']) not in handled]
data['version']=2;data['notes']='Prepared offline. Original timestamps retained; reviewed per-word rectangles draw right-to-left. Unprinted narration has no marker; automatic audio alignment still requires listening review.'
(root/'lib/a0/audio-timings.json').write_text(json.dumps(data,ensure_ascii=False,separators=(',',':'))+'\n')
(root/'lib/a0/audio-review-report.json').write_text(json.dumps({'tracks':len(data['tracks']),'refined':changed,'newlyMapped':added,'preservedLegacyRectangles':unresolved,'mapped':sum('rect' in w for t in data['tracks'].values() for w in t['words']),'directEditorialRectangles':sum('rect' in p for p in overrides),'splitEvents':sum('split' in p for p in overrides),'unresolvedSpeech':[p for p in overrides if p.get('unresolved')],'humanListeningComplete':False},ensure_ascii=False,indent=2)+'\n')
print('audio tracks',len(data['tracks']),'refined boxes',changed,'new matches',added,'legacy preserved',len(unresolved))
