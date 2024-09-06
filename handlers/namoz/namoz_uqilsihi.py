from keyboard_buttons import admin_keyboard
from aiogram import  F
from aiogram.types import Message,CallbackQuery
from loader import dp





@dp.callback_query(F.data == "orqa_qaytish")
async def qaytar_handler(callback: CallbackQuery):
    await callback.message.answer(text="Menyulardan birini tanlang", reply_markup=admin_keyboard.tanlash_)
    await callback.message.delete()
@dp.callback_query(F.data == "qaytish")
async def qaytar_handler(callback: CallbackQuery):
    await callback.message.answer(text="Menyulardan birini tanlang", reply_markup=admin_keyboard.start_buttonnew)
    await callback.message.delete()

# "🕋NOMOZ O'QISHNI O'RGANISH🤲" tugmasi uchun handler
@dp.message(F.text == "NAMOZ")
async def massaeg(messaga: Message):
    await messaga.answer("Tanlang", reply_markup=admin_keyboard.tanlash_)
    await messaga.delete()
    
# Erkaklar namozi uchun callback query
@dp.callback_query(F.data == "erkak_namozi")
async def erkak_namoz(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="Tanlang", reply_markup=admin_keyboard.erkak_namoz)

# Azon matnini ko'rsatish uchun callback query
@dp.callback_query(F.data == "azon")
async def azon(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=""" 
Allohu akbar  اَللهُ أَكْبَر 
Allohu akbar  اَللهُ أَكْبَر 
Allohu akbar اَللهُ أَكْبَر 
Allohu akbar اَللهُ أَكْبَر 
Ashhadu alla ilaha illalloh  أَشْهَدُ أَلاَّ إِلَهَ إِلاَّ الله 
Ashhadu alla ilaha illalloh   أَشْهَدُ أَلاَّ إِلَهَ إِلاَّ الله 
Ashhadu anna Muhammadar Rasululloh  أَشْهَدُ أَنَّ مُحَمَّدًا رَسُولُ الله 
Ashhadu anna Muhammadar Rasululloh  أَشْهَدُ أَنَّ مُحَمَّدًا رَسُولُ الله 
Hayya alas solah  حَيَّ عَلَى الصَّلاَة 
Hayya alas solah  حَيَّ عَلَى الصَّلاَة 
Hayya alal falah  حَيَّ عَلَى الْفَلاَح 
Hayya alal falah  حَيَّ عَلَى الْفَلاَح 
Allohu akbar  اَللهُ أَكْبَر 
Allohu akbar اَللهُ أَكْبَر 
La ilaha illalloh لاَ إِلَهَ إِلاَّ الله 
<a href='https://t.me/namoz_uqishni_urganish_Kanal/28'>Bizning kanal📢</a>
""")
    
    await callback.message.answer(text="""
Azon duosi - Allohumma robba hazihid da’vatit tammah. Vas-solatil qoimah, ati Muhammadanil vasiylata val faziylah. Vad-darojatal ’aliyatar rofi’a. Vab’as-hu maqomam mahmudanillaziy va’adtah. Varzuqna shafa-’atahu yavmal qiyamah. Innaka la tuxliful mi’ad!
""", reply_markup=admin_keyboard.erkak_namoz)

# Bomdod namozi haqida ma'lumot
@dp.callback_query(F.data == "bomdod")
async def bomdod(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="Bomdod (fors.) — erta tong payti, sahar va shu paytda oʻqiladigan namoz. Bomdod namozi kun chiqish taraf yorishganidan boshlab to kun chiqqunga qadar oʻqiladi. Bamdod namozi ikki rakat sunnat va ikki rakat farzdan iborat. Erta tongda oʻqilgan namozning savobi qolgan namozlarga qaraganda kattaroq boʻladi. Namoz oʻqish musulmonlarning farzi hisoblanadi. <a href='https://t.me/namoz_uqishni_urganish_Kanal/14'>.</a>", reply_markup=admin_keyboard.erkak_namoz)


# Peshin namozi haqida ma'lumot
@dp.callback_query(F.data == "peshin")
async def peshin(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Peshin (fors.) — kunning yarmi oʻtgan payti va shu paytda oʻqiladigan namoz. Peshin namozi toʻrt rakat sunnat, toʻrt rakat farz va ikki rakat sunnatdan iborat. Peshin namozi Quyosh qiyomdan ogʻa boshlashidan to asr namozining vaqti kirguncha ado etiladi. <a href='https://t.me/namoz_uqishni_urganish_Kanal/9'>.</a>""", reply_markup=admin_keyboard.erkak_namoz)

# Asr namozi haqida ma'lumot
@dp.callback_query(F.data == "asr")
async def asr(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Asr namozi - Alloh taolo tomonidan farz qilingan namozlardan biri. Bu namozni musulmon kishi har kuni oʻqiydi. Ushbu namoz 4 rakat boʻlib faqat farzdan iborat.
<a href='https://t.me/namoz_uqishni_urganish_Kanal/10'>Bizning kanal📢</a>""", reply_markup=admin_keyboard.erkak_namoz)

# Shom namozi haqida ma'lumot
@dp.callback_query(F.data == "shom")
async def shom(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Shom — Quyosh botib, qorongʻulik boshlangan payt va shu vaqtda oʻqiladigan namoz. Shom namozi Quyosh botgandan boshlab, magʻrib ufqidagi qizil shafaqning koʻrinmay ketadigan vaqtigacha ado etiladi, uch rakat farz va ikki rakat sunnatdan iborat.
<a href='https://t.me/namoz_uqishni_urganish_Kanal/11'>Bizning kanal📢</a>""", reply_markup=admin_keyboard.erkak_namoz)

# Xufton namozi haqida ma'lumot
@dp.callback_query(F.data == "xufton")
async def xufton(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Xufton (fors. uxlash) — Quyosh botib ufqdagi qizillik yo'qolganidan keyin oʻqiladigan kechki namoz; bomdod namozi vaqti kirgungacha davom etadi. Xufton namozi to'rt rakat farz, ikki rakat sunnatdan iborat. Xufton namozining to'rt rakat farzi asr namozining farzi kabi o'qilib, faqat niyatda farq bo'ladi. Xuftonning ikki rakat sunnati ham yuqorida o'rganganimiz bomdod va shom namozlarining ikki rakat sunnatlari kabi bir xil tartibda o'qiladi. Bundan tashqari xufton namozi ōz ichiga 3 rakat vitr vojib namozini ham oladi. Ushbu vitr namozining 3-rakatida Fotiha va zam suralarni o'qigandan keyin "Qunut" duosi ōqiladi.
<a href='https://t.me/namoz_uqishni_urganish_Kanal/12'>Bizning kanal📢</a>""", reply_markup=admin_keyboard.erkak_namoz)

# Istixora namozi haqida ma'lumot
@dp.callback_query(F.data == "istixora")
async def istixora(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Istixora (baʼzan istihora ham deyiladi; arabcha: الاستخارة) — ikki rakaatdan iborat namoz. Ushbu namozdan so'ng musulmon kishi Allohdan maʼlum bir masala boʻyicha toʻgʻri qaror qabul qilishda yordam berishini soʻraydi.
<a href='https://t.me/namoz_uqishni_urganish_Kanal/59'>Bizning kanal📢</a>""", reply_markup=admin_keyboard.erkak_namoz)

# Hojat namozi haqida ma'lumot
@dp.callback_query(F.data == "hojat")
async def hojat(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Hojat namozining rakatlari borasida ixtilof qilingan. Molikiy va hanbaliylar nazdida, hojat namozi ikki rakatdir. Hanafiy ulamolar nazdida, hojat namozi to‘rt rakat o‘qiladi. Hanafiy mazhabimizdagi bir qavlda ikki rakat ham deyilgan. Bunga sabab shuki, hojat namozi haqida turli xil rivoyatlar kelgan. Ba’zi kitoblarimizda o‘n ikki rak’at ham deyilgan. Bizningcha, hojat namozining ikki rak’at ekanligi dalil jihatidan kuchlirog‘i bo‘lsa ajabmas. Vallohu a’lam!
Zero, hojat namozini ikki rakat o‘qish va unda qanday duo qilish haqidagi rivoyat Abdulloh ibn Abu Avvo va Anas ibn Molik roziyallohu anhumodan naql qilingan. Uni Imom Termiziy o‘zlarining mashhur hadis to‘plamlarida rivoyat qilib keltirganlar. Boshqa rivoyatlarning esa ayrim fiqhiy kitoblarda mazmuni zikr qilingan bo‘lsada, ammo roviysi va qaysi hadis to‘plamida keltirilganligiga ishora qilinmagan.
<a href='https://t.me/namoz_uqishni_urganish_Kanal/60'>Bizning kanal📢</a>""", reply_markup=admin_keyboard.erkak_namoz)


#--------------------------------------------------------------------------------------------------------
# Ayollar uchun Namoz o'qishni o'rganish bo'limi

#-----------------------------------------------------------------------------------------------------------
""" Ayollar uchun Namoz o'qishni o'rganish """
#-----------------------------------------------------------------------------------------------------------

# "ayol_namoz" tugmasi uchun handler
@dp.callback_query(F.data == "ayol_namoz")
async def ayol_namoz(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Tanlang", reply_markup=admin_keyboard.ayol_namoz)

# Ayollar bomdod namozi haqida ma'lumot
@dp.callback_query(F.data == "bomdod2")
async def ayol_namoz(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Bomdod (fors.) — erta tong payti, sahar va shu paytda oʻqiladigan namoz. Bomdod namozi kun chiqish taraf yorishganidan boshlab to kun chiqqunga qadar oʻqiladi. Bamdod namozi ikki rakat sunnat va ikki rakat farzdan iborat. Erta tongda oʻqilgan namozning savobi qolgan namozlarga qaraganda kattaroq boʻladi. Namoz oʻqish musulmonlarning farzi hisoblanadi.
<a href='https://t.me/namoz_uqishni_urganish_Kanal/2'>Bizning kanal📢</a>
""", reply_markup=admin_keyboard.ayol_namoz)

# Ayollar peshin namozi haqida ma'lumot
@dp.callback_query(F.data == "peshin2")
async def peshin(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Peshin (fors.) — kunning yarmi oʻtgan payti va shu paytda oʻqiladigan namoz. Peshin namozi toʻrt rakat sunnat, toʻrt rakat farz va ikki rakat sunnatdan iborat. Peshin namozi Quyosh qiyomdan ogʻa boshlashidan to asr namozining vaqti kirguncha ado etiladi.
<a href='https://t.me/namoz_uqishni_urganish_Kanal/3'>Bizning kanal📢</a>
""", reply_markup=admin_keyboard.ayol_namoz)

# Ayollar asr namozi haqida ma'lumot
@dp.callback_query(F.data == "asr2")
async def asr(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Asr namozi - Alloh taolo tomonidan farz qilingan namozlardan biri. Bu namozni musulmon kishi har kuni oʻqiydi. Ushbu namoz 4 rakat boʻlib faqat farzdan iborat.
<a href='https://t.me/namoz_uqishni_urganish_Kanal/4'>Bizning kanal📢</a>

""", reply_markup=admin_keyboard.ayol_namoz)

# Ayollar shom namozi haqida ma'lumot
@dp.callback_query(F.data == "shom2")
async def shom(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Shom — Quyosh botib, qorongʻulik boshlangan payt va shu vaqtda oʻqiladigan namoz. Shom namozi Quyosh botgandan boshlab, magʻrib ufqidagi qizil shafaqning koʻrinmay ketadigan vaqtigacha ado etiladi, uch rakat farz va ikki rakat sunnatdan iborat.
<a href='https://t.me/namoz_uqishni_urganish_Kanal/6'>Bizning kanal📢</a>
""", reply_markup=admin_keyboard.ayol_namoz)

# Ayollar xufton namozi haqida ma'lumot
@dp.callback_query(F.data == "xufton2")
async def xufton(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Xufton (fors. uxlash) — Quyosh botib ufqdagi qizillik yo'qolganidan keyin oʻqiladigan kechki namoz; bomdod namozi vaqti kirgungacha davom etadi. Xufton namozi to'rt rakat farz, ikki rakat sunnatdan iborat. Xufton namozining to'rt rakat farzi asr namozining farzi kabi o'qilib, faqat niyatda farq bo'ladi. Xuftonning ikki rakat sunnati ham yuqorida o'rganganimiz bomdod va shom namozlarining ikki rakat sunnatlari kabi bir xil tartibda o'qiladi. Bundan tashqari xufton namozi ōz ichiga 3 rakat vitr vojib namozini ham oladi. Ushbu vitr namozining 3-rakatida Fotiha va zam suralarni o'qigandan keyin "" duosi ōqiladi.
<a href='https://t.me/namoz_uqishni_urganish_Kanal/5'>Bizning kanal📢</a>
""", reply_markup=admin_keyboard.ayol_namoz)

# Ayollar bomdod namozi videosi haqida ma'lumot
@dp.callback_query(F.data == "videosi2")
async def videosi2(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Bomdod namozi ikki rakat sunnat, ikki rakat farz – jami to'rt rakatdan iborat.
<a href='https://t.me/namoz_uqishni_urganish_Kanal/2'>Bizning kanal📢</a>
""", reply_markup=admin_keyboard.ayol_namoz)

# Ayollar islomdagi o'rni haqida ma'lumot
@dp.callback_query(F.data == 'xolat')
async def xolat(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Islom dini ayolning jamiyatdagi o'rni va ta'sirini juda katta baholaydi. Chunki ayollar islom ummatining tarbiyachilari hisoblanadi. Shu sababli ularning bilim olishi, ma'naviyati va ilm tarqatishi birinchi o'rindagi masalalardandir. Ayniqsa, ayollar uchun birinchi navbatda o'rganishi farz bo'lgan ilmlar - ularning o'zlariga xos bo'lgan masalalardir.
<a href='https://t.me/namoz_uqishni_urganish_Kanal/7'>Bizning kanal📢</a>
""", reply_markup=admin_keyboard.ayol_namoz)

# Ayollar istixora namozi haqida ma'lumot
@dp.callback_query(F.data == "istixora2")
async def istixora(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Istixora (baʼzan istihora ham deyiladi; arabcha: الاستخارة) — ikki rakaatdan iborat namoz. Ushbu namozdan so'ng musulmon kishi Allohdan maʼlum bir masala boʻyicha toʻgʻri qaror qabul qilishda yordam berishini soʻraydi.
<a href='https://t.me/namoz_uqishni_urganish_Kanal/59'>Bizning kanal📢</a>
""", reply_markup=admin_keyboard.ayol_namoz)

# Ayollar hojat namozi haqida ma'lumot
@dp.callback_query(F.data == "hojat2")
async def hojat(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Hojat namozining rakatlari borasida ixtilof qilingan. Molikiy va hanbaliylar nazdida, hojat namozi ikki rakatdir. Hanafiy ulamolar nazdida, hojat namozi to‘rt rakat o‘qiladi. Hanafiy mazhabimizdagi bir qavlda ikki rakat ham deyilgan. Bunga sabab shuki, hojat namozi haqida turli xil rivoyatlar kelgan. Ba’zi kitoblarimizda o‘n ikki rak’at ham deyilgan. Bizningcha, hojat namozining ikki rak’at ekanligi dalil jihatidan kuchlirog‘i bo‘lsa ajabmas. Vallohu a’lam!
Zero, hojat namozini ikki rakat o‘qish va unda qanday duo qilish haqidagi rivoyat Abdulloh ibn Abu Avfo va Anas ibn Molik roziyallohu anhumodan naql qilingan. Uni Imom Termiziy o‘zlarining mashhur hadis to‘plamlarida rivoyat qilib keltirganlar. Boshqa rivoyatlarning esa ayrim fiqhiy kitoblarda mazmuni zikr qilingan bo‘lsada, ammo roviysi va qaysi hadis to‘plamida keltirilganligiga ishora qilinmagan.
<a href='https://t.me/namoz_uqishni_urganish_Kanal/61'>Bizning kanal📢</a>
""", reply_markup=admin_keyboard.ayol_namoz)


#  jamoat namozlari ----
@dp.callback_query(F.data == "JAMOAT_namoz")
async def ayol_namoz(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Jamoat namozi – savobi ulug‘ ibodat. Ibn Umar roziyallohu anhumodan rivoyat qilinadi. Rasululloh sollallohu alayhi vasallam: “Jamoat namozi yolg‘iz o‘qilgan namozdan yigirma yetti daraja afzaldir”, dedilar (Imom Buxoriy, Imom Muslim rivoyati)", reply_markup=admin_keyboard.jamoat
""", reply_markup=admin_keyboard.jamoat)

@dp.callback_query(F.data == 'juma')
async def juma_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Juma namozi (arabcha: صَلَاة ٱلْجُمُعَة, Ṣalāt al-Jumuʿah) — Musulmonlarning umumiy namozi. Juma kuni masjidlarda peshin namozi vaqtida oʻqiladi. Juma namozi erkin, voyaga yetgan erkaklarga farzdir. Juma namozi ikki rakat farz boʻlib, undan oldin va keyin toʻrt rakat sunnat oʻqiladi. Ilk va oxirgi sunnatlar peshin namozining sunnatlari kabi oʻqiladi. Imomga iqtido qilib oʻqiladigan ikki rakat farz esa, bomdod namozining farzi kabi oʻqiladi. Ayollar, bolalar va jismoniy zaif kishilar uchun juma namozi shart emas. Ayrim zamonaviy hanafiy ilohiyotshunoslari keksa ayollarning jamoaviy namozga borishini nomaqbul deb hisoblaydilar. Musulmonlarga juma namozini uzrsiz sababsiz tark etish taqiqlangan. Tabiiy ofatlar (qattiq ayoz, qor koʻchkisi xavfi, kuchli yomgʻir va h.k.) yuz berganda juma namozi ixtiyoriy holga keladi. Namozdan oldin musulmon toʻliq tahorat olib, tirnoqlarini kesib, toza, bayramona kiyim kiyishi tavsiya etiladi. Bundan tashqari, mushk sepish tavsiya etiladi. Masjidga kirishdan oldin sarimsoq, piyoz va boshqa oʻtkir hidli yeguliklarni isteʼmol qilish taqiqlanadi. Namozdan oldin ikkinchi azon aytiladi va xutba oʻqiladi. Xutba ikki qismdan iborat. Xutbaning bu qismlari orasida imomning qisqa vaqt oʻtirishi maqsadga muvofiqdir. Xutbadan keyin namozxonlar imomdan keyin ikki rakat namoz oʻqiydilar. Juma namozining oʻqilishi peshin namozini oʻqishdan xalos qiladi. Masjidga kechikib kelish mumkin emas. Eng oxirgi kelgan kishi boshqa dindorlarni bosib oʻtmasligi, qator oralarida yurmasligi va boshqalarni bezovta qilib, oldingi qatorlardan joy olishga harakat qilmasligi kerak. Imom xutba oʻqish uchun minbarga chiqqan bir paytda gaplashib, boshqa odamlarni chalgʻitib boʻlmaydi.
<a href='https://t.me/namoz_uqishni_urganish_Kanal/13'>Bizning kanal📢</a> 
""", reply_markup=admin_keyboard.jamoat)

@dp.callback_query(F.data == 'ied')
async def ied_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Alloh rizoligi uchun Ramazon hayiti namozini o‘qishga niyat qilinadi.
Imom “Allohu akbar” deya takbir aytgach jamoat ham qo‘llarini ko‘tarib, ichida iftitoh takbiri (Allohu akbar)ni aytadi. Takbir aytilganidan so‘ng, qo‘lni qovushtirib turib, har kim ichida sano duosini o‘qiydi. So‘ngra imom qo‘llarini quloqlariga ko‘tarib, uch marta takbir aytadi. Jamoat ham unga ergashadi. Birinchi va ikkinchi takbirda qo‘llar yon tomonga tushiriladi. Uchinchi takbirdan so‘ng qo‘llar bog‘lanib, qiyom holida turiladi. Imom ichida “A’uzu”ni va “Bismillah”ni aytib, ovoz chiqarib “Fotiha” surasini va zam surani o‘qiydi. Takbir aytib ruku va sajda ado etiladi. Shundan so‘ng ikkinchi rakatga turiladi. Imom “Fotiha” surasi bilan zam sura o‘qigach, rukuga bormay turib, xuddi birinchi rakatdagi kabi uch marta takbir aytadi. To‘rtinchi takbirda qo‘l ko‘tarmasdan imom orqasidan ruku va sajda ado qilinadi. Sajdadan so‘ngra “Attahiyyot”, “Salovat” va “Duo” o‘qilib, salom berilib, namoz tugatiladi. Alloh ibodatlaringizni O‘z dargohida qabul etsin!
<a href='https://t.me/namoz_uqishni_urganish_Kanal/22'>Bizning kanal📢</a> 
""", reply_markup=admin_keyboard.jamoat)

@dp.callback_query(F.data == 'janoza')
async def janoza_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Janoza namozi – vafot etgan musulmonlar uchun jamoat boʻlib oʻqiladigan namoz. Mayyit yuvilib, kafanlanadi, masjidga keltiriladi. Jamoatning oldiga yuqoriroq yerga qoʻyiladi. Imom jamoatning oldiga oʻtib Janoza namozini oʻqiydi. Janoza namozini oʻquvchi kishi avval: "Niyat qildim ushbu marhum uchun Janoza namozini oʻqimoqqa, iqtido qildim ushbu imomga. Xolisan lillohi Taolo", deb niyat qiladi. Imom baland ovoz bilan, qolganlar imomga iqtido qilib maxfiy su'ratda (faqatgina o'zi eshitadigan darajada) "Allohu Akbar" deb qoʻllarini bogʻlaydi. Iqtido qilib oʻquvchi aytganini o'zi eshitadigan darajada takbir aytib qoʻllarini bogʻlaydi. Soʻngra ovoz chiqarmasdan "Sano"ni oʻqiydi: "Subhanakallohumma va bihamdika va tabarokasmuka va taʻala jadduka va la ilaha gʻoyruk". Soʻngra imom bilan birgalikda takror takbir aytiladi. Lekin qoʻllar koʻtarilmaydi. Solli va Barik duolari oʻqiladi. Takror yana qoʻllar koʻtarilmagan holda takbir aytiladi, janoza duosi oʻqiladi. Janoza duosini bilmaydiganlar esa, Qunut duosini yoki duo niyati bilan Fotiha surasini oʻqisa ham boʻladi. Soʻngra imom bilan birgalikda takror takbir qilinib oldin oʻngga, keyin chapga salom beriladi. Janoza namozi oʻqilib boʻlganidan keyin mayyit mozorga olib boriladi, qabrga qoʻyiladi, ruhdariga bagʻishlab Qurʼon tilovat va duo qilinadi
<a href='https://t.me/namoz_uqishni_urganish_Kanal/19'>Bizning kanal📢</a> 
""", reply_markup=admin_keyboard.jamoat)

@dp.callback_query(F.data == 'tarovih')
async def tarovih_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Tarovih – istirohat ma’nosidagi "tarviha" so‘zining ko‘pligidir. To‘rt rakat o‘qib, ortidan dam olingani uchun bu namoz shunday nomlangan.
Ramazon oyi fazilatlarga boydir. Uning fazilatlaridan biri oy davomida xufton namozidan keyin tarovih namozi o‘qishdir. Payg‘ambarimiz sallallohu alayhi vasallam tarovih namozi haqida shunday deganlar:
“Alloh taolo Ramazon ro‘zasini farz qildi va men uning qiyomini sizlar uchun sunnat qildim. Kimki iymon va ishonch bilan, savob umidida ro‘za tutsa va kechalari qoim tursa, onadan tug‘ilgan kunidagidek gunohlardan pok bo‘ladi” (Imom Nasoiy rivoyatlari).
<a href='https://t.me/namoz_uqishni_urganish_Kanal/20'>Bizning kanal📢</a> 
""", reply_markup=admin_keyboard.jamoat)