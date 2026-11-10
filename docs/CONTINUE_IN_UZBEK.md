# Yangi ChatGPT uchun Arabiyat konteksti

## Vazifa

Foydalanuvchi boshqa alohida ChatGPT hisobida shu loyihani davom ettirmoqchi. Kod va tayyor kontentni shu repositorydan oling. O‘qishdan oldin yana barcha talablarni qayta so‘ramang. Foydalanuvchi keyingi kitobni bersa, shu tizimga qo‘shing.

## Mahsulot va dizayn

Nom va logo — Arabiyat. Auditoriya — arab tilini o‘rganayotgan o‘zbek o‘quvchilar. Kutubxonada ikkita asosiy to‘plam: Manhajul ‘Alamiy (A0, A1, A2, B1, B2, C1, C2) va At-Tanal. Kitob→vahda→sahifa. Faqat haqiqatda berilgan fayl tayyor deb ko‘rsatilsin. Hozir asl A0 bor; boshqa kitoblar hali to‘liq kiritilmagan. Glass uslubidagi ixcham boshqaruvlar va yengil animatsiyalar, o‘qishga qulay sahifa; reduced-motion saqlansin.

## Kitob oynasi

Kitob birdan ekran bo‘ylab ochiladi; katta ustki/pastki panellar uni berkitmaydi. Bir bosish boshqaruvlarni ochadi, so‘zni taxminan500ms bosib turish tarjimani ochadi. Tarjima kichik, shaffof, ko‘rinib turgan kitob markazida. Play yo‘q. Bo‘yash o‘sha so‘zni bo‘yaydi, Saqlash uni Mening lug‘atim→Saqlanganlarga qo‘shadi. Har bir bosma so‘z/harf alohida joy xaritasiga ega bo‘lsin; harakatlarga e’tibor bering.

Qalam yoqilganda ayni sahifa va yon bo‘shliqlarga yozish mumkin. Nuqta kursor, qalam, marker, qisman artadigan o‘chirg‘ich, matn, ko‘chirish, undo/redo mavjud. Qaydlar hisobga saqlanadi, mahalliy qoralama bor; to‘liq offline sinxronlash tayyor deyilmasin. Mobil fon aylanishi qulflanadi. Varaq surish va sahifa tugmalari saqlansin.

## Audio

QR yonidagi tugma aynan original audioni ijro etadi. Audio va so‘z tarjimasi doim bepul. Tayyor vaqt belgisi o‘qilayotgan so‘z ostida uning uzunligicha, o‘ngdan chapga, shu so‘z aytilish vaqti davomida chiziq chizadi. Sun’iy teng vaqt bo‘lib qo‘yish yo‘q. Bosmada bo‘lmagan yoki noaniq nutqqa boshqa so‘z nishoni o‘ylab topilmaydi. API transkripsiyasi yoqilmasin.

## Tarjima va sarf/nahv

API ishlatilmaydi: barcha tayyor ma’no va tahlillar oldindan kiritiladi. A0da Sarf/Nahv va Ko‘proq o‘chiq. Keyingi Manhaj kitoblarida bitta so‘z ma’nosi va uning BUTUN haqiqiy gapi uchun sarf/nahv alohida beriladi: gap tarjimasi, har bir bo‘lak turi/vazifasi/i’robi/belgisi/sababi, bog‘lanishlar, kerakli yashirin olmosh/foil, sodda to‘liq tushuntirish, o‘xshash harakatli misol. Barcha fe’llar to‘rt shaklda. Tayyor izoh topilmasa aniq xabar; jonli AI bilan uydirilmasin.

At-Tanal uchun umumiy sarf/nahv menyusi kerak emas: aynan o‘sha qoida joyidagi ma’no, tushuntirish va misollar beriladi. Qoidalar bo‘limlari: sarf-nahv, af’ol-xamsa, ism foil/maf’ul, majhul, raf/nasb/jarr/jazm, lam/lan/la/laysa/hatta/li, ismiy va fe’liy jumlalar.

## Asl mashqlar

192 faoliyat; muqova va dastlabki7sahifada vazifa yo‘q. Har bir vazifani kitob rasmining o‘ziga qarab moslang: rasm osti/yoniga qo‘yish, harfni to‘ldirish, tartiblash, chiziq bilan ulash, yozish, tinglash va suhbat. Tashqi bank panelidan emas, sahifaning o‘zidan bo‘lak tanlash/sudrash. Rasm ustini javob bloki bilan yopmang. Oldindan matni to‘liq dialogga soxta bo‘shliq qo‘shmang. Tekshirilmagan audio kalitini taxmin qilmang. Qalamda/erkin bajarish o‘zini tekshirish, mustaqil lug‘at aniqligini oshirmaydi.

## Lug‘at, iboralar va progress

Har bir kitob va vahdaga bog‘langan lug‘at, flashcard, Bilmaganlarim, yozma javob va oltita mashq usuli bor. Javobni klaviaturada yozish alohida imkoniyat. O‘yin tanlanganda kitob va vahda tanlanadi, faqat o‘sha doiradan so‘raladi. Savollar bittadan. Xatoda sabab, noto‘g‘ri variantning ma’nosi, u ishlatilsa gap qanday o‘zgarishi va o‘xshash misol bilan qayta o‘rgatish kerak. Arabcha to‘liq harakatli va alohida blokda.

Muhadasa iboralari lug‘atlar yonidagi alohida bo‘limda: misol, yodlash va qo‘llash. Kundalik progress, natijalar tarixi, xatolar, takrorlash jadvali, kitob/vahda tugallanishi va aniqligi haqiqiy javoblardan hisoblanadi. Bir so‘zni ko‘p marta topish umumiy o‘zlashtirish foizini sun’iy oshirmaydi. Lug‘at aniqligi va kitob topshirig‘i progressi alohida. So‘z yodlashning keyingi yangi ko‘rinishi foydalanuvchi bilan keyin kelishiladi.

## Hisob va obuna

7kun bepul yozuvi va sinov bor; audio va so‘z tarjimasi sinovdan keyin ham bepul. Narxlar va to‘lov xizmati belgilanmagan, o‘ylab topmang. Kengaytirilgan tayyor tahlil ruxsati serverda tekshiriladi. Google/Apple/Telegram kirishi mahsulot talabi, hozir ulanmagan; mavjud Sites nashri ChatGPT identitysiga tayanadi. Bitta ichki hisobda obuna/qayd/natija saqlanishi kerak. AndroidAPK/iOS kelgusi bosqich, hali tayyor emas.

## Original fayllar ham bor

`python scripts/restore-original-media.py` buyrug‘i1PDF va82MP3ni media/restored/ ga tiklaydi. PDF14qismdan aynan originalSHA256 bilan hosil qilinadi. media/original-manifest.json asl nomlar, kalitlar va hashlarni saqlaydi. index.json omborga import uchun mahalliy yo‘lni beradi. Kitob yoki audio haqida bilmayman demasdan shu fayllarni va lib/a0/ xaritalarini tekshiring. To‘liq tarixiy loyiha rejasi docs/PROJECT_PLAN.md da.

## Kod yo‘l xaritasi

- app/components/reader.tsx, audio-word-marker.tsx, word-panel.tsx — o‘qish va yordam.
- app/components/book-activities.tsx, lib/book-work.ts — sahifa ichidagi mashq va baholash.
- lib/a0/book.json — haqiqiy14bo‘lim(13vahda+muqaddima),112sahifa,QR xaritasi.
- lib/a0/worksheets.json — 6715 so‘z/harf va192mashq.
- lib/a0/audio-timings.json — 82audio uchun tayyor intervallar/joylar.
- lib/prepared-content.ts, lib/content-schema.ts — kelgusi kitoblar tayyor gap izohi formati.
- app/api/word-at, analyze, book-page, audio-timing — tayyor ma’lumot, pullik AI yo‘q.
- app/api/learning, notes, book-work — hisobga alohida saqlash, scope va409to‘qnashuv.
- scripts/a0-review/README.md — kontentni qayta tuzish.
- drizzle/ — D1 sxemasi/migratsiyalar; original media R2da.

## Tekshiruv va qolgan ishlar

So‘nggi manbada TypeScript/build/domain/mashq/o‘chirg‘ich/API testlari o‘tgan;6715nishon markazi va111matnli sahifa so‘z olish yo‘li tekshirilgan.82audio vaqt yo‘li AI kalitisiz va tarmoq o‘chirilgan testda ishlagan. Barcha yozuvlar odam tomonidan to‘liq tinglab tasdiqlangan emas. Mobil/stilusning yakuniy vizual sinovi, haqiqiy tashqi OAuth, to‘lovlar, to‘liq offline va mobil paketlar qolgan. Foydalanuvchi yangi kitob taqdim etsa avval asl mundarija/sahifa/audio/mashqlarni tekshirib, keyin har bir so‘z va gapni shu tuzilishga moslang.
