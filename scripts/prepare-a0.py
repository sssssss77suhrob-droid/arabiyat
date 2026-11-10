"""Rebuild reviewed A0 page metadata from the supplied scan; original PDF stays unchanged.
Usage: PYTHONPATH=<opencv-dir> python scripts/prepare-a0.py <source-assets-dir>
"""
import sys,json,hashlib,uuid,re,pathlib,unicodedata,collections
import fitz,cv2,numpy as np
from PIL import Image
root=pathlib.Path(__file__).resolve().parents[1]
work=pathlib.Path(sys.argv[1]);pdf=work.parent.parent/'upload'/'المنهج العالمي المستوي التمهيدي.pdf'
# The argument normally points to tmp/a0; resolve the attached original explicitly.
if not pdf.exists():pdf=pathlib.Path('/workspace/scratch/33c7dd527a7a/upload/المنهج العالمي المستوي التمهيدي.pdf')
doc=fitz.open(pdf)
def norm(s):return re.sub(r'[\u064b-\u065f\u0670ـ\s\u200e\u200f.,؛،:!?؟]','',s)
lex={}
for line in (root/'scripts/a0-lexicon.tsv').read_text().splitlines():
 ar,uz=line.split('\t');lex[norm(ar)]={'ar':ar,'uz':uz}
for line in (root/'scripts/a0-verbs.tsv').read_text().splitlines():
 a=line.split('\t');forms=dict(zip(['past','present','command','masdar'],a[:4]))
 for ar,uz in zip(a[:4],a[4:]):lex[norm(ar)]={'ar':ar,'uz':uz,'forms':forms}
# Definite forms keep their own meaning; grammatical inflection is supplied separately.
for k,v in list(lex.items()):
 if len(k)>2 and not k.startswith('ال') and 'forms' not in v:lex.setdefault('ال'+k,{**v,'ar':'الْ'+v['ar'].replace('ٌ','ُ')})
# OCR is used only to locate known, reviewed words, never to invent their translations.
aliases={}
for k,v in lex.items():
 a=k.translate(str.maketrans('أإآ','ااا'))
 if a not in aliases:aliases[a]=v
 elif aliases[a]['uz']!=v['uz']:aliases[a]=None

def R(x,y,w,h):return {'x':round(x,5),'y':round(y,5),'w':round(w,5),'h':round(h,5)}
def item(ar,i):
 v=lex.get(norm(ar),{});return {'id':f'i{i}','ar':ar,'uz':v.get('uz','')}
def slot(i,rect,accepted=None,items=None,label=None):
 s={'id':f's{i}','rect':rect,'label':label or f'{i+1}-javob'}
 if accepted:s['accepted']=accepted
 if items:s['acceptItems']=items
 return s

def lines_on(page):
 im=cv2.imread(str(work/'ocr'/f'{page:03}.png'));h,w=im.shape[:2];gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
 ink=(gray<210).astype('uint8')*255
 closed=cv2.morphologyEx(ink,cv2.MORPH_CLOSE,np.ones((1,4),np.uint8))
 lines=cv2.morphologyEx(closed,cv2.MORPH_OPEN,np.ones((1,int(w*.04)),np.uint8))
 contours,_=cv2.findContours(lines,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
 rects=[]
 for c in contours:
  x,y,b,a=cv2.boundingRect(c)
  if not(.15<y/h<.97 and .05<b/w<.34 and a/h<.005):continue
  row=gray[y:y+max(a,1),x:x+b];density=(row<180).mean();saturation=cv2.cvtColor(im[y:y+max(a,1),x:x+b],cv2.COLOR_BGR2HSV)[:,:,1].mean()
  if density>.88 or saturation>28:continue
  above=gray[max(0,y-15):max(0,y-3),x:x+b];below=gray[y+a+3:y+a+15,x:x+b]
  if above.size and below.size and (above<150).mean()<.08 and (below<150).mean()<.08:
   r=R(max(.015,(x-3)/w),max(.03,y/h-.026),min(.35,(b+6)/w),.029)
   if all(abs(q['y']-r['y'])>.008 or abs(q['x']-r['x'])>.03 for q in rects):rects.append(r)
 return sorted(rects,key=lambda r:(round(r['y']/.035),-r['x']))

def geometry(n):
 im=cv2.imread(str(work/'ocr'/f'{n:03}.png'));h,w=im.shape[:2];hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV);mask=cv2.inRange(hsv,(0,40,65),(180,255,255));mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,np.ones((3,3),np.uint8));cs,_=cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE);photos=[];cards=[]
 for c in cs:
  x,y,b,a=cv2.boundingRect(c);X,Y,B,A=x/w,y/h,b/w,a/h
  if .05<Y<.95 and .075<B<.4:
   if .06<A<.17 and .12<B<.23:photos.append(R(X,Y,B,A))
   elif .018<A<.065 and B/A>1.8:cards.append(R(X,Y,B,A))
 def dedupe(rs):
  out=[]
  for r in sorted(rs,key=lambda r:r['w']*r['h'],reverse=True):
   if any(r['x']>=q['x']-.005 and r['y']>=q['y']-.005 and r['x']+r['w']<=q['x']+q['w']+.005 and r['y']+r['h']<=q['y']+q['h']+.005 for q in out):continue
   out.append(r)
  return sorted(out,key=lambda r:(round(r['y']/.025),-r['x']))
 return dedupe(photos),dedupe(cards)

letter_pages={16:'أ',17:'ب',18:'ت',19:'ث',25:'ج',26:'ح',27:'خ',34:'د',35:'ذ',42:'ر',43:'ز',50:'س',51:'ش',57:'ص',58:'ض',65:'ط',66:'ظ',74:'ع',75:'غ',81:'ف',82:'ق',83:'ك',90:'ل',91:'م',97:'ن',98:'ه',104:'و',105:'ي'}
conversation=[8,22,30,39,47,54,62,69,78,88,94,101,110]
contrast=[23,31,40,48,55,63,71,89,95]
listening=[21,29,37,45,53,60,68,77,85,93,100,107]
match_pages=[33,49,64,72,80,92,106]
qrs=json.loads((work/'qr-codes.json').read_text());audio=json.loads((work/'audio-metadata.json').read_text())
by_audio={x['id']:x for x in audio};assets=[];uploads=[]
def add_asset(path,id,name,mime):
 raw=path.read_bytes();key='content/'+str(uuid.uuid5(uuid.NAMESPACE_URL,'arabiyat/a0/'+id));a={'id':key.split('/')[1],'key':key,'name':name,'size':len(raw),'mime':mime,'sha256':hashlib.sha256(raw).hexdigest()}
 assets.append(a);uploads.append({**a,'path':str(path)});return key
pdf_key=add_asset(pdf,'original-pdf-v1',pdf.name,'application/pdf')
for a in audio:a['key']=add_asset(work/'audio'/(a['id']+'.mp3'),a['id'],a['name'],a['mime'])

page_data=[];counts=collections.Counter()
for n in range(1,113):
 words=[];seen=[];p=doc[n-1];iw=round(p.rect.width*2.5);ih=round(p.rect.height*2.5)
 tsv=work/'ocr'/f'{n:03}.tsv'
 if tsv.exists():
  for line in tsv.read_text().splitlines()[1:]:
   x=line.split('\t',11)
   if len(x)<12 or x[0]!='5':continue
   _,_,_,_,_,_,left,top,w,h,conf,t=x
   if float(conf)<20 or len(t)>30:continue
   k=norm(t);v=lex.get(k) or aliases.get(k.translate(str.maketrans('أإآ','ااا')))
   if not v:continue
   r=R(int(left)/iw,int(top)/ih,int(w)/iw,int(h)/ih)
   if r['w']>.4 or r['h']>.07 or r['y']>.96:continue
   words.append({**v,'rect':r})
   if v['ar'] not in seen:seen.append(v['ar'])
 exercises=[]
 def ex(kind,title,instruction,region,items=None,slots=None,repeat=False):
  e={'id':f'a0-p{n:03}-e{len(exercises)+1}','kind':kind,'title':title,'instruction':instruction,'region':region,'items':items or [],'slots':slots or []}
  if repeat:e['repeat']=True
  exercises.append(e);return e
 rects=lines_on(n) if n>=8 else []
 if n in letter_pages:
  # Original bottom writing tasks remain on the scan, with actual answer fields above their underlines.
  write=[R(x,.67,.14,.027) for x in [.695,.48,.265,.05]]
  if not write:write=[R(x,.675,.14,.025) for x in [.695,.48,.265,.05]]
  ex('write','Tinglang, o‘qing va yozing','QR audiosini tinglang. Rasmlar ostidagi so‘zlarni javob joylariga yozing.',R(.04,.49,.87,.22),[item(a,i) for i,a in enumerate(seen) if 'forms' not in lex.get(norm(a),{})], [slot(i,r) for i,r in enumerate(write)])
  bottom=[R(.76,y,.08,.028) for y in [.753,.803,.853,.903]]
  if not bottom:bottom=[R(.76,y,.08,.028) for y in [.753,.803,.853,.903]]
  ex('place','Harf va so‘zni to‘ldiring','Kitobdagi bo‘laklarni moslang. So‘zni yoki harfni tanlang, so‘ng javob joyini bosing; sudrab qo‘yish ham mumkin.',R(.04,.71,.87,.23),[item(a,i) for i,a in enumerate(seen)][:18]+[item(letter_pages[n],len(seen))], [slot(i,r) for i,r in enumerate(bottom)],True)
 elif n in conversation:
  ex('speak','Suhbatni mashq qiling','QR audiosini tinglang. Rollarni navbat bilan o‘qib, so‘ng suhbatni kitobga qaramasdan ayting.',R(.12,.11,.77,.47))
  if n!=8:
   fields=[r for r in rects if r['y']>.57][:12]
   if not fields:fields=[R(.58,y,.22,.028) for y in [.63,.69,.75,.81]]
   ex('write','Suhbatni xotiradan to‘ldiring','Kitobdagi savollarga o‘zingiz haqingizda javob yozing. Bu erkin javoblar to‘g‘ri/noto‘g‘ri lug‘at foiziga qo‘shilmaydi.',R(.1,.55,.8,.38),[],[slot(i,r) for i,r in enumerate(fields)])
 elif n in contrast:
  ex('speak','O‘xshash tovushlarni farqlang','Ikki tovushni QR audiosida tinglang va juft so‘zlarni navbat bilan takrorlang.',R(.12,.12,.76,.54))
  slots=[slot(i,R(x,y,.13,.035),label=f'{i//2+1}-juft: {i%2+1}-variant') for i,(y,x) in enumerate((y,x) for y in [.72,.78,.84,.9] for x in [.65,.25])]
  ex('choice','Tinglagan variantingizni belgilang','Har qatorda tinglagan tovushingizga mos variantni bosing. Audio bilan solishtirgach, bajarilgan deb belgilang.',R(.08,.67,.82,.27),[],slots)
 elif n in listening:
  groups={21:4,29:3,37:2,45:2,53:2,60:2,68:2,77:2,85:3,93:2,100:2,107:2}[n]
  photos,_=geometry(n);top_photos=[r for r in photos if r['y']<.63 and r['x']<.72]
  sl=[]
  for r in top_photos:
   rr=R(r['x'],r['y']+r['h']+.033,r['w'],.027)
   if rr['y']<.64:sl.append(slot(len(sl),rr))
  if len(sl)<groups*2:sl=[slot(i,R(x,y,.15,.027)) for i,(y,x) in enumerate((y,x) for y in np.linspace(.18,.60,groups) for x in [.53,.34,.15])]
  ex('write','Cho‘ziq tovushlarni tinglab yozing','Asl QR audiosini tinglang va rasmlar tagidagi cho‘ziq tovushli so‘zlarni yozing.',R(.08,.08,.84,.55),[],sl)
  first=.74 if groups==4 else .77 if groups==2 else .75
  sl=[slot(i,R(x,float(y),.115,.027)) for i,(y,x) in enumerate((y,x) for y in np.linspace(first,.94,groups) for x in [.725,.54,.355,.17])]
  ex('write','Harfning shakllarini yozing','Harfning alohida, so‘z boshidagi, o‘rtasidagi va oxiridagi shakllarini katak yoki chiziqqa yozing. Qalamdan ham foydalanish mumkin.',R(.08,.64,.84,.32),[],sl)
 elif n in match_pages:
  begin={33:.46,49:.48,64:.46,72:.48,80:.48,92:.14,106:.15}[n];end=.59 if n in [92,106] else .95
  photos,cards=geometry(n);sources=[r for r in cards if .32<r['x']<.5 and .18<r['w']<.36 and begin<r['y']<end]
  targets=[r for r in photos if (r['x']<.3 or r['x']>.7) and begin<r['y']<end]
  if len(sources)<4:sources=[R(.39,y,.28,.04) for y in np.linspace(begin+.015,end-.05,8)]
  # The source has four picture rows, two sides; fill occasional border-detection gaps.
  if len(targets)<len(sources):
   left=min((r['x'] for r in targets),default=.1);right=max((r['x'] for r in targets),default=.77);ys=sorted(r['y'] for r in targets);clusters=[]
   for y in ys:
    if not clusters or abs(clusters[-1]-y)>.04:clusters.append(y)
   row_y=clusters if len(clusters)==4 else list(np.linspace(begin+.015,end-.11,4))
   targets=[R(x,float(y),.166,.095) for y in row_y for x in [right,left]]
  targets=targets[:len(sources)]
  items=[{'id':f'i{i}','crop':r} for i,r in enumerate(sources[:len(targets)])]
  ex('match','Gapni rasm bilan juftlang','Kitobning o‘rta ustunidagi gap kartochkasini tanlang va mos rasmga olib boring.',R(.05,begin,.9,end-begin),items,[slot(i,r,label=f'{i+1}-rasm') for i,r in enumerate(targets)])
 elif n in [13,14]:
  ex('trace','Harflarni yozib mashq qiling','Qalamni tanlab kitobdagi harflar ustidan yozing. Chiziqlar va yon qaydlar avtomatik saqlanadi.',R(.05,.13,.86,.77))
  if n==14:
   ex('write','Harflarni tartiblang','Kitobdagi harflarni kerakli tartibda yozing.',R(.06,.57,.85,.22),[item(a,i) for i,a in enumerate('ا ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ي'.split())],[slot(i,R(x,.7,.2,.04)) for i,x in enumerate([.64,.35,.06])])
 elif n in [9,10,11,12,86,108,111,112]:pass
 else:
  if len(rects)>18:rects=[]
  if rects:
   ex('place','Sahifadagi topshiriqni bajaring','Kitobdagi ko‘rsatmaga muvofiq yozing yoki so‘z kartochkasini javob joyiga olib boring.',R(.04,.13,.88,.8),[item(a,i) for i,a in enumerate(seen) if 'forms' not in lex.get(norm(a),{})][:24],[slot(i,r) for i,r in enumerate(rects)])
  else:
   ex('write','Kitobdagi mashq bilan ishlang','Sahifadagi vazifani javob maydonlarida bajaring. Erkin javoblarni audio yoki ustoz bilan solishtiring.',R(.05,.15,.86,.75),[item(a,i) for i,a in enumerate(seen)][:18],[slot(i,R(.56,y,.25,.034)) for i,y in enumerate([.74,.79,.84,.89])])
 page_data.append({'page':n,'words':words,'exercises':exercises})

def override(n,entries):page_data[n-1]['exercises']=entries

def activity(n,index,kind,title,instruction,region,items,slots,repeat=False):
 e={'id':f'a0-p{n:03}-e{index}','kind':kind,'title':title,'instruction':instruction,'region':region,'items':items,'slots':slots}
 if repeat:e['repeat']=True
 return e
# Reviewed answer keys. Other open/listening tasks explicitly use self/teacher review.
words20=['كِتَابٌ','مَكْتَبٌ','بَيْتٌ','تِينٌ','تِلْفَازٌ','ثَلْجٌ','ثَوْبٌ','بَقَرَةٌ','زَيْتٌ','تَمْرٌ','كَأْسٌ','أَثَاثٌ']
items20=[item(a,i) for i,a in enumerate(words20)]
slots20=[slot(i,R(x,y,.17,.037),[a]) for i,(a,x,y) in enumerate((a,x,y) for a,(y,x) in zip(words20,((y,x) for y in [.294,.495,.700,.909] for x in [.655,.365,.075])))]
override(20,[activity(20,1,'place','Rasmlarning nomini joylang','So‘zni tanlab mos rasm ostiga qo‘ying yoki klaviaturada yozing.',R(.03,.11,.87,.83),items20,slots20)])
# Page 28: eight words match the actual pictures.
a28=['جَبَلٌ','جُبْنٌ','وَجْهٌ','لَحْمٌ','مِلْحٌ','خَرُوفٌ','خِيَارٌ','مَطْبَخٌ'];it28=[item(a,i) for i,a in enumerate(a28)]
positions28=[(.72,.4),(.05,.28),(.72,.16),(.05,.16),(.72,.28),(.05,.52),(.72,.52),(.05,.4)]
slots28=[slot(i,R(x,y,.15,.095),[a]) for i,(a,(x,y)) in enumerate(zip(a28,positions28))]
override(28,[activity(28,1,'match','So‘zlarni mos rasmga qo‘ying','Har bir so‘zni o‘ng yoki chap tomondagi mos rasmga qo‘ying.',R(.03,.13,.85,.5),it28,slots28),*[{**e,'id':'a0-p028-e2'} for e in page_data[27]['exercises'][:1]]])
# Page 36: insert dal/dhal, not the whole word.
a36=['د','ذ','د','ذ','ذ','د','د','د','ذ','ذ','د','د'];slots36=[slot(i,R(x,y,.055,.03),[a]) for i,(a,(y,x)) in enumerate(zip(a36,((y,x) for y in [.246,.38,.516] for x in [.735,.515,.295,.085])))]
override(36,[activity(36,1,'place','Yetishmayotgan harfni qo‘ying','Rasm nomiga qarab dal yoki zal harfini bo‘sh joyga qo‘ying.',R(.03,.13,.86,.43),[item('د',0),item('ذ',1)],slots36,True),activity(36,2,'write','So‘zni tovush qismlariga ajrating','Kitobdagi namunaga qarab so‘zning tovush bo‘laklarini yozing.',R(.03,.56,.86,.38),[],[slot(i,R(x,y,.24,.04)) for i,(y,x) in enumerate((y,x) for y in [.645,.775,.9] for x in [.545,.055])])])
# Page 52: sin/shin and six long-vowel words.
slots52=[slot(i,R(x,y,.055,.032),[a]) for i,(a,(y,x)) in enumerate(zip(['س']*4+['ش']*4,((y,x) for y in [.14,.31] for x in [.78,.57,.36,.15])))]
long52=['سَاعَةٌ','سُورٌ','سِينٌ','شَارِعٌ','قُشُورٌ','شِينٌ']
sl52=[slot(i,R(x,y,.14,.03),[a]) for i,(a,(y,x)) in enumerate(zip(long52,((y,x) for y in [.69,.905] for x in [.54,.33,.12])))]
override(52,[activity(52,1,'place','Sin yoki shin?','Rasm nomidagi yetishmagan harfni tanlab qo‘ying.',R(.08,.13,.83,.32),[item('س',0),item('ش',1)],slots52,True),activity(52,2,'write','Cho‘ziq tovushlarni yozing','Asl audioni tinglab, rasm ostidagi so‘zni yozing.',R(.08,.5,.83,.44),[item(a,i) for i,a in enumerate(long52)],sl52)])
# Page 33: original matching sentences with their Uzbek meanings.
e33=page_data[32]['exercises'][0]
texts33=[('يَجْلِسُ عَلَى الْكُرْسِيِّ.','Stulga o‘tiradi.'),('يَخْرُجُ مِنَ الصَّفِّ.','Sinfdan chiqadi.'),('يَفْتَحُ الْكِتَابَ.','Kitobni ochadi.'),('يُعْطِي النُّقُودَ.','Pul beradi.'),('يَقِفُ بِجَانِبِ الْكُرْسِيِّ.','Stul yonida turadi.'),('يُغْلِقُ النَّافِذَةَ.','Derazani yopadi.'),('يَأْخُذُ الدَّفْتَرَ.','Daftarni oladi.'),('يَدْخُلُ الْبَيْتَ.','Uyga kiradi.')]
e33['items']=[{'id':f'i{i}','ar':ar,'uz':uz} for i,(ar,uz) in enumerate(texts33)]
for target,answer in zip(e33['slots'],[1,4,3,5,2,6,7,0]):target['acceptItems']=[f'i{answer}']
# Page 96: all 17 original word-bank items; any order inside the correct column.
moon=['الْمَنْزِلُ','الْقَلَمُ','الْكُرْسِيُّ','الْمَسْجِدُ','الْكِتَابُ','الْحَقِيبَةُ','الْقَمَرُ','الْحَاسُوبُ']
sun=['الشَّارِعُ','السَّبُّورَةُ','الصَّفُّ','الدَّفْتَرُ','الشَّمْسُ','الطَّعَامُ','السَّاعَةُ','الطَّاوِلَةُ','الْجُمُعَةُ']
its=[item(a,i) for i,a in enumerate(moon+sun)];sl=[]
for side,arr,x in [(0,moon,.205),(1,sun,.58)]:
 for j in range(len(arr)):sl.append(slot(len(sl),R(x,.698+j*.025,.285,.023),None,[f'i{i}' for i in (range(8) if side==0 else range(8,17))],('Qamariya' if side==0 else 'Shamsiya')+f' {j+1}'))
override(96,[activity(96,1,'place','So‘zlarni ikki ustunga ajrating','Kartochkalarni qamariya yoki shamsiya ustuniga joylang. Ustun ichidagi tartib erkin.',R(.14,.45,.79,.49),its,sl)])

# Render the supplied scan for fast, precise page overlays and cropped word cards.
for n,page in enumerate(doc,1):
 dest=root/'public/books/a0'/f'page-{n:03}.webp'
 if not dest.exists():
  pix=page.get_pixmap(matrix=fitz.Matrix(1600/page.rect.width,1600/page.rect.width));im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);dest.parent.mkdir(parents=True,exist_ok=True);im.save(dest,quality=87,method=4)
# Additional alphabet tasks transcribed from the actual printed prompts.
join_keys={25:['مَسْجِدٌ','ثَلْجٌ','جَمَلٌ','جُبْنٌ','رَجُلٌ'],26:['حَافِلَةٌ','حَمَّامٌ','حَقِيبَةٌ','صَحْنٌ','حِصَانٌ'],27:['أَخْضَرُ','طَبَّاخٌ','خَرُوفٌ','خِمَارٌ','خِيَارٌ'],34:['دَبُّوسٌ','دَفْتَرٌ','صُنْدُوقٌ','حَدِيقَةٌ','هُدْهُدٌ'],43:['زَبِيبٌ','زُجَاجَةٌ','زُبْدَةٌ','خُبْزٌ','زَيْتُونٌ','زَهْرَةٌ'],51:['شَجَرَةٌ','شُرْفَةٌ','شَرَابٌ','قُمَاشٌ','شَمْسٌ','مِشْمِشٌ'],57:['عَصِيرٌ','مِصْبَاحٌ','مِصْعَدٌ','صُورَةٌ','صَابُونٌ','قَمِيصٌ'],65:['مَطْبَخٌ','قِطَّةٌ','مَطْعَمٌ','طُيُورٌ','خَيَّاطٌ','طَائِرَةٌ'],91:['مِلْحٌ','طَعَامٌ','عَمِيقٌ','مُتَرْجِمٌ','مَدْرَسَةٌ','مُهَنْدِسٌ'],97:['إِنْسَانٌ','نَافِذَةٌ','أَسْنَانٌ','أَرْنَبٌ','قُنْفُذٌ','نَخْلَةٌ']}
for n,answers in join_keys.items():
 points=[(.56,y) for y in [.76,.813,.865]]+[(.08,y) for y in [.76,.813,.865]]
 if len(answers)==5:points=points[1:]
 e=activity(n,2,'place','Harflardan so‘z tuzing','Kitobdagi ajratilgan harflarni birlashtiring. So‘zni yozing yoki kartochkani mos joyga qo‘ying.',R(.04,.71,.85,.22),[item(a,i) for i,a in enumerate(answers)],[slot(i,R(x,y,.12,.029),[a]) for i,(a,(x,y)) in enumerate(zip(answers,points))])
 page_data[n-1]['exercises'][-1]=e
whole_keys={66:['وَاعِظٌ','ظَفْرٌ','يَسْتَيْقِظُ','نَظَافَةٌ'],74:['بَائِعٌ','مَلْعَقَةٌ','مَصْنَعٌ','نَعْنَاعٌ'],75:['غَزَالٌ','مَشْغُولٌ','غَسَّالَةٌ','غُرُوبٌ'],82:['قَلَمٌ','بَقَرَةٌ','فُنْدُقٌ','صُنْدُوقٌ'],83:['كُرَةٌ','كِتَابٌ','مَكْتَبٌ','سِوَاكٌ'],90:['مَشْغُولٌ','لُعْبَةٌ','لَيْمُونٌ','حَلِيبٌ'],98:['هَاتِفٌ','وُجُوهٌ','هَدِيَّةٌ','زَهْرَةٌ'],104:['وَرَقَةٌ','وَرْدَةٌ','وِسَادَةٌ','شَوْكَةٌ']}
for n,answers in whole_keys.items():
 x=.55 if n==82 else .08
 e=activity(n,2,'place','So‘zni to‘ldirib yozing','O‘ng va o‘rta ustundagi bo‘laklarni birlashtiring, hosil bo‘lgan so‘zni javob joyiga qo‘ying.',R(.04,.71,.85,.22),[item(a,i) for i,a in enumerate(answers)],[slot(i,R(x,y,.15,.029),[a]) for i,(a,y) in enumerate(zip(answers,[.755,.803,.85,.898]))])
 page_data[n-1]['exercises'][-1]=e
# Use the printed fragments as drag cards on the first four letter pages.
for n in [16,17,18,19]:
 e=page_data[n-1]['exercises'][-1];e['items']=[{'id':f'i{i}','crop':R(.445,y,.065,.03)} for i,y in enumerate([.75,.8,.85,.9])];e['kind']='match';e.pop('repeat',None);e['slots']=[slot(i,R(.76,y,.065,.03)) for i,y in enumerate([.75,.8,.85,.9])];e['instruction']='O‘rta ustundagi bo‘lakni tanlab o‘ngdagi so‘zning bo‘sh qismiga qo‘ying. So‘ng hosil bo‘lgan so‘zni chapdagi rasm bilan solishtiring.'
# Four phonetic tables remain open-ended: show one answer cell per printed word.
for n in [42,50,58,81]:
 e=page_data[n-1]['exercises'][-1];e['kind']='write';e['items']=[];e['title']='So‘zlarni tovush bo‘laklariga ajrating';e['instruction']='Har bir so‘zning tovush bo‘laklarini kitobdagi kataklarga yozing. Namunaga qarab yoki ustoz bilan tekshiring.';e['slots']=[slot(i,R(x,y,.24,.04)) for i,(y,x) in enumerate((y,x) for y in [.795,.885] for x in [.55,.1])]
# Page 105: the six blanks all ask for ya.
n=105;e=activity(n,2,'place','Yo harfini qo‘ying','Yetishmagan yo harfini oltita so‘zning bo‘sh joyiga qo‘ying.',R(.04,.71,.86,.23),[item('ي',0)],[slot(i,R(x,y,.055,.028),['ي']) for i,(y,x) in enumerate((y,x) for y in [.765,.82,.875] for x in [.755,.29])],True);page_data[104]['exercises'][-1]=e
# Page 28 second task only covers the six printed lower answer lines.
e=page_data[27]['exercises'][1];e['region']=R(.04,.67,.84,.26);e['slots']=[slot(i,R(x,.736,.085,.03)) for i,x in enumerate([.762,.622,.482,.342,.202,.062])];e['title']='Harflardan so‘z tuzing va rasmga moslang'
# Audio QR positions are taken from the actual scan; old clock link uses the same book's published audio folder.
for p in page_data:
 n=p['page'];qr=[]
 for i,c in enumerate(q for q in qrs if q['page']==n):
  m=re.search(r'/file/d/([^/]+)',c['text']);audio_id=m.group(1) if m else None
  if n==46:audio_id='1S868n8qG7v4LPtBBG6KnFG370aJnu_X0'
  if n==74 and not audio_id:audio_id='1Y6nhllxeknhWUePMJ3nToq3rW5RnudSw'
  xs=[v[0] for v in c['points']];ys=[v[1] for v in c['points']];a=by_audio.get(audio_id)
  qr.append({'id':f'a0-qr-{n}-{i+1}','sourceUrl':c['text'],'title':f'{i+1}-audio','rect':R(min(xs),min(ys),max(xs)-min(xs),max(ys)-min(ys)),**({'key':a['key']} if a else {'folder':True})})
 p['qrAudio']=qr

starts=[1,8,16,25,34,42,50,57,65,74,81,90,97,104]
titles=['Muqaddima va mundarija','Tanishuv va arab alifbosi','Alif, bo, to, so','Jim, ho, xo','Dol va zol','Ro va zoy','Sin va shin','Sod va dod','To va zo','Ayn va g‘ayn','Fo, qof, kof','Lom va mim','Nun va ho','Vov va yo']
ar_titles=['الْمُقَدِّمَةُ','السَّلَامُ عَلَيْكُمْ','أَ بَ تَ ثَ','جَ حَ خَ','دَ ذَ','رَ زَ','سَ شَ','صَ ضَ','طَ ظَ','عَ غَ','فَ قَ كَ','لَ مَ','نَ هَ','وَ يَ']
units=[];thumbroot=root/'public/books/a0';thumbroot.mkdir(parents=True,exist_ok=True)
for i,start in enumerate(starts):
 end=starts[i+1]-1 if i+1<len(starts) else 112
 pix=doc[start-1].get_pixmap(matrix=fitz.Matrix(.7,.7));im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);im.thumbnail((250,340));im.save(thumbroot/f'unit-{i:02}.webp',quality=83)
 pages=[{'number':p['page'],'title':titles[i],'sentences':[],'qrAudio':p['qrAudio'],'exerciseCount':len(p['exercises'])} for p in page_data if start<=p['page']<=end]
 units.append({'id':f'manhaj-a0-v1-unit-{i:02}','title':('Muqaddima' if i==0 else f'{i}-vahda. {titles[i]}'),'arTitle':ar_titles[i],'description':('Kitob haqida va mundarija' if i==0 else f'Asl kitobning {start}–{end}-sahifalari · '+str(sum(x['exerciseCount'] for x in pages))+' ta interaktiv topshiriq'),'startPage':start,'endPage':end,'wordIds':[],'phrases':[],'pages':pages,'coverUrl':f'/books/a0/unit-{i:02}.webp'})
book={'id':'manhaj-a0','series':'manhaj','level':'A0','title':'Manhajul ‘Alamiy','subtitle':'Asl kitob · 13 vahda va muqaddima · 112 sahifa','edition':'Foydalanuvchi taqdim etgan A0 skaner nusxasi, v1','status':'published','sample':False,'pdfKey':pdf_key,'coverUrl':'/books/a0/cover.webp','coverColor':'#053c56','interactive':True,'words':[],'units':units}
for p in page_data:p.pop('qrAudio',None)
# Reviewed photo labels supplement OCR misses. Positions use the same printed grid.
import statistics
for line in (root/'scripts/a0-labels.tsv').read_text().splitlines():
 n,labels=line.split('\t');page=next(p for p in page_data if p['page']==int(n));labels=labels.split('|')
 for row in range(2):
  group=labels[row*4:row*4+4];low,high=((.44,.55) if row==0 else (.62,.74));matches=[w['rect']['y'] for w in page['words'] if norm(w['ar']) in {norm(a) for a in group} and low<w['rect']['y']<high]
  y=statistics.median(matches) if matches else (.493 if row==0 else .68)
  for col,ar in enumerate(group):
   center=[.77,.56,.35,.14][col];r=R(center-.075,y-.012,.15,.043);page['words']=[w for w in page['words'] if not(abs(w['rect']['x']+w['rect']['w']/2-center)<.095 and low<w['rect']['y']<high)]
   page['words'].append({**lex[norm(ar)],'rect':r})
label_norms={norm(a) for line in (root/'scripts/a0-labels.tsv').read_text().splitlines() for a in line.split('\t')[1].split('|')}
plural_norms={norm(a) for a in ['أَلْوَانٌ','ثِيَابٌ','حُرُوفٌ','طُيُورٌ','لُصُوصٌ','خُضَارٌ','حُفَّاظٌ','نُقُودٌ','أَرَانِبُ','فَوَاكِهُ','وُجُوهٌ']}
adjectives={norm(a) for a in ['صَحِيحٌ','أَخْضَرُ','لَذِيذٌ','أَزْرَقُ','مَشْغُولٌ','صَغِيرٌ','فَارِغٌ','جَيِّدٌ']}
for p in page_data:
 for w in p['words']:
  w['id']='a0w-'+hashlib.sha256((str(p['page'])+':'+w['ar']+':'+str(w['rect']['x'])+':'+str(w['rect']['y'])).encode()).hexdigest()[:20]
  if 'forms' not in w:
   if norm(w['ar']) in label_norms:
    w['sarf']=('Sifat: narsaning belgisini bildiradi.' if norm(w['ar']) in adjectives else 'Ism. Ko‘plik shaklida kelgan.' if norm(w['ar']) in plural_norms else 'Ism: rasmda ko‘rsatilgan narsa yoki tushunchaning nomi. Fe’lning to‘rt shakli bu birlikka tatbiq qilinmaydi.')
    w['nahv']='Bu joyda so‘z rasmning nomi sifatida alohida berilgan. U to‘liq gap tarkibida emas, shuning uchun unga dalilsiz mubtado, xabar yoki maf’ul vazifasi belgilanmaydi.'
   else:w['sarf']='Aniq vazn va so‘z turining tahrirlangan izohi hali kiritilmagan.'
(root/'lib/a0/book.json').write_text(json.dumps(book,ensure_ascii=False,separators=(',',':')))
(root/'lib/a0/worksheets.json').write_text(json.dumps(page_data,ensure_ascii=False,separators=(',',':')))
(root/'lib/a0/assets.json').write_text(json.dumps(assets,ensure_ascii=False,indent=2))
(work/'import-files.json').write_text(json.dumps(uploads,ensure_ascii=False,indent=2))
print(json.dumps({'pages':len(page_data),'units':len(units),'exercises':sum(len(p['exercises']) for p in page_data),'wordHotspots':sum(len(p['words']) for p in page_data),'audioFiles':len(audio),'qrCodes':sum(len(p['qrAudio']) for u in units for p in u['pages']),'bytes':sum(a['size'] for a in assets)}))
