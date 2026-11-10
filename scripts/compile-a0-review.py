"""Compile inspected word occurrences and faithful exercises; no online inference.
Run after editing scripts/a0-review page assets. --partial is for work checkpoints only.
"""
import pathlib,json,unicodedata,re,sys,math,copy
from PIL import Image
root=pathlib.Path(__file__).resolve().parents[1];folder=root/'scripts/a0-review'
def norm(s):return ''.join(c for c in unicodedata.normalize('NFD',s).replace('ـ','') if '\u0621'<=c<='\u064a' and not unicodedata.combining(c))
def formkey(s):return ''.join(c for c in unicodedata.normalize('NFC',s) if '\u0621'<=c<='\u065f' and c!='ـ')
base={p['page']:p for p in json.load(open(folder/'baseline.json'))};review={}
for f in sorted(folder.glob('pages-*.json')):
 for p in json.load(open(f)):
  if p['page'] in review:raise ValueError('Duplicate reviewed page '+str(p['page']))
  review[p['page']]=p
missing=sorted(set(range(1,113))-review.keys())
if missing and '--partial' not in sys.argv:raise ValueError('Unreviewed pages remain: '+str(missing))
extra=[]
for f in folder.glob('exercise-*.json'):
 extra.extend(json.load(open(f)))
for p in review.values():
 if p['page']!=3 and not p['words']:raise ValueError('Empty reviewed text page '+str(p['page']))
for p in extra:
 if p['page'] in review:review[p['page']]['exerciseAudit'].extend(p['exerciseAudit'])
letters=dict(zip('ابتثجحخدذرزسشصضطظعغفقكلمنهوي',['alif','bo','to','so','jim','ho','xo','dol','zol','ro','zo','sin','shin','sod','zod','to','zo','ayn','g‘ayn','fo','qof','kof','lom','mim','nun','ho','vov','yo']))
fix={'محطة':'bekat; stansiya','المطعم':'restoranda; ovqatlanish joyida','الظرف':'o‘rin-payt ravishini','المناسب':'mos; munosib'}
def meaning(w):
 uz=w['uz'];ar=w['ar'];key=norm(ar)
 if 'TEKSHIRISH KERAK' not in uz:return uz
 if key in fix:return fix[key]
 digits=''.join(c for c in ar if c.isdecimal())
 if digits:return str(int(digits))+' soni'
 if key and key[0] in letters and len(key)<=2:
  if len(key)==2 and key[1] in 'اوي':return letters[key[0]]+' harfi; cho‘ziq '+{'ا':'a','و':'u','ي':'i'}[key[1]]+' tovushi'
  if len(key)==1:return letters[key]+' harfi'+(' (so‘z o‘rtasidagi shakl)' if ar.startswith('ـ') and ar.endswith('ـ') else ' (so‘z oxiridagi shakl)' if ar.startswith('ـ') else ' (so‘z boshidagi shakl)' if ar.endswith('ـ') else '')
 raise ValueError('Unresolved translation '+ar)
def cleanrect(r):
 r={k:round(float(r[k]),6) for k in ['x','y','w','h']}
 if r['x']<0 or r['y']<0 or r['w']<=0 or r['h']<=0 or r['x']+r['w']>1.002 or r['y']+r['h']>1.002:raise ValueError('Bad rectangle '+str(r))
 r['w']=min(r['w'],1-r['x']);r['h']=min(r['h'],1-r['y']);return r
# Retain precise geometry for text; do not infer glyph edges from solid banner backgrounds.
def tighten(image,r):
 W,H=image.size;x,y,w,h=[r[k] for k in ['x','y','w','h']];box=(max(0,int(x*W)),max(0,int(y*H)),min(W,math.ceil((x+w)*W)),min(H,math.ceil((y+h)*H)));crop=image.crop(box);pixels=crop.load();pts=[]
 for yy in range(crop.height):
  for xx in range(crop.width):
   red,green,blue=pixels[xx,yy]
   if min(red,green,blue)<130 and max(red,green,blue)-min(red,green,blue)<180:pts.append((xx,yy))
 if len(pts)<5 or len(pts)>crop.width*crop.height*.55:return r
 l=max(0,min(a for a,b in pts)-2);rr=min(crop.width,max(a for a,b in pts)+3);t=max(0,min(b for a,b in pts)-2);bb=min(crop.height,max(b for a,b in pts)+3)
 if rr-l<crop.width*.35:return r
 return cleanrect({'x':(box[0]+l)/W,'y':(box[1]+t)/H,'w':(rr-l)/W,'h':(bb-t)/H})
forms={formkey(w['ar']):w.get('forms') for p in review.values() for w in p['words'] if w.get('forms')}
for p in base.values():
 for w in p['words']:
  if w.get('forms'):forms.setdefault(formkey(w['ar']),w['forms'])
supplements={formkey(k):v for k,v in json.load(open(folder/'verb-form-supplements.json')).items()}
report=[];output=[]
for n in range(1,113):
 p=copy.deepcopy(base[n]);r=review.get(n)
 if r:
  old=p['words'];words=[];used=set();image=Image.open(root/f'public/books/a0/page-{n:03}.webp').convert('RGB')
  for i,w in enumerate(r['words']):
   rect=cleanrect(w['rect']);key=norm(w['ar']);similar=[t for t in old if t.get('id') not in used and norm(t['ar'])==key and abs(t['rect']['x']+t['rect']['w']/2-rect['x']-rect['w']/2)<.04 and abs(t['rect']['y']+t['rect']['h']/2-rect['y']-rect['h']/2)<.035]
   id=(min(similar,key=lambda t:abs(t['rect']['x']-rect['x'])+abs(t['rect']['y']-rect['y']))['id'] if similar else w.get('id',f'a0-p{n:03}-r{i+1:04}'))
   if id in used:id=f'a0-p{n:03}-r{i+1:04}-new'
   used.add(id);record={'id':id,'ar':w['ar'],'uz':meaning(w),'rect':tighten(image,rect),'hasSentence':False,'contextVerified':True}
   supplement=supplements.get(formkey(w['ar']))
   f=({k:supplement[k] for k in ['past','present','command','masdar']} if supplement else w.get('forms') or forms.get(formkey(w['ar'])))
   if supplement and supplement.get('formsNote'):record['formsNote']=supplement['formsNote']
   if not f and key in ['اكتبها','واكتبها']:f=forms.get(formkey('اُكْتُبْ'))
   if key=='ظل' and 'ٌ' in w['ar']:record['uz']='soya';f=None
   if f:record['forms']=f
   words.append(record)
  p['words']=words
  exercises={e['id']:e for e in p['exercises']}
  for a in r['exerciseAudit']:
   id=a.get('id')
   if a['action']=='remove':
    if id:exercises.pop(id,None)
    else:exercises={}
   elif a['action']=='correct':
    if not id:id=f'a0-p{n:03}-e{len(exercises)+1}'
    e=exercises.get(id,{'id':id,'kind':'write','title':'Kitob mashqi','instruction':'','region':{'x':.04,'y':.1,'w':.88,'h':.8},'items':[],'slots':[]})
    e.update({k:v for k,v in a.items() if k not in ['action','reason']});e['id']=id
    if e['kind']=='speak':e['items']=[];e['slots']=[]
    e['title']={'connect':'Mosini ulash','write':'Javobni yozish','place':'Bo‘sh joyni to‘ldirish','choice':'Eshitib tanlash','trace':'Yozuv mashqi','speak':'Suhbat va talaffuz'}.get(e['kind'],e['title'])
    exercises[id]=e
  p['exercises']=list(exercises.values())
 if n<=7:p['exercises']=[]
 for e in p['exercises']:
  if e['kind']=='choice' and not e.get('choiceGroups'):
   rows=[]
   for s in sorted(e['slots'],key=lambda s:s['rect']['y']):
    row=next((r for r in rows if abs(r[0]['rect']['y']-s['rect']['y'])<.018),None)
    if row is None:rows.append([s])
    else:row.append(s)
   e['choiceGroups']=[{'id':f'g{i}','slotIds':[s['id'] for s in row]} for i,row in enumerate(rows)]
  for slot in e['slots']:slot['rect']=cleanrect(slot['rect'])
  for item in e['items']:
   for k in ['source','crop']:
    if item.get(k):item[k]=cleanrect(item[k])
  if e['kind']=='connect' and (not e['items'] or not e['slots']):raise ValueError('Empty connection exercise '+e['id'])
 report.append({'page':n,'reviewed':bool(r),'words':len(p['words']),'exercises':len(p['exercises']),'notes':r.get('notes',[]) if r else ['Review pending']});output.append(p)
(root/'lib/a0/worksheets.json').write_text(json.dumps(output,ensure_ascii=False,separators=(',',':'))+'\n')
b=json.load(open(root/'lib/a0/book.json'));b['analysisMode']='none'
for u in b['units']:
 for p in u['pages']:p['exerciseCount']=len(output[p['number']-1]['exercises'])
(root/'lib/a0/book.json').write_text(json.dumps(b,ensure_ascii=False,separators=(',',':'))+'\n')
(root/'lib/a0/review-report.json').write_text(json.dumps({'pages':report,'unreviewed':missing,'totalWords':sum(len(p['words']) for p in output),'totalExercises':sum(len(p['exercises']) for p in output)},ensure_ascii=False,indent=2)+'\n')
print('pages reviewed',112-len(missing),'words',sum(len(p['words']) for p in output),'exercises',sum(len(p['exercises']) for p in output))
