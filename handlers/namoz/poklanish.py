from keyboard_buttons import admin_keyboard
from aiogram import  F
from aiogram.types import Message,CallbackQuery
from loader import dp

# Tahorat haqida ma'lumot berish
@dp.message(F.text == "TAHORAT")
async def massaeg(messaga: Message):
    await messaga.answer("""TAHORAT """,reply_markup=admin_keyboard.ruza_buttan)


# Tahorat haqida batafsil ma'lumot berish (callback query)
@dp.callback_query(F.data == 'erkaklar_tahorat')
async def erkaklar_tahorat(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Tahorat uchun suv hozirlagandan keyin:
1. Qibla tomonga qarab, ichida „Tahorat olishni niyat qildim“ deyiladi.
2. Auzu billahi minash-shaytonir rojiym. Bismillahir rohmanir rohiym“, deyiladi.
3. Qoʻllar bandigacha 3 marta yuviladi.
4. Oʻng qoʻlda suv olinib, ogʻiz 3 marta gʻargʻara qilib chayiladi va misvok qilinadi.
5. Burunga oʻng qoʻl bilan 3 marta suv tortilib, chap qoʻl bilan qoqib tozalanadi.
6. Yuz 3 marta yuviladi.
7. Avval oʻng qoʻl tirsaklar bilan qoʻshib ishqalab yuviladi, soʻngra chap qoʻl.
8. Hovuchga suv olib, toʻkib tashlab, hoʻli bilan boshning hamma qismiga masx tortiladi.
9. Koʻrsatkich barmoq bilan quloqlarning ichi, bosh barmoqlar bilan esa quloq orqasi masx qilinadi.
10. Ikkala kaftning orqasi bilan boʻyin masx qilinadi.
11. Chap qoʻl bilan oʻng oyoqni oshiq qismi bilan qoʻshib, barmoqlar orasini ishqalab 3 marta yuviladi, keyin chap oyoq.
12. Qibla tomonga qarab, ichida „Ashhadu an La ilaha illallohu va ashhadu anna Muhammadan abduhu va rosuluh“ deyiladi. 
                       
<a href= 'https://t.me/mukammal_namoz/51'>Bizning kanal📢</a>
""", reply_markup=admin_keyboard.tahorat_orqa_button)

@dp.callback_query(F.data == 'ayollr_tahorat')
async def ayollr_tahorat(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""Tahorat ayollar uchun <a href = 'https://t.me/mukammal_namoz/52'>Bizning kanal📢</a>   """,reply_markup=admin_keyboard.tahorat_orqa_button)

@dp.callback_query(F.data == 'tahorat_button_orqga')
async def tahorat_button_orqga(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""TAHORAT""",reply_markup=admin_keyboard.ruza_buttan)


# Tahorat haqida batafsil ma'lumot berish (callback query)
@dp.callback_query(F.data == 'tarif')
async def valyuta_back(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Tahorat — namoz oʻqish, ibodat oldidan yuvinish, poklanish jarayoni. Xususiy shakli sifatida tayammum koʻriladi. Islomda tahoratning ikki turi mavjud: vuzuʼ — kichik tahorat — qoʻloyoq va yuzni yuvish; gʻusul — katta tahorat — toʻla yuvinish, choʻmilish.

Tahoratning 4 ta farzi bor:
- Yuzni yuvmoq;
- Ikki qoʻlni tirsak ila qoʻshib yuvmoq;
- Ikki oyoqni toʻpigʻi ila qoʻshib yuvmoq;
- Boshning toʻrtdan bir qismiga mas'h tortish.

Bu farzlardan birortasi bajarilmasa, tahorat haqiqiy boʻlmaydi.

""", reply_markup=admin_keyboard.Admin)


# G'usl haqida ma'lumot
@dp.message(F.text == "G'USL")
async def massaeg(messaga: Message):
   
    await messaga.answer(
        text="""
GʻUSLNING FARZLARI[2]
Bas, gʻuslning farzi ogʻzini, burnini va butun badanini yuvmoqdir. 
Bu jumladan gʻuslning farzi uchta ekani anglab olinadi:
1. Ogʻizni chayqash.
Albatta, ogʻizni yaxshilab chayqash gʻuslning f arzlaridan biri ekani hammaga maʼlum. 
Busiz gʻusl boʻlishi mumkin emas.
2. Burunni chayqash.
Burunni yaxshilab, mubolagʻa ila chayish ham gʻuslning farzi hisoblanadi.
3. Badanning barcha yerini yuvish.
Butun tanani, biror tuki ostini ham qoʻymay, suv yetkazib yuvish ham gʻuslning farzidir. 
Gʻuslning farzligi „Moida“ surasidagi: „Agar j unub boʻlsalaringiz, poklaninglar“ (6-oyat) oyatidan olingan. 
Bunda yuvish imkoni bor barcha joyni poklash maʼnosi bordir. 
Alloh taolo yana „Niso“ surasida: „Va j unub holingizda ham, to gʻusl qilmaguningizcha (masjidda turmang). 
Magar yoʻldan oʻtuvchi boʻlsa, mayli“, degan (43-oyat). 
Ushbu ikki oyatda ogʻiz, burun va badanning barchasini yuvish maʼnosi bor. 
Abu Hurayra roziyalloxu anhudan rivoyat qilinadi

<a href='https://t.me/mukammal_namoz/53'>Bizning kanal</a>

""", 
        reply_markup=admin_keyboard.Admin
    )
    await messaga.delete()

