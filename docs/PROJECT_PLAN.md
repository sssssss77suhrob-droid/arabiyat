# Repositoryga topshirilgan to‘liq loyiha rejasi

Bu tarixiy loyiha rejasi. Joriy holat README.md va docs/CONTINUE_IN_UZBEK.md da. Pastdagi eski API rejalarini qayta yoqmang: so‘nggi qaror APIsiz ishlash. Manbada tayyor A0 kontenti va original media paketlari saqlanadi; shaxsiy ma’lumotlar va kalitlar kiritilmaydi.

# Arabiyat: interaktiv arab tili platformasi

## Amaldagi holat — A0 to‘liq qayta ko‘rib chiqildi, 2026-11-09

Bu bo‘lim eng so‘nggi qaror va bajarilgan ishlarni qayd etadi. Pastdagi oldingi ish hisobotlari tarix hisoblanadi; API haqidagi avvalgi rejalar foydalanuvchining yangi «APIsiz ishlaymiz» qarori bilan almashtirilgan.

Sayt: https://arabiyat-academy.navbahor077.chatgpt.site

- Asl A0ning 112 sahifasi ko‘rib chiqildi; 3-sahifa haqiqatan bo‘sh. 111 matnli sahifada jami **6 715 ta so‘z yoki harf belgisi uchrashi** uchun tayyor o‘zbekcha ma’no va alohida joy xaritasi bor. Bu noyob lug‘at birliklari soni emas. Muqova, kirish, ko‘rsatmalar, dialog, so‘z banklari, harf va raqamlar ham xaritaga kiritilgan.
- Tarjima so‘zni **bosib turish** bilan ochiladi. Oyna bosilgan nuqtaga ergashmaydi: ko‘rinib turgan kitob markazida, kichik va shaffof chiqadi. Bo‘yash va saqlash qolgan; Play yo‘q. Telefon uchun kichik so‘zlarning bosish maydoni kengaytirildi, maydonlar ustma-ust kelsa yaqin so‘z tanlanadi.
- A0da Sarf/Nahv va Ko‘proq tugmalari chiqarilmaydi; server ham bu kitob uchun tahlilni o‘chiradi. Kitobning dastlabki sahifalari va ayrim darslarida qisqa matnlar borligi aniqlandi, ammo foydalanuvchi qaroriga ko‘ra A0da grammatika paneli kerak emas.
- Keyingi kitoblar uchun to‘liq gap tarjimasi, sarf, nahv, har bir bo‘lakning vazifasi, o‘xshash misol va fe’llarning to‘rt shaklini **oldindan tayyorlab saqlash** formati va server yo‘li bor. Hali berilmagan kitoblarning tahlillari tayyor deb ko‘rsatilmaydi; tayyor ma’lumot bo‘lmasa aniq xabar chiqadi.
- Fe’l shakllari harakatlari bilan beriladi. 37 qo‘shimcha fe’l yozuvi tayyorlandi. Majhul so‘zlar uchun asosiy ma’lum nisbatdagi to‘rt shakl va tushuntirish beriladi; mavjud bo‘lmagan majhul amr o‘ylab topilmaydi. Harakati boshqa bo‘lgan ot va fe’lni adashtirmaslik uchun shakl qidiruvida harakatlar saqlanadi; masalan, «soya» oti fe’l qilib ko‘rsatilmaydi.
- **192 ta asl kitob topshirig‘i** xaritasi bor. Muqova va kirishning dastlabki 7 sahifasida topshiriq yo‘q; eski ortiqcha natijalar progressga qo‘shilmaydi. Rasmli vazifalarda javob joyi rasm osti yoki yonidagi haqiqiy chiziq/katakda. Ulanadigan vazifalar chiziq bilan bajariladi. So‘z/bo‘lak sahifaning o‘zidan tanlanadi yoki sudraladi; alohida tashqi bankdan olish talab qilinmaydi.
- Yozish vazifalarida klaviatura yoki qalam ishlatiladi. Qo‘lda bajarilgan/erkin topshiriqlar o‘zini tekshirish deb ajratiladi; lug‘at testining to‘g‘ri javob foizini oshirmaydi. 9 tinglab tanlash vazifasida oltitadan mustaqil juftlik bor va har birida bitta javob tanlanadi. Tekshirilmagan audio javob kalitlari taxmin qilinmagan.
- Kitob boshqaruvlari va audio pleyeri ixcham shaffof bloklarga aylantirildi. Yozishda qalam kursorining ko‘rinishi nuqta; o‘chirg‘ich yozuvning tegilgan qismini doska artgandek o‘chiradi. Telefonning fon sahifasi kitob ochiq paytda qulflanadi; kitob tafsilotidagi katta yopishib qoladigan muqova kichraytirildi.
- 82 original QR audiosi saqlandi. Tayyor vaqt belgilarida **1 735 ta bosma so‘z/harfga mos nishon** bor. Chiziq har bir so‘zning o‘z kengligida, uning aytilish oralig‘ida **o‘ngdan chapga** asta chiziladi. 41 ta qo‘shimcha joylashuv tuzatildi, 3 birlashgan parcha asl mahalliy transkriptning haqiqiy vaqt chegaralarida ajratildi. Ikki noaniq/bosilmagan so‘z uchun aloqasiz joyga chiziq qo‘yish bekor qilindi.
- O‘qishdagi tarjima, so‘z joyini topish, gap izohi va audio vaqti uchun pullik AI chaqiruvi yo‘q. Mavjud maxfiy kalit oshkor qilinmadi va foydalanilmaydi; yangi API krediti talab qilinmaydi.

Saqlash qarori: original PDF va audio mavjud R2da, hisob qaydlari, natijalar va saqlanganlar D1da qoladi. Tayyor ma’nolar va tahrirlangan sahifa xaritalari sayt manbasi bilan versiyalanadi. Google Drive kerak bo‘lsa original fayllarning qo‘shimcha zaxirasi sifatida ishlatilishi mumkin; jonli o‘qish uchun alohida yangi xizmat ulanmadi.

Tekshiruv: TypeScript va yakuniy build o‘tdi. 6 715 nishon markazi, barcha 112 sahifa javobi va 111 matnli sahifadagi so‘z olish yo‘li, tayyor gap tahlili, A0dagi tahlilni o‘chirish, saqlash/ajratish, 119 javob kalitli mashq va 9 tanlov guruhlari tekshirildi. Barcha 82 audio vaqt yo‘li API kalitisiz va tashqi tarmoq o‘chirilgan holatda ishladi. Qayd to‘qnashuvi, haqiqiy R2 range javobi, qisman o‘chirish va foydalanuvchilar ma’lumotlarini ajratish sinovlari ham o‘tdi.

Cheklovlar: mobil va stilus bilan haqiqiy brauzerda yakuniy vizual tekshiruv brauzer ulanishi sabab tugallanmagan. Barcha audio yozuvlar boshidan oxirigacha odam tomonidan qayta tinglangan deb da’vo qilinmaydi: oldingi mahalliy nutq moslashuvi va o‘lchangan fonetik intervallar saqlandi, qolgan sinxron xatolar tinglab tahrir qilinishi mumkin. Sahifa joylari tekshirildi, ammo mutlaq piksel aniqligi yoki tahrir xatosi yo‘qligi kafolatlanmaydi.

Nashr muvaffaqiyatli. Manba commit: d1683bdbcbadcb99cb009a1ab956a162bad76ee7
Versiya: appgprj_6af0d85b0f5c8191aa580160828c3634~appgver_1e94e07326e88191a426ded9b57daf88
Deployment: appgdep_6af2160bf5648191b5e3c449eefa3271
Mavjud faqat egasiga ochiq auditoriya saqlandi. Ommaviy ochish, tashqi Google/Apple/Telegram kirishi va Android/iOS paketlari hali alohida ishlar.

## Oldingi ishlar va saqlanadigan talablar

## Audio belgilarining API xarajati olib tashlandi — 2026-11-09
Foydalanuvchi barcha audioni API bilan emas, oldindan hisoblab moslashni so‘radi. 82 original MP3 qayta olindi va SHA-256 tekshirildi; jami 88.4 daqiqa. Eski soat va ayn havolalari nashriyot papkasidagi aynan bir xil fayllardan tiklandi.
Audio ijrosidagi AI chaqiruvi olib tashlandi. /api/audio-timing hozir tayyor statik xaritani beradi, API kaliti, kredit, transkripsiya yoki yangi audio yuklash talab qilmaydi. Original audioning o‘zi odatdagidek tinglanadi. Jonli tarjima/sarf/nahvning API talabi alohida, o‘zgarishsiz.
82 audio uchun 2197 vaqt hodisasi saqlandi, 1491 o‘qilish holati bosma so‘z/harf joyiga bog‘langan. Bu 1491 ta noyob lug‘at birligi degani emas. 15 harf/tanvin/cho‘ziq tovush audiosida 379 nishon original to‘lqindagi haqiqiy boshlanish-tugashlardan bosma tartibga moslandi; vaqtlar teng taqsimlanmadi. 12-sahifada qisqa84 va uzun84 tovush mavjud. Bosmada bo‘lmagan qo‘shimcha talaffuz uchun chiziq o‘ylab topilmaydi.
Oddiy dialog va lug‘atlarda kompyuterning o‘zidagi model yordamida dastlabki vaqtlar ajratildi, bosma matn/OCR bilan solishtirildi; qo‘shimcha so‘z joylari original rasmdan qo‘lda belgilandi. Bu barcha88daqiqani odam tinglab tasdiqladi degani emas. Dialog/OCR moslashida xatolar qolishi mumkin; tekshiruv kerak bo‘lgan joylar ochiq qayd etildi. API ishlatilmagan.
TypeScript, ishlab chiqarish buildi,82audio aktivlari, original manba hash/davomiyligi, chegaralar, Reader va umumiy API testlari o‘tdi. 82ta haqiqiy endpoint javobi AI kalitisiz va barcha tashqi tarmoq o‘chirilgan holda tekshirildi. Telefon/stilusda audio chizig‘ining yakuniy vizual tekshiruvi bu nashrda tasdiqlanmagan.
So‘nggi kod: 2e761e12407bb1e989560ff40d7d5b68e8d6133b. Version: appgprj_6af0d85b0f5c8191aa580160828c3634~appgver_3f37bc31a1d0819196269af12e47f8a4. Deployment: appgdep_6af1a68884a881919da1c116ed87917e. Holat: succeeded. Sayt: https://arabiyat-academy.navbahor077.chatgpt.site. Quyidagi eski “audio belgilariga API krediti kerak” qaydlari shu bo‘lim bilan almashtiriladi.
Ma’lumot lib/a0/audio-timings.json ichida, qayta tuzish manbalari scripts/a0-timing-inputs ichida; python scripts/prepare-a0-timings.py bilan APIsiz qayta tuziladi. Manba va nashr Sites Git’da saqlangan.


## Eng so‘nggi tuzatish — dars uslubi va ixcham oyna
2026-11-09: foydalanuvchi sarf/nahvni «Mavzuni tushuntirish» chatidagi kabi sodda, batafsil so‘radi. Endi butun gap tarjimasi, jumla tuzilishi, barcha so‘zlarning sarfi/i’robi, belgi va uning sababi, omil/bog‘lanish, yashirin foil va olmosh qaytishi kabi tegishli jihatlar tushuntiriladi. Oxirida o‘xshash harakatli misol va tarjima; asl gap va misoldagi barcha fe’llar to‘rt shaklda. lesson-analysis-v4 keshi eski qisqa javoblarni qayta ishlatmaydi. Jonli javob sifati API krediti to‘ldirilgach tekshiriladi.
Tarjima kichik oynasi 340 px o‘rniga 264 px; matn va tugmalar ixcham. Fon 68% xira, tugmalar fonining xiraligi 46%; orqadagi sahifa ko‘rinadi. Kengaytirilgan Sarf/Nahv oynasi alohida.
QR original audio uchun joriy so‘z ostidagi chiziq kodi mavjud, vaqt/pozitsiya o‘zgarganda yumshoq siljiydi. Haqiqiy timestampni olish API kreditiga bog‘liq, jonli sinxronlash hali tasdiqlanmagan. Taxminiy vaqt qo‘yilmaydi.
Nashr muvaffaqiyatli: https://arabiyat-academy.navbahor077.chatgpt.site; commit ea22a930942f4f8d21f363afc68186120bfc0467; version appgprj_6af0d85b0f5c8191aa580160828c3634~appgver_6c52bd4061588191849f486df9739db6; deployment appgdep_6af19097fff48191a846236f12868290. Bu qiymatlar quyidagi oldingi nashr identifikatorlarini yangilaydi. TypeScript, build, reader va API testlari o‘tdi; oxirgi faqat CSS tuzatishidan so‘ng build o‘tdi. Avvalgi topshirish ZIPi oldingi nashrning nusxasi; oxirgi kod mavjud Site Git manbasida.


## Joriy holat — 2026-11-09, oxirgi nashr
Bu bo‘lim oldingi nashr qaydlaridagi eskirgan holatlarni almashtiradi. Pastdagi batafsil talablar saqlanadi.

Sayt: https://arabiyat-academy.navbahor077.chatgpt.site
Sites project ID: `appgprj_6af0d85b0f5c8191aa580160828c3634`
Manba commit: `91fef0813d72d11e6c6d7aa4497cadee7f45da3b`
Version ID: `appgprj_6af0d85b0f5c8191aa580160828c3634~appgver_056ab727f3748191bcde828acd5b5cc2`
Deployment ID: `appgdep_6af18e4b7d9c8191bd16f21c7da1bd65`
Nashr: `succeeded`; runtime revision: 5. Auditoriya egasiga xususiy; boshqa hisob taklif qilinmagan.

### So‘z yordamining yakuniy talabi va amalga oshirilgan ko‘rinishi
- Oddiy bosish tarjimani ochmaydi. O‘qish rejimida so‘zni taxminan 500 ms bosib turish kichik oynani ochadi. Barmoq siljishi yoki bekor qilinishi kutishni to‘xtatadi; Enter/Space ham ochadi.
- Kichik oyna kitob ustida, tanlangan so‘zga yaqin, krem/zaytun rangli shaffof ko‘rinishda. Faqat o‘sha so‘zning ma’nosi; pastida Ko‘proq, Bo‘yash, Saqlash. Play/Tinglash tugmasi yo‘q.
- Ko‘proq markaziy katta oynani ochadi: Gap tarjimasi / Sarf / Nahv. Arabcha to‘liq haqiqiy gap alohida RTL blokda, tanlangan so‘z rang bilan ajratilgan. Tarjima bitta so‘zga; sarf/nahv butun gapga, har bir so‘zning shu gapdagi vazifasiga tegishli.
- Alohida rasm nomiga gap yoki sintaktik vazifa o‘ylab topilmaydi. Skaner konteksti noma’lum bo‘lsa asl sahifa tasviridan olinadi. Har bir fe’l moziy, muzori’, amr va masdar bilan, to‘liq harakatli.
- Bo‘yash asl sahifadagi so‘z joyini bo‘yaydi, qayta bosish olib tashlaydi; shaxsiy sahifa qaydida saqlanadi. Saqlash Mening lug‘atim → Saqlanganlarga qo‘shadi. Orqaga kichik oynaga qaytaradi, X/Escape yopadi.
- At-Tanal uchun Gap tarjimasi / Qoida izohi; Manhajdagi Sarf/Nahv qo‘yilmaydi. Asl At-Tanal PDF hali kutilmoqda.
- Bepul tarjima javoblaridan grammatik qismlar serverda olib tashlanadi. Obunali tahlil ruxsati serverda tekshiriladi. Audio va so‘z tarjimasi doim bepul.

### Kitob va mashqlar
- A0: asl 112 sahifa, muqaddima + 13 vahda, asl PDF va 82 MP3 R2’da. 83 QR nuqtasi, shundan biri papka havolasi.
- Ekran bo‘ylab o‘qish, boshqaruvlarni bir bosishda ochish, joyidan siljimaydigan yozish/chizish asboblari va yon qaydlar saqlanadi. Chet tugmalari va 100% holatda gorizontal surish bilan varaqlash qo‘shildi.
- Reader’dagi tashqi so‘z banki o‘rniga mashqning asl bosilgan so‘z/harf/rasmlari tanlanadi yoki sudraladi. 584 manba maydoni belgilandi. Telefon uchun tanlash → bo‘sh joyni bosish ham bor. Barcha mashqlar avtomatik baholanmaydi.
- 2027 so‘z nuqtasi: 1572 tayyor lug‘at tarjimasi, 455 tahrirlanmagan OCR nuqtasi. Noma’lum matnning tarjimasi sifatida xom OCR ko‘rsatilmaydi; asl tasvirni AI o‘qishi kerak. Tayyor nuqtalar tashqarisidagi bosib turish ham tasvirli so‘rov beradi.
- Audio vaqt belgilariga mos so‘z tagidagi chiziq uchun server/client kodi qo‘shildi. Faqat original audio transkripsiyasidagi haqiqiy vaqt va aynan mos so‘z ishlatiladi, taxminiy vaqt yaratilmaydi. Hamma sahifaning jonli sinxronligi tasdiqlanmagan.

### OpenAI — haqiqiy holat
Foydalanuvchi API kaliti yaratish va aniq mahalliy manzilga yozishni tasdiqladi. Kalit yaratilib, ignor qilingan `.env.local` va Sites `OPENAI_API_KEY` maxfiy runtime sozlamasiga yozildi; `OPENAI_MODEL=gpt-4.1-mini`. Qiymatlar hujjat yoki topshirish ZIPiga kiritilmaydi.
Jonli sinov 429 `credit_balance_exhausted` / `insufficient_quota` qaytardi. Shuning uchun yangi vision, jonli tarjima/tahlil va audio timestamps ishladi deb ko‘rsatilmaydi. Egasi OpenAI hisobiga kredit qo‘shgach jonli tekshiruv kerak. ChatGPT obunasi API kreditini o‘zi to‘ldirmaydi.
Joriy transkripsiya adapteri `whisper-1`; rasmiy tugash sanasidan oldin almashtirish kerak. AI test yaratish va tahrirchi nazorati hali keyingi bosqich.

### Tekshiruv va ochiq ishlar
TypeScript, ishlab chiqarish buildi, domen/A0, API va yangi Reader sinovlari o‘tdi. Tekshirilganlar: so‘z saqlash/ajratish/kesh, alohida so‘zga gap tahlilini rad etish, butun gap natijalari va fe’l shakllari, highlight qaydlari va hisoblar izolyatsiyasi, bepul javobda grammatikaning yashirilishi, kredit xatosi, timestamp mosligi va bo‘shliqlar.
AI va timestamp sinovlari mock/fixture bilan; ular jonli xizmat natijasi emas. Sinov brauzeri `terminal.local` uchun `ERR_CONNECTION_REFUSED` qaytardi: dizayn, long press, drag va stilus haqiqiy qurilmada hali tekshirilishi kerak. Yaratilgan UI rasmi konsept, brauzer skrinshoti emas.
Google/Apple/Telegram OAuth, to‘lov/narxlar, to‘liq offline, APK/iOS hali tugallanmagan. A0 lug‘at yodlash bo‘limini qayta ishlab chiqish foydalanuvchi bilan keyin kelishiladi.

### Boshqa hisobda davom ettirish
`Arabiyat_davom_ettirish.md` va `Arabiyat_source_transfer.zip` alohida tayyorlandi. Gmail yoki promptning o‘zi mavjud Site’ga tahrirlash ruxsati bermaydi. Hozirgi native editor yo‘li bir workspace ichidagi account IDlari bilan; tashqi email taklifi ko‘rish uchundir. Ruxsat yoki auditoriya o‘zgartirilmadi.
`OWNER_PRIVATE_PREVIEW=true` egasiga xususiy sinov uchun. Ulashishdan OLDIN uni o‘chirish va aniq `ADMIN_USER_IDS` ni sozlash shart.
ZIP — maxfiy kalitsiz manba, to‘liq ma’lumotlar zaxirasi emas. Unda Git tarixi, D1 foydalanuvchi ma’lumoti, R2’dagi original PDF/MP3, runtime kalitlar yo‘q. Alohida yangi Site yangi URL va qayta sozlashni talab qiladi.

## Oldingi nashrlar va kelishilgan batafsil talablar
Quyidagi oldingi holat qaydlaridagi “API ulanmagan”, “oddiy bosish” va eski nuqta sonlari yuqoridagi joriy holat bilan almashtiriladi.

Yangilangan sana: 2026-11-09. Holat: Arabiyatning ikkinchi veb-nashrida foydalanuvchi taqdim etgan A0 muqova va asl kitobi joylandi. Sayt faqat egasiga ochiq. Quyidagi hujjatda bajarilgan ishlar, kelishilgan talablar va keyingi bosqichlar ajratilgan. Oldingi shaxsiy Arabiyat paneli alohida saqlandi.



## Ekran va saqlangan so‘zlar — keyingi yangilanish

Foydalanuvchi yuborgan skrinshotga ko‘ra doimiy yuqori sarlavha/asboblar va pastki audio chizig‘i asosiy kitob ko‘rinishidan yashirildi. Kitob sahifasi nisbatini buzmasdan ekran balandligiga sig‘adi; kompyuterning keng ekranida yon maydonlar qayd uchun qoladi. Kitobni ochish bosilishida brauzer qo‘llasa native fullscreen so‘raladi, aks holda ekran bo‘ylab o‘qish ko‘rinishi ishlaydi.

Sahifaning bo‘sh joyiga bir marta bosilganda suzuvchi boshqaruvlar animatsiya bilan ochiladi. Qalam yoqilganda qalam/marker/o‘chirg‘ich/matn/ko‘chirish/rang/undo/redo ko‘rinadi; ular mutlaq joylashgan, sahifa va chiziqlarni siljitmaydi. Oddiy o‘qish holatida so‘zni bosish tarjima oynasini ochadi; sarf va nahv tugmalari oldingi obuna ruxsatlari bilan qoladi.

A0 tarjima nuqtalari 1275 taga kengaytirildi. 28 alifbo sahifasidagi 224 asosiy rasm nomi qo‘lda o‘qib tekshirildi, skrinshotdagi 34-sahifaning yetishmayotgan nomlari ham qo‘shildi. Bu barcha skaner matnining to‘liq tarjimasi tayyor degani emas: qolgan matn tahriri va kontekstli tahlil hali kerak. Rasm nomlari uchun ism/sifat/ko‘plik haqidagi tayyor sarfiy izoh, alohida so‘zga gap vazifasi tayinlanmasligi haqidagi nahviy izoh beriladi. Jonli AI API kaliti/model hali ulanmagan.

Sahifadagi so‘zlarni hisobdagi Mening lug‘atim → Saqlanganlarga qo‘shish, saqlanganlik belgisi, olib tashlash va asl sahifaga qaytish qurildi. Bu alohida saqlangan matn bo‘lib, lug‘at testining progressini o‘zgartirmaydi. Server asl kontent va kitob/vahda/sahifa/so‘z IDlarini tekshiradi. Boshqa foydalanuvchi yozuvlarini ko‘rish yoki o‘zgartirishga yo‘l qo‘yilmaydi.

Tekshiruv: TypeScript, build, domen/A0 hamda API → D1 → qayta yuklash sinovlari o‘tdi. So‘zni saqlash, dublikat, o‘chirish, yolg‘on tarjima yuborilishi, noto‘g‘ri sahifa/vahda, hisoblar orasidagi ajratish tekshirildi. Sinov brauzeri terminal.local ulanishini rad etdi; ekran, animatsiya va stilusdagi amaliy vizual tekshiruv hali tasdiqlanmagan.

## Ikkinchi nashr — asl A0 kitobi va jonli topshiriqlar

Foydalanuvchining yangi talabi: taqdim etilgan A0 muqova va PDFning o‘zi ishlatilsin; kitob bosilganda vahdalar ochilsin; QR yonidagi tugma original audioni yoqsin; kitob mashqlari sudrash/joylash, yozish va moslashtirish orqali bajarilsin. So‘z yodlash bo‘limining yangi ko‘rinishi keyingi muhokamaga qoldirildi.

Bajarilgan:
- Foydalanuvchi taqdim etgan haqiqiy muqova. 112 sahifali asl PDF o‘zgartirilmasdan saqlandi; sahifalari tez ochilishi uchun undan olingan WebP tasvirlar ishlatiladi. Asl PDFni ochish/yuklash havolasi bor.
- Haqiqiy mundarijaga ko‘ra 13 dars/vahda va muqaddima. Kartalarda shu kitobning sahifa rasmlari, sahifa oralig‘i va topshiriq progressi.
- 83 QR nuqtasi: 82 original MP3 va bitta umumiy audio papkasi. QR joyi yonida ijro tugmasi, tezlik va takrorlash. Buzilgan eski soat havolasi uchun shu kitobning nashriyot audio papkasidan mos fayl topildi; ayn darsi qisqa havolasining haqiqiy Drive fayli olindi. PDF va barcha audiolar hajm hamda SHA-256 orqali tekshirildi.
- Kitob ichida 169 topshiriq yozuvi: harf/so‘z yozish, so‘z va gap kartalarini joylash, juftlash, tovush variantlari, suhbat va erkin yozish. Kartani sudrash yoki kartochka va joyni navbat bilan bosish; qalam va yon qaydlar shu o‘qish oynasida ishlaydi.
- Aniq kaliti tayyorlangan topshiriqlar serverda avtomatik tekshiriladi. Boshqa ochiq, tinglash va talaffuz mashqlari original audio yoki ustoz bilan o‘zini tekshirish uchun; hamma 169 topshiriq avtomatik baholanadi degani emas.
- Javob va topshiriq tugallanishi har bir foydalanuvchiga alohida saqlanadi; versiya to‘qnashuvi nazorati va qurilmadagi qoralama mavjud. Vahda/kitob topshiriq foizlari lug‘at testi foizlaridan alohida hisoblanadi.
- Tayyor ma’nosi tekshirilgan lug‘atdan sahifa bo‘ylab 794 bosiladigan so‘z nuqtasi. Fe’llarga moziy, muzori’, amr va masdar to‘rtligi harakat bilan beriladi. Bu skanerdagi hamma so‘z va gapning to‘liq tarjima/tahlili tayyor degani emas; to‘liq matn tahriri keyingi ish.
- A0 yangi lug‘at test to‘plami bu bosqichda yaratilmagan. Mavjud so‘z yodlash usuli saqlandi; uning qayta ishlanishi foydalanuvchi bilan keyin kelishiladi.

Tekshiruv: TypeScript, ishlab chiqarish buildi, domen va A0 kontent sinovlari, API → D1 → qayta yuklash, foydalanuvchi chegaralari, topshiriq versiyasi/409, kalit bilan baholash, lug‘at natijasiga ta’sir qilmasligi va audio faylning importi/R2/range zanjiri o‘tdi. Nashr Sites orqali tasdiqlandi. Ushbu nashrda sinov brauzeri ulanishi ishlamadi: telefon/stilus/sudrashning vizual sinovi va avtomatik ajratilgan har bir ochiq maydonning sahifaga mosligini alohida tekshirish yakunlanmagan.

Chegaralar: to‘liq arabcha OCR matni va kontekstli tarjima/tahlil tahriri, barcha topshiriqlarga javob kaliti, haqiqiy qurilmada interaksiya tekshiruvi qolmoqda. Google/Apple/Telegram kirishi, API kaliti/model, obuna narxlari, APK/iOS bu yangilanishda yoqilmadi. Audio va mavjud so‘z tarjimasi bepul qoladi.

## Birinchi nashr — avval bajarilgan ishlar

Sayt: https://arabiyat-academy.navbahor077.chatgpt.site

- Arabiyat nomi va yashil ochiq kitob belgisi. To‘q yashil kabinet, och rangli kitob maydoni, glass boshqaruvlari, o‘tish animatsiyalari va animatsiyani kamaytirish qo‘llovi.
- Manhajul ‘Alamiy A0–C2 katalogi va At-Tanalning alohida kitob bo‘limi. Asl PDFlar berilmagani sababli A2 va At-Tanalda Arabiyatning original namuna materiallari bor; boshqa darajalarda «PDF kutilmoqda» holati. Muqovalar hozir dizayn namunasi.
- Kitobning yagona oynasi: so‘z va gap tarjimasi, alohida RTL arabcha bloklar, Manhaj sarf/nahv qulfchalari, At-Tanal qoida izohi. Fe’lning to‘rt harakatli shakli tarjima/kartochka/mashq izohlarida beriladi.
- Sahifa va yon bo‘shliqlar uchun qalam, marker, matnli qayd, o‘chirg‘ich, yozuvni ko‘chirish, bekor qilish/qaytarish, masshtab va sahifa boshqaruvi. Hisobdagi qaydlar avtomatik saqlanadi; ikki oynadagi o‘zgarishlar ustma-ust yozilmasligi uchun versiya tekshiriladi. Qurilmada qoralama nusxa va saqlashni qayta urinish tugmasi bor. Pointer bilan yozishning to‘liq brauzer sinovi hali yakunlanmagan.
- Oltita mashq: ma’noga mos so‘z, klaviaturada yozish, qurilmada arabcha ovoz bo‘lsa tinglab yozish, bo‘sh joy, gap tuzish, fe’l shakllari. Kitob, bitta/bir nechta/barcha vahda, saqlangan/bilinmagan/takror filtrlari. Savollar bittadan; xato so‘zlar qo‘shimcha misol bilan yordamli mustahkamlanadi.
- Alohida kartochkalar: javobni ochish, Bilmadim/Qiyin/Bildim, shaxsiy lug‘at, bilmagan so‘zlar va natijadan hisoblangan takror sanalari. Kartochkadagi o‘zini baholash mustaqil test foizini oshirmaydi.
- Vahda va kitob foizlari mustaqil to‘g‘ri topilgan yagona so‘zlardan hisoblanadi. Bir so‘zni takror topish foizni oshirmaydi. Vahda aniqligi oxirgi 20 ta mustaqil javobdan, kitob foizi jami so‘z birliklaridan hisoblanadi. Kunlik so‘z maqsadi, davomiylik, javoblar tarixi, natija diagrammasi va qolgan sahifadan davom etish bor.
- Iboralar bo‘limida kitob/vahda, ma’no, vaziyat, tinglash va yozib eslash namunasi. Ibora yozish natijasi hozir sessiya ichida; alohida iboralar tarixi va rol o‘yinlari keyingi bosqich.
- Boshqaruv paneli: 25 MBgacha PDF/audio yuklash, vahda sahifalarini belgilash, sahifaga original audio bog‘lash, JSON orqali lug‘at/gap/ibora kiritish, qoralama va nashr holatlari. PDF.js matnli PDFni ko‘rsatadi; skanerlangan kitobga OCR va so‘z joylarini tayyorlash kerak. Katta PDFlar uchun yuklashni kengaytirish keyingi bosqich.
- Audio va so‘z tarjimasi doim bepul. «7 kun bepul» va qolgan kunlar hisob yaratilgan paytdan hisoblanadi; bu boshlanish nuqtasi hozirgi amalga oshirish qarori, foydalanuvchi bilan alohida tasdiqlanmagan. Narx/to‘lov yo‘q, obunali tahlil uchun ruxsat serverda tekshiriladi.
- Hozirgi xususiy nashr ChatGPT kirishi orqali hisobdagi natija va qaydlarni saqlaydi. Google/Apple/Telegram kirishi hali ulanmagan va interfeysda shunday belgilangan. Ommaviy ishga tushirishdan oldin autentifikatsiya va admin vakolati alohida sozlanadi.
- OpenAI uchun server adapteri tayyor: kontekstli Responses so‘rovi, tuzilgan javob, kesh, foydalanish chegarasi va obuna tekshiruvi. OpenAI plagini foydalanuvchi tomonidan allaqachon ulangan. Sayt uchun API kaliti/model hali sozlanmagan, jonli AI ishlayapti deb ko‘rsatilmaydi. AI test yaratish/tahrir jarayoni keyingi bosqich.
- Mobilga mos CSS va veb manifest bor; APK va iOS nashrlari hali qurilmagan.

Tekshiruv: TypeScript, ishlab chiqarish buildi, o‘qish/mashq domen tekshiruvlari va API → ma’lumotlar bazasi → qayta yuklash sinovlari o‘tdi. Foydalanuvchi/vahda chegaralari, takror so‘rov, yordamli javob, qayd 409 to‘qnashuvi, admin, yuklash/fayl turi, R2 range va AI ruxsatlari tekshirildi. Desktop brauzerda kitob ochish, so‘z tarjimasi va tahlil qulfi ko‘rildi; keyin brauzer infratuzilmasi javob bermay qoldi. Mobil vizual sinov va pointer bilan yozishni tekshirish yakunlanmagan.

Texnik qayd: yangi nashr uchun yagona vahda IDlari ishlatiladi. Hisoblar va obunalarni Google/Apple/Telegram orqali birlashtirish, asl QR audioni ajratish, har bir PDF sahifasidagi so‘zlarni tayyorlash va tahlillarni tahrirchi tekshiruvi keyingi ishlar.

## Asosiy yo‘nalish va brend
- Auditoriya: arab tilini o‘rganayotgan o‘quvchilar. Interfeys va tushuntirishlar o‘zbekcha.
- Arabiyat nomi, yashil fondagi ochiq kitob belgisi va arabiyat. yozuvi saqlanadi.
- Dizayn namunalari: https://almanhajalalami.com/ar/books/adults-a2-student-book/units hamda https://mastermockai.uz va foydalanuvchi yuborgan kutubxona/kitob/shaxsiy kabinet skrinshotlari. MasterMock kabineti skrinshot orqali ko‘rilgan; uning ichki o‘yinlari tekshirildi deb da’vo qilinmaydi.
- Zamonaviy muqova kartalari, glass uslubi, kitob ochilishi va bo‘lim almashish animatsiyalari. O‘qiladigan matn fonini tiniq saqlash, animatsiyani kamaytirish va qurilmaga mos ishlash taklif qilinadi.

## Foydalanuvchi belgilagan katalog
Bosh sahifada ikki asosiy to‘plam kartasi:
1. Manhajul ‘Alamiy. Bosilganda A0, A1, A2, B1, B2, C1, C2 darajalari, so‘ng kitob, vahda va sahifa ochiladi.
2. At-Tanal. Bosilganda shu kitobga maxsus bo‘lim ochiladi.
Kitob PDFlarini foydalanuvchi keyinchalik taqdim etadi. Hali yuklanmagan kitoblarni tayyor kontent sifatida ko‘rsatmaslik.

Har bir Manhaj kitobida: kitob, vahda lug‘atlari, muhadasa iboralari, mashqlar va natijalar. Iboralar lug‘atlar yonida turadi; iboralar tegishli kitobning muhadasa bo‘limidan olinadi.

## 7 kunlik sinov va obuna
Foydalanuvchi belgilagan:
- Saytda «7 kun bepul» yozuvi va bepul sinov bo‘ladi.
- Sinovda kitob o‘qish mumkin.
- Audio tinglash va so‘z ustiga bosilganda tarjimasini ko‘rish doimiy BEPUL: 7 kun tugagach ham bu ikkala imkoniyat ochiq qoladi. Bu foydalanuvchining tasdiqlangan qarori.
- Kitobni o‘qishning 7 kundan keyingi bepul yoki obunali holati hali aniqlashtirilmagan.
- Manhaj sarfiy va nahviy tahlillari qulf bilan ko‘rinadi, bosilganda obuna taklifi ochiladi.
- Narxlar keyin belgilanadi; hozir narx yoki to‘lov shartlarini o‘ylab topmaslik.
Hali kelishilmagan: 7 kundan keyin kitobni o‘qish holati; sinov qachon boshlanadi; qaydlar, lug‘at o‘yinlari va At-Tanal qoida izohlarining tarifdagi o‘rni; obuna muddati va to‘lov usuli.
Taklif: to‘lovsiz va kartasiz sinov; qolgan kunlarni aniq ko‘rsatish, ruxsatlarni serverda tekshirish.

## Kitob o‘qish: yangi talab oldingi ikki rejim taklifini almashtiradi
- Bitta asosiy kitob ko‘rinishi bo‘ladi. Alohida matn o‘qish rejimi talab qilinmaydi.
- Oddiy holatda bosish so‘z tarjimasi yoki tanlangan gap yordamiga xizmat qiladi.
- Qalam tugmasi bosilganda shu oynada yozish vositalari ochiladi; kitob ustiga erkin yozish va tarjima qaydlarini qo‘shish mumkin.
- Kitobning tashqarisidagi yon bo‘shliqlarga ham yozish mumkin.
- Qaydlar saqlanishi va qaytib kirilganda tiklanishi kerak.
Takliflar: qalam, marker, o‘chirg‘ich, klaviatura bilan matn, belgilangan yozuvni ko‘chirish, bekor qilish/qaytarish; yon qayd maydonini kengaytirish; telefon ekranida shu sahifaga bog‘langan qayd maydonini ochish. Bu alohida kitob o‘qish rejimi emas.
- Yozish va so‘z tanlash bosishlari to‘qnashmasligi kerak. Kattalashtirishda qayd so‘zdan siljimasin.
- Har bir foydalanuvchining qaydlari o‘ziga tegishli. Avtomatik saqlash, saqlanganlik belgisi va qurilmalararo tiklash taklif qilinadi.
- Qurilmada qoralama nusxa va qayta saqlash tugmasi bor. Tarmoq qaytganini avtomatik kuzatib sinxronlash va to‘qnashgan ikki nusxani birlashtirish keyingi bosqich; to‘liq offline rejim tayyor deb ko‘rsatilmaydi.

## Manhajdagi so‘z va gap yordami
- So‘z bosilganda shu gapdagi ma’nosi chiqadi. Gapni qulay tanlash va tarjimasini ochish imkoniyati bo‘ladi.
- Tegishli ruxsatli foydalanuvchi sarfiy va nahviy tahlilni alohida tugmalar bilan ochadi.
- Sarf: so‘z turi, ildiz, vazn, kerakli shakllar. Fe’l uchun moziy, muzori’, amr, masdar harakatlari bilan. Mavjud bo‘lmagan shakllar yasalmaydi va sababi izohlanadi.
- Nahv: so‘zning aynan ushbu gapdagi vazifasi, i’robi, belgisi va sababini tushuntirish.
- Arabcha matn alohida RTL blokda; o‘zbekcha va lotin yozuvli tushuntirishlar alohida bloklarda.
- Taklif: tinglash, shaxsiy lug‘atga saqlash va asl sahifaga qaytish.

## At-Tanalning alohida talabi
- So‘z ustiga bosilganda tarjima chiqadi.
- Manhajdagi kabi avtomatik sarf/nahv tahlil tugmalari kerak emas.
- Qoidaning aynan o‘sha joydagi ma’nosi, tushuntirishi va misollari beriladi. Qoida yordamining aniq tarkibi keyingi muhokamada belgilanadi.
- At-Tanal qoida izohlari sinovda ochiqmi yoki obunadami — hali kelishilmagan.

## Audio
- Sahifada QR yonida uning original audiosini tinglash tugmasi.
- Har bir sahifa va vahda to‘g‘ri audio bilan bog‘lanadi. QR bo‘lmagan sahifaga o‘zboshimchalik bilan audio yaratilmaydi.
- Taklif: tezlikni boshqarish, parcha/jumla takrori, jumlaga vaqt belgilari orqali audio bilan birga yoritish.
- Original yozuv va sun’iy talaffuz bir xil sifatida ko‘rsatilmaydi.

## Lug‘at va iboralarni yodlash
Talab: har bir kitob/vahdaga bog‘langan lug‘at, takrorlash va 5–6 xil mashq/o‘yin; muhadasa iboralari uchun qo‘llash mashqlari.
Taklif qilingan oltita mashq:
1. Arabcha-o‘zbekcha juftini topish.
2. Tarjimadan arabcha so‘zni xotiradan yozish.
3. Audio eshitib yozish.
4. Gapdagi bo‘sh joyni to‘ldirish.
5. So‘zlardan gap yig‘ish.
6. Fe’l shakllarini tanish va o‘zgartirish.
Iboralar: vaziyat, ma’no, audio, misol; dialog rolini bajarish, yashirilgan javobni tiklash, shaxs/vaqt/joyni almashtirish, ovozni yozib original bilan solishtirish takliflari.
- Savollar bittadan. Xato javobda sabab, har bir noto‘g‘ri variantning ma’nosi va unga mos to‘g‘ri gap beriladi; o‘xshash misol bilan mustahkamlanadi.
- Takrorlash jadvali foydalanuvchining haqiqiy natijalariga bog‘lanadi. Tanib olish, yozish, tinglab tushunish va gapda ishlatish natijalarini ajratish taklif qilingan.
- Kunlik progress, javoblar tarixi, shaxsiy xatolar daftari, qolgan joydan davom etish va kitoblararo qidirish takliflari mavjud.


## Hisobga kirish va obunani saqlash — foydalanuvchi talabi
- Google orqali (Gmail Google hisobining elektron pochtasi), Apple orqali (iCloud hisobiga tegishli Apple Account) va Telegram orqali kirish imkoniyatlari kerak.
- Qo‘shimcha elektron pochtaga tasdiqlash kodi bilan kirish yordamchi taklif; hali tasdiqlanmagan.
- Obuna, qaydlar, shaxsiy lug‘at va barcha natijalar bitta ichki Arabiyat foydalanuvchi hisobiga bog‘lanadi; veb/Android/iOS bir xil hisob ma’lumotidan foydalanadi.
- «Hisoblarni bog‘lash» taklifi: o‘quvchi allaqachon kirgan hisobiga boshqa kirish usulini ham tasdiqlab ulashi mumkin. Google/Apple/Telegram orqali kirganlarni email yoki ism bir xilligi sabab avtomatik birlashtirmaslik.
- Faqat email manziliga emas, provayder tasdiqlagan barqaror identifikatorga tayanish; obuna huquqini serverda saqlash va tekshirish taklifi.
- Google/Apple/Telegram xizmatlarini ro‘yxatdan o‘tkazish, sozlash va sinash hali bajarilmagan. Hozirgi shaxsiy Sites paneli ChatGPT kirishidan foydalanadi. Yangi ommaviy platformada tashqi kirish usullarini qo‘llash uchun hosting va autentifikatsiya arxitekturasi mosligi qurishdan oldin tekshiriladi; mavjud Sites imkoniyatlari dalilsiz va’da qilinmaydi.

## So‘z o‘yinlari: kitob va vahda doirasi — foydalanuvchi talabi
- O‘quvchi So‘z o‘yinlari → to‘plam (Manhaj yoki At-Tanal) → daraja/kitob → vahda yoki butun kitob → mashq usulini tanlaydi.
- Mashqda faqat tanlangan kitob va tanlangan vahda(lar) so‘zlari ishlatiladi; boshqa kitoblardagi so‘zlar o‘z-o‘zidan qo‘shilmaydi.
- «Butun kitob», «Bitta vahda», «Bir nechta vahda», «Bilmaganlarim», «Bugungi takror» filtrlari taklifi; tanlangan doira mashq davomida ko‘rinib turadi.
- Alohida yozma mashq majburiy: javobni variant tanlash bilan emas, klaviaturada yozish.
- Taklif: o‘zbekchadan arabchaga yozish, arabchadan o‘zbekchaga yozish, audiodan arabcha yozish; ekrandagi arabcha klaviatura va harakat tugmalari.
- Taklif: imlo va harakat xatolarini alohida ajratish; harakatlarni talab qilishni mashq maqsadiga mos sozlash; hamza yoki boshqa ma’no farqlovchi harflarni o‘zboshimchalik bilan tenglashtirmaslik; tarjimada tahrirchi tasdiqlagan muqobil javoblarni qabul qilish.
- Xatoda to‘g‘ri javob va tushuntirish, keyin qayta mustahkamlash. Xatolarni umumiy noma’lum so‘zlar to‘plamiga bog‘lash taklifi.

## So‘zlarni yodlash va Bilmaganlarim — foydalanuvchi talabi
- So‘z o‘yinlaridan alohida «So‘zlarni yodlash» bo‘limi.
- Har bir kitob va vahdani tanlash; aynan shu vahdaning so‘zlarini bittadan flashcard ko‘rinishida o‘rganish.
- Kartochka oldi: so‘z yoki tanlangan yo‘nalishga qarab tarjima; orqasi: javob, kitobdan misol va audio taklifi. Arabcha va o‘zbekcha alohida bloklarda.
- Javob o‘ylangandan keyingina kartani ochish; «Bilmadim», «Qiyin», «Bildim» tugmalari taklifi.
- Bilmagan so‘zlarni alohida saqlash va faqat ular ustida ishlash majburiy.
- Taklif: bir xil so‘z har safar yangi nusxa bo‘lib ko‘paymasin; asl kitob/vahda/sahifaga bog‘lanishi saqlansin; bir so‘zning turli ma’nolari ajratilsin.
- Taklif: xato yozilgan, eshitib topilmagan va kartochkada bilinmagan so‘zlar bir markaziy to‘plamda, xato turi bilan ko‘rinsin; takrorlash bir necha kunlik natijaga qarab rejalansin.
- Bir marta «Bildim» bosish darhol uzoq muddat o‘zlashtirilgan degani bo‘lmasin. Tanib olish va yozib eslash natijalari alohida.
- Sessiyani tugatmasdan chiqilsa, keyin qolgan kartadan davom etish taklifi.


## Kitob va vahda kartalaridagi progress — foydalanuvchi talabi
- Lug‘at testiga kirishdan oldin kitob va vahda tanlash kartalarining ostida natija va progress ko‘rinishi kerak.
- Har bir vahdada so‘zlar to‘g‘ri topilgan sari o‘zlashtirish foizi ortadi; tugatilgan vahdalar ajratib belgilanadi.
- Kitob kartasidagi umumiy foiz vahdalar ichidagi natijalar asosida yangilanadi; tugagan vahdalar soni ham ko‘rsatiladi.
- Hisoblash taklifi: vahda o‘zlashtirishi = tanlangan lug‘at birliklaridan kamida bir marta mustaqil to‘g‘ri javob berilganlari / vahdadagi jami birliklar × 100. Bir birlikni qayta-qayta topish ushbu hisobni oshirmaydi. Uzoq muddat eslab qolish/takror natijasi alohida.
- Kitob foizi jami vahdalardagi o‘zlashtirilgan birliklar / shu kitob vahdalaridagi jami birliklar asosida; vahdalar hajmi turlicha bo‘lsa, foizlarning oddiy o‘rtachasini olmaslik taklifi.
- «Javob aniqligi» boshqa o‘lchov: to‘g‘ri javoblar / hisobga olingan urinishlar × 100. Oxirgi test aniqligi va tarixdagi natijalar ajratiladi; testda hali javob bo‘lmasa chiziq ko‘rsatiladi, sun’iy 0 yoki 100 emas.
- Xato javobdan keyingi javobni ko‘rib qayta yozish birinchi mustaqil javobdan ajratib saqlanishi taklifi.
- Kartada: progress chizig‘i, o‘zlashtirilgan/jami so‘zlar, tugallangan/jami vahdalar, oxirgi test aniqligi, davom etish tugmasi.
- Natijalar har bir foydalanuvchi, kitob, nashr, vahda, lug‘at birligi va mashq usuliga bog‘lanadi. Foizlarni dastur haqiqiy javoblardan hisoblaydi; AI o‘ylab chiqarmaydi.
- Vahdalarni sahifalarga bo‘lish, ularni ochish tartibi va audio joylashtirish kitoblar taqdim etilgandan keyin haqiqiy mundarija va audio manbalarga ko‘ra bajariladi. A0 PDFi va muqovasi qabul qilinib ishlatildi; qolgan darajalar fayllari keyin taqdim etiladi.

## Tarjima va tahlil: amaldagi APIsiz yo‘nalish
- Foydalanuvchining so‘nggi qarori: kitob ma’nolari va keyingi kitoblarning gap tahlillarini oldindan tayyorlab, tayyor ma’lumotdan ochish.
- Sayt o‘quvchi so‘z bosganida yoki tayyor tahlilni ochganida OpenAIga murojaat qilmaydi. Audio original yozuvdan ijro etiladi; vaqt belgisi ham tayyor fayldan olinadi.
- Sarf va nahv alohida so‘zga hukm yasash bilan cheklanmaydi: tanlangan so‘zning to‘liq gapi uchun saqlangan izoh ochiladi. Fe’llar harakatli moziy, muzori’, amr va masdar bilan ko‘rsatiladi; mavjud bo‘lmagan shakl yasalmaydi.
- A0da sarf/nahv o‘chiq. At-Tanalda ayni qoidaning ma’nosi va izohi beriladi. Narxlar belgilanishini kutish va obuna ruxsatini serverda tekshirish qarori saqlanadi.
- Hali berilmagan kitoblar va ularning tahlillari keyin foydalanuvchi taqdim etgan asl nashr bo‘yicha tahrir qilinadi. Tayyor tahlil topilmasa jonli AI bilan to‘ldirishga urinish bo‘lmaydi.
- Oldingi OpenAI adapteri tarixiy manbada saqlangan bo‘lishi mumkin; joriy o‘qish yo‘llari undan foydalanmaydi. Kalit, token va hisob ma’lumotlari chatga yoki ko‘chirish hujjatiga joylanmaydi.

## Boshqaruv va kontent tayyorlash
- Qulay administrator paneli: kitob/PDF qo‘shish, daraja va vahda ajratish, sahifa va QR-audioni bog‘lash, lug‘at/ibora/qoida izohlarini tahrirlash.
- Suratli PDFdagi arabcha matn, harakatlar va so‘z joylarini ajratish hamda tekshirish kerak.
- Tarjima va tahlilni qoralama/tekshirilgan holatlarida boshqarish taklifi.
- O‘quvchi xatoni bildira olishi; tuzatilgan umumiy izohning bog‘langan kartochkalarda yangilanishi taklifi.

## Mobil mahsulotlar
Foydalanuvchi so‘ragan maqsadlar: veb-sayt, Android APK, iOS ilova.
Taklif: bir xil hisob va ma’lumotlar asosida ishlash; avval mobilga mos veb, keyin Android va iOS paketlari. PWA ham ko‘rib chiqiladi. Android/iOS qurilishi, imzolash, haqiqiy qurilmalarda sinov va tarqatish alohida ishlar; sayt tayyor bo‘lishi avtomatik APK yoki App Store nashri degani emas.

## Dizaynni tanlash vakolati — yangi tasdiqlangan talab
- Nom va logo o‘sha Arabiyat bo‘lib qoladi.
- Foydalanuvchi ranglar, vizual uslub va animatsiya yo‘nalishini mashhur saytlarni o‘rganib tanlashni assistentga topshirdi; palitrani qayta so‘rash shart emas.
- Linear, Readwise Reader va Duolingo dizayn materiallari qo‘shimcha o‘rganildi. Taklif: tartibli kabinet, o‘qishga qulay kitob maydoni, foydali natija animatsiyalari; Arabiyatning o‘ziga mos yagona dizayn tizimi.
- Glass effekt boshqaruvlarda; matnda yuqori o‘qilish; telefonga moslashuv va harakatni kamaytirish imkoniyati. Hech bir dizayn hammaning didiga mutlaq mos tushishi kafolatlanmaydi.
- Birinchi palitra va asosiy ekranlar qurildi: to‘q yashil kabinet, mint aksentlar va o‘qish uchun och rangli sahifa. Keyingi dizayn tuzatishlari haqiqiy qurilma va foydalanuvchi fikriga asoslanadi.

## Dizayn va yordamchi vositalar
- Glass effekt: boshqaruv panellari, menyu va dialoglarda; kitob matni ortida tiniq, o‘qishga qulay fon taklifi.
- Animatsiya: muqovadan kitobga, kitobdan vahdaga o‘tish, yordam oynalarining ochilishi; tezlik va animatsiyani kamaytirish sozlamalari.
- Figma ixtiyoriy dizayn/prototip hamkorligi uchun foydali, qurishni boshlash uchun majburiy emas.
- Foydalanuvchida Gemini, Claude va GPT bor. U tashqi vositalardan yordam berishga tayyor. Vazifa kerak bo‘lsa aniq ajratiladi; hozir topshirilgan tashqi ish yo‘q. Modellarning birini dalilsiz hamma ishda kuchli deb aytmaslik.

## Hali javobsiz qarorlar
1. Kitobni o‘qish ham 7 kundan keyin bepul qoladimi? Audio va so‘z tarjimasi doimiy bepul ekani allaqachon tasdiqlangan.
2. Sinovda qaydlar, lug‘at o‘yinlari va At-Tanal qoida izohlari ochiqmi?
3. Mustaqil o‘quvchilar bilan birga ustoz guruhlari, vazifa va o‘quvchi natijalarini ko‘rish boshidanoq kerakmi?
4. Narxlar, obuna muddatlari va to‘lov usullari.
5. A0dan boshqa kitoblarning PDFlari, audio manbalari va nashr versiyalari. A0ning taqdim etilgan asl nusxasi va QR audiolari kiritildi.

## Keyingi ishlab chiqish bosqichlari
Avval A0 topshiriqlarini haqiqiy telefon/stilusda ko‘rib tekshirish va qolgan matn/kalitlarni tahrir qilish; foydalanuvchi bilan so‘z yodlashning yangi usulini kelishish. Keyin boshqa daraja yoki At-Tanal PDFi berilganda haqiqiy sahifa/vahda/lug‘atni tayyorlash; oldindan tayyorlangan izohlar va tashqi kirish usullarini yakunlash; keyin qolgan darajalar va mobil paketlar. Narxlar foydalanuvchi belgilaguncha to‘lov xizmati yoqilmaydi.

## O‘rganilgan namunalar
- Manhaj katalogi: https://almanhajalalami.com/ar/books/adults-a2-student-book/units
- Readlang: https://readlang.com/features
- LingQ: https://www.lingq.com/en/ios-app-support/
- Anki: https://docs.ankiweb.net/manual/background
- Quizlet: https://help.quizlet.com/hc/en-us/articles/360030986971-Studying-with-Learn
- LiquidText yon ish maydoni: https://www.liquidtext.net/features
- Goodnotes yozuvni tanlash: https://support.goodnotes.com/hc/en-us/articles/7353695644175-Select-Move-and-Edit-Content-With-the-Lasso-Tool
- Capacitor: https://capacitorjs.com/docs
- Figma animatsiyalari: https://help.figma.com/hc/en-us/articles/360040522373-Prototype-animations
Qo‘shimcha rasmiy manbalar: https://developers.google.com/identity/gsi/web/guides/display-button ; https://core.telegram.org/bots/telegram-login ; https://developer.apple.com/help/account/capabilities/configure-sign-in-with-apple-for-the-web ; https://docs.ankiweb.net/manual/studying
Qo‘shimcha dizayn manbalari: https://linear.app ; https://readwise.io/read ; https://blog.duolingo.com/core-tabs-redesign/
