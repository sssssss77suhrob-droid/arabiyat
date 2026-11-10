"""Add OCR click targets and draggable sources from the original page scans.
Run after prepare-a0.py: python scripts/augment-a0.py <directory-of-TSV-files>.
Unknown OCR text is read from the actual image at tap time; it is never a reviewed translation.
"""
import sys,pathlib,json,re,hashlib
from PIL import Image
root=pathlib.Path(__file__).resolve().parents[1];directory=pathlib.Path(sys.argv[1]);target=root/'lib/a0/worksheets.json';pages=json.loads(target.read_text())
def norm(x):return re.sub(r'[\u064b-\u065f\u0670ـ\s\u200e\u200f.,؛،:!?؟]','',x)
lex={}
for l in (root/'scripts/a0-lexicon.tsv').read_text().splitlines():
 ar,uz=l.split('\t');lex[norm(ar)]={'ar':ar,'uz':uz}
for l in (root/'scripts/a0-verbs.tsv').read_text().splitlines():
 a=l.split('\t');forms=dict(zip(['past','present','command','masdar'],a[:4]))
 for ar,uz in zip(a[:4],a[4:]):lex[norm(ar)]={'ar':ar,'uz':uz,'forms':forms}
def intersects(a,b):return max(a['x'],b['x'])<min(a['x']+a['w'],b['x']+b['w']) and max(a['y'],b['y'])<min(a['y']+a['h'],b['y']+b['h'])
def rect(x,y,w,h):return {'x':x,'y':y,'w':w,'h':h}
for p in pages:
 f=directory/f"{p['page']:03}.tsv"
 if f.exists():
  iw,ih=Image.open(root/f"public/books/a0/page-{p['page']:03}.webp").size
  for l in f.read_text().splitlines()[1:]:
   a=l.split('\t',11)
   if len(a)!=12 or a[0]!='5':continue
   x,y,w,h=map(int,a[6:10]);t=a[11];k=norm(t);known=lex.get(k);conf=float(a[10])
   if not known and (conf<72 or len(k)<3 or not re.fullmatch('[\u0621-\u064a]+',k)):continue
   if known and conf<30:continue
   r=rect(round(x/iw,5),round(max(0,y/ih-.003),5),round(w/iw,5),round(min(.065,h/ih+.006),5))
   if r['w']>.45 or r['y']>.96 or r['x']+r['w']>1 or r['y']+r['h']>1:continue
   if any(intersects(r,v['rect']) for v in p['words']):continue
   v={**(known or {'ar':t,'uz':''}),'rect':r,'context':t}
   v['id']='ocrw-'+hashlib.sha256((str(p['page'])+':'+t+':'+str(r)).encode()).hexdigest()[:20];p['words'].append(v)
 for e in p['exercises']:
  for item in e['items']:
   if item.get('crop'):item['source']=item['crop'];continue
   candidates=[w for w in p['words'] if norm(w['ar'])==norm(item.get('ar',''))]
   if candidates:item['source']=min(candidates,key=lambda w:abs(w['rect']['y']-e['region']['y']))['rect']
 # Verified printed source positions. A letter group is taken from the book itself.
 if p['page']==20:
  e=p['exercises'][0]
  for i,item in enumerate(e['items']):item['source']=rect([.64,.33,.07][i%3],[.134,.335,.539,.748][i//3],.23,.035)
 if p['page']==28:
  for i,item in enumerate(p['exercises'][0]['items']):item['source']=rect(.4,[.156,.215,.274,.333,.389,.447,.505,.564][i],.11,.035)
 if p['page']==33:
  for i,item in enumerate(p['exercises'][0]['items']):item['source']=rect(.405,[.477,.535,.593,.65,.707,.764,.821,.879][i],.21,.041)
 if p['page']==96:
  positions=[(.805,.505),(.41,.505),(.274,.505),(.14,.505),(.542,.56),(.41,.56),(.14,.56),(.61,.615),(.675,.505),(.542,.505),(.805,.56),(.675,.56),(.274,.56),(.74,.615),(.475,.615),(.34,.615),(.205,.615)]
  for item,(x,y) in zip(p['exercises'][0]['items'],positions):item['source']=rect(x,y,.12,.041)
target.write_text(json.dumps(pages,ensure_ascii=False,separators=(',',':')))
print(json.dumps({'targets':sum(len(p['words']) for p in pages),'translatedTargets':sum(bool(w['uz']) for p in pages for w in p['words']),'inlineSources':sum(bool(i.get('source')) for p in pages for e in p['exercises'] for i in e['items'])}))
