# Ko‘chirish holati

Repository manba va tayyor editorial kontentni saqlaydi. GitHubga kod joylash mavjud Sites URLi yoki omborlariga egalikni ko‘chirmaydi. Hozirgi ishlab turgan nashr saqlangan.

OriginalPDF va82MP3 uchun media/TRANSFER_STATUS.json ni tekshiring. Har bir original faylning kaliti, o‘lchami vaSHA256 lib/a0/assets.json da. Ko‘chiriladigan fayllar hash bilan tekshirilsin. Qaydlar, o‘quvchi natijalari, shaxsiy lug‘at va obunalar public GitHubga chiqarilmaydi; ular alohida vakolatli eksport/import talab qiladi.

CloudflareWorker/D1/R2 muhitiga DB vaBUCKET bindinglari hamda drizzle/ migratsiyalari kerak. TashqiRailway/Vercelga ayni kodni ko‘r-ko‘rona yuklash yetmaydi: ma’lumotlar bazasi/fayl adapterlari va autentifikatsiya moslashtiriladi. Sites tomonidan tekshiriladigan oai-authenticated-user-* headerlariga oddiy internet mijozidan ishonmang. Server tekshiradigan haqiqiy sessiya va egalik nazorati kerak.

OPENAI_API_KEY runtime’da kerak emas. Eski adapter foydalanilmaydi. Maxfiy kalitlar, .env, tokenlar va cookie repositoryga kiritilmaydi. OWNER_PRIVATE_PREVIEW faqat platforma himoyalagan egasiga xususiy sinov uchun bo‘lgan; tashqi yoki ommaviy hostingda u bilan admin ruxsati ochilmasin. Eski foydalanuvchiIDlari yangiSite/OAuth hisobIDlari bilan avtomatik tenglashtirilmasin.

BoshqaChatGPT hisobida shu repositoryga vakolatli GitHub ulanishi kerak. To‘liq nashr qilish uchun hostingga ham vakolat talab qilinadi. Ruxsatlar va yangi nashr ishlashi tekshirilmaguncha ko‘chirish tugadi deyilmasin.
