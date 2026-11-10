import a0BookData from './a0/book.json';
import type {Book,Word,Sentence,Forms,Unit} from './types';
const noun=(id:string,ar:string,uz:string,example:string,exampleUz:string,acceptedUz:string[]=[]):Word=>({id,ar,uz,acceptedUz:[uz,...acceptedUz],kind:'noun',sarf:'Ism. Lug‘at shakli birlikda va raf’ holatida berilgan. Gapdagi vazifasiga qarab oxirgi harakati o‘zgaradi.',nahv:'Ushbu misolda ismiy jumlaning xabari bo‘lib, dammatayn bilan marfu’ kelgan.',example,exampleUz});
const verb=(id:string,uz:string,forms:Forms,example:string,exampleUz:string):Word=>({id,ar:forms.past,uz,acceptedUz:[uz],kind:'verb',forms,sarf:'Moziy — o‘tgan zamon, muzori’ — hozirgi yoki kelajak, amr — buyruq, masdar — zamonsiz ish nomi. Kartada ma’lum fe’lning birlik shakllari berilgan.',nahv:'Ushbu misolda moziy fe’l; undan keyingi bajaruvchi fā’il bo‘lib marfu’ kelgan.',example,exampleUz});
export const sampleWords:Word[]=[
 noun('student','طَالِبٌ','talaba','هٰذَا طَالِبٌ.','Bu talaba.',['o‘quvchi','oquvchi']),
 noun('teacher','مُعَلِّمٌ','o‘qituvchi','هٰذَا مُعَلِّمٌ.','Bu o‘qituvchi.',['ustoz','oqituvchi']),
 noun('book','كِتَابٌ','kitob','هٰذَا كِتَابٌ.','Bu kitob.'),
 noun('lesson','دَرْسٌ','dars','هٰذَا دَرْسٌ.','Bu dars.'),
 noun('school','مَدْرَسَةٌ','maktab','هٰذِهِ مَدْرَسَةٌ.','Bu maktab.'),
 noun('friend','صَدِيقٌ','do‘st','هٰذَا صَدِيقٌ.','Bu do‘st.',['dost']),
 noun('house','بَيْتٌ','uy','هٰذَا بَيْتٌ.','Bu uy.'),
 noun('language','لُغَةٌ','til','هٰذِهِ لُغَةٌ.','Bu til.'),
 verb('read','o‘qimoq',{past:'قَرَأَ',present:'يَقْرَأُ',command:'اِقْرَأْ',masdar:'قِرَاءَةٌ'},'قَرَأَ الطَّالِبُ الْكِتَابَ.','Talaba kitobni o‘qidi.'),
 verb('write','yozmoq',{past:'كَتَبَ',present:'يَكْتُبُ',command:'اُكْتُبْ',masdar:'كِتَابَةٌ'},'كَتَبَ الطَّالِبُ الدَّرْسَ.','Talaba darsni yozdi.'),
 verb('learn','o‘rganmoq',{past:'تَعَلَّمَ',present:'يَتَعَلَّمُ',command:'تَعَلَّمْ',masdar:'تَعَلُّمٌ'},'تَعَلَّمَ الطَّالِبُ الْعَرَبِيَّةَ.','Talaba arab tilini o‘rgandi.'),
 verb('understand','tushunmoq',{past:'فَهِمَ',present:'يَفْهَمُ',command:'اِفْهَمْ',masdar:'فَهْمٌ'},'فَهِمَ الطَّالِبُ الدَّرْسَ.','Talaba darsni tushundi.'),
 noun('water','مَاءٌ','suv','هٰذَا مَاءٌ.','Bu suv.'),
 noun('bread','خُبْزٌ','non','هٰذَا خُبْزٌ.','Bu non.'),
 noun('food','طَعَامٌ','ovqat','هٰذَا طَعَامٌ.','Bu ovqat.',['taom']),
 noun('room','غُرْفَةٌ','xona','هٰذِهِ غُرْفَةٌ.','Bu xona.'),
 noun('morning','صَبَاحٌ','tong','هٰذَا صَبَاحٌ جَمِيلٌ.','Bu go‘zal tong.',['ertalab']),
 noun('evening','مَسَاءٌ','oqshom','هٰذَا مَسَاءٌ جَمِيلٌ.','Bu go‘zal oqshom.',['kech','kechqurun']),
 noun('door','بَابٌ','eshik','هٰذَا بَابٌ.','Bu eshik.'),
 noun('pen','قَلَمٌ','qalam','هٰذَا قَلَمٌ.','Bu qalam.'),
 verb('drink','ichmoq',{past:'شَرِبَ',present:'يَشْرَبُ',command:'اِشْرَبْ',masdar:'شُرْبٌ'},'شَرِبَ الطَّالِبُ الْمَاءَ.','Talaba suvni ichdi.'),
 verb('go','bormoq',{past:'ذَهَبَ',present:'يَذْهَبُ',command:'اِذْهَبْ',masdar:'ذَهَابٌ'},'ذَهَبَ الطَّالِبُ إِلَى الْمَدْرَسَةِ.','Talaba maktabga bordi.'),
 verb('return','qaytmoq',{past:'رَجَعَ',present:'يَرْجِعُ',command:'اِرْجِعْ',masdar:'رُجُوعٌ'},'رَجَعَ الطَّالِبُ إِلَى الْبَيْتِ.','Talaba uyga qaytdi.'),
 verb('sit','o‘tirmoq',{past:'جَلَسَ',present:'يَجْلِسُ',command:'اِجْلِسْ',masdar:'جُلُوسٌ'},'جَلَسَ الطَّالِبُ فِي الْغُرْفَةِ.','Talaba xonada o‘tirdi.'),
];
// A different, reviewed example is used after a wrong answer.
const nounReteach:Record<string,[string,string]>={student:['هٰذَا طَالِبٌ مُجْتَهِدٌ.','Bu tirishqoq talaba.'],teacher:['هٰذَا مُعَلِّمٌ جَدِيدٌ.','Bu yangi o‘qituvchi.'],book:['هٰذَا كِتَابٌ جَدِيدٌ.','Bu yangi kitob.'],lesson:['هٰذَا دَرْسٌ جَدِيدٌ.','Bu yangi dars.'],school:['هٰذِهِ مَدْرَسَةٌ جَدِيدَةٌ.','Bu yangi maktab.'],friend:['هٰذَا صَدِيقٌ جَدِيدٌ.','Bu yangi do‘st.'],house:['هٰذَا بَيْتٌ كَبِيرٌ.','Bu katta uy.'],language:['هٰذِهِ لُغَةٌ جَدِيدَةٌ.','Bu yangi til.'],water:['هٰذَا مَاءٌ بَارِدٌ.','Bu sovuq suv.'],bread:['هٰذَا خُبْزٌ طَازَجٌ.','Bu yangi non.'],food:['هٰذَا طَعَامٌ لَذِيذٌ.','Bu mazali ovqat.'],room:['هٰذِهِ غُرْفَةٌ كَبِيرَةٌ.','Bu katta xona.'],morning:['هٰذَا صَبَاحٌ هَادِئٌ.','Bu sokin tong.'],evening:['هٰذَا مَسَاءٌ هَادِئٌ.','Bu sokin oqshom.'],door:['هٰذَا بَابٌ كَبِيرٌ.','Bu katta eshik.'],pen:['هٰذَا قَلَمٌ جَدِيدٌ.','Bu yangi qalam.']};
for(const w of sampleWords){if(w.kind==='verb'){w.reteachExample=w.example.replace('الطَّالِبُ','الْمُعَلِّمُ');w.reteachExampleUz=w.exampleUz.replace('Talaba','O‘qituvchi');}else if(nounReteach[w.id]){[w.reteachExample,w.reteachExampleUz]=nounReteach[w.id];}}
const particle=(id:string,ar:string,uz:string,sarf:string):Word=>({id,ar,uz,kind:'particle',acceptedUz:[uz],sarf,nahv:sarf,example:'',exampleUz:''});
export const helperWords:Word[]=[particle('ana','أَنَا','men','Alohida kishilik olmoshi. Quyidagi gapda mubtada vazifasida.'),particle('haza','هٰذَا','bu','Erkak jinsdagi yaqin birlik uchun ko‘rsatish olmoshi; ushbu gapda mubtada.'),particle('hazihi','هٰذِهِ','bu','Ayol jinsdagi yaqin birlik uchun ko‘rsatish olmoshi; ushbu gapda mubtada.'),particle('fi','فِي','ichida','Jarr harfi. Undan keyingi ism majrur bo‘ladi.'),particle('ila','إِلَى','tomon','Jarr harfi. Undan keyingi ism kasra bilan majrur keladi.'),particle('wa','وَ','va','Bog‘lovchi harf. So‘z yoki gaplarni bog‘laydi.'),particle('lam','لَمْ','o‘tgan zamon inkori','Muzori’ni jazm qiladi va o‘tgan zamon ishini inkor etadi.'),particle('lan','لَنْ','kelajak inkori','Muzori’ni nasb qiladi va kelajakdagi ishni inkor etadi.'),particle('arabic','الْعَرَبِيَّةُ','arab tili','Ism. Til nomi sifatida ishlatilgan.')];
const t=(ar:string,wordId?:string,uz?:string,nahv?:string)=>({ar,wordId,uz,nahv});
const sentences:Sentence[]=[
 {id:'s1',tokens:[t('أَنَا','ana'),t('طَالِبٌ','student')],uz:'Men talabaman.',analysis:'Men — mubtada o‘rnidagi olmosh. Talaba — xabar, dammatayn bilan marfu’. Bu ismiy jumla.'},
 {id:'s2',tokens:[t('هٰذَا','haza'),t('كِتَابٌ','book')],uz:'Bu kitob.',analysis:'Bu — mubtada o‘rnidagi ko‘rsatish olmoshi. Kitob — xabar, dammatayn bilan marfu’.'},
 {id:'s3',tokens:[t('أَقْرَأُ','read','o‘qiyman','Marfu’ muzori’. Fā’il yashirin men olmoshi.'),t('الْكِتَابَ','book','kitobni','Maf’ulun bihi, fatha bilan mansub.')],uz:'Men kitobni o‘qiyman.',analysis:'O‘qiyman — muzori’, damma bilan marfu’; fā’il yashirin men. Kitobni — maf’ulun bihi, mansub.'},
 {id:'s4',tokens:[t('أَتَعَلَّمُ','learn','o‘rganyapman','Muzori’ marfu’; fā’il yashirin men.'),t('الْعَرَبِيَّةَ','arabic','arab tilini','Maf’ulun bihi, fatha bilan mansub.')],uz:'Men arab tilini o‘rganyapman.',analysis:'O‘rganyapman — muzori’, marfu’. Arab tilini — maf’ulun bihi, mansub.'},
 {id:'s5',tokens:[t('كَتَبَ','write','yozdi'),t('الطَّالِبُ','student','talaba','Fā’il, damma bilan marfu’.'),t('الدَّرْسَ','lesson','darsni','Maf’ulun bihi, fatha bilan mansub.')],uz:'Talaba darsni yozdi.',analysis:'Yozdi — moziy. Talaba — fā’il, marfu’. Darsni — maf’ulun bihi, mansub.'},
 {id:'s6',tokens:[t('فَهِمَ','understand','tushundi'),t('الطَّالِبُ','student','talaba','Fā’il, damma bilan marfu’.'),t('الدَّرْسَ','lesson','darsni','Maf’ulun bihi, fatha bilan mansub.')],uz:'Talaba darsni tushundi.',analysis:'Tushundi — moziy. Talaba — fā’il, marfu’. Darsni — maf’ulun bihi, mansub.'},
];
const everyday:Sentence[]=[
 {id:'d1',tokens:[t('شَرِبَ','drink','ichdi'),t('الطَّالِبُ','student','talaba','Fā’il, marfu’.'),t('الْمَاءَ','water','suvni','Maf’ulun bihi, mansub.')],uz:'Talaba suvni ichdi.',analysis:'Ichdi — moziy; talaba — fā’il, marfu’; suvni — maf’ulun bihi, mansub.'},
 {id:'d2',tokens:[t('ذَهَبَ','go','bordi'),t('الطَّالِبُ','student','talaba','Fā’il, marfu’.'),t('إِلَى','ila'),t('الْمَدْرَسَةِ','school','maktabga','Jarr harfidan keyin kelgan ism, kasra bilan majrur.')],uz:'Talaba maktabga bordi.',analysis:'Bordi — lozim moziy fe’l; talaba — fā’il, marfu’; maktab — jarr harfidan keyin majrur.'},
 {id:'d3',tokens:[t('رَجَعَ','return','qaytdi'),t('الطَّالِبُ','student','talaba','Fā’il, marfu’.'),t('إِلَى','ila'),t('الْبَيْتِ','house','uyga','Jarr harfidan keyin kelgan ism, majrur.')],uz:'Talaba uyga qaytdi.',analysis:'Qaytdi — moziy; talaba — fā’il; uy — jarr harfidan keyin kasra bilan majrur.'},
];
const demoUnits:Unit[]=[
 {id:'a2-sample-1',title:'Ilm yo‘lidagi ilk qadam',arTitle:'فِي طَلَبِ الْعِلْمِ',description:'Tanishuv, kitob va dars haqida original namunaviy matn.',startPage:1,endPage:2,wordIds:sampleWords.slice(0,12).map(w=>w.id),pages:[{number:1,title:'O‘qiymiz va tushunamiz',sentences:sentences.slice(0,4)},{number:2,title:'Gapni tahlil qilamiz',sentences:sentences.slice(4)}],phrases:[{id:'phrase-learn',ar:'أَتَعَلَّمُ الْعَرَبِيَّةَ.',uz:'Men arab tilini o‘rganyapman.',usage:'O‘rganayotgan tilingiz haqida aytishda.',analysis:sentences[3].analysis,wordIds:['learn']},{id:'phrase-read',ar:'أَقْرَأُ الْكِتَابَ.',uz:'Men kitobni o‘qiyman.',usage:'O‘qiyotgan ishingizni aytishda.',analysis:sentences[2].analysis,wordIds:['read']}]},
 {id:'a2-sample-2',title:'Kun tartibim',arTitle:'يَوْمِي',description:'Kundalik ishlar, suv, maktab va uyga qaytish.',startPage:3,endPage:3,wordIds:sampleWords.slice(12).map(w=>w.id),pages:[{number:3,title:'Kundalik hayot',sentences:everyday}],phrases:[{id:'phrase-go',ar:'ذَهَبَ الطَّالِبُ إِلَى الْمَدْرَسَةِ.',uz:'Talaba maktabga bordi.',usage:'O‘tgan ishni aytishda.',analysis:everyday[1].analysis,wordIds:['go']}]}
];
const tanalUnits:Unit[]=[
 {id:'tanal-sample-1',title:'Ismiy va fe’liy jumla',arTitle:'الْجُمْلَةُ',description:'Mubtada, xabar, fā’il va maf’ulun bihini farqlash.',startPage:1,endPage:1,wordIds:['student','teacher','book','lesson','pen','write','read','understand'],pages:[{number:1,title:'Jumlaning tuzilishi',sentences:[sentences[0],sentences[1],sentences[4]],rule:'Ismiy jumlada mubtada va xabar bo‘ladi. Oddiy ismiy jumlaning mubtada va mufrad xabari marfu’. Fe’liy jumlada ma’lum fe’lning fā’ili marfu’, maf’ulun bihisi esa mansub bo‘ladi.'}],phrases:[]},
 {id:'tanal-sample-2',title:'Lam va lan',arTitle:'النَّفْيُ',description:'Inkorning ma’nosi va muzori’ fe’lning oxirgi harakati.',startPage:2,endPage:2,wordIds:['read','write','learn','understand'],pages:[{number:2,title:'O‘tgan va kelajak zamon inkori',sentences:[{id:'n1',tokens:[t('لَمْ','lam'),t('يَكْتُبْ','write','yozmadi'),t('الطَّالِبُ','student','talaba'),t('الدَّرْسَ','lesson','darsni')],uz:'Talaba darsni yozmadi.',analysis:'Lam o‘tgan zamonni inkor qilib, muzori’ni jazm qiladi. Bu fe’lning jazm alomati sukun.'},{id:'n2',tokens:[t('لَنْ','lan'),t('يَكْتُبَ','write','yozmaydi (kelajakda)'),t('الطَّالِبُ','student','talaba'),t('الدَّرْسَ','lesson','darsni')],uz:'Talaba darsni yozmaydi (kelajakda).',analysis:'Lan kelajakni inkor qilib, muzori’ni nasb qiladi. Bu fe’lning nasb alomati fatha.'}],rule:'Lam — o‘tgan zamon inkori va jazm. Lan — kelajak zamon inkori va nasb. So‘zning ma’nosini undan oldingi vosita bilan birga tushuning.'}],phrases:[]}
];
const levelColors=['#8b9b6b','#4d827b','#2d8c75','#677bc0','#8d72b6','#b59160','#7b8597'];
export const defaultBooks:Book[]=[...['A0','A1','A2','B1','B2','C1','C2'].map((level,i):Book=>({id:'manhaj-'+level.toLowerCase(),series:'manhaj',level,title:'Manhajul ‘Alamiy',subtitle:level==='A2'?'Arabiyat namuna darslari':'Kitob PDFi kutilmoqda',edition:'Asosiy',status:level==='A2'?'sample':'planned',sample:level==='A2',coverColor:levelColors[i],units:level==='A2'?demoUnits:[],words:level==='A2'?sampleWords:[]})),{id:'at-tanal',series:'tanal',level:'Sarf · Nahv',title:'At-Tanal',subtitle:'Arabiyat namuna qoidalari',edition:'Asosiy',status:'sample',sample:true,coverColor:'#bb9960',units:tanalUnits,words:sampleWords}];
const a0Index=defaultBooks.findIndex(b=>b.id==='manhaj-a0');if('id' in a0BookData)defaultBooks[a0Index]=a0BookData as unknown as Book;
export const getWord=(book:Book,id:string)=>book.words.find(w=>w.id===id)??helperWords.find(w=>w.id===id);
export const sentenceText=(s:Sentence)=>s.tokens.map(t=>t.ar).join(' ') + '.';
