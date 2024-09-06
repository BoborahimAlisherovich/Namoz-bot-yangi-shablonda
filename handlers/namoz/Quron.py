
from aiogram.types import CallbackQuery,Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loader import dp
from keyboard_buttons import admin_keyboard
from aiogram import F

ITEMS_PER_PAGE = 20

def get_paginated_keyboard(page=0):
    start = page * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    surah_page = admin_keyboard.SURAH_NAMES[start:end]

    keyboard_builder = InlineKeyboardBuilder()
    
    for name, callback_data in surah_page:
        keyboard_builder.button(text=name, callback_data=callback_data)
    
    keyboard_builder.adjust(2)  # Adjust buttons in rows of 2

    # Add Previous and Next buttons in a new row
    pagination_buttons = []
    if page > 0:
        pagination_buttons.append(("⬅️ Oldinga", f"page_{page-1}"))
    if end < len(admin_keyboard.SURAH_NAMES):
        pagination_buttons.append(("➡️ Keyingi", f"page_{page+1}"))
    
    # If there are pagination buttons, add them in a new row
    if pagination_buttons:
        for text, callback_data in pagination_buttons:
            keyboard_builder.button(text=text, callback_data=callback_data)
        keyboard_builder.adjust(2)  # Ensure pagination buttons are in a new row

    return keyboard_builder.as_markup()

@dp.message(F.text == "QURON")
async def show_surah_list(message: Message):
    keyboard = get_paginated_keyboard(page=0)
    print("salom")
    await message.answer("Tanlang:", reply_markup=keyboard)

@dp.callback_query(F.data.startswith("page_"))
async def paginate_callback(query: CallbackQuery):
    page = int(query.data.split("_")[1])
    keyboard = get_paginated_keyboard(page)
    await query.message.edit_reply_markup(reply_markup=keyboard)

@dp.callback_query(F.data == "orqaga_qaytamiz")
async def qaytar_handler(callback: CallbackQuery):
    await callback.message.answer(text="Menyulardan birini tanlang", reply_markup=get_paginated_keyboard(page=0))
    await callback.message.delete()

#fotiha surasi
@dp.callback_query(F.data == "fotiha_quron")
async def fotiha(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Makkiy, 7 oyatdan iborat
<a href='https://t.me/mukammal_namoz/3'>Bizning kanal📢</a> """,
   reply_markup=admin_keyboard.orqaga_qayt,
        parse_mode="HTML"
    )
    
#baqara
@dp.callback_query(F.data == "baqara")
async def baqar(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=""" 
 Makkiy, 286 oyatdan iborat                                  
<a href='https://t.me/namoz_uqishni_urganish_Kanal/77'>Bizning kanal📢</a>  """,
 parse_mode="html", 
reply_markup=admin_keyboard.orqaga_qayt
) 

#Oli Imron 
@dp.callback_query(F.data == "oli_imron")
async def oli_imron(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
 Makkiy, 200 oyatdan iborat 
    <a href='https://t.me/namoz_uqishni_urganish_Kanal/78'>Bizning kanal📢</a>  """,
 parse_mode="html",  # To'g'ri joylash
reply_markup=admin_keyboard.orqaga_qayt
) 

#niso
@dp.callback_query(F.data == "niso")
async def niso(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 200 oyatdan iborat 
<a href='https://t.me/namoz_uqishni_urganish_Kanal/79'>Bizning kanal📢</a> """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "moida")
async def peshin(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=""" 
Makkiy, 120 oyatdan iborat 
    <a href='https://t.me/namoz_uqishni_urganish_Kanal/83'>Bizning kanal📢</a> """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "anom")
async def moida(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 165 oyatdan iborat
    <a href='https://t.me/namoz_uqishni_urganish_Kanal/84'>Bizning kanal📢</a> """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "arof")
async def arof(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 206 oyatdan iborat
    <a href='https://t.me/namoz_uqishni_urganish_Kanal/85'>Bizning kanal📢</a> """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "anfol")
async def anfol(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 75 oyatdan iborat
            <a href='https://t.me/namoz_uqishni_urganish_Kanal/86'>Bizning kanal📢</a> """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "tavba")
async def tavba(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 129 oyatdan iborat
    <a href='https://t.me/namoz_uqishni_urganish_Kanal/95'>Bizning kanal📢</a> """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "yunus")
async def yunus(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 109 oyatdan iborat
        <a href='https://t.me/namoz_uqishni_urganish_Kanal/87'>Bizning kanal📢</a> """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "hud")
async def hud(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 123 oyatdan iborat
    <a href='https://t.me/namoz_uqishni_urganish_Kanal/87'>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "yusuf")
async def hud(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 111 oyatdan iborat
    <a href='https://t.me/namoz_uqishni_urganish_Kanal/89'>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

#rod
@dp.callback_query(F.data == "rod")
async def hud(callback: CallbackQuery):
    await callback.message.delete()
    parse_mode= "html"
    await callback.message.answer(text="""    
Makkiy, 43 oyatdan iborat
    <a href='https://t.me/namoz_uqishni_urganish_Kanal/90'>Bizning kanal📢</a>
        """,
        reply_markup=admin_keyboard.orqaga_qayt
    )
#ibrohim   
@dp.callback_query(F.data == "ibrohim")
async def ibrohim(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 52 oyatdan iborat
        <a href='https://t.me/namoz_uqishni_urganish_Kanal/90'>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "hijr")
async def hijr(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 99 oyatdan iborat                                  
    <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "nahl")
async def nahl(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 128 oyatdan iborat
<a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "isro")
async def isro(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 111 oyatdan iborat
    <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "kahf")
async def kahf(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 110 oyatdan iborat
    <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "maryam")
async def maryam(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 98 oyatdan iborat
        <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "toha")
async def taho(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 135 oyatdan iborat
 <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "anbiyo")
async def anbiyo(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 112 oyatdan iborat
     <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "haj")
async def haj(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 78 oyatdan iborat
     <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "muminum")
async def muminum(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 118 oyatdan iborat
     <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "Nur")
async def Nur(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 64 oyatdan iborat
 <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "furqon")
async def furqon(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 77 oyatdan iborat
    <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "shuaro")
async def shuaro(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 227 oyatdan iborat
        <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "naml")
async def naml(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 93 oyatdan iborat
      <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "qosos")
async def qosos(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 88 oyatdan iborat
        <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "ankobut")
async def ankobut(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 69 oyatdan iborat
 <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "rum")
async def rum(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 60 oyatdan iborat
        <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "luqmon")
async def luqmon(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 34 oyatdan iborat     
           <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "sajda")
async def sajda(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 30 oyatdan iborat
    <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "ahzob")
async def ahzob(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 73 oyatdan iborat
          <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 


@dp.callback_query(F.data == "saba")
async def saba(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 54 oyatdan iborat
 <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "fotir")
async def fotir(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 45 oyatdan iborat         
 <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "yaasiyn")
async def yaasiyn(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 83 oyatdan iborat             
 <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 


@dp.callback_query(F.data == "soffaat")
async def soffaat(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 182 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 



@dp.callback_query(F.data == "sod")
async def sod(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 88 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 


@dp.callback_query(F.data == "zumar")
async def zumar(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 75 oyatdan iborat
      <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "gofir")
async def gofir(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 85 oyatdan iborat
      <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "fusilat")
async def fusilat(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 54 oyatdan iborat
      <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "shuuro")
async def shuuro(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 53 oyatdan iborat
             <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "zuxrof")
async def zuxrof(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 89 oyatdan iborat       
 <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "duxon")
async def duxon(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 59 oyatdan iborat
        <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "josiya")
async def josiya(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 37 oyatdan iborat    
<a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 


@dp.callback_query(F.data == "ahqof")
async def ahqof(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 35 oyatdan iborat                                  
     <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "Muhammad")
async def Muhammad(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 38 oyatdan iborat     
<a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 
    
@dp.callback_query(F.data == "fatx")
async def fatx(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 29 oyatdan iborat        
 <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "hujurot")
async def hujurot(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 18 oyatdan iborat         
<a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "qof")
async def qof(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 45 oyatdan iborat
<a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "zoriyat")
async def zoriyat(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 60 oyatdan iborat
<a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "tur")
async def tur(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 49 oyatdan iborat
<a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "najm")
async def najm(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 62 oyatdan iborat
<a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "qamar")
async def qamar(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 55 oyatdan iborat
<a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 



@dp.callback_query(F.data == "Ar_Rohman")
async def Ar_Rohman(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 78 oyatdan iborat
<a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "voqi'a")
async def voqia(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 96 oyatdan iborat
<a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "hadid")
async def hadid(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 29 oyatdan iborat
<a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "mujodala")
async def mujodala(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 22 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "hashr")
async def hashr(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 24 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 


@dp.callback_query(F.data == "mumtahana")
async def mumtahana(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 13 oyatdan iborat
   <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "soof")
async def soof(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 73 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "juma_quron")    
async def juma_quron(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 11 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "munofiqun")    
async def munofiqun(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 11 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "tagabun")    
async def tagabun(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 18 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 


@dp.callback_query(F.data == "taloq")    
async def taloq(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 12 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "tahrim")    
async def tahrim(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 12 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "mulk")    
async def mulk(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 30 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 


@dp.callback_query(F.data == "qalam")    
async def qalam(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 52 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "haaqqo")    
async def haaqqo(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 52 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "maorij")    
async def maorij(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 44 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "nuh")    
async def nuh(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 28 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 


@dp.callback_query(F.data == "jin")    
async def jin(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 28 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "muzzammil")    
async def muzzammil(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 20 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 


@dp.callback_query(F.data == "muddassir")    
async def muddassir(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 56 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "qiyaama")    
async def qiyaama(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 40 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "inson")    
async def inson(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 31 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 


@dp.callback_query(F.data == "mursalaat")    
async def mursalaat(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 50 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 


@dp.callback_query(F.data == "Naba")    
async def Naba(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 40 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "naziaat")    
async def naziaat(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 46 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "abasa")    
async def abasa(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 42 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "takvir")    
async def takvir(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 29 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "infitor")    
async def infitor(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 19 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "mutoffiful")    
async def mutoffiful(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 36 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "inshiqoq")    
async def inshiqoq(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 25 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "buruj")    
async def buruj(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 22 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 
    
@dp.callback_query(F.data == "toriq")    
async def toriq(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 17 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "alaa")    
async def alaa(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 19 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "goshiya")    
async def goshiya(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 26 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 


@dp.callback_query(F.data == "fajr")    
async def fajr(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 30 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "balad")    
async def balad(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 20 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "shams")    
async def shams(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 15 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "layl")    
async def layl(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 21 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "zuho")    
async def zuho(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 11 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "sharh")    
async def sharh(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 8 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 


@dp.callback_query(F.data == "tiyn")    
async def tiyn(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 8 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 


@dp.callback_query(F.data == "alaq")    
async def alaq(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 19 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "qadr")    
async def qadr(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 5 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "bayyina")    
async def bayyina(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 8 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "zalzala")    
async def zalzala(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 8 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "adiyat")    
async def adiyat(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 11 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "qoria")    
async def qoria(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 11 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "takaasur")    
async def takaasur(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 8 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "asr_quron")    
async def asr_quron(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 3 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "humaza")    
async def humaza(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 9 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "fiyl")    
async def fiyl(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 5 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "quraysh")    
async def quraysh(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 4 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "maauun")    
async def maauun(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 7 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "kavsar")    
async def kavsar(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 3 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "kaafirun")    
async def kaafirun(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 6 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 


@dp.callback_query(F.data == "nasr")    
async def nasr(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 3 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "masad")    
async def masad(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 3 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "ixlos")    
async def ixlos(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 4 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "falaq ")    
async def falaq(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 5 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 

@dp.callback_query(F.data == "nos_quron")    
async def nos_quron(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""  
Makkiy, 6 oyatdan iborat
  <a href=''>Bizning kanal📢</a>
 """,reply_markup=admin_keyboard.orqaga_qayt) 
