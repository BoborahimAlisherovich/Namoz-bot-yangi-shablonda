from keyboard_buttons import admin_keyboard
from aiogram import  F
from aiogram.types import Message,CallbackQuery
from loader import dp

#makka online 
@dp.message(F.text == "MAKKA ONLINE")
async def message(messaga:Message):
    await messaga.answer("Makka Onlayn kuzatish",reply_markup=admin_keyboard.makka) 


#IBODATI ISLOMIYA  haqida ma'lumot
@dp.message(F.text == "IBODATI ISLOMIYA")
async def massaeg(messaga: Message):
    await messaga.answer(
        text="""
Isomning besh ustuni (أركان الإسلام; ham أركان الدين „ dinning ustunlari“) — Islomdagi asosiy amallar boʻlib, barcha musulmonlar uchun farz qilingan ibodatlar hisoblanadi. Ular Jabroil alayhissalom hadislarida jamlangan. .Sunniylar va shialar bu harakatlarning bajarilishi va amaliyotining asosiy tafsilotlari boʻyicha hamfikir, lekin shialar ularni bir xil nom bilan ifodalamaydi. Islomning 5 ustuni: shahodat, namoz, zakot, ramazon oyida ro'za tutish va qodir boʻlganlar uchun Makkaga haj qilishdir
<a href='https://t.me/c/2342502353/35'>.</a>   
""", 
        reply_markup=admin_keyboard.Admin
    )

# Bosh menyu
@dp.message(F.text == "SHAHODAT")
async def orqa(message: Message):
    await message.answer(text="""   
Ashhadu alla ilaha illohu va ashhadu anna Muhammadan 'abduhu va rasuluh

Guvohlik beramanki, Allohdan o'zga iloh yo'q va yana guvohlik beramanki, Muhammad (s.a.v) Uning bandasi va elchisidir.  
 <a href='https://t.me/mukammal_namoz/84'>.</a>                                                    
""",reply_markup=admin_keyboard.Admin)
