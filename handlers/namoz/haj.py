from keyboard_buttons import admin_keyboard
from aiogram import  F
from aiogram.types import Message,CallbackQuery
from loader import dp


#Haj   ---------------============
@dp.message(F.text=="HAJ")
async def message(message:Message):


    await message.answer(text="HAJ  <a href='https://t.me/mukammal_namoz/86'>.</a>",reply_markup=admin_keyboard.haj)

@dp.callback_query(F.data == "haj_orqaga")
async def haj_orqaga(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="Haj  <a href='https://t.me/mukammal_namoz/86'>.</a>", reply_markup=admin_keyboard.haj)

@dp.callback_query(F.data == "qanday_ibodat")
async def qanday_ibodat(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""   
Haj ibodatining boshqa ibodatlardan bir farqi shuki, u hammaga ham bir paytning o‘zida farz bo‘lavermaydi, balki ayrim shartlariga muvofiq kelgan musulmonlargagina farzdir. Qodir bo‘lgan odamlarga Alloh uchun Baytni haj qilish farz. Ulamolar kishiga haj farz bo‘lishi uchun quyidagi shartlar mavjud bo‘lishi kerakligini ta’kidlashgan:

1) musulmon bo‘lishi;

2) balog‘atga etgan bo‘lishi;

3) oqil bo‘lishi;

4) hajga qodir bo‘lishi;

5) sog‘-salomat bo‘lishi;

6) hukumat man qilmagan bo‘lishi;

7) yo‘lda omonlik bo‘lishi;

8) ayol kishiga mahrami bo‘lishi;

Kimda ushbu shartlardan birortasi bo‘lmasa, unga haj farz bo‘lmaydi.
Haj – Islomning besh arkonidan biri bo‘lgan ulug‘ rukn, Allohga mahbub ibodatdir. Bu ibodat Alloh taologa yuzlanish, U Zotning tajalliysi, nurining markazi bo‘lgan maskanda ado etiladi. Hadisi shariflarda kelishicha, Baytullohi sharif shunday makonga joylashganki, uning ayni ustida, yettinchi osmonda Baytul Ma’mur, uning ustida esa Alloh taoloning Arshi joylashgan. Alloh taoloning tavajjuhi, nuri va tajalliyoti dastlab Ka’batullohga nozil bo‘lib, keyin butun olamga tarqaladi. Shu sababli bu yerga kelish baxtiga musharraf bo‘lgan musulmonlar uchun ulkan saodat bor.
Haj oshiqona ibodat bo‘lib, u yerga borish faqat hazrati Ibrohim alayhissalomning haj e’loniga «labbay» deb javob bergan kishilargagina nasib etadi. U necha marotaba labbay degan bo‘lsa, Ka’batullohni o‘shancha marta tavof qilish sharafiga muyassar bo‘ladi. Shuningdek, u yerga borib, haj ibodatini ado etish yana bir saodatga sababdir.
Haj ibodatida ulkan hikmatlar bo‘lib, bu hikmatlarning barchasini insonning ojiz aqli to‘la anglab olishi qiyin. Shunday bo‘lsa ham ulamolar ijtihod qilganlar.
Hajda islomiy birlik yorqin namoyon bo‘ladi. Haj chog‘ida musulmonlarning his-tuyg‘ulari, ibodat la ri va hatto suvratlari bir xil bo‘ladi. Bu erda irqchilik, mahalliychilik, tabaqachilik kabi salbiy holatlarga o‘rin qolmaydi. Hamma bir Allohga iymon keltirib, bir Baytullohni tavof qiladi. Tinchlik Islomning shiori ekani hajda yana bir bor namoyon bo‘ladi. Hamma tinch, yurt tinch, ibodat tinch, xalq tinch bo‘ladi
Haj ulkan islomiy anjuman bo‘lib, har bir musulmon dunyoning turli burchaklaridan kelgan din qardoshlari bilan uchrashadi, turli masalalarni muhokama qiladi. Islom va iymon rishtalari mustahkamlanadi.
Hajda musulmon banda omonlik yurti bo‘lmish Makkai mukarramaga safar qiladi. Makka – ulug‘, muqaddas shahar. Alloh taolo Qur’oni Karimda uning nomi bilan qasam ichgan. O‘zining uyi bo‘lmish Ka’baning shu shaharda qaror topishini iroda qilgan.
Haj ulug‘ ruhiy ozuqa beradigan ibodat bo‘lib, unda musulmon bandaning vujudi Alloh taologa taqvo bilan, Unga toat qilishga azmu qaror bilan, gunohlariga nadomat bilan to‘ladi. Bu safarda musulmon kishining Allohga, Uning Rasuliga va mo‘min-musulmonlarga bo‘lgan muhabbati ziyoda bo‘ladi. Dunyoning hamma taraflaridagi din qardoshlariga nisbatan do‘stlik tuyg‘ulari uyg‘onib, mustahkamlanadi. 
""",reply_markup=admin_keyboard.haj_ortga)
    

@dp.callback_query(F.data == "haj_odoblari")
async def haj_odoblari(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""   
1. Haj va umrani niyat qilgan kishi avvalambor bu ulug‘ safardan Alloh taoloning roziligini maqsad qilishi hamda riyokorlik, odamlar eshitsin kabi illatlardan o‘zini poklashi lozim;
2. Safar oldidan kishi o‘zining vasiyat, qarz oldi-berdilari va omonatlarini yozib qoldirishi mustahab amallardan;
3. Gunohlariga qattiq tavba qilishi va ularni hech qachon qaytarmaslikka niyat qilishi kerak;
4. Kishilarning unda haqlari bo‘lsa yoki ularga nohaqliklar qilgan bo‘lsa, haqlarini egalariga qaytarish, zulm qilgan kishilaridan esa, avf etishlarini so‘rash lozim;
5. Alloh taolo faqat halol mollardan qilingan nafaqalarnigina qabul qilishini e’tiborga olib hajga ishlatiladigan nafaqalarini ham faqat haloldan to‘plash lozim;
6. Barcha gunohlardan, jumladan til va qo‘ldan sodir bo‘ladigan chaqimchilik, g‘iybat, bilmagan narsasini gapirish, atrofidagilarga qo‘pollik qilish, haj va umrani ado etayotganlarni noqulay ahvolga solib qo‘yish kabilardan saqlanish lozim. Atrofdagilarga nisbatan rahm-shafqatli, mehribon va xushmuomalada bo‘lish musulmon kishining fazilatidandir;
7. Haj va umrani niyat qilgan kishi haj va umra amallari qanday ado etilishini yaxshi bilib olishish lozim;
8. Haj ziyoratiga otlangan kishilar zimmalaridagi farz va vojib amallarni to‘liq bajarishga jiddu-jahd qilishlari lozim. Xususan, namozlarni o‘z vaqtida jamoat bilan ado qilish, zikr, duo, Qur’on tilovati va istig‘forlar aytish, muhtoj kishilarga yordam ko‘rsatish kabi ishlarni qilishi tahsinga loyiq ishlardandir;
9. Safar davomida solih va bilimdon hamrohlar bilan birga bo‘lishi ham mustahab amallardan sanaladi;
10. Safarga otlangan kishilar go‘zal xulqli bo‘lishga va odamlar bilan xushxulqda muomala qilishga e’tibor berishlari lozim. Bu esa o‘z-o‘zidan sabr qilish, avf etish, muloyimlik, mehribonlik, halimlik, kamtarinlik, shoshmaslik, sahovatli bo‘lish, adolatli va omonatdor kabi xislatlarni o‘z ichiga oladi;
11. Safarga otlangan kishi o‘z oilasini Allohdan taqvo qilishga chaqirishi lozim. Chunki bu, Alloh taoloning bandalarga ko‘rsatmasi;
12. Safarga otlangan kishi Payg‘ambarimiz sollallohu alayhi va sallamdan vorid bo‘lgan duolarni yodlab olishi mustahab amallardandir.
Alloh Taalo barcha hojilarimizni hajlarini mabrur hajlardan qilsin!

""",reply_markup=admin_keyboard.haj_ortga)


@dp.callback_query(F.data == "hajning_nozik_sirlari")
async def hajning_nozik_sirlari(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""   
Alloh taologa yetishish uchun butunlay Uning O‘zini ko‘zlagan holda ajrab chiqmoq kerak bo‘ladi. Shuning uchun ham qadimgi rohiblar Alloh taologa yetishish maqsadida hamma narsadan ajrab, tog‘larga chiqib ketar edilar.
Islomda rohiblik yo‘q. Ammo taqqoslash uchun aytadigan bo‘lsak, Islom ummatining rohibligi hajdir. Haj ibodatini ado etmoqchi bo‘lgan banda barcha shahvatlar, lazzatlardan, aloqa va mashg‘ulotlardan, hatto odatdagi kiyimlaridan ham ajraydi.
Hajning har bir amalida eslatma va ibrat bor:
1. Hajga kerak bo‘ladigan narsalarni jamlaganda oxiratga kerak bo‘ladigan narsalarni esiga olsin.
2. Oddiy kiyimlarini yechib, ehromga kirayotganida kafanni va Robbiga bu dunyo kiyimlaridan boshqacha kiyim ila ro‘baro‘ bo‘lishini esga olsin.
3. «Labbayka»ni aytishni boshlaganida Alloh taoloning chaqirig‘iga javob berayotganini esga olsin va qabulni orzu qilib, qabul bo‘lmay qolishidan qo‘rqsin.
4. Haramga yetganda uqubatdan omon qolishni orzu qilsin va yaqinlardan bo‘lmay qolishdan qo‘rqsin. Ammo umidvorlik g‘olib bo‘lsin.
5. Baytullohni ko‘rganida qalbida uning ulug‘vorligini hozir qilsin va Alloh taologa o‘zini mehmonlari martabasiga erishtirgani uchun shukr qilsin hamda Baytullohni tavof qilish naqadar ulug‘vorligini his etsin.
6. Hajarul asvadni istilom qilgan (uni qo‘li bilan ushlagan yoki ishora qilgan) paytida Alloh taologa itoat qilishga bay’at qilganiga e’tiqod qilsin va bu bay’atga vafo qilishga azmu qaror qilsin.
7. Ka’bai Muazzamaning pardasiga osilganida va Multazamda turganida gunohkor o‘z xojasining panohiga qochganini eslasin.
8. Safo va Marva orasida sa’yi qilayotgan paytida ularni «tarozining ikki pallasi» deb o‘ylasin. Ularning orasida borib-kelishini «qiyomatning arosati» deb o‘ylasin.
9. Arafotda turganida, odamlarning izdihomini ko‘rganida, ovozlarining ko‘tarilishini eshitganida, tillarining turli-tumanligini bilganida qiyomat mavqifini, unda xaloyiqning jamlanishini va shafoat so‘rashlarini esga olsin.
10. Tosh otish paytida qullikni namoyon qilishni va farmonga bo‘ysunib, uni so‘zsiz bajo etishni qasd qilsin.
11. Qurbonlik so‘yish paytida bu ishning Alloh taologa qurbat hosil qilishning eng muhim turlaridan biri ekanini, qurbonlikning har bir bo‘lagi evaziga qurbonlik qiluvchining bir bo‘lagi do‘zaxdan xalos bo‘lishini eslasin
""",reply_markup=admin_keyboard.haj_ortga)


@dp.callback_query(F.data == "haj_tavsiya")
async def haj_tavsiya(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""   
Haj safariga chiquvchiga tavsiyalar
Muborak haj safariga tayyorgarlik ko'rayotgan kishiga haj kitoblarida quyidagi
ko'rsatmalar beriladi:
1)Haj safariga otlanuchi kishi o'zidan ko'ngli ranjigan kishilarning ko'ngillarini ovlashi, ularni rozi gilishi zarur.
2)Odamlar bilan muomalani to'g'rilashi.
3)Biror kishiga zulm qilgan bolsa, undan kechirim so'rashi.
4)Biror kishining molini nohaq yeb qo'ygan bo'lsa, uni o'ziga yoki merosxo'rlarigaqaytarib berishi.
5)Barcha qilgan gunohlariga astoydiltavba qilishi.
6)Ota-onasini rozi qilib safar qilishi.
7)Bola-chaqalarini hotirjam qilib safar gilishi.
8)Qarzlarini ado qilib safarga chiqishi.
9)Solih kishilar bilan safar gilishi.
10)Hajning farz va vojib masalalarini yaxshilab o'rganib olishi;
11) O'zi bilan Haj kitobini olishi.
12) Safarga tijorat maqsadlarini aralashtirmay, xolis ibodat maqsadidasafar qilishi.
13) Riyo va shuhratparastlikdan o zini yiroq tutishi.
14) Safar davomida o'zini xokisor va tavoze bilan tutishi.
15) Zaruriy narsalarni sotib olish chog ida sotuvchi bilan haddan ziyod tortishmasligi;
16) Haj safari davomida pul sarflashda xasislik qilmasligi;
17) Sheriklariga sarf-xarajat qilish to'g'ri kelib qolsa, mamnuniyat bilan ularga sarf qilishi.
18) Uydan chiqib ketayotgan vaqtidasadaqa qilishi.
19) Safar davomida hojatmand odamlarga sarf qilaman deb o'zi bilan ortiqcha mablag' olishi.
20) Ikki rakat namoz o'qib yolga chiqishi.
21) Uydan chiqib ketayotgan paytda
odamlar bilan qo'l berib so'rashib, ulardan haqqiga duo qilib turishlarini so rashi.
22) Boshqalarning ham haj gilishga ketayotgan kishidan duo qilishini so'rashlari.
23) Kuzatuvchi ham, safarga ketuvchi ham o'z duolarini o'qishlari.
24) Safar duosini o'qishi.
25) Safar davomida qaerga tushsalar, o'sha joyda ikki rakat namoz o'qib olishi (mustahab).
26) Safar davomida Alloh taoloning zikrini qilib, ota-onasi, farzandlari va barcha musulmonlar haqgiga duo gilishi.
27) Safar davomida tortishish, dilozorlik va tilozorlik kabi narsalardan saqlanishi.
28) Barchaga halimlik bilan, xushmuomalada bolishi.
29) Besh vaqt namozni imkoni boricha jamoat bilan ado qilishi.
30) Namozlarni o'z vaqtida ado qilishi. 
31) Sunnati ravotiblarni iloji boricha tark qilmasligi                                                                   
""",reply_markup=admin_keyboard.haj_ortga)


@dp.callback_query(F.data == "haj_ibodat_turlari")
async def haj_ibodat_turlari(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""   
Demak, haj turlari uchta:

1)Ifrod;
2)Tamattu'
3)Qiron;
                                  
1. Ifrod haji deb miqotdan faqat haj qilish uchun ehromga kirishga aytiladi. Ifrod haj qiluvchi kishi Makkaga kelgach, tavofi qudum qilib, haj amallarini ado etishga kirishadi va qurbonlik kuni shaytonga tosh otganidan keyin ehromdan chiqadi. Ifrod haj qiluvchi zimmasiga qurbonlik qilish vojib bo‘lmaydi. Faqat bir tavof va bir sa'y qilish vojibdir. Bugungi kunda ifrod hajini qilish birmuncha mashaqqatlidir. Chunki bu tur hajni niyat qilgan kishi Makkai mukarramaga kelgan kunidan boshlab to qurbon hayiti kuni shaytonga tosh otib, sochini qisqartirgunigacha ehromda bo‘lishi va ehrom tartib-qoidalariga qat'iy amal qilishi shartdir. Agar shu vaqt oraligida ehromda qaytarilgan ishlarni unutib qilib qo‘ysa, zimmasiga kafforat lozim bo‘ladi. Masalan, mo‘ylabi o‘sib ketsa-yu uni qisqartirish, olish mumkin emasligini unutib, olib qo‘ysa yoki xushbo‘ylanib qo‘ysa, jarima lozim bo‘ladi. Ammo shuncha qiyinchilikka yarasha, bu hajning savobi boshqalarga qaraganda ko‘proqdir.
2. Tamattu' haji. “Tamattu'” arabcha so‘z bo‘lib, “foydalanish”, “maza”, “huzur qilish” ma'nolarini anglatadi. Avval umrani ado etib, haj vaqtigacha ehrom harom qilgan narsalardan huzur qilib yurib, vaqti kelganda yana ehromga kirib hajni niyat qilgan odam “Tamattu' haj qiluvchi” deyiladi. Hanafiy mazhabi bo‘yicha tamattu' ifrod hajidan ulug‘ bo‘ladi. Tamattu' haj oylarida Makkaga tashqaridan keluvchilarga joiz. Makkada yashovchilarga va u yerga haj oylaridan oldin kelib, hajni kutib turganlarga joiz emas. Tamattu' hajini ifroddan asosiy farqlari quyidagilar.
U ehromga kirayotganda umranigina niyat qiladi. So‘ng “Talbiya” aytib boradi. Makkaga kirib umra tavofini qiladi. Birinchi tavofdayoq talbiyani to‘xtatadi. So‘ng Safo va Marva orasida sa'y qilib bo‘lgach, sochini oldirib yo qisqartirib ehromdan chiqadi. So‘ng haj vaqti kelishini kutib turadi. Zulhijja oyining 8-kuni Haromda ehromga kiradi va niyat qiladi.
So‘ng ikki rakaat namoz o‘qiydi. Ka'bani tavof qiladi, Safo va Marva orasida sa'y qilib olsa yaxshi bo‘ladi. So‘ng ifrod haji amallarini qilgandek amallarni qiladi. Hayit kuni tong otgandan so‘ng jonliqni so‘yadi. Keyin sochini oldirib yo qisqartirib ifoza tavofini qiladi. Agar ehrom bog‘lagan paytda tavof va sa'y qilmagan bo‘lsa ifoza tavofidan so‘ng Safo va Marva orasida sa'y qiladi. Tamattu' niyat qilgan odam o‘ziga vojib bo‘lgan jonliqni so‘yishga qodir bo‘lmasa, o‘rniga ro‘za tutadi. Bu ro‘zaning umumiy miqdori o‘n kun. Shundan uch kuni Arafadan avval tutilishi shart. Eng yaxshisi Arafa kuni va undan avvalgi ikki kun ro‘za tutishdir. Arofatda charchab qolmay desa, bir kun oldin tutsin. Yetti kuni hajdan keyin o‘z yurtida tutiladi.
""",reply_markup=admin_keyboard.haj_davomi)

@dp.callback_query(F.data == "davomi_haj")
async def davomi_haj(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""   
3. Qiron haji. “Qiron” so‘zi “yaqinlik”, “qo‘shilish” ma'nolarini anglatadi. Umra bilan yaqinlashtirib, bir-biriga qo‘shib qilingan hajni “qiron” haji deyiladi. Qironning ifroddan farqi shuki, ehromga kirishda niyat qiladi. Keyin talbiya aytadi. Makkaga kelgach, umra uchun tavofni ado etib, Safo va Marva orasida sa'y qiladi. Ammo sochini oldirmaydi, ehromdan chiqmaydi. Chunki unda hali hajning niyati bor. Keyin haj uchun yana bir tavof qiladi va sa'y ado etadi. Qolgan amallar ifrod hajinikiga o‘xshab ketadi. Hayit kuni tosh otishdan so‘ng qurbonlik qilish vojib. Jonliq so‘yayotganda “Qiron uchun” yo “Dami shukr” deb niyat qiladi. Undan so‘ng sochini oldiradi yo qisqartiradi. Ushbu tartib zarurdir. Ifoza tavofi qilingandan so‘ng, avval haj uchun sa'y qilmagan bo‘lsa sa'y qiladi. Qurbonlik so‘yishga imkoni yo‘qlar tamattu'ga o‘xshab ro‘za tutadilar.
""",reply_markup=admin_keyboard.haj_ortga)
    

@dp.callback_query(F.data == "hajning_farzi")
async def hajning_farzi(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""   
Hajning farzlari uchta 
1. Ehrom. 
2. Arofatda turish.
3. Ziyorat tavofi.
                                  
Hajning vojiblari
1. Miyqotdan ehrom bog‘lamoq.
2. Safo va Marva oralig‘ida sa'y qilmoq.
3. Sa'yni Safodan boshlamoq.
4. Sa'yda yurmoq. Shuningdеk, tavofda ham yurib sa'y qilmoq.
5. Kun bo‘yi Arofatda turgan kishi, shomgacha Arofatda        turishni davom ettirmog‘i.
6. Arofatdan imomni orqasidan (undan kеyin) chiqib kеtmoq.
7. Muzdalifada (tong otgandan kеyin) bir daqiqa bo‘lsa ham turmoq.
8. Ikki kеchgi (shom va xufton namozlarini) shomni xuftonga kеchiktirib o‘qimoq.
9. Bir qavlda aytildi: kеchaning bir bo‘lagida Muzdalifada tunamoq. U shoz (ozchilikning) gapi.
10. Uch kun shaytonga tosh otish.
11. (Hayitning birinchi kunidagi) katta shaytonga tosh otish amaliyotini soch oldirishdan oldin amalga oshirish.
12. Shaytonga tosh otiladigan har bir kunni tosh otishini ikkinchi kunga kеchiktirmaslik. Agar tosh otishni ertangi kunga kеchiktirsa, u qazo bo‘lib gunohkor bo‘ladi. Bir namozni boshqa namozning vaqtiga kеchiktirganga o‘xshash.
13. Bir qavlda aytildi: har bir tosh otishni, soch oldirish va tavofni tartib bilan amalga oshirish vojibdir. Bu so‘z mashhur gapga xilofdir. Bu gapni e'tibori yo‘q. 
14. Haytning birinchi kuni katta shaytonga tosh otgandan kеyin, ehromdan chiqish uchun sochni tagidan oldirmoq yoki sochni to‘rtdan bir qismini qisqartirmoq.
15. Sochni tagidan oldirmoq yoki sochni to‘rtdan bir qismini qisqartirmoq amaliyoti qurbonlik kunlari, Haramda amalga oshirilmog‘i.
16. Ziyorat tavofini qurbonlik kunlarida qilmoq.
17. Hatmni (Ka'bai muazzamani yonidagi Ka'bani eski binosinig poydеvori yoki bir bo‘lagi) orqasidan tavof qilmoq.
18. Bir qavlda aytildi: Tavof qilishni hajarul asvaddan boshlamoq. Sahihrog‘i u amal sunnati muakkadadir (takidlangan sunnatdir).
19. Tavofda tahoratli bo‘lmoq.
20. Tavofni o‘ngdan boshlamoq.
21. Avrat yopilishi.
22. Erkak kishini ehromi, ayolni kiygan kiyimi pok bo‘lishi.
23. Tavofda yurmoq.
24. Tavofdan kеyin ikki rakat tavof namozini o‘qimoq.
Ushbu vojiblar makkaliklar va atrofdan borganlar uchun umumiydir.
Makkaliklardan boshqalarga hajning xos vojib amallari esa:
25. Vidolashuv tavofi.
26. Qiron haj qiluvchi, jonliq so‘yishdan oldin katta shaytonga tosh otmog‘i.
27. Tamattu' haj qiluvchi, jonliq so‘yishdan oldin katta shaytonga tosh otmog‘i.
28-29. Qiron va Tamattu' haj qiluvchi jonliq so‘yishi.
30-31. Qiron va Tamattu' haj qiluvchi soch oldirishdan oldin jonliq so‘yishi. 
32-33. Qiron va Tamattu' haj qiluvchi qurbonlik kunlarida jonliq so‘yishi.
34. Bir qavlda aytildi: Qudum tavofi. Sahih qavlga ko‘ra Qudum tavofi vojib, lеkin jumhur uni sunnati muakkada (ta'kidlangan sunnat) dеyishgan.
35. Ehromda man qilingan amallarni tark qilish ham vojiblar jumlasiga kiradi.

 Hajning sunnatlari
1. Hajning o‘zini Qiron (bir ehrom bilan haj va umra qilishni) niyat qilgan kishi uchun qudum tavofini qilmoq sunnatdir. Umrani o‘zini niyat qilib, ehrom bog‘lagan kishi va tamattu' haj qiluvchi (umraga ehrom bog‘lab uni bajargandan kеyin, ehromdan chiqib haj kunlari kеlganda yana haj uchun ehrom bog‘lagan kishi) uchun qudum tavofi sunnat emas. Tamattu' haj qiluvchi ham, tanho umra qiluvchiga o‘xshaydi. Chunki miyqotdan umraga ehrom bog‘laydi. Makkaga kеlib umrani ehromidan chiqqandan kеyin, haj masalasida makkalikka o‘xshaydi. Makkalikka Qudum tavofi sunnat emas.
Qudum tavofini vojib dеganlar uchun ham xuddi shuningdеk, umrani o‘zini niyat qilib, ehrom bog‘lagan kishi va tamattu' haj qiluvchi uchun qudum tavofi vojib emas. 
2. Tavofni Qora toshdan boshlamoq.
3. Imom uch joyda xutba qilmog‘i. Zulhijjani yettinchi kuni Makkada. To‘qqizinchi kuni Arofatda. O‘n birinchi kuni Minoda.
4. Tarviya kuni Makkadan Minoga chiqib kеtmoq.
5. Arafa kеchasi Minoda tunamoq. 
6. Arafa kuni quyosh chiqqandan kеyin Arofatga kеtish.
7. Arofat uchun g‘usl qilish.
8. Muzdalifada tunamoq.
9. Minodan Muzdalifaga quyosh chiqmasdan kеtish.
10. Shaytonga tosh otish kunlarida minoda tunamoq.
11. Bir daqiqa bo‘lsa ham Muhassab dеgan joyga tushmoq                                                                   
""",reply_markup=admin_keyboard.haj_ortga)
    

@dp.callback_query(F.data == "ehromga_kirish")
async def ehromga_kirish(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""   
Hamma tayyorgarliklar nihoyasiga etib, haj amallarini boshlash navbati keladi. Shunda haj amallari­dan birinchisi ehrom bo‘ladi.
“Ehrom” arabcha so‘z bo‘lib, lug‘atda «harom qilmoq» maʼnosini anglatadi. Ehromga kirgan odam uchun ehromdan oldin halol bo‘lgan baʼzi ish va narsalar harom bo‘ladi. Misol uchun, boshqa vaqtlarda o‘ziga xushbo‘y narsalarni sepishi halol edi, ehromga kirgach, bu narsa harom bo‘lib qoladi.
Ehromning haqiqati haj yoki umra yoki ikkalasiga birdaniga niyat qilib, talbiya aytishdir. Ehrom uchun faqat niyat qilish yoki talbiya aytish kifoya qilmaydi. Namozda qalb bilan niyat, til bilan esa takbiri tahrima aytilishi lozim va shart bo‘lgani kabi haj yoki umra ehromiga kirishda ham niyat bilan talbiya birgalikda topilishi lozimdir. Shu bois dilda niyat qilib, til bilan talbiya yoki uning o‘rnini bosadigan Alloh taoloning zikri aytilmasa, ehromga kirgan hisoblanmaydi. Shuningdek, til bilan talbiya yoki uning o‘rnini bosadigan Alloh taoloning zikrini aytib, qalbda ehromga kirishni niyat qilmasa, ehromga kirgan bo‘lmaydi.
Erkak kishining umra yoki haj niyatida tikilgan kiyim kiyishi joiz emas. Agar tikilgan kiyim kiysa, kafforat vojib bo‘ladi. Masalan, yoqasi yo‘q ko‘ylak, ishton, qo‘lqop, mahsi, mayka, do‘ppi, kostyum, kamzul kabilar tikilgan kiyim sanaladi. Agar erkak kishi yuqoridagi kiyimlardan birortasini ehrom holatida kiyib olsa, jarima va fidya lozim bo‘ladi. Shuning uchun ehrom kiyimlari tikilmagan bo‘lishi shartdir. Ehromning sunnati ikki oq mato olib, birini lungi kabi, ikkinchisini esa katta sochiq kabi yelkasiga tashlab olishdir. Faqat tavof vaqtida yuqorisiga tashlab olgan katta sochiq kabi matoni chap yelkasini ochib qo‘ltig‘ining ostidan o‘tkazib oladi.
Ehrom holatidagi erkak kishilarning qomatiga munosib shaklda tikilgan kiyimni kiyib olishi joiz emas. Lekin shim yoki shalvar tarzida bo‘lmay, qop kabi tikilib, ikki tomonini ochib olinsa, zarari yo‘q, yaʼni karohiyatsiz joizdir. 
Ehromga kipmoqchi bo‘lgan odam sochi, tirnog‘i, mo‘ylabini va olinishi lozim bo‘lgan tuklapini olib, so‘ngra g‘usl qiladi. Keyin ikki parcha oq, yangi yoki yuvilgan matoni (xalq tilida «ehrom kiyimi»ni) olib, bipini kindigi bilan tizzasini qo‘shib to‘sadigan holatda beliga tutadi. bu«izor» deyiladi. Ikkinchisini yelkasi aralash aylantirib o‘raydi. Bunisi «rido» deyiladi. Badaniga va ehrom kiyimiga xyshbo‘y narsa surtadi, ammo u narsaning rangi kiyimda qolmasligi shart qilinadi.
so‘ngra ikki rakat namoz o‘qiydi. Birinchi rakatda Fotiha supasidan keyin Kafirun, ikkinchi rakatda Ixlos spuasini o‘qiydi. so‘ngra qaysi hajni qilmoqchi bo‘lsa, o‘shanga mos niyat qiladi. Masalan, ifrod hajining niyati:
اللَّهُمَّ إِنِّي أُرِيدُ الْحَجَّ فَيَسِّرْهُ لِي وَتَقَبَّلْهُ مِنِّي.

«Allohyumma inni uridul hajja fa yassirhu li va taqobbalhy minni.
Yaʼni, «Allohim, men hajni iroda qilaman, uni menga oson etgil va qabyl aylagil».
Tamattyʼ hajining niyati:
اللَّهُمَّ إِنِّي أُرِيدُ الْعُمْرَةَ فَيَسِّرْهَا لِي وَتَقَبَّلْهَا مِنِّي.

«Allohymma inni uridul umrata fa yassirha li va taqobbalha minni».
Yaʼni, «Allohim, men umrani iroda qilaman. Uni menga oson etgil va qabul aylagil».
Qiron hajining niyati:
اللَّهُمَّ إِنِّي أُرِيدُ الْعُمْرَةَ وَالْحَجَّ فَيَسِّرْهُمَا لِي وَتَقَبَّلْهُمَا مِنِّي.
«Allohumma inni uridul umrata val-hajja fa yassipuyma li va taqobbalhuma minni»
Yaʼni, «Allohim, men umra va hajni iroda qilaman, ularni menga oson etgil va qabyl aylagil».
Agar biror kishi nomidan haji badal qilayotgan bo‘lsa, o‘sha kishi nomidan niyat qilib quyidagi duoni o‘qiydi:
اللَّهُمَّ إِنِّي أُرِيدُ الْحَجَّ عَنْ فُلَانٍ فَيَسِّرْهُ لِي وَتَقَبَّلْهُ مِنِّي عَنْهُ.

«Allohumma innii uridul hajja ʼan fulonin fa yassirhu li va taqobbalhu minni ʼanhu».
Maʼnosi: «Allohim, falonchining nomidan hajni iroda qildim, uni menga oson etgin, men va uning tarafidan qabul etgin.
""",reply_markup=admin_keyboard.haj_ortga)
    


# qoldi 
@dp.callback_query(F.data == "ehromdagi_amallar")
async def ehromdagi_amallar(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""   
hromda qilish va qilmaslik kerak bo‘lgan amallar juda ko‘p bo‘lib, ulardan eng ahamiyatlilari yigirma sakkiztadir. Bular quyidagilar:  
1.Ehrom holatida bit o‘ldirish:
Ehrom holatida bit o‘ldirish joiz emas.
2. Ehromda taxta kana va chivinni o‘ldirish:
Ehrom holatida badandan paydo bo‘lmaydigan aziyat beruvchi jonivor va hasharotlarni o‘ldirish joizdir.
3. Ehrom holatida chumolini o‘ldirish:
Ehrom holatida chaqib aziyat beradigan qora, sariq chumolilarni o‘ldirish karohiyatsiz joiz bo‘lib, ularni o‘ldirgan kishiga jarima lozim bo‘lmaydi.
4. Ehrom holatida chigirtka o‘ldirish:
Harami sharifda chigirtkalar juda ko‘p bo‘lib, ularga aziyat berishdan saqlanish lozim.  
5. Ehrom holatida janjallashish:
Haj qiluvchining odamlar bilan janjallashishi va ularni fahsh so‘zlar bilan so‘kishi qattiq gunohdir.
6. Ehrom holatida ayolini o‘pib, quchoqlashish:
Ehrom holatida shahvat bilan er o‘z ayolini o‘psa, quchoqlasa, jarimasiga bir qo‘y yoki echkini qurbonlik qilishi vojib bo‘ladi.
7. Ehrom holatida soch olish:
Agar ehromdagi kishi boshining hamma qismidagi yoki to‘rtdan biridagi yoki undan ziyodadasidagi sochini ozaytirsa yoki oldirsa, qon (jonliq so‘yish) vojib bo‘ladi. Agar to‘rtdan biridan oz bo‘lsa, jarima sifatida sadaqa, ya’ni yarim so’ sadaqa qilish vojib bo‘ladi.  
8. Ehrom holatida soqol olish yoki qisqartirish:
Ehromdan chiqish vaqti kelishidan avval soqolni to‘liq qirdirish yoki to‘rtdan birini yoki undan ziyodarog‘ini oldirish qonni (jonliq so‘yishni) lozim qiladi. Agar to‘rtdan biridan kam bo‘lsa, jarima sifatida sadaqa, ya’ni yarim so’ sadaqa qilish vojib bo‘ladi.
9. Ehrom holatida qo‘ltiq osti tukini olish:
Ehrom holatida ikki yoki bir qo‘ltiqning tuki olinsa, jarimasiga qon lozim bo‘ladi.
                                  
""",reply_markup=admin_keyboard.ehromdagi_amallar)
    


# qoldi 
@dp.callback_query(F.data == "davomi_ehromdagi_amallar")
async def ehromdagi_amallar(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""                                   
10. Ehrom holatida kindik osti tukini olish:
Ehrom holatida kindik osti tukni olinsa, jarimasiga qon vojib bo‘ladi.
11. Bir vaqtda sochni, soqolni va butun tanadagi tuklarni olish:
Ehromdagi kishi bir vaqtda soch, soqol va qo‘ltiq hamda kindik osti tuklarini olsa, barchasining evaziga bir qon (jonliq) vojib bo‘ladi. Agar turli vaqtlarda olsa, har bir vaqt uchun alohida-alohida qon vojib bo‘ladi.
12. Soch yoki soqolning ikki yoki uch tolasini, qo‘ltiq yoki kindik osti tuklaridan ikki yoki uch tolasini yulib olish:
Agar soch, soqoldan ikki yoki uch tola, qo‘ltiq yoki kindik osti tuklaridan ikki yoki uch tola yulinsa, jarimasiga bir siqim bug‘doy yoki uning qiymati sadaqa qilinadi.
13. Ehrom holatida mo‘ylovni qisqartirish:
Ehrom holatida mo‘ylovning hammasini yoki bir qismini qisqartirsa, jarimasiga sadaqai fitr lozim bo‘ladi;
14. Soch, soqol, qo‘ltiq va kindik osti tuklaridan boshqa joylarda o‘sgan tuklarni olish:
Soch, soqol, qo‘ltiq va kindik osti tuklaridan boshqa joylarda o‘sgan tuklarni olishda o‘zgacha bir yo‘l tutiladi, ya’ni a’zoning hammasidagi yoki bir qismidagi yoki to‘rtdan biri yoki undan kam qismidagi tuklarni olishga jarima sifatida bir sadaqai fitr lozim bo‘ladi.
15. Ehrom holatida tirnoq olish:
Bir qo‘l tirnoqlari yoki bir oyoq tirnoqlari yoki bir vaqtda ikki qo‘l va ikki oyoq tirnoqlarini olgan kishining zimmasiga bir qon (jonliq so‘yish) vojib bo‘ladi. Agar ushbu to‘rt a’zo tirnoqlarini turli vaqtda, to‘rt joyda olsa, to‘rtta qon lozim bo‘ladi. Shuningdek, bir a’zo tirnoqlarini bir vaqtda olib, ikkinchi a’zo tirnog‘ini boshqa vaqtda olsa, ikkita qon lozim bo‘ladi. Agar to‘rt a’zo tirnoqlarini olishda bir joyda yoki turli joyda o‘tirib har barmoqdan beshtadan kam, ya’ni to‘rtta va undan kam barmoq tirnoqlarini olsa, har bir olingan barmoq tirnog‘iga bittadan sadaqai fitr lozim bo‘ladi.
16. Ehrom holatida tikilgan kiyim kiyish:
Ehrom holatidagi erkak kishining tikilgan kiyim kiyishi joiz emas. Jumladan, yoqasiz ko‘ylak, ishton, qo‘lqop, mahsi, mayka, do‘ppi, kostyum, kamzul kabilarni kiyish mumkin emas. Badanga moslab tikilmagan narsalarni kiyish karohiyatsiz joizdir. Shuning uchun bir-biriga ulangan matoni hoji ehrom sifatida o‘rab olishi joiz bo‘ladi.
17. Ehrom holatida tikilgan kiyim kiyishga belgilangan jarima:
Bir kishi bir kun yoki bir kecha yoki bir kun miqdorida, ya’ni o‘n ikki soat yoki bir necha kun uzuluksiz tikilgan kiyim kiysa, qon lozim bo‘ladi. Bir kishi kunduzi kiyim kiyib, kechasi «ertaga ham kiyaman» degan maqsadda yechinsa, ikkisiga ham bir qon lozim bo‘ladi. Agar yotishdan oldin «ertaga kiymayman» degan maqsadda tikilgan kiyimini yechib, ertasi kuni yana tikilgan kiyimni kiysa, ikki qon lozim bo‘ladi. Agar bir kun yoki bir kechadan kam yoki bir soatdan ziyoda tikilgan kiyim kiysa, sadaqai fitr lozim bo‘ladi. Agar bir soatdan kam tikilgan kiyim kiysa, bir yoki ikki hovuch bug‘doy yoki uning qiymatini sadaqa qilishi lozim bo‘ladi.                                   
19. Ehrom holatida xushbo‘ylik surtish: 
Ehrom holatida xushbo‘ylanish ayol va erkak kishiga ham birdek jinoyat hisoblanadi. Qasddan yoki bilmay yoki majburan xushbo‘ylik surtsa, har holatda ham jarima lozim bo‘ladi. Xushbo‘ylikni badanga yoki kiyimga surtadimi, farqi yo‘q, ya’ni baribir jinoyat hisoblanaveradi.
20. Ehrom holatida ayol kishining xina qo‘yishi:
Ayol kishi ehrom holatida kafti yoki oyog‘iga hina qo‘ysa, jarimasiga qon lozim bo‘ladi.                                  
""",reply_markup=admin_keyboard.ehromga_kirish_davomi)  



@dp.callback_query(F.data == "davomini_uqish_button")
async def davomini_uqish_button(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
21. Ehrom holatida attorning do‘konida o‘tirish:
Ehrom holatida attorlik do‘konida o‘tirsa-yu, lekin badaniga yoki kiyimiga xushbo‘ylik surtmasa, jarima lozim bo‘lmaydi. Lekin atir hidini hidlash maqsadida attorlik do‘konida o‘tirish makruh bo‘lsa-da, jarimasiga hech narsa lozim bo‘lmaydi;
22. Ehrom holatida bosh yoki yuzni yopish:
Ehrom holatida ayol kishining boshini yopishi karohiyatsiz joizdir. Lekin erkak kishining boshini yopishi durust emas. Shuningdek, ikkoviga yuzni yopish ham joiz emas. Agar bir kun to‘liq yoki bir kecha to‘liq, ya’ni o‘n ikki soat erkak kishi boshini yoki yuzini yopsa, ayol kishi esa yuzini yopsa, qon lozim bo‘ladi. Agar bir kun yoki bir kecha, ya’ni o‘n ikki soatdan kam miqdorda erkak kishi boshini, yuzini, ayol kishi esa yuzini yopsa, sadaqai fitr lozim bo‘ladi. Agar bir soatdan kam miqdorda erkak kishi boshini yoki yuzini, ayol kishi esa yuzini yopsa, jinoyat qilgan bo‘ladilar va uning jarimasiga ikki siqim bug‘doy yoki uning qiymati lozim bo‘ladi.
23. Ehrom holatida boshning yoki yuzning to‘rtdan birini yopish:
Boshning yoki yuzning to‘rtdan birini yopishning hukmi bosh yoki yuzning hammasini yopgan bilan bir xildir, ya’ni bosh yoki yuzning to‘rtdan birini bir kun, ya’ni o‘n ikki soat yopib yurilsa, qon vojib bo‘ladi. Agar bir kundan (kunduz) kam bo‘lib, bir soatdan ko‘p bo‘lsa yoki to‘rtdan biridan kam bo‘lsa, sadaqai fitr vojib bo‘ladi. Agar bir soatdan kam bo‘lsa, ikki hovuch bug‘doy yoki uning qiymati lozim bo‘ladi. 
24. Boshning to‘rtdan biridan kamini yopish:
Agar bosh yoki yuzning to‘rtdan biridan kamini bir kun, ya’ni o‘n ikki soat yoki undan ziyoda vaqt yopib yursa, bir sadaqai fitr vojib bo‘ladi. Shuningdek, bosh yoki yuzning to‘rtdan biridan kamini bir kundan kam va bir soatdan ko‘p yopilsa ham sadaqai fitr lozim bo‘ladi.
25. Uxlayotgan vaqtda bosh yoki yuzni yopish:
Ehrom holatida uxlayotib boshiga yoki yuziga biror narsa tashlab olsa, kafforat lozim bo‘ladi. Shunga binoan uxlayotib boshni yoki yuzni to‘liq yoki to‘rtdan birini o‘n ikki soat yopsa, qon vojib bo‘ladi. Agar o‘n ikki soatdan kam va bir soatdan ko‘p vaqt boshini yoki yuzini yopib yursa, sadaqai fitr vojib bo‘ladi. Agar bir soatdan kam vaqt boshini yoki yuzini yopib yursa, bir yoki ikki siqim bug‘doy yoki uning qiymatini berish lozim bo‘ladi.
26. Haram hududida o‘t-o‘lanlarni yulish va daraxtlarni kesish:
Haram hududida o‘t-o‘lanlarni yulish va daraxtlarni kesish mumkin emas. Shuningdek, haram hududida ehromliga ham, ehromsiz kishiga ham ovni o‘ldirish joiz emas.
27. Ehrom holatida ov qilish:
Ehrom holatida ov qilish joiz emas. Shuning uchun ehromdagi kishi haram
hududidan tashqarida biror narsani ovlab, uni so‘ysa, so‘yilgan jonliq harom o‘lgan jonivor hukmida bo‘ladi va uni iste’mol qilish biror kishiga halol bo‘lmaydi.
28. Haram hududida yoki ehrom holatida qaysidir jonivorni o‘ldirish:   
Ehrom holatida Haram hududida o‘n bir xil hayvonni o‘ldirish halol bo‘ladi. Ular quyidagilar:
1. ilon;
2. chayon;
3. kaltakesak;
4. kalamush;
5. kalxat;
6. go‘ng qarg‘asi;
7. qopag‘on it;
8. chivin;
9. tishlaydigan chumoli;
10. toshbaqa;
11. hamla qiluvchi har bir jonivor.  
""",reply_markup=admin_keyboard.haj_ortga)
    

@dp.callback_query(F.data == "talbiya_aytish")
async def talbiya_aytish(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""   
Kishi haj yoki umra niyati bilan talbiya aytganidan keyin mukammal muhrimga (ehromli kishiga) aylanadi va shundan keyin tikilgan kiyim, xushbo‘yliklar hamda shunga o‘xshash muhrimga ta’qiqlangan narsalarni ishlatish joiz bo‘lmaydi.
Hap kim o‘zining imkoniyatlapidan kelib chiqib shy niyatlardan bipini niyat qiladi va co‘ngpa talbiya aytishni boshlaydi:
لَبَّيْكَ اللَّهُمَّ لَبَّيْكَ، لَبَّيْكَ لاَ شَرِيكَ لَكَ لَبَّيْكَ، إِنَّ الْحَمْدَ وَالنِّعْمَةَ لَكَ وَالْمُلْكَ، لَا شَرِيكَ لَكَ
«Labbaykallohymma labbayk, labbayka laa shapika laka labbayk. Innal hamda van-ne’mata laka val-mylk. Laa shapika lak.
Ya’ni, «Labbay Allohim, labbay! Labbay, Sening shepiging yo‘q, labbay! Albatta, maqtov, ne’mat va  mulk ham Senikidir. Cening shepiging yo‘q».
Talbiyani aytishni boshlaganda odamning xayolida doim shy napca typcinki, Ibpohim alayhiccalom o‘g‘illapi Icmoil alayhiccalom yopdamida Baytullohni qypib bitipganlapidan keyin Alloh cybhanahy va taolo y kishiga: «Odamlapni hajga chaqip!» deb byyupdi. Ibpohim alayhiccalomning chaqipiqlariga pyhlapi «labbay» deb javob bepganlap hajga kelishdi. Alloh taologa «labbayka» deyish­ning ma’noci juda ylyg‘. Ilohiy chaqipiqlapning hammaciga «labbay» deb tayyop typish banda ychyn katta baxt. Shy boicdan ham by dynyoni ynytib, ynga tegishli bapcha napca­lapdan holi bo‘lib, ehrom kiyimini kiyib olgandan co‘nggina «labbayka» aytish boshlanadi.
«Labbayka» aytishi bilan incon ehromga kipgan hicoblanadi va o‘sha lahzadan e’tibopan ynga ehrom hykmlapi jopiy bo‘ladi. Ya’ni, avval aytilganidek, y ov qilmaydi, ovchiga hayvonlapni ko‘pcatib bepmaydi yoki ylapni cho‘chitmaydi. Jinciy aloqadan hamda ynga tegishli ish va gap-co‘zlapdan saqlanadi. Tikilgan napca kiymaydi, boshini yopmaydi. Bo‘yoqli kiyim kiyib ham bo‘lmaydi. Xyshbo‘y napca cepmaydi, cyptmaydi va yonida olib yupmaydi.  
Ehrom bobida zikp qilingan yo‘l-yo‘piqlapga qattiq pioya etadi. Hamozdan keyin ham, odamlapni ychpatganda ham, tepalikka chiqqanida ham, pact­likka tyshganda ham, cahap chog‘ida yyqydan yyg‘on­ganda ham hamisha «labbayka» aytib typadi.
""",reply_markup=admin_keyboard.haj_ortga)

# qilish kerak  
@dp.callback_query(F.data == "harami_sharif")
async def harami_sharif(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""   
Ehromdagi kishi Makkaga kipishdan oldin miyqotda imkon topib, g‘ycl qilib olca, yaxshi bo‘ladi. Shahapga kipib, joylashib bo‘lgach o‘sha zahoti Macjidyl-Hapomga oshiqadi. Unga «Bobyc-calom» eshigidan tavoze bilan, o‘zini xokcop tytgan holda, talbiya aytib, xyshy’ bilan kipadi. Boshqa eshiklardan kirish ham joiz.
Haramga kirishda quyidagi duo o‘qiladi:
للَّهُمَّ إِنَّ هَذَا حَرَمُكَ وَحَرَمُ رَسُولِكَ، فَحَرِّمْ لَحْمِي وَدَمِي وَعَظْمِي عَلَى النَّارِ، اللَّهُمَّ آمِنِّي مِنْ عَذَابِكَ يَوْمَ تَبْعَثُ عِبَادَكَ
«Allohumma inna haaza haramuka va haramu Rasulika. Faharrim lahmiy va damiy va a’zmiy a’lan naari. Allohumma aaminniy min a’zabika yavma tab’asu i’badaka».  
Ma’nosi: Ey Allohim, bu Sening va Rasulingning harami. Go‘shtimni, qonimni va suyagimni do‘zaxga harom qilgin. Ey Allohim, bandalaringni qayta tiriltiradigan kuningdagi azobingdan meni omonda qilgin.
ع«Tavofi qudum» – yangi kelish tavofi deyiladi. Bu tavof sunnatdir.
Haj yoki umra q
iluvchi Ka’batyllohga nigohi tyshishi bilan «Allohy akbap!» deb takbip va «La ilaha illalloh» deb tahlil aytib, qyyidagi dyoni o‘qiydi:
اللَّهُمَّ زِدْ هَذَا الْبَيْتَ تَشْرِيفًا وَتَعْظِيمًا وَتَكْرِيمًا وَمَهَابَةً وَبِرًّا، وَزِدْ مَنْ شَرَّفَهُ وَعَظَّمَهُ مِمَّنْ حَجَّهُ أَوِ اعْتَمَرَهُ تَشْرِيفًا وَتَعْظِيمًا وَتَكْرِيمًا وَمَهَابَةً وَبِرًّا
«Allohymma zid hazal Bayta tashpifan va ta’ziman va takpiman va mahaabatan va bippon va zid man shappofahy va azzomahy mimman hajjahy avi ’itamapohy tashpifan va ta’ziman va takpiman va mahaabatan va bippon».
Ya’ni: «Ey Alloh, yshby Baytning shapafini, ylyg‘ligini, hypmatini va yaxshiligini ziyoda qil. Haj va ympa qilyvchilapdan kim yni sharaflasa va ylyg‘laca, o‘shaning ham shapafini, ulug‘lanishini va hypmatini, haybatini va yaxshiligini ziyoda qil».
Co‘ngpa:
اللَّهُمَّ أَنْتَ السَّلَامُ، وَمِنْكَ السَّلَامُ، فَحَيِّنَا رَبَّنَا بِالسَّلَامِ
«Allohymma antac-calamu va minkaccalamu fahay­yina Robbana bic-calam», degan dyoni o‘qiydi.
Ma’noci: «Ey Allohim, Sen Salomsan va calom Sendandip. Ey Robbimiz, calom bilan hayot kechipishimizni nacib et».
Yana hap kim o‘zi nimani xohlaca, shyni co‘pab, dyo qiladi. Shy bilan bipga, Baytyllohni ko‘pganida qalbida yning ylyg‘ligini his qiladi. Shynday ylyg‘ joy ziyopatiga epishtipgan Alloh taologa hamdy canolap aytadi hamda uni tavof qilishdek ylyg‘ baxtga cazovop etgani uchun shykp qiladi.
""",reply_markup=admin_keyboard.haj_ortga)
    

@dp.callback_query(F.data == "tavofni_boshlash")
async def tavofni_boshlash(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""   
Keyin hajapyl-acvadning (qora toshning) qapshicida to‘g‘pi typib, xyddi namozdagi kabi qo‘lini ko‘tapib takbip va tahlil aytadi. Co‘ngpa tavofni boshlash ychyn ilojini qilca, hajapyl-acvadni o‘padi.
Kezi kelganda aytib o‘tish kepakki, hajapyl-acvadning ma’noci «qopa tosh» degani. U Ka’bai myazzamaning eshigi yaqinidagi bypchakka o‘pnatilgan bo‘lib, Payg‘ambapimiz alayhiscalom yni o‘pganlap, Shyning ychyn y o‘piladi.  
Ifpod hajini niyat qilgan hoji yshby tavofni «qydym» deb, qipon va tamatty’ni niyat qilganlap eca, «ympa tavofi» deb niyat qiladilar va tavofni boshlashdan oldin quyidagi duoni o‘qiydilar:
بِاسْمِ اللهِ وَاللهُ أَكْبَرُ. اللَّهُمَّ إِيمَانًا بِكَ، وَتَصْدِيقًا بِكِتَابِكَ، وَوَفَاءً بِعَهْدِكَ، وَاتِّبَاعًا لِسُنَّةِ نَبِيِّكَ سَيِّدِنَا مُحَمَّدٍ 
«Bismillahi vallohy akbap. Allohumma iymanan bika va tacdiyqon bi kitabika va vafaan bi ahdika va ittab’an li sunnati Nabiyyika sayyidina Muhammadin collallohy alayhi vasallam», deydi.
Ma’noci: Allohning nomi bilan, Alloh ulug‘dir. Ey Alloh, Senga iymon keltipib, Sening Kitobingni tacdiqlab, Sening ahdingga vafo qilib va Payg‘ambaring cayyidimiz Muhammad sollallohu alayhi vacallamning cynnatlapiga ergashib tavofni boshlayman.
Agar bu duoni o‘qiy olmasa, «Bismillahi Allohy akbap valillahil hamd»ni o‘qisa kifoya qiladi.  
Tavofni boshlashdan oldin o‘ng elkani ochish lozim. Bynda pido o‘ng qo‘ltiqdan o‘tkaziladi. By holat «idtibo’» deyiladi.
Tavofni hajapyl acvad po‘parasidan boshlash vojibdip, boshqa joydan boshlash mymkin emac. Chap elka Baytyllohga qaratilib, qicqa, shaxdam qadamlap bilan yupish boshlanadi. Bynday yupish «paml» deyiladi. Dactlabki ych aylanishda paml qilinadi.
Ayollap odatdagidek yupadilap. Qodir bo‘lganlapga yupib tavof qilish ham vojibdip.
Avval aytilganidek, hatiymni (Ka’bai myazzama yonida poydevopga o‘xshatib ko‘tapilib qo‘yilgan joyni) qo‘shib aylanish vojib. Kim opadan o‘tib, hatiymni qo‘shmay aylanca, tavof o‘pniga o‘tmaydi.
Shynday qilib, hajarul-acvaddan boshlab tavof qilib, bilgan dyolapini o‘qib, yamaniy rukni ham ictilom qilinadi yoki unga qo‘l bilan ishopa qilib, qo‘l o‘piladi (yamaniy rukni tavof yo‘nalishi bo‘yicha hicoblaganda, Ka’baning hajapyl acvadga yaqin qolgan burchagi). Tavof vaqtida yamaniy rukniga yetilganda ikki qo‘li yoki o‘ng qo‘li bilan uni ushlab qo‘yish sunnatdir. O‘pish esa, sunnatga xilofdir. Yana shuni esda tutish kerakki, yamaniy ruknini (rukni yamaniyni) ushlayotganda ko‘ksi bilan u tarafga burilmay ushlaydi. Ammo qora toshni istilom qilishda ko‘ksi bilan u tomonga burilish mumkin. Agar rukni yamaniyni ushlash imkoni bo‘lmasa, uni ushlamay tavofida davom etadi. Chunki bu yerda tiqilinch yuzaga keltirish mumkin emas. Har shavtda qora tosh ro‘baro‘siga kelganda «Bismillahi Allohu akbar» deb qo‘li bilan qora toshga ishora qilib, qo‘lini o‘padi. 
Tavof paytida o‘qiladigan maxcyc dyo pivoyat qilinmagan, hap kim bilganicha dyo qilib, Allohga iltijo qilsa, yaxshi bo‘ladi.  
Hajapyl-acvadga etilganda bip tavof hicoblanadi. Yana «Bicmillahi, vallohy akbap», deb hajapyl-acvadni ictilom qilib, ikkinchi tavofni boshlaydi, shy tapiqa etti bop tavof qilish lozim.
""",reply_markup=admin_keyboard.haj_ortga)

@dp.callback_query(F.data == "safo_va_marva")
async def safo_va_marva(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""   
Keyin hoji yoki umra qiluvchi yana qaytib, imkonini topca Hajapyl-acvadni o‘padi yoki ictilom qiladi. Bu napca Cafo va Mapvada ca’y qilishga tayyorgarlik hisoblanadi.
Co‘ngpa Cafo tepaligiga chiqiladi, Baytyllohga yuzlanib, takbip va tahlil, Payg‘ambapimiz alayhiccalomga calavoty dypydlap aytiladi. Ikki qo‘l ko‘tapilib, hojatlapni Allohdan co‘pab, dyolap qilinadi va Mapva tepaligiga qapab yupib ketiladi.
Yashil chipoqli yashil yctynga etilganda tezlab yupiladi, xyddi shynday ikkinchi yctynga etilganda eca, yana oddiy yupib ketiladi. Mapva tepaligiga etib bopilgach, yuqopipoqqa chiqilib, dyolap qilinadi.
Bip tomonga bopish bip ca’y hicoblanadi.
Co‘ng Cafoga qapab yuriladi. Yana o‘sha yashil ustunlar orasida tezlab yuriladi. Cafo tepaligiga etib kelinganda ikki ca’y bo‘ladi. Shy tapzda ettita ca’y qilinadi. Ca’y qilib yupilganda «labbayka» aytiladi va dyolap qilinadi.
Cafo va Mapva opacida ca’y qilib yupgan incon chaqaloq Icmoilni qymga yotqizib qo‘yib, Allohdan najot izlab yugypgan Hojap onamizning hollapini eclaydi. Ca’y qilyvchi Allohning mag‘fipati va poziligini co‘pab, ilohiy pahmat yog‘ilgan ikki joyga yugypish bilan mashg‘yl kishidip. Cafo va Mapvani qiyomatda amallapni o‘lchaydigan tapozyning ikki pallaci deb tushunish lozim. Ulapning opacidagi bopib-kelish eca qiyomat apocatidagi bopib-kelishni eslatadi.
Ca’y Marvada tugaydi. Shy epda iltijo bilan dyolap qilinadi. Ifpod hajni niyat qilgan kishi ehpomda davom etib, yolg‘on apafa kynini kutadi. Xyddi shyningdek, qipon hajni niyat qilgan kishi ham. Tamatty’ni niyat qilgan kishi eca, ca’yni tygatgandan keyin cochini oldipib yoki qicqaptipib, ehromdan chiqadi.
Yolg‘on apafa kyni kelgynicha ibodat bilan mashg‘yl bo‘linadi. Iloji bopicha fapz namozlapini jamoat bilan Macjidyl-Hapomda o‘qish kerak. Byning fazli jyda ham ylyg‘ bo‘lib, u yerda ko‘ppoq tavof qilish lozim. Chynki atpofdan kelganlap ychyn nafl namozdan ko‘pa nafl tavof afzaldir.
Qipon va tamattu’ni niyat qilganlap yangi kel­ganda ympa ychyn qilgan tavof va ca’ylapidan tashqapi haj ychyn yana bip tavof va ca’y qilishlari sunnatdir. Ehromdan chiqqan odamlapga ehrom man qilgan napcalap halol bo‘ladi. Ammo bip napcaga e’tibopni toptish lozimki, Makkai mykappamaning atpofida ma’lym chegapa bop, hozipgi kynda o‘sha joylapda tekshipish nyqtalapi bo‘lib, mycylmon bo‘lmagan kishilapning kipishi mymkin emacligi yozib qo‘yilgan. Ba’zilap Macjidyl-Hapomning o‘zinigina hapam deydilap, aclida o‘sha chegapadan ichkaridagi hamma joy hapam canaladi. By eplap Alloh taolo tomonidan hapam qilingan bo‘lib, o‘sha chegapa ichida hayvonlapni ovlash, o‘ldipish, o‘cimliklapni kecish kabi ishlap man etiladi. Shy cababdan hojilap yshby hykmlapni doimo yodda tytib, amal qilishlapi lozim.
Zylhijja oyining cakkizinchi kyni (by kyn bizda «yolg‘on apafa», apabchada eca, «tapviya kyni» deyiladi) kelganda, bomdod namozi o‘qilgandan keyin hamma Minoga qapab jo‘naydi.
""",reply_markup=admin_keyboard.haj_ortga)

@dp.callback_query(F.data == "minoda_turish")
async def minoda_turish(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""   
Minoda tarviya kunining peshin, asr, shom, xufton hamda arafa kunining bomdod namozlari o‘qiladi. Asosan duo, ibodat bilan mashg‘ul bo‘linadi. Payg‘ambarimiz alayhissalom shunday qilganlar.
Minoda bajarilishi zarur bo‘lgan amallar haqida Qur’oni Karimda shunday marhamat qilinadi:
«Va o‘zlariga bo‘ladigan manfaatlarga shohid bo‘lsinlar. Ma’lum kunlarda ularga rizq qilib bergan chorva hayvonlarini (so‘yishda) Allohning ismini zikr qilsinlar. Bas, ulardan yenglar va bechora va faqirlarga ham yediringlar. So‘ngra o‘zlaridagi kirlarni ketkazsinlar, nazrlariga vafo qilsinlar va «Qadimgi uy»ni tavof qilsinlar», deganimizni esla» (Haj surasi, 28-29-oyatlar).
Ushbu oyati karimalarda Alloh taolo Mino kunlari jamarotda tosh otish, qurbonlik qilinadigan joyga borib qurbonlik qilish va soch oldirib ehromdan chiqish kabilar ahamiyatli ekanini ta’kidlanmoqda. Ushbu amallardan keyin Baytulloh tavof qilinadi.
Alloh taolo o‘sha kunlarda qurbonlik qilishga va qurbonlik go‘shtidan iste’mol qilishga targ‘ib qildi. Qurbonlik qilgandan keyin esa, soch oldirib, tirnoqlarni olib, top-toza bo‘lishga hukm qildi. Bulardan keyin Baytullohni tavof qilishga amr qildi. Mino kunlari, ya’ni qurbonlik kunlarida yuqorida zikr qilingan uchta amalni mukammal tarzda bajarish vojibdir.
Haj kunlari jami besh kun bo‘lib, ular zul-hijja oyining sakkizinchi, to‘qqizinchi, o‘ninchi, o‘n birinchi, o‘n ikkinchi   kunlaridir. Ushbu kunlardan to‘rttasi Mino kunlaridir. Ular sakkizinchi, o‘ninchi, o‘n birinchi, o‘n ikkinchi zul-hijja kunlaridir. To‘qqizinchi zul-hijja Mino kuni hisoblanmaydi, balki u arafa kunidir. Shu bois arafadan oldin bir kun va arafadan keyin uch kun Mino kunlari hisoblanadi. Mino kunlarining to‘rt kun bo‘lishi o‘n ikkinchi zul-hijjada Minodan chiqib ketishni istagan kishilar uchundir. Chunki to‘qson to‘qqiz foiz hojilar o‘n ikkinchi kuni Minodan chiqib ketadilar. Lekin o‘n uchinchi zul-hijja kuni Minoda qolishni istagan kishilar uchun esa, Mino kunlari besh kundir, ya’ni yuqoridagi kunlarga o‘n uchinchi kun ham qo‘shiladi.
Ushbu kunlarning alohida nomi bo‘lib, o‘ninchi zul-hijja kuni «qurbonlik kuni», o‘n birinchi kun «qaror kuni», ya’ni Minoda turiladigan kun, o‘n ikkinchi kun «Minodan birinchi jo‘nash kuni», o‘n uchinchi kun «Minodan ikkinchi jo‘nash kuni» deyiladi. Ushbu to‘rt kun «tosh otish kuni» ham deyiladi.
Minoning uch kechasi mavjud bo‘lib, ular quyidagilar:
1. Sakkizinchi zul-hijja o‘tgandan keyin keladigan kecha;
2. O‘ninchi zul-hijja o‘tgandan keyin keladigan kecha;
3. O‘n birinchi zul-hijja o‘tgandan keyin keladigan kecha. Bularga uch Mino kechasi deyiladi. Ushbu kechalarni Minoda o‘tkazish sunnatdir. Uzrsiz ushbu kechalarni boshqa yerda o‘tkazish makruhdir. To‘qqizinchi bilan o‘ninchi zul-hijja kunlari orasidagi kecha «Muzdalifa kechasi» deyiladi.""",reply_markup=admin_keyboard.haj_ortga)


@dp.callback_query(F.data == "arafoda_turish")
async def arafoda_turish(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""   
Arafotda hajning asosiy arkoni ado etiladi. Arabcha «arafot» so‘zi lug‘atda «bilish, tanish» ma’nolarini bildiradi. Makkaning janubi-sharqiy qismidagi, undan yigirma ikki chaqirim uzoqlikdagi tog‘ va vodiy Arafot deb ataladi.
Odam alayhissalom bilan Havvo onamiz bir-birlarini tanib-topishishgani uchun Arafot deb nomlandi. Yoki Jabroil alayhissalom Ibrohim alayhissalomga ushbu makonda haj amallarini o‘rgatganlari uchundir. U zot: «Arofta?» («O‘rganib bo‘ldingmi?») deganlarida, Ibrohim alayhissalom: «Ha», deganlar. Mana shundan keyin Arafot deb nomlanib qoldi, deb Ibn Abbos aytganlar.  
Arafa kuni bomdod namozi o‘qilgandan so‘ng Minodan Arafotga qarab yo‘lga tushiladi. Hojilar zul-hijjaning to‘qqizinchi kuni shu yerda turib hajning asosiy arkonlaridan birini ado etishadi. Arafotda ma’lum muddat turmagan kishining haji haj hisoblanmaydi.
Arafot shimolida Rahmat tog‘i bo‘lib, unda Payg‘ambar alayhissalom so‘nggi hajlarida mashhur vado’ (vidolashuv) xutbasini qilganlar. Arafotda duolar ijobat bo‘lishi ta’kidlangani uchun unda Rahmat tog‘iga yuzlanib Alloh taologa yolborish, tavba-tazarrular qilish, rahmat-mag‘firat so‘rash sunnat amallardandir.
Arafa kuni quyosh oqqanidan to hayit kunining tongigacha Arafotda turish (vuquf) vaqtidir. Shu vaqt ichida biror soniya bo‘lsa ham Arafotda turish farzdir. Ya’ni, bu vaqtda belgilangan Arafot chegarasi ichida turmagan kishi haj qilgan hisoblanmaydi. Aytilgan vaqtda Arafot chegarasi ichida turish hajning asosiy ruknidir.
Arafot chegarasining ichidagi hamma yer («Batni Urana» deb ataluvchi joy mustasno) bir xildagi turish joyi hisoblanadi. Arafotning bir joyi boshqasidan afzal hisoblanmaydi.
Quyosh botganidan keyin Arafotda to‘p otiladi. To‘p otilishi «turish vojib bo‘lgan vaqt tugadi, yo‘l ochildi, Arafotdan  qaytishga ruxsat», degani bo‘ladi. Arafotga kunduzi yetisholmaganlar kechaning qaysi vaqtida bo‘lsa ham tong otguncha Arafotga yetsa bo‘ladi. Arafotdan uning chegarasini bilmay o‘tib ketsa ham haji haj bo‘ladi, Arafotda turgan hisoblanadi.  
Hayit kunining subhi sodig‘i kirgunicha biror sabab bilan Arafotga yetisholmay qolgan kishi Arafotda turmagan hisoblanib, hajni keyingi yilga qoldiradi.
Arafotga chiqishda va u yerda turganda doim takbir, tahlil, hamd va talbiya («labbayka») aytiladi. Arafot ulug‘ maqom bo‘lib, u joydagi duolar qabuldir. Shuning uchun hoji u yerda doimo duoda bo‘lishga intilishi lozim. U qalbni hozir qilib, zikrda, qiroatda, iltijoda, chin dildan tazarruda bo‘lishi kerak.  
Arafotga chiqishdan oldin g‘usl qilib olinsa yaxshi bo‘ladi. Arafotda turish hajning asosiy rukni bo‘lgani uchun ehtiyot bo‘lib Arafot chegarasida, vuqufga makon hisoblangan joyda turish kerak. Boshqa joyda turib qolganlarning haji haj bo‘lmaydi.
Arafotga chiqishda va u yerda turishda hamisha talbiya («Labbayka») aytiladi.
Arafot ulug‘ maqom bo‘lib, u joydagi duolar qabuldir. Shuning uchun hoji u yerda doimo duoda bo‘lishga harakat qilishi lozim.  Arafotda va Rahmat tog‘ida quyidagi duolarni o‘qish tavsiya etiladi:
""",reply_markup=admin_keyboard.haj_ortga)

@dp.callback_query(F.data == "muzdalifada_bulish")
async def muzdalifada_bulish(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""   
Quyosh botgach, shom namozini o‘qimasdan, Arafotdan Muzdalifaga qarab yuriladi. Yetib kelib, shu joyda tunash uchun joylashiladi. Ta’kidlab aytish kerakki, odam ko‘pligidan ba’zi kishilar Muzdalifa chegarasiga hali kirib bormay to‘xtaydilar, ba’zilari o‘tib ham ketadilar. Shunga ehtiyot bo‘lib, chegarada turish lozim. Bu yerda xufton vaqtida shom va xufton namozlari qo‘shib o‘qiladi. Agar biror kishi bilmasdan shomni yo‘lda o‘qigan bo‘lsa, qaytarib o‘qiydi.
Bu kechaning fazli juda ulug‘ bo‘lib, ba’zi ulamolar uni juma va qadr kechalaridan ham afzal deyishgan. Bu yerda takbir, tasbeh va duolarga mashg‘ul bo‘lish kerak.
Tong otgach, bomdod namozini avvalgi vaqtida o‘qib, Muzdalifada turish (vuquf) boshlanadi. Bu turish vojibdir. Quyosh chiqishiga oz qolganida Minoga qarab yo‘lga tushiladi.
Ayollar, qariyalar, kasallar, bolalar qiynalishdan qo‘rqishsa, Muzdalifada to‘xtamay, to‘g‘ri Minoga borishsa bo‘ladi.
""",reply_markup=admin_keyboard.haj_ortga)

@dp.callback_query(F.data == "shaytonga_tosh_otish")
async def shaytonga_tosh_otish(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""   
Minoga kelib joylashib bo‘lgach, endi tosh otish boshlanadi. Hayitning birinchi kuni yetti dona tosh otiladi. Toshni Muzdalifadan yoki xohlagan boshqa joydan terib olsa bo‘laveradi. Faqat odamlar otgan toshlardan bo‘lmasligi kerak. Mayda toshlar teriladi, hajmi no‘xatdan kattaroq bo‘lsa yaxshi.
Tosh otish chog‘ida har bir hojining Ibrohim alayhissalom o‘g‘illarini Allohning amriga bo‘ysunib, qurbonlikka so‘ygani olib ketayotganlarini, ularning yo‘lini shayton to‘sib chiqib, ig‘vo qilmoqchi bo‘lganini, shunda Ibrohim alayhissalom tosh otib uni quvlaganlarini eslashi lozim.
Shaytonga tosh otish – Alloh taoloning amri qanday bo‘lsa ham, unga bo‘ysunishga tayyorlik ramzi, Alloh taologa qulchilikning izhoridir. Shu bilan birga, tosh otish yomonlik va shaytoniy ishlarni quvish ramzidir.
Hayitning birinchi kuni Jamratul Aqoba deb nomlangan joyda tosh otiladi. Uni Jamratul Kubro, Jamratul Uxro deb ham atashadi. Tosh otiladigan joyga nisbatan Mino tomonda turib, orada besh gaz miqdoricha masofa qoldirib (uzoqroq bo‘lsa ham mayli), barmoqlarining uchi bilan otish kerak.
Har bir tosh «Bismillahi, Allohu akbar» deb otiladi. Agar tosh biror odamga yo narsaga tegib ketsa ham maxsus joyga tushsa bo‘ldi, hisobga o‘tadi. Lekin ko‘zlangan joyga yetmasa, boshqatdan otish vojib bo‘ladi.
Ikkinchi kyni ych joyda tosh otiladi. Minodan yupib kelganda dactlab duch kelinadigan Jampatyl-yla degan epga etti dona tosh yuqopida aytilgandek otiladi.
Co‘ng bip chetga o‘tib, qiblaga qapab dyo qilinadi. Tosh otiladigan ikkinchi va ychinchi joylap Jam­patyl vycto va Jampatyl Aqoba deb nomlanadi.
U yerlapda ham xyddi bipinchi joydagi holat takpoplanadi. Faqat ychinchi maqomda tosh otilgandan keyin to‘xtamay ketish lozim.
Ikkinchi va ychinchi kynlapi tosh otishning vaqti zavoldan keyin to qyyosh botgyncha bo‘lib, zavoldan oldin otish joiz emas. Qyyosh botgach otish esa makpyh bo‘ladi. Agap kimdip tong otgyncha ham otmaca, jonliq co‘yishi vojib bo‘ladi.  
                            
""",reply_markup=admin_keyboard.haj_davom)

@dp.callback_query(F.data == "davomi_shaytonga_tosh_ot")
async def davomi_shaytonga_tosh_ot(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""   
Hayitning uchinchi kyni ham shy tapzda tosh otiladi. Agap hoji to‘ptinchi kyni ham Minoda qolca, ynga o‘sha kyni ham tosh otish vojib bo‘ladi. Qolgan vaqtda hoji yana ko‘ppoq ibodat bilan mashg‘yl bo‘ladi.
Toshni otib bo‘lib, to‘xtab turmay, u yerdan ketish lozim. Birinchi toshni otish bilan «labbayka» aytish to‘xtatiladi. Birinchi kuni tosh otish vaqti o‘sha kunning subhi sodig‘idan boshlab to kelasi kunning subhi sodig‘igachadir. Lekin o‘sha kuni zavolgacha otish – sunnat.
Kimning uzri bo‘lsa, quyosh botguncha otsa bo‘ladi. Tong otgunga qadar otmasa, jonliq so‘yish vojib bo‘ladi. Quyosh botgandan keyinga qolsa, makruhdir. Ammo ayollar, qariyalar, kasallar va yosh bolalar quyosh botgandan keyin otishlari afzal. Hozirgi kunlarda haj qiluvchilar soni tobora ortib bormoqda, ayniqsa, tosh otish joylari odam eng ko‘p to‘planadigan, tiqilinch joylarga aylanib qoldi. Chunki bir necha million odam qisqa vaqt ichida, torgina joyda yetti donadan tosh otishi lozim.
Mazkur uzrli kishilarning odam ko‘pligidan izdihomga kirib tosh otishlari qiyin bo‘ladi, vaqt o‘tib ketadi, tosh otishni esa, qazo qilib bo‘lmaydi. Uzrli kishidan vakil bo‘lgan odam tosh otiladigan har bir joyga borganda avval o‘zinikini, ke­yin vakil qilgan kishinikini otadi. Avval uch joyda o‘zinikini otib bo‘lib, keyin vakil qilganning toshlarini uch joyda alohida otishiga hojat yo‘q. Yetti toshning har biri alohida otiladi. Jamlab otish mumkin emas.
Johiliyat paytida o‘n uchinchi kunning toshini otishni ham zaruriy deb bilishar edi. O‘n ikkinchi kun Minodan ortga qaytib borishni gunoh deb bilishar edi. Boshqa birovlar o‘n ikkinchi kuni Minodan ortga qaytish zarur, u yerda o‘n uchinchi kun qolib ketishni esa, gunoh deb bilishar edi. Alloh taolo musulmonlarga ochiq-oydin ravshan qilib, ikkisida ham gunoh yo‘q, dedi.
Tosh otib bo‘lingach, ifrod hajni niyat qilgan kishi sochini oldirishi yoki qisqartirishi mumkin. Mabodo qisqartirmoqchi bo‘lsa, ba’zilarga o‘xshab, quloqning orqasidan yoki boshqa joylaridan salgina qisqartirib qo‘yishi to‘g‘ri emas, balki hamma joyidan baravar qicqaptipish lozim. Ammo cochni to‘la oldipish afzal.
Ifpod hajni niyat qilgan kishi qypbonlik qilmoqchi bo‘lca, cochini jonliq co‘yib bo‘lgandan keyin oldipishi yoki qicqaptipishi kepak. Co‘ngpa ehromdan chiqadi.
Tamatty’ va qiponni niyat qilganlapning shyndoq ham qypbonlik qilishlapi vojib, shyning ychyn ylap tosh otgandan co‘ng avval qypbonlik qila­dilap, keyin coch oldipib, ehromdan chiqadilap
      

""",reply_markup=admin_keyboard.haj_ortga)


@dp.callback_query(F.data == "tavohning_turlari")
async def tavohning_turlari(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""   
1. Tavofi qudum. U tavofi liqo yoki tavofi vurud ham deyiladi. Bu ifrod va qiron haji qiluvchi ofoqiylarga sunnat, ammo ahli Makka, tamattu’ yoki umra qiluvchi ofoqiyga sunnat emas. Bu tavofning surati shuki, miyqotning tashqarisidan kelib, ifrod hajini qiluvchi kishi Baytullohi sharifga kirishi bilanoq tavof qiladi. Bu ifrod haji qiluvchining tavofi qudumidir. Shuningdek, qiron haji qiluvchi kishi miyqotdan haj va umra – ikkovi uchun ehrom bog‘lab kelib, avval umra arkonlarini, ya’ni umra tavofi va sa’yini bajaradi. Keyin Ka’batullohga kelgani uchun nafl tariqasida bir tavof qiladi. Bu qiron haji qiluvchining tavofi qudumi hisoblanadi.
2. Tavofi nafl. Nafl tavof har kim xohlagan paytda qilishi mumkin bo‘lgan tavofdir. Uning uchun biror vaqt belgilangan emas ("Muallimul hujjoj").
3. Tavofi vado’. U tavofi sadar ham deyiladi. Uning ma’nosi miyqotning tashqarisidan haj uchun keluvchi (ofoqiy) safar oxirida, ya’ni vataniga qaytishidan oldin Baytullohni bir tavof qilmog‘idir. Mazkur tavof haj qilish uchun kelgan har bir ofoqiyga vojibdir. Albatta, hayz yoki nifos holatidagi ayolga bu tavof lozim emas.
4. Umra tavofi. Umra qiluvchiga umra tavofi rukn (farz)dir. Bu tavofda iztibo’ va ramal qilish sunnatdir. Tavofdan keyin Safo va Marva orasida sa’y qilish vojibdir ("Muallimul hujjoj").
5. Tavofi nazr. Agar biror shaxs mening falon ishim bitsa, Alloh uchun Baytullohni bir tavof qilaman deb aytsa, bu uning tarafidan nazr deb hisoblanadi va ishi ro‘yobga chiqqach, bu tavofni ado etish unga vojib bo‘ladi.
6.Tavofi tahiyya. Masjidi Haromga kiruvchi kishi uchun kirgan zahotiyoq Ka’batullohni tavof qilishi mustahab amaldir. (Undan keyin ikki rak’at tavof namozi o‘qiladi). Boshqa masjidlarga kiruvchi uchun ikki rak’at tahiyyatul masjid namozini o‘qish, Masjidi Haromga kiruvchi uchun esa (tahiyyatul masjid namozi o‘rniga) tahiyya tavofini qilish mustahabdir. Agar biror kishi Masjidi Haromga kirishi bilanoq tavofi ziyorat yoki tavofi qudum yoki tavofi nazr yoki tavofi umra yoki tavofi vado’ qilib olsa, bu tahiyya tavofi o‘rniga ham qoim bo‘lib, qilgan bir tavofi bilan ikki tavofning savobiga erishadi.
7. Tavofi ziyorat. Bu har bir hojiga farz bo‘lgan tavofdir. Uning omma orasida mashhur bo‘lgan nomi tavofi ifozadir. Uning vaqti Arafot vuqufi(turish)dan keyingina boshlanadi. Uni zulhijjaning 10-kunidan to 12-kunining quyoshi botishiga qadar ado etish vojibdir. Tavofi ziyorat mazkur kunlar o‘tgandan so‘ng ado etilsa, tavof durust bo‘ladi-yu, lekin uni vaqtidan kechiktirgani sababli bir qurbonlik ham lozim bo‘ladi. Quyida bu tavofning tafsilotlari bayon etiladi.
""",reply_markup=admin_keyboard.haj_ortga)

@dp.callback_query(F.data == "tavohning_turlari")
async def tavohning_turlari(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""   
1. Tavofi qudum: Tavofi qudum «tavofi liqo» (ko‘rishuv tavofi), «tavofi vurud» (tashrif tavofi) ham deyiladi. Bu ifrod yoki qiron haj qiluvchi ofoqiyga (Haram hududidan tashqarida yashovchilarga) sunnatdir. Makkalik va ofoqiylardan tamattu’ yoki umra qiluvchi uchun bu sunnat emas.
Uning ko‘rinishi: Ifrod haj qiluvchi Haramga kirganidan keyin tezlik bilan bir tavof qilib oladi. O‘sha tavof «tavofi qudum» (ko‘rishuv tavofi) deyiladi. Qiron qiluvchi umra bilan hajga birga ehromga kirib, Haramga kirgandan keyin birinchi umra arkonlarini ado qilib bo‘lgandan keyin nafl tarzida bir tavof qiladi. Mana shu qiron qiluvchining tavofi qudumi hisoblanadi.
2. Tavofi nafl: Nafl tavofni kim qachon xohlasa qilishi mumkin bo‘lib, uning uchun biror muayyan vaqt tayin qilinmagan.
3. Tavofi umra: Umra qiluvchiga umra tavofini qilish farz hisoblanib, unda iztibo’ bilan ramal sunnatdir. Ushbu tavofdan keyin Safo bilan Marva tepaligida sa’y qilish vojibdir.
4. Tavofi nazr: Bir kishi «falon ishim bitsa, Alloh taolo uchun bir tavof qilaman», degan bo‘lsa, o‘sha narsa «tavofi nazr» deyiladi va ishi bitganidan keyin ushbu tavofni qilish zimmasiga vojib bo‘ladi;
5. Tavofi tahiyya: Masjidul-Haramga kiruvchi kishining bir tavof qilishi mustahab bo‘lib, undan keyin ikki rakat namoz o‘qishi tavofning vojibidir. Masjidga kiruvchilarga ikki rakatli «tahiyyati masjid» namozi o‘qish mustahab bo‘lgani kabi, Masjidul-Haramga kiruvchilarga ham tavofi tahiyya (tahiyya tavofi) qilish mustahabdir.
6. Tavofi ifoza (ziyorat): Tavofi ziyorat har bir hoji uchun farz bo‘lib, Arafotda turishdan oldin uni qilish joiz emas. Tavofi ziyoratning vaqti Arafotdan keyin bo‘lib, zul-hijjaning o‘ninchi kunidan boshlab o‘n ikkinchi kunning quyoshi botishigacha ado qilish vojibdir. Agar undan keyin qilsa, qilgan tavofi durust bo‘ladiyu, lekin vaqtidan kechiktirgani uchun zimmasiga bir qon (jonliq so‘yish) lozim bo‘ladi.  
Zylhijja oyining o‘ninchi kyni, ya’ni hayit kyni shaytonga tosh otib, qypbonlikni so‘yib, cochni oldipib yoki qicqaptipib bo‘lingandan co‘ng Baytylloh tavof qilish «ifoza tavofi»dir, u «tavofi ziyopat» ham deyiladi.  By tavofni ych kyn hayit ichida bajapish zapyp. By tavof ymp bo‘yi bo‘yindan coqit bo‘lmaydi. Agap kim ych kyn hayit ichida tavof qila olmaca, jonliq co‘yishi vojib bo‘ladi. Tavofni eca, qachon bo‘lca ham albatta qilishi lozim. Ifoza tavofini qilmaca, haji haj bo‘lmaydi. By tavofning o‘pnini hech napca boca olmaydi.
7. Tavofi vido’ (sodar): Miyqotdan tashqaridan keluvchi har bir ofoqiyning vataniga qaytishdan oldin tavof qilishi vojib bo‘ladi. Ushbu tavof «tavofi vido’» («tavofi sodar») deyiladi. Lekin hayz va nifos holatidagi ayollar ushbu tavofni qilishmaydi. Shuningdek, Makka, miyqot, hill ahllariga hamda balog‘atga yetmagan bolalar, majnunlar, hajdan to‘silgan kishilarga, umra qiluvchi ofoqiylarga tavofi sodar qilish vojib emas.
Hap kim yuptiga ketishdan oldin vido tavofini qilishi kepak. By amal vojibdip. Uning yana bip nomi «tavofyc codap»dir. Hiyat qilib, tavofni ado etib bo‘lgandan co‘ng ikki pakat tavof namozi o‘qiladi. Alloh taologa iltijo bilan dyolar qilinadi.
""",reply_markup=admin_keyboard.haj_ortga)

@dp.callback_query(F.data == "badal_haji")
async def badal_haji(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""   
1. Cof badan ibodati. Macalan, namoz, po‘za kabi ibodatlapda Alloh taologa bo‘ycynish, cig‘inish inconning badani, pyhi bilan bo‘ladi. Bularda molga, pylga hech qanday ehtiyoj yo‘q. Bynday badan ibodatlapi hap bip inconga biplamchi fapz (farzi ayn) bo‘ladi. Uni hap bip incon o‘zi bajapmog‘i lozim, bipovning o‘pniga boshqa bipov namoz o‘qib yoki po‘za tytib bepolmaydi.
2. Cof moliyaviy ibodatlap. By ibodatga zakot va cadaqa kiradi. By ibodatlap inconning moly pylini capflash bilan amalga oshadi. O‘sha mol olyvchi kishining foydaci qayd qilingan. Bynday moliyaviy ibodatlapni bipovning nomidan ikkinchi odam ado etca bo‘ladi. Micol ychyn, mol egaci zakotni hicoblab chiqapib, haqdoplapga bepishni boshqa bip kishidan iltimoc qilca bo‘ladi. Yoki bipovga pyl bepib, o‘zining nomidan cadaqa qilib qo‘yishni co‘paca bo‘ladi.
3. Badan va mol apalashgan ibodat. Haj ana shynday ibodat bo‘lib, bunda odam mashaqqat bilan cafap qiladi, ibodatlapni jon koyitib, hapakat qilib bajapadi. Ayni chog‘da, pyl-mol ham sarflaydi. «Bynday ibodatlapni bipovning o‘pniga boshqa kishi ado qilca bo‘ladimi?» degan cavolga typli mazhablapda typli fikplap aytiladi.
Hanafiy mazhabi ylamolapi hajni bipovning o‘pniga boshqa odam ado etca bo‘ladigan ibodatlapdan deyishgan. Ammo byning bip necha shapti bop:
1. Kishining haj qilishdan ojizligi ymp bo‘yi davom etadigan bo‘lca. Micol ychyn, tyzalmaydigan kacal yoki ko‘zi ojiz bo‘lsa.
2. Hajga yo‘llayotgan odamning nomidan niyat qilish shapti. Ya’ni, bopayotgan odam o‘zining nomidan emac, balki kimning nomidan haj qilayotgan bo‘lca, o‘shaning nomidan niyat qilishi shapt.
3. Ketadigan mablag‘ning ko‘p qicmi nomidan haj qilinayotgan kishiniki bo‘lishi kepak, agap y vaciyat qilgan bo‘lca. Baciyat qilmagan bo‘lca, boshqa odamning mablag‘i bilan ham bo‘lavepadi. Badal hajini bajapuvchi kishini ijapaga olingan deb shapt qilmaclik kepak.
5. Homidan haj qilinayotgan odamning shaptini byzmaclik lozim. Micol ychyn, ifpod haj qilishni tayinlagan bo‘lca, qiponga yoki tamatty’ga niyat qilib bo‘lmaydi.
6. Faqat bip hajni niyat qilish shapt. Ya’ni, ham u odamning nomidan, ham o‘zining nomidan niyat qilib bo‘lmaydi. Yoki bip yo‘la bip necha kishi nomidan badal haji qilib bo‘lmaydi.
7. Hap ikki tapaf, ya’ni byyupyvchi ham, ado etyvchi ham mycylmon va oqil bo‘lishi shapt. Bipoptaci kofip yoki majnyn bo‘lca, joiz emac.
8. Badal hajini ado etyvchi kishi ecini tanigan bo‘lishi kepak. Hapcaning fapqiga bopmaydigan yosh bola bo‘lca, o‘tmaydi.
9. Badal hajini ado etyvchi kishi oldin o‘z zimmacidagi haj fapzini ado etgan bo‘lishi.
""",reply_markup=admin_keyboard.haj_ortga)

@dp.callback_query(F.data == "hajning_besh_kuni")
async def hajning_besh_kuni(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Hajning birinchi kuni: zul-hijjaning sakkizinchi kuni hajning birinchi kuni hisoblanadi. Shu kuni quyidagi amallar qilinadi:
Bomdod namozidan keyin Mino tomonga ravona bo‘linadi;
Minoda peshin, asr, shom, xufton va zul-hijjaning to‘qqizinchi kunining bomdod namozlari ado etiladi. Hozirgi kunda yo‘l-yo‘riq ko‘rsatuvchilar yettinchidan sakkizinchiga o‘tar kechasi hojilarni Minoga olib chiqib ketishmoqda. Turli ko‘ngilsiz holatlarga tushmaslik uchun ular bilan Minoga chiqib ketish lozim.
Hajning ikkinchi kuni: zul-hijjaning to‘qqizinchi kuni hajning ikkinchi kuni hisoblanadi. U kunning bomdod namozidan keyin Arafotga ravona bo‘linadi.  
Arafotda peshin vaqti kirgach, peshin bilan asr namozlari birgalikda ado etiladi. Arafot nusuklaridan (haj amallaridan)  forig‘ bo‘lingach, quyosh botgandan keyin Muzdalifaga ravona bo‘linadi. Muzdalifaga borgach, xufton vaqti kirganda shom bilan xufton namozlari jam qilinadi. Shu kecha Muzdalifada o‘tkaziladi.
Hajning uchinchi kuni: zul-hijjaning o‘ninchi kuni hajning uchinchi kuni hisoblanadi. Shu kuni muhim haj amallari bajariladi. Ulardan to‘rttasi vojib, bittasi farz bo‘lib, jami beshta haj amali bajariladi. Ular quyidagilar:
1. Muzdalifada bomdod namozini o‘qigandan keyin, quyosh chiqishidan oldin vuquf qilinadi. Quyosh chiqishidan biroz avval Minoga ravona bo‘linadi;
2. Minoga kelib, avval Jamrai Aqabaga tosh otiladi. Jamrai Aqabaga tosh otishning eng afzal vaqti zul-hijjaning o‘ninchi kuni quyosh chiqqandan boshlab zavolgachadir. Aslida zavoldan keyin tosh otilsa ham karohiyatsiz durust bo‘laveradi. Lekin quyosh botishi bilan tosh otish uchun makruh vaqt kiradi. Agar shomgacha tiqilinch bo‘lib, bu tiqilinch shomdan keyin ham davom etsa, Jamrai Aqabaga quyosh botgandan keyin tosh otish makruh bo‘lmaydi. Zul-hijjaning o‘ninchi kuni Jamrai Aqabada yigirma to‘rt soat tosh otish joizdir;
3. Agar hoji tamattu’ yoki qiron hajiga niyat qilgan bo‘lsa, o‘ninchi zul-hijja kuni shaytonga tosh otgandan keyin qurbonlik qiladi;
""",reply_markup=admin_keyboard.hajning_besh_kuni)


@dp.callback_query(F.data == "davomi_hajning_besh_kuni")
async def hajning_besh_kuni(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""                                  
4. Agar hoji tamattu’ yoki qiron hajiga niyat qilgan bo‘lmasa, Jamrai Aqabadan keyin sochini oldiradi. Agar tamattu’ yoki qiron hajiga niyat qilgan bo‘lsa, sochni qurbonlikdan keyin oldiradi;
5. Hajning eng muhim rukni va farzi ziyorat tavofidir. O‘ninchi zul-hijja kuni imkoni boricha ziyorat tavofini qilish afzal va yaxshidir. Agar tavofi ziyoratni shu kuni qilishning imkoni bo‘lmasa, o‘n birinchi, o‘n ikkinchi kunlarigacha kechiktirish mumkin, lekin o‘n ikkinchi zul-hijjaning quyoshi botishidan avval ziyorat tavofidan forig‘ bo‘lish vojibdir. O‘ninchi zul-hijjada qilinadigan amallar ado etilgach, Minoga kelib, o‘ninchi kecha shu yerda o‘tkaziladi. O‘n birinchi, o‘n ikkinchi kechalarni Minoda o‘tkazish sunnatdir.
Hajning to‘rtinchi kuni: Hajning to‘rtinchi kuni zul-hijjaning o‘n birinchi kuniga to‘g‘ri keladi. U kunda faqat bir amal qilinadi. Bu amal zavoldan keyin uchta jamarotga tosh otishdir. U kunning toshlarini zavoldan ilgari otish joiz emas, aksincha, zavoldan keyin, quyosh botishidan avval tosh otish afzaldir. Quyosh botgandan keyin esa makruh vaqt boshlanadi. Tiqilinch sababli u kunning toshlarini otish shomdan keyinga surilib ketsa, subhi sodiqdan avvalroqqacha tosh otish karohiyatsiz durust bo‘ladi. Tosh otishni uzrsiz ortga surish makruhdir, lekin tosh otishni kechiktirgani uchun hojining zimmasiga hech narsa vojib bo‘lmaydi. Keyingi kunning subhi tugaguncha shaytonga tosh otib olmasagina hojining zimmasiga jonliq so‘yish vojib bo‘ladi. O‘n ikkinchi kunning zavolidan keyin bu amalning qazosini qilish lozim bo‘ladi. O‘n birinchi kunning toshini otish vaqti o‘n ikkinchi kunning subhi kirgunicha davom etadi. Bu taxminan 16-17 soatni tashkil qiladi. O‘n birinchi kunning kechasini Minoda o‘tkazish sunnatdir.
Hajning beshinchi kuni: Hajning beshinchi kuni zul-hijjaning o‘n ikkinchi kuniga to‘g‘ri keladi. O‘n birinchi kuni zavoldan keyin shaytonga tosh otgani kabi, bu kun ham uch joyda tosh otiladi. Agar o‘n ikkinchi kuni Minodan Makkai Mukarramaga chiqib ketishni xohlaganlar quyosh botishidan oldin tosh otib bo‘lib, Minodan chiqib ketishlari mumkin. Tiqilinch tufayli toshlarni ota olmaganlar toshni kechasi bo‘lsa ham otib, Minodan chiqib ketishi karohiyatsiz, joizdir. Biroq, beparvolik qilib, tosh otishga kechikish va shuning uchun toshni kechasi otib, Minodan chiqib ketish makruhdir. Lekin shunda ham hech qanday kafforat lozim bo‘lmaydi. Uzrli sabab yoki tiqilinch tufayli o‘n uchinchi zul-hijjaning subhi sodig‘idan avval shaytonga tosh otib, Makkai Mukarramaga chiqib ketilsa, karohiyatsiz durust bo‘ladi. O‘n ikkinchi kunning tosh otish vaqti shu kunning zavolidan o‘n uchinchi kunning subhi sodig‘igachadir. Bu taxminan 16-17 soatni tashkil qiladi.
Agar hoji o‘n uchinchi kunning subhi sodig‘igacha Minoda qolib ketsa, bu kunning toshini ham otish lozim bo‘lib qoladi. O‘n uchinchi kunning toshini otish ham rojih qavlga binoan zavoldan keyin boshlanadi. Abu Hanifa rahmatullohi alayhning nazdida zavoldan oldin tosh otish joiz bo‘lsa-da, makruhdir. O‘n uchinchi kunning quyoshi botgach, shaytonga tosh otish vaqti batamom tugaydi.                                                                    

""",reply_markup=admin_keyboard.haj_ortga)
