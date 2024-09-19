from keyboard_buttons import admin_keyboard
from aiogram import  F,types
from loader import dp
from aiogram.types import Message, InlineKeyboardButton,InlineKeyboardMarkup



# 99 ta ism ------====================
allah_names = [
    "1) Alloh: lloh lafzi «alaha» fe’lidan olingan «iloh» masdariga mansub bo‘lib ma’bud - ibodat qilingan zot - ma’nosini anglatadi. Arablarda «iloh»ning avvaliga alif va lom harflari kiritilgan va «al-ilohu» hosil bo‘lgan. So‘ngra hamzaning harakatini lomi ta’rifga naql qilingan va bir jinsdagi ikki harfni idg‘om qilingandan keyin «Alloh» lafzi hosil bo‘lgan. Alloh lafzi yakkayu yagona ma’budi haqqa ism bo‘lib qolgan. U zotdan boshqaga bu ism ishlatilmagan. Ba’zi ulamolar, Alloh ismi a’zamdir, deganlar. Bu lafzi jalola haqida Ibn Atoulloh Sakandariy kabi zotlar alohida kitoblar ham yozganlar.",
    "2) Ar-Rahmon: «Rahmon» – ulug‘ ne’matlarni beruvchi. «Rahmon» sifati faqat Allohga xos bo‘lib, barchaga–kofirga ham, mo‘minga ham mehribon va ne’mat beruvchi, ma’nosini anglatadi. Rahmon sifatini Alloh taolodan boshqa hech kimga nisbatan ishlatib bo‘lmaydi.",
    "3) Ar-Rohiym: «Rohiym» – latif ne’matlarni beruvchi. «Rohiym» sifati esa xosroq bo‘lib, qiyomat kuni faqat mo‘minlarga rahm qiluvchi ma’nosini anglatadi va Allohdan o‘zgalarga, jumladan, Payg‘ambar alayhissalomga nisbatan ham ishlatiladi.",
    "4) Al-Malik: «Malik» – barcha narsaning egasi. «Malik» – haqiqiy egadir, Undan o‘zga ega yo‘q. Shuning uchun bandalar faqat Unga qul bo‘ladilar. Hech vaqtda bir qulga ikki xo‘ja bo‘lmaydi. Shuning uchun insonlar o‘zlariga o‘xshagan insonlarga emas, balki yagona yaratganga, haqiqiy ega-Malikka qul bo‘lishlari lozim.",
    "5) Al-Quddus: «Quddus» - barcha ayblardan holi, noloyiq sifatlardan pok. Mutlaq muqaddaslik va mutlaq poklik Allohning O‘zigagina xosdir.",
    "6) As-Salom: «Salom» - nuqsonlardan salomat, shuningdek, tinchlik-xotirjamlik va rohat beruvchi zot. Alloh «Salom» sifati ila bandalarga tinchlik, omonlik, xotirjamlik ato qiladi.",
    "7) Al-Mo‘min:  iymon va omonlikni beruvchi.",
    "8) Al-Muhaymin: «Muhaymin» - hamma narsani qamrab oluvchi, ya’ni, Alloh bandalaring barcha holatlariga guvoh bo‘lib turadi, Undan hech narsa maxfiy qolmaydi.",
    "9) Al-Aziz: barchaning ustidan g‘olib. Undan biror narsa g‘olib kela olmaydi.",
    "10) Al-Jabbor:    oliy qadar, ulug‘, Uning oldida o‘zgalar o‘zini xor tutadi.",
    "11) Al-Mutakabbir:   kibiryosi va ulug‘ligi mubolag‘ali zot. Uning oldida boshqalar qul bo‘lib turadigan zot.",
    "12) Al-Xoliq:   Asli va o‘xshashi yo‘q narsalarni aniq bir o‘lchovlar bilan yaratuvchi. U zotda maxluqi yo‘qligida ham Xoliqlik ma’nosi mavjuddir. Alloh maxluqlar vujudga keltirilishidan oldin Xoliq, degan vasfga ega edi. U xaloyiqni xalq qilganidan boshlab Xoliq ismini olgani yo‘q. Xoliq mutlaq vujudga keltiruvchidir.",
    "13) Al-Bori’:  - yo‘qdan paydo qiluvchi, vujudga keltiruvchi. Bori’ tafovutsiz qilib vujudga keltiruvchidir.",
    "14) Al-Musavvir:   maxluqotlarning suvratini shakllantiruvchi. Har bir narsaga o‘ziga xos suvrat beruvchi.",
    "15) Al-Gʻaffor: Ko‘plab mag‘firat qilib, bandalarning aybini O‘z fazli ila ularni itob qilmasdan kechib yuboruvchi.",
    "16) Al-Qahhor: Barcha maxluqotlarni qabzasida tutib, ularni O‘z hukmiga yuritib va qudrati ila bo‘ysundirib turuvchi.",
    "17) Al-Vahhob: Ko‘plab ne’matlarni behisob beruvchi.",
    "18) Al-Razzoq: Ko‘plab rizq beruvchi. Rizqlarni va ularning vositalarini yaratuvchi. Alloh maxluqotlariga hech bir o‘irliksiz va qiyinchiliksiz yoki yordam so‘ramasdan rizq beruvchidir.",
    "19) Al-Fattoh: Ko‘plab narsalarni ochuvchi. O‘z rahmat xaziynasini bandalariga ochuvchi.",
    "20) Al-Aliym: Har bir narsani biluvchi. Bo‘lgan va bo‘ladigan, avvalgi va oxirgi, zohir va botin narsalarning barchasini biluvchi.",
    "21) Al-Qobiz: Ruhlarni qabz qiluvchi - tutuvchi. Xohlagan kishisining rizqini qabz qiluvchi. Qalblarni qabz qiluvchi.",
    "22) Al-Bosit: Ruhlarni kenglikka qo‘yib yuboruvchi. Xohlagan kishisining rizqini keng qilib qo‘yuvchi. Qalblarni keng qiluvchi.",
    "23) Al-Xofiz: Pasaytiruvchi. Misol uchun kofir va fosiqlarning martabasini ularni xoru zor qilib pasaytiradi.",
    "24) Ar-Rofe’: Ko‘taruvchi. Misol uchun mo‘min va taqvodorlarning martabasini ularni azizu mukarram qilib ko‘taradi.",
    "25) Al-Mu’izz: Aziz qiluvchi. Kimni xohlasa to‘g‘ri yo‘lga solib aziz qiladi.",
    "26) Al-Muzill: Xor qiluvchi. Kimni xohlasa egri yo‘lga yurgani uchun xor qiladi.",
    "27) As-Samiy’: Har bir narsani eshituvchi.",
    "28) Al-Basiyr: Har bir narsani ko‘ruvchi.",
    "29) Al-Hakam: Hukm qiluvchi.",
    "30) Al-Adl: Mutlaq adolat qiluvchi.",
    "31) Al-Latiyf: O‘ta lutf ko‘rsatuvchi. Barcha narsalarning nozik va daqiq joylarigacha biluvchi.",
    "32) Al-Xabiyr: Hamma narsadan o‘ta xabardor.",
    "33) Al-Haliym: Gʻazabi qo‘zimaydigan va iqob qilishga shoshilmaydigan.",
    "34) Al-Aziym: Aql tasavvur qila olmaydigan darajada azamatli va ulug‘.",
    "35) Al-Gʻafur: Ko‘p mag‘firat qiluvchi.",
    "36) Ash-Shakur: Oz amal uchun ko‘p savob beruvchi.",
    "37) Al-Aliy: Martabasi oliylikda benihoya.",
    "38) Al-Kabiyr: Har bir narsadan katta.",
    "39) Al-Hafiyz: Har bir narsani komil muhofaza qiluvchi.",
    "40) Al-Muqiyt: Barcha moddiy va ruhiy qutlarni yaratuvchi.",
    "41) Al-Hasiyb: Kifoya qiluvchi. Qiyomat kuni bandalarning hisobini qiluvchi.",
    "42) Al-Jaliyl: Sifatlarida ulug‘likka ega bo‘lgan zot.",
    "43) Al-Kariym: Birov so‘ramasa ham, biror narsaning evaziga bo‘lmasa ham narsalarni ko‘plab ato qiluvchi. Lutf bilan itob qiluvchi. Qarama-qarshiliklardan pok bo‘lgan. Karamli ishlar va xislatlar sohibi.",
    "44) Al-Raqiyb: Hech bir zarrani ham qo‘ymay muroqaba qilib turuvchi.",
    "45) Al-Mujiyb: Duolarni ijobat qiluvchi.",
    "46) Al-Vose’: Keng – hamma narsani qamrab oluvchi.",
    "47) Al-Hakiym: Har bir narsani hikmat ila qiluvchi.",
    "48) Al-Vadud: Barchaga yaxshilikni ravo ko‘ruvchi.",
    "49) Al-Majiyd:Shon - sharafi va qadri baland va cheksiz.",
    "50) Al-Bo’is: Yuboruvchi: xalqlarga payg‘ambarlar yuboruvchi. Kishilarga himmat yuboruvchi. O‘liklarni qayta tiriltiruvchi..",
    "51) Ash-Shahiyd: Har bir narsaga hoziru nozir. Barchaga shohidlik beruvchi.",
    "52) Al-Haqq:O‘zgarmas sobit zot. Haqni yuzaga chiqaruvchi zot.",
    "53) Al-Vakil: Barchaning ishi unga topshirilgan zot.",
    "54) Al-Qaviy: Quvvatli zot.",
    "55) Al-Matiyn: Matonatli zot.",
    "56) Al-Valiy: Muhabbat qiluvchi, nusrat beruvchi va xalqining ishini yurituvchi zot.,"
    "57) Al-Hamiyd: Barcha maqtovlar ila maqtalgan zot.",
    "58) Al-Muhsiy: Barcha narsaning hisobini olgan zot.",
    "59) Al-Mubdi: Barcha narsalarni avval boshdan bor qilgan zot.",
    "60) Al-Muid: Yo‘q bo‘lgan narsalarni yana qaytadan bor qiluvchi.",
    "61) Al-Muhyiy: Tiriltiruvchi. O‘liklarni tiriltiruvchi va hayot beruvchi zot.",
    "62) Al-Mumiyt: O‘ldiruvchi. Barcha jonzotlarning jonini oluvchi.",
    "63) Al-Hayy: Tirik. U tirikdir, o‘lmas.",
    "64) Al-Qayyum: O‘z-o‘zidan qoim bo‘lgan va boshqalarni qoim qilgan zot.",
    "65) Al-Vojid: Xohlagan narsasini topuvchi. ",
    "66) Al-Mojid: Majdu sharaf sohibi bo‘lgan zot.",
    "67) Al-Vohid: Yagona. U zot birdir va bo‘linmas.",        
    "68) As-Somad: Ulug‘, itoat qilingan va hech kimga hojati tushmaydi, barchaning hojati Unga tushadi.",
    "69) Al-Qodir: Cheksiz qudrat sohibi.",
    "70) Al-Muqtadir: Juda ham qudratli.",
    "71) Al-Muqaddim: Oldinga suruvchi.",
    "72) Al-Muaxxir: Orqaga suruvchi.",
    "73) Al-Avval: Hamma narsadan avval bor bo‘lgan zot.",
    "74) Al-Oxir: Hamma narsa yo‘q bo‘lganda ham O‘zi qoladi.",
    "75) Az-Zohir: Uning mavjudligi oshkor va ochiq-oydindir.",
    "76) Al-Botin: Ko‘zga ko‘rinmaydi, hamma narsani biluvchi zot.",
    "77) Al-Voliy: Har bir narsaga ega bo‘lgan zot.",
    "78) Al-Mutaoliy: Nuqsonlardan yuqori turuvchi zot.",
    "79) Al-Barr: Ulug‘ yaxshilik qiluvchi.",
    "80) At-Tavvob: Bandalarni tavbaga yo‘llovchi va tavbani qabul qiluvchi zot.",
    "81) Al-Muntaqim: Zolim va osiylardan intiqom oluvchi.",
    "82) Al-Afuvv: Afv qiluvchi.",
    "83) Ar-Ra’uf: O‘ta shafqatli va mehribon.",
    "84) Molikul Mulk: Mulk egasi. Bu dunyodagi ishlarni xohlaganicha qiluvchi.",
    "85) Zul Jalol val Ikrom: Sharaf va kamol egasi, karam va ikrom sohibi.",
    "86) Al-Muqsit: O‘z adolati ila mazlumlarga nusrat va zolimlarga jazo beruvchi.",
    "87) Al-Jome’: Barcha haqiqatlarni va odamlarni qiyomat kuni jamlovchi.",
    "88) Al-G‘aniy: Behojat. Uning hech kim va hech narsaga hojati tushmaydi.",
    "89) Al-Mug‘niy: Behojat qiluvchi.",
    "90) Al-Moni: Man qiluvchi.",
    "91) Az-Zorr: Zarar qiluvchi narsalarni yaratuvchi.",
    "92) An-Nofi: Manfaat beruvchi.",
    "93) An-Nur: O‘z-o‘zi ila zohir bo‘lgan va o‘zgalarni zohir qiluvchi.",
    "94) Al-Hodiy: Hidoyat qiluvchi, to‘g‘ri yo‘l ko‘rsatuvchi zot.",
    "95) Al-Badiy’: O‘xshashi yo‘q narsalarni keltiruvchi." ,
    "96) Al-Boqiy: Boqiy qoluvchi. Foniy bo‘lmas.",
    "97) Al-Voris: Muvjudotlar yo‘q bo‘lganda ham boqiy qoluvchi zot.",
    "98) Ar-Rashiyd: To‘g‘ri yo‘lga irshod qiluvchi.",
    "99) As-Sabur: O‘ta sabrli, osiylarni azoblashga shoshilmaydi.",

]

NAMES_PER_PAGE = 9

def get_pagination_keyboard(current_page):
    buttons = []
    if current_page > 0:
        buttons.append(InlineKeyboardButton(text="⬅️ Orqaga", callback_data=f"prev:{current_page - 1}"))
    if (current_page + 1) * NAMES_PER_PAGE < len(allah_names):
        buttons.append(InlineKeyboardButton(text="Oldinga ➡️", callback_data=f"next:{current_page + 1}"))

    # "⬅️ Orqaga" va "Oldinga ➡️" tugmalari bitta qatorda bo'ladi
    pagination_row = buttons

    # "🏠 Bosh Menyu" tugmasi alohida qatorga qo'shiladi
    menu_row = [InlineKeyboardButton(text="🏠 Bosh Menyu", callback_data="qaytish")]

    return InlineKeyboardMarkup(inline_keyboard=[pagination_row, menu_row])

def get_names_page(page):
    start = page * NAMES_PER_PAGE
    end = start + NAMES_PER_PAGE
    return "\n\n".join(allah_names[start:end])

@dp.message(F.text == "99 TA ISMLAR")
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
