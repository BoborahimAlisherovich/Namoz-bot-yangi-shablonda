from keyboard_buttons import admin_keyboard
from aiogram import  F
from aiogram.types import Message,CallbackQuery
from loader import dp


#  40 farz
@dp.message(F.text == "40 FARZ")
async def namoz_vaqti(message: Message):
    await message.delete()
    
    await message.answer(
        text="""
40 farz
""",reply_markup=admin_keyboard.qiriq_farz)
    

@dp.callback_query(F.data == "besh_farz")    
async def nos_quron(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Islomda beshta farz bor:
1. Iymon;
2. Namoz;
3. Ro‘za;
4. Zakot;
5. Haj.
 """,reply_markup=admin_keyboard.bu_uchun_orqaga) 


@dp.callback_query(F.data == "yetti_farz")    
async def yetti_farz(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Iymonda yettita farz bor:
1. Allohga ishonish;
2. Allohning farishtalariga ishonish;
3. Allohning kitoblariga ishonish;
4. Allohning payg‘ambarlariga ishonish;
5. Oxirat kuniga ishonish;
6. Qadarga — yaxshilik ham, yomonlik ham Alloh taoloning irodasi bilan bo‘lishiga ishonish;
7. O‘lgandan keyin qayta tirilishga ishonish.

 """,reply_markup=admin_keyboard.bu_uchun_orqaga) 


@dp.callback_query(F.data == "tort_farz")    
async def tort_farz(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Tahoratning farzlari to‘rtta:
1. Yuzni to‘liq yuvish;
2. Qo‘llarni tirsaklari bilan qo‘shib yuvish;
3. Boshning to‘rtdan biriga mash tortish;
4. Oyoqlarni to‘pig‘i bilan qo‘shib yuvish.
 """,reply_markup=admin_keyboard.bu_uchun_orqaga) 

@dp.callback_query(F.data == "tayammum_turt_farz")    
async def tayammum_turt_farz(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Tayammumning farzlari to‘rtta:
1. Niyat;
2. Pok tuproqni qasd qilish;
3. Ikki qo‘lni toza tuproqqa urib, so‘ng yuzga surish;
4. Ikki qo‘lni tuproqqa urib, tirsak bilan qo‘shib qo‘llarga surish.
 """,reply_markup=admin_keyboard.bu_uchun_orqaga) 

@dp.callback_query(F.data == "uch_farz")    
async def uch_farz(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Gʻuslning farzlari uchta:
1. Og‘izni g‘arg‘ara qilib chayish;
2. Burunni achishtirib chayish;
3. Badanning hamma joyiga suv yetkazib yuvish.
 """,reply_markup=admin_keyboard.bu_uchun_orqaga) 
    
@dp.callback_query(F.data == "on_ikki_farz")    
async def uch_farz(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Namozning farzlari o‘n ikkita bo‘lib, oltitasi namoz tashqarisidadir, ular "namozning shartlari", deyiladi:
1. Badanning (junub, tahoratsizlik, hayz, nifosdan) pok bo‘lmog‘i;
2. Kiyimning pok bo‘lmog‘i va avratning to‘silmog‘i;
3. Namoz o‘rnining pok bo‘lmog‘i;
4. Namoz vaqtining kirmog‘i;
5. Qiblaga yuzlanib o‘qimoq;
6. Dildan (xolis) niyat qilmoq;
                                  
Oltitasi namoz ichida bo‘lib, ular "namozning ruknlari" deyiladi:
1. Namozga takbiri tahrima bilan kirish;
2. Qiyom;
3. Qiroat;
4. Ruku’;
5. Sajda;
6. Qa’dai oxir.
 """,reply_markup=admin_keyboard.bu_uchun_orqaga) 


@dp.callback_query(F.data == "amru_maruf")    
async def uch_farz(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Yaxshi amallarni o'zi bajarib, boshqalarga ham buyitish

Yomon amallardan avval o'zi saqlanib boshqalarni ham qaytarish 
 """,reply_markup=admin_keyboard.bu_uchun_orqaga) 

@dp.callback_query(F.data == "ikki_farz")    
async def uch_farz(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Ilm izlash, o'qish farz.  Inson hayoti davomida kerak bo‘ladigan halol-haromga doir ilmlarni o‘zlashtirishi farzdir.
 """,reply_markup=admin_keyboard.bu_uchun_orqaga) 

@dp.callback_query(F.data == "orqaga_uchun_farz")    
async def uch_farz(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
40 farz
 """,reply_markup=admin_keyboard.qiriq_farz) 