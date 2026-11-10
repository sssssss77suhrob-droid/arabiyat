# Arabiyat

O‘zbek tilida interaktiv arab tili o‘rganish platformasi. Bu repository mavjud Arabiyat loyihasini boshqa ChatGPT hisobida davom ettirish uchun foydalanuvchining ruxsati bilan public qilindi.

## Avval o‘qing

- [Yangi ChatGPT uchun to‘liq yo‘riqnoma](docs/CONTINUE_IN_UZBEK.md)
- [Alohida hisobda Sites bilan ishga tushirish](docs/NEW_ACCOUNT_SITES.md)
- [Hosting va ma’lumotlarni ko‘chirish](docs/MIGRATION.md)
- [To‘liq loyiha rejasi va tarix](docs/PROJECT_PLAN.md)
- [Asl kitob/audio paketlari](media/README.md)
- [Manba kelib chiqishi](source-provenance.json)

## Hozirgi haqiqiy kontent

- Asl Manhajul ‘Alamiy A0: 112 WebP sahifa va muqova; 3-sahifa bo‘sh.
- 6 715 so‘z/harf uchrashi uchun tayyor o‘zbekcha ma’no va koordinata.
- 192 mashq; dastlabki 7 sahifada vazifa yo‘q. Haqiqiy bo‘sh kataklar, so‘zni sahifadan tanlash va chiziq bilan juftlash.
- 82 original QR audio xaritasi, 1 735 bosma nishonga mos tayyor vaqt hodisasi.
- Bosib turishda kichik markaziy shaffof tarjima, bo‘yash, saqlash; nuqtali qalam va qisman artadigan o‘chirg‘ich.
- Hisobga alohida qayd/natija/lug‘at; oltita mashq usuli, flashcard va takrorlash.

**Original PDF va82MP3 to‘liq kiritilgan.** PDF qismlarini tiklash va83originalni tekshirish: `python scripts/restore-original-media.py`. Holat `media/TRANSFER_STATUS.json` da. `lib/a0/assets.json` — 83 original faylning o‘lcham/hash/kalit manifesti; manifestning o‘zi media fayllari emas. Foydalanuvchilarning D1 yozuvlari va maxfiy kalitlari public repositoryga kiritilmaydi.

## Muhim qarorlar

Pullik OpenAI API ijro vaqtida ishlatilmaydi. Tarjima, so‘z joyi, audio va tahlil tayyor ma’lumotdan ochiladi. A0da Sarf/Nahv o‘chiq; kelgusi kitoblarda butun gap uchun oldindan tayyorlangan izoh ko‘rsatiladi. Audio va so‘z tarjimasi doim bepul; narxlar hali belgilanmagan. Qolgan Manhaj A1–C2 va At-Tanalning asl fayllari keyin beriladi, ular tayyor material sifatida ko‘rsatilmasin.

## Texnika va ishga tushirish

React 19, TypeScript, Vinext/Vite, Cloudflare Worker, Drizzle/D1 va R2. Mavjud build Sites uchun tayyorlangan. `.openai/hosting.json` dagi eski loyiha IDsi bu nusxadan olib tashlangan. Yangi hisob eski Site egasi bo‘lib qolmaydi; yangi nashr uchun ruxsatli hosting va bindinglar kerak.

Joriy `package.json`/lockfile asosida dependency o‘rnating. Sites bilan ishlaganda o‘sha muhitdagi Sites yo‘riqnomasi va yordamchilaridan foydalaning. Testlar:

```sh
node node_modules/typescript/bin/tsc --noEmit
node tests/domain.test.mjs
node tests/book-work.test.mjs
node tests/eraser.test.mjs
node tests/audio-prepared.test.mjs
```

Server buildidan keyin `tests/api.test.mjs`, `tests/reader.test.mjs`, `tests/audio-api.test.mjs` ishlaydi. `scripts/a0-review/README.md` kontentni qayta tuzish tartibini tushuntiradi.

## Tekshiruv chegarasi

So‘nggi manbada TypeScript/build/domen/mashq/API sinovlari o‘tgan. Barcha audio odam tomonidan boshidan oxirigacha tinglab tasdiqlangan deyilmaydi; mobil/stilusdagi yakuniy vizual tekshiruv tugallanmagan.

Uchinchi tomon kitoblari va boshqa materiallarning huquqlari o‘z egalarida qoladi. Public repositoryga joylash ularga yangi ochiq litsenziya berilganini anglatmaydi.
