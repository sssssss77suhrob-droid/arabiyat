# Alohida ChatGPT hisobida Sites bilan davom ettirish

## Eng qisqa yo‘l

Bu repositoryni ikkinchi ChatGPT hisobida GitHub orqali oching. Avval AGENTS.md, README.md, docs/CONTINUE_IN_UZBEK.md va docs/PROJECT_PLAN.md ni o‘qing. Kod, 112 sahifa, 6715 so‘z/harf, 192 mashq, original PDF va82MP3 hammasi repositoryda. Kitob materialini yana foydalanuvchidan so‘rashdan oldin shu manbani tekshiring.

Eski Site egasi birinchi hisob bo‘lib qoladi. Ikkinchi hisob o‘ziga tegishli Sites nusxasini shu manbadan yaratishi mumkin; bu yangi URL beradi. GitHub kodini davom ettirish eski URLga avtomatik nashr huquqini bermaydi. Yangi nusxa yaratish yoki hosting ko‘chirish niyatini foydalanuvchi bilan aniqlab, joriy Sites yo‘riqnomasi bo‘yicha ishlang.

## Yangi Sites nusxasi uchun aniq tartib

1. Repo fayllarini mahalliy checkoutga tayyorlang. Public nusxadagi .openai/hosting.json DB vaBUCKET bindinglarini saqlaydi, eski project_id yo‘q. source-provenance.json dagi ID eski manbani tavsiflaydi, u yangi loyiha identifikatori emas.
2. Sites’ning joriy yaratish/ochish oqimidan foydalaning. Yangi ID qaytganda uni saqlang; bir yangi loyiha uchun qayta-qayta create chaqirmang. Saytning dastlabki auditoriyasi egasiga xususiy bo‘lsin.
3. Drizzle migratsiyalaridagi haqiqiy sxemani DBga qo‘llash va BUCKET fayl omborini tayyorlash Sites saqlash ko‘rsatmalariga muvofiq bajariladi. DB/R2 bindinglari o‘z-o‘zidan eski ombor ma’lumotlarini ko‘chirmaydi.
4. `python scripts/restore-original-media.py` ni ishga tushiring. U media/restored/ ichiga1PDF va82MP3ni aynan original hash bilan tiklaydi, index.json yaratadi. Internet yoki AI kerak emas.
5. Tiklangan83faylni index.json/lib/a0/assets.json dagi ASL content/UUID kalitlari bilan yangi BUCKETga import qiling. Mavjud app/api/admin/import/route.ts ni o‘qib, uning haqiqiy autentifikatsiya va streaming protokolidan foydalaning. Kalitni o‘zgartirsangiz kitob, QR va timing havolalarini ham izchil yangilash talab qilinadi; asl kalitni saqlash qulayroq.
6. Runtime’da OPENAI_API_KEY kerak emas. Tayyor tarjima va tahlillar ishlaydi. Yangi nashrda egasining admin huquqini sozlang; faqat egasiga yopiq sinovda OWNER_PRIVATE_PREVIEW ishlatilgan. Auditoriyani kengaytirishdan oldin uni o‘chirib, aniq admin IDsini tekshiring. Maxfiy import tokeni kerak bo‘lsa joriy Sites maxfiy sozlama oqimidan foydalaning; chatga yoki GitHubga qiymat chiqarmang.
7. Kodni tekshirib, build va API sinovlarini o‘tkazing, keyin yangi egaga tegishli Site’ga nashr qiling. Native natija muvaffaqiyatini tekshiring. Kitob, audio, so‘z tarjimasi, yozuv/saqlash va mashqlarni haqiqiy sahifalarda ko‘ring.

## Oldingi natijalar va hisoblar

Foydalanuvchilarning qayd, natija, saqlangan lug‘at va obuna yozuvlari public repositoryga kiritilmagan. Ularni ko‘chirish alohida vakolatli, yopiq eksport/import ishidir. Eski va yangi Site foydalanuvchi IDsini teng deb taxmin qilmang. Hisobda ma’lumot yo‘q bo‘lsa, bu kitob yoki loyiha kodi yo‘q degani emas.

## Tashqi hosting varianti

Railway/Vercel yoki boshqa muhitga o‘tilsa CloudflareD1/R2 adapterlari va Sites’ga bog‘liq kirish tizimi moslashtiriladi. Oddiy mijoz yuborgan oai-authenticated-user-* headerlariga ishonilmaydi. Shu sabab joriy kodni bunday hostingda o‘zgarishsiz ishlaydi deb va’da bermang.
