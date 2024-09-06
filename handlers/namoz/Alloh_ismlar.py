from keyboard_buttons import admin_keyboard
from aiogram import  F,types
from loader import dp
from aiogram.types import Message, InlineKeyboardButton,InlineKeyboardMarkup



# 99 ta ism ------====================
allah_names = [
    "1) Ar-Rohim: Latif ne'matlar beruvchi (qiyomat kuni faqat mo'minlarga)",
    "2) Al-Malik: Barcha narsaning egasi",
    "3) Al-Quddus: Barcha ayblardan xoli",
    "4) As-Salom: Barcha nuqsonlardan salomat va tinchlik omonlik va rohat beruvchi",
    "5) Al-Mu'min: Iymon va omonlik beruvchi",
    "6) Al-Muhaymin: Hamma narsani qamrab oluvchi",
    "7) Al-Aziz: Barchaning ustidan g'olib",
    "8) Al-Jabbar: Oliy qadar, ulug' zot",
    "9) Al-Mutakabbir: Kibriyosi va ulug'ligi behad",
    "10) Al-Xoliq: Asli va o'xshashi yo'q narsalarning o'lchovini mos qilib yaratuvchi",
    "11) Al-Bari': Yo'qdan paydo qiluvchi, vujudga keltiruvchi",
    "12) Al-Musavvir: Mahluqotlarning suratini shakillantiruvchi",
    "13) Al-G'affor: Ko'plab mag'firat qiluvchi",
    "14) Al-Qahhor: Barcha maxluqotlarni qabzida tutib, ularni o'z hukmiga yuritib va qudrati ila bo'ysundirib turuvchi",
    "15) Al-Vahhab: Ne'matlarni behisob beruvchi",
    "16) Ar-Razzaq: Ko'plab rizq beruvchi",
    "17) Al-Fattah: Ko'plab narsani ochuvchi",
    "18) Al-'Alim: Har bir narsani biluvchi",
    "19) Al-Qabid: Ruhlarni qabz qiluvchi",
    "20) Al-Basit: Ruhlarni kenglikka qo'yib yuboruvchi",
    "21) Al-Khafid: Pasaytiruvchi",
    "22) Ar-Rafi': Ko'taruvchi",
    "23) Al-Mu'izz: Aziz qiluvchi",
    "24) Al-Mudhill: Xor qiluvchi",
    "25) As-Sami': Har bir narsani eshituvchi",
    "26) Al-Basir: Har bir narsani ko'ruvchi",
    "27) Al-Hakam: Mukkamal hukm egasi",
    "28) Al-'Adl: Mutlaq adolat qiluvchi",
    "29) Al-Latif: Barcha nozik narsalarni ham biluvchi, o'ta lutf ko'rsatuvchi",
    "30) Al-Khabir: Hamma narsadan o'ta xabardor",
    "31) Al-Halim: G'azabi qo'zmaydigan va iqob qilishga shoshilmaydigan",
    "32) Al-'Azim: Aql tasavvur qila olmaydigan darajada azamatli va ulug'",
    "33) Al-Ghafur: Ko'plab mag'firat qiluvchi",
    "34) Ash-Shakur: Oz amal uchun ham ko'p savob beruvchi",
    "35) Al-'Aliy: Martabasi oliylikda benihoya",
    "36) Al-Kabir: Har bir narsadan katta",
    "37) Al-Hafiz: Har bir narsani Komil muhofaza qiluvchi",
    "38) Al-Muqit: Barcha moddiy va ruhiy rizqlarni yaratuvchi",
    "39) Al-Hasib: Kifoya qiluvchi va Qiyomatda bandalarini hisob qiluvchi",
    "40) Al-Jalil: Sifatlarda ulug'likka ega",
    "41) Al-Karim: Birov so'ramasa ham, hech bir evaz olmasdan ham, narsalarni ko'plab ato etuvchi",
    "42) Ar-Raqib: Hech bir zarrani ham qo'ymay tekshirib turuvchi",
    "43) Al-Mujib: Duolarni ijobat qiluvchi",
    "44) Al-Wasi': Keng-hamma narsani keng ilmi ila ihota qilgan, Barcha i keng rahmati ila qamrab oluvchi",
    "45) Al-Hakim: Har bir narsani hikmat ila qiluvchi",
    "46) Al-Wadud: Barcha yaxshilikni ravo ko'ruvchi",
    "47) Al-Majid: Shon-Sharafi va qadri behad yuksak",
    "48) Al-Ba'ith: Xalqlarga payg'ambarlarni yuboruvchi",
    "49) Ash-Shahid: Har bir narsaga hoziru nozir",
    "50) Al-Haqq: O'zgarmas,sobit Zot",
    "51) Al-Wakil: Barchaning ishni topshirilgan zot",
    "52) Al-Qawiyy: O'ta kuchli va quvvatli zot",
    "53) Al-Matin: Quvvatida mustahkam va matonatli",
    "54) Al-Waliyy: Muhabbat qiluvchi, nusrat beruvchi va xalqining ishini yurituvchi",
    "55) Al-Hamid: Barcha maqtovlar ila maqtalgan zot",
    "56) Al-Muhsi: Barcha narsaning hisobini oluvchi zot",
    "57) Al-Mubdi': Barcha narsalarni avvalboshidan bor qilgan Zot",
    "58) Al-Mu'id: Yo'q bo'lgan narsalarni yana qaytadan bor qiluvchi",
    "59) Al-Muhyi: Tiriltiruvchi",
    "60) Al-Mumit: O'ldiruvchi",
    "61) Al-Hayy: Tirik",
    "62) Al-Qayyum: O'zi qoim bo'lgan va boshqalarni qoim qilgan",
    "63) Al-Wajid: Topuvchi",
    "64) Al-Majid: Ulug'lik va sharaf sohibi",
    "65) Al-Wahid: Yagona,bitta.",
    "66) As-Samad: Hech kimga hojati tushmaydi, Barchaning hojati unga tushadi",
    "67) Al-Qadir: Cheksiz qudrat sohibi",
    "68) Al-Muqtadir: Juda ham qudratli",
    "69) Al-Muqaddim: Oldinga suruvchi",
    "70) Al-Mu'akhkhir: Orqaga suruvchi",
    "71) Al-Awwal: U hamma narsadan avval",
    "72) Al-Akhir: Hamma narsa yo'q bo'lib ketganda ham, Uning O'zi qoladi",
    "73) Az-Zahir: Uning mavjudligi oshkor, ochiq-oydindir",
    "74) Al-Batin: U ko'zga ko'rinmaydi",
    "75) Al-Wali: Har narsaga voliy ega bo'lgan Zot",
    "76) Al-Muta'ali: Nuqsonlardan yuqori turuvchi zot",
    "77) Al-Barr: Ulug' yaxshilik qiluvchi",
    "78) At-Tawwab: Bandalarni tavbaga yo'llovchi va ularning tavbasini ko'plab qabul qiluvchi Zot",
    "79) Al-Muntaqim: Zolim va osiylardan intiqom oluvchi",
    "80) Al-'Afuww: Avf qiluvchi",
    "81) Ar-Ra'uf: O'ta shavqatli va mehirbon",
    "82) Malik-ul-Mulk: Mulk egasi",
    "83) Dhul-Jalali wal-Ikram: Sharaf va kamol egasi",
    "84) Al-Muqsit: Adolat ila mazlumlarga nusrat va zolimlarga jazo beruvchi",
    "85) Al-Jami': Jamlovchi. Barcha haqiqatlarni jamlovchi",
    "86) Al-Ghaniyy: Behojat. Uning hech kimga va hech narsaga hojati tushmaydi",
    "87) Al-Mughni: Behojat qiluvchi",
    "88) Al-Mani': Man' qiluvchi. U himoya qiluvchi",
    "89) Ad-Darr: Xohlagan bandasiga zarar beruvchi",
    "90) An-Nafi': Foyda beruvchi",
    "91) An-Nur: O'zi nurli va O'zi nur beruvchi",
    "92) Al-Hadi: O'zi hidoyat topgan va O'zi hidoyat qiluvchi",
    "93) Al-Badi': O'xshashisiz, mislsiz va nihoyatda go'zal narsalarni yaratuvchi",
    "94) Al-Baqi: Mangu qoluvchi",
    "95) Al-Warith: So'nggida qoluvchi voris. Hammadan so'ng U qoladi",
    "96) Ar-Rashid: To'g'ri yo'l ko'rsatuvchi",
    "97) As-Sabur: Juda sabrli",
    "98) Al-Muqtadir: Har narsaga qodir",
    "99) Al-Muqaddim: Har narsani o'z vaqtida oldinga suruvchi",
]

NAMES_PER_PAGE = 9
def get_pagination_keyboard(current_page):
    buttons = []
    if current_page > 0:
        buttons.append(InlineKeyboardButton(text="⬅️ Orqaga", callback_data=f"prev:{current_page - 1}"))
    if (current_page + 1) * NAMES_PER_PAGE < len(allah_names):
        buttons.append(InlineKeyboardButton(text="Oldinga ➡️", callback_data=f"next:{current_page + 1}"))
    return InlineKeyboardMarkup(inline_keyboard=[buttons])

def get_names_page(page):
    start = page * NAMES_PER_PAGE
    end = start + NAMES_PER_PAGE
    return "\n".join(allah_names[start:end])

@dp.message(F.text=="99 TA ISMLAR")
async def send_names(message: types.Message):
    await message.delete()
    current_page = 0
    await message.answer(
        text=get_names_page(current_page),
        reply_markup=get_pagination_keyboard(current_page)
    )

@dp.callback_query(lambda c: c.data and (c.data.startswith('next') or c.data.startswith('prev')))
async def process_pagination(callback_query: types.CallbackQuery):
    action, page = callback_query.data.split(':')
    current_page = int(page)
    await callback_query.message.edit_text(
        text=get_names_page(current_page),
        reply_markup=get_pagination_keyboard(current_page)
    )
    await callback_query.answer()

