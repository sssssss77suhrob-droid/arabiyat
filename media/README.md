# Asl A0 kitobi va 82 audio

Bu repositoryda original PDFning barcha baytlari va82ta originalMP3 bor. Har bir fayl eski nashrdagi SHA-256 bilan solishtirilgan. PDF kattaligi sabab media/pdf/ ichida14qismga ajratilgan; qismlarni quyidagi buyruq asl57MBPDFga aynan tiklaydi. MP3lar media/audio/ ichida to‘liq fayl sifatida turadi. Arabcha asl nomlar va R2kalitlari original-manifest.json da.

```sh
python scripts/restore-original-media.py
```

Natija media/restored/ ichida1PDF,82MP3 va index.json bo‘ladi. Tiklash internet yoki API ishlatmaydi; qismlar va har bir to‘liq original hashini tekshiradi. YangiChatGPT shu buyruqni ishlatib kitob va audiolarni oladi. index.json mahalliy yo‘lni originalR2kalitiga bog‘laydi; yangi omborga import qilganda kalitlar o‘zgarmasin. Ovozlarning vaqt/so‘z xaritasi lib/a0/audio-timings.json da.

EskiSite’ning shaxsiy D1natijalari va kalitlari bu ommaviy paketda yo‘q. Manba borligi eski saytga tahrirlash huquqini bermaydi; yangi hosting va hisob ruxsatlari alohida sozlanadi.
