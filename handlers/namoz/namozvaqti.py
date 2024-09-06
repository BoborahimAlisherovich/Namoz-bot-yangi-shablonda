from keyboard_buttons import admin_keyboard
from aiogram import  F
from aiogram.types import Message
from funksiyalar.namoz_vaqti import vaqti, mintaqalar
from loader import dp

# Namoz vaqtlarini ko'rsatish
mintaqalar = {
    "Toshkent": 27,
    "Andijon": 1,
    "Buxoro": 4,
    "Guliston": 5,
    "Samarqand": 18,
    "Namangan": 15,
    "Navoiy": 14,
    "Jizzax": 9,
    "Nukus": 16,
    "Qarshi": 25,
    "Qo'qon": 26,
    "Xiva": 21,
    "Marg'ilon": 13
}

@dp.message(F.text.in_(mintaqalar.keys()))
async def ism_func(message: Message):
    try:
        vaqtlar = vaqti(mintaqalar.get(message.text))
        text = (
            f"""{vaqtlar[1]} - {vaqtlar[-1]} | {vaqtlar[2]} \n
🌅Bomdod: {vaqtlar[3]}\n
🌄Quyosh chiqishi : {vaqtlar[4]}\n
☀️Peshin vaqti : {vaqtlar[5]}\n
☀️Asr vaqti: {vaqtlar[6]}\n
🌜Shom vaqti {vaqtlar[7]}\n
🌕Xufton vaqti: {vaqtlar[8]}"""
        )
        await message.answer(text=text, reply_markup=admin_keyboard.Admin)
    except:
        await message.answer(text="Serverda Xatolik yuz berdi")

# Namoz vaqtlarini tanlash
@dp.message(F.text == "⌛️NAMOZ VAQTLARI⌛️")
async def namoz_vaqti(message: Message):
    await message.answer(text="Hududingizni tanlang", reply_markup=admin_keyboard.hudud)


# Namoz vaqtlarini tanlash
@dp.message(F.text == "🏠 Bosh Menyu")
async def namoz_vaqti(message: Message):
    await message.answer(text="Assalomu alaykum", reply_markup=admin_keyboard.start_buttonnew)
