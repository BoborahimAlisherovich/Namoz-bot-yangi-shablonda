from keyboard_buttons import admin_keyboard
from aiogram import  F
from aiogram.types import Message,CallbackQuery
from loader import dp

 #  zakot = ==============---
@dp.message(F.text=="ZAKOT")
async def message(message:Message):
    await message.answer(text="ZAKOT  <a href='https://t.me/mukammal_namoz/87'>Bizning kanal</a>   ",reply_markup=admin_keyboard.zakot)  


@dp.callback_query(F.data == "zakot_orqa_button")
async def zakot_nima(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=""" Zakot <a href='https://t.me/mukammal_namoz/87'>Bizning kanal</a> """,reply_markup=admin_keyboard.zakot)

@dp.callback_query(F.data == "zakot_nima")
async def zakot_nima(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
«Zakot» so‘zi lug‘atda «poklik» va «o‘sish» degan ma’nolarni anglatadi. Zakot bergan kishining moli poklanadi. Qachon zakotini bersa, poklanadi, bo‘lmasa yo‘q. Zakoti berilgan molga baraka kiradi, ko‘payib, o‘sadi.
Shar’iy istilohda «Zakot – maxsus moldan maxsus juzni maxsus shaxsga Allohning roziligi uchun shariatda tayin qilingandek mulk qilib berishdir».
«Maxsus mol» – nisobga yetgan mol demakdir. «Maxsus juz» – zakot beruvchining mulkidan ajratiladigan miqdordir. Misol uchun, bir kishiga «Ushbu uyda bir yil o‘tirib turishing senga zakot», deb bo‘lmaydi. «Maxsus shaxs» deganda zakot olishga haqli bo‘lgan shaxs nazarda tutilgan. «Allohning roziligi uchun» jumlasi esa zakotning ibodat niyati bilan berilishi kerakligini anglatadi. «Shariat tayin qilgan» deganda zakot chiqarish miqdori shariatda ko‘rsatilgan miqdorga to‘g‘ri kelishi kerakligi nazarda tutiladi. Ozgina sadaqa berib, «shu zakot» deb bo‘lmaydi. «Mulk qilib berish» degan jumladan esa «o‘sha berilayotgan mol uni oluvchiga mulk bo‘lmagunicha zakot bo‘lmaydi» degan ma’no anglanadi.
Zakot Islomning besh ruknidan biri bo‘lib, shariat farz qilgan amaldir.
Zakot Islomdagi besh ruknning uchinchisidir. U islomiy ibodat bo‘lib, aqiydaning ajralmas qismidir. Kim zakotni inkor etsa, kofir bo‘ladi, bordiyu uni ado etmasa, osiy bo‘ladi. 
Fiqh kitoblarimizda ibodatlar qismi alohida, muomalalar qismi alohida bayon qilingan bo‘lib, zakot ibodatlar qismida kelgan. Zakotda ibodat ma’nosi bo‘lishi bilan birga, ulug‘ insoniy g‘oyalar, axloqiy ko‘rinishlar, ruhiy qadriyatlar ham mavjud. Unda faqat moddiy ma’no emas, balki ma’naviy, ruhiy, axloqiy ma’nolar ham o‘z aksini topgan. Zakotda uni beruvchiga ham, zakot oluvchiga ham, ular yashab turgan jamiyatga ham ko‘plab dunyoviy va uxroviy foydalar bor.
Zakot ibodati tufayli zakot beruvchi kishi o‘zining ixtiyoridagi mol-dunyo Alloh tomonidan berilgan ne’mat ekanini, bu mol-dunyoga vaqtinchalik ega bo‘lib turganini tushunib yetadi. Shuning uchun u qo‘lidagi mol-dunyoni Alloh ko‘rsatgan halol-pok yo‘llarga sarflashga intiladi. Bu har bir shaxs, har bir jamiyat uchun iqtisodiy muammolarni hal qilishda juda muhim va zarur omildir. 
Zakot ibodati nafaqat zakot beruvchi va zakot oluvchiga, balki jamiyatga ham ulkan foyda keltiradi. Shuning uchun zakot ibodati tatbiq qilingan jamiyat 
""",reply_markup=admin_keyboard.zakot_orqa_button)
  


  
@dp.callback_query(F.data == "fiqh_hukumlari")
async def fiqh_hukumlari(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Zakotberuvchida bo‘lishi lozim shartlar:
1. Musulmon bo‘lish.
2. Balog‘atga yetgan bo‘lish.
3. Oqil bo‘lish. 
4. Hur bo‘lish.
II. Zakotfarz bo‘lishi uchun molda bo‘lishi lozim shartlar:
1. Nisobgayetishi.
2. To‘liqmulk bo‘lishi.
3. Fe’lanyoki taqdiran o‘suvchi mol bo‘lishi.
4. Hojatiasliyadan ortiqcha bo‘lishi.
5. Qarzdanxoli bo‘lishi.
6. Bir yil to‘lgan bo‘lishi kerak.
III. Zakotning to‘g‘ri bo‘lishi shartlari:
1. Niyat.
2. Haqdorga mulk qilib berilishi.
1. Niyat. 
Zakotni ado etish vaqtida yoki uni ajratish vaqtida niyat qilish shartdir. Molning hammasini sadaqa qilib yuborsa, niyat qilish shart emas.
Zakotning to‘g‘ri bo‘lib, o‘rniga o‘tishi uchun eng muhim shart zakot berishni niyat qilishdir. Chunki Islomda hech bir ibodat niyatsiz bo‘lmaydi. 
2. Haqdorga mulk qilib berilishi. 
Zakot to‘g‘ri bo‘lishi uchun ajratilgan mol zakot beruvchi tomonidan haqdorlarga mulk qilib berilishi kerak. Foydalanib turishga berilgan buyumlar zakot bo‘lmaydi, shuningdek, kishilarni taomlantirib, «mana shu mening zakotim» deyish ham joiz emas. Lekin taom sotib olib, zakot deb niyat qilib bersa bo‘ladi.
Hanafiy mazhabi bo‘yicha, aqli zaif yoki yosh bolaga zakot berib bo‘lmaydi. 
«Sadaqa qilindi» degani «birovga bir narsa mulk qilib berildi» deganidir. «Faqirlargadir» deganda ham arab tili qoidasida ularga mulk qilib berish tushuniladi.
""",reply_markup=admin_keyboard.zakot_orqa_button)
  
 
@dp.callback_query(F.data == "chorvaning_zakoti")
async def chorvaning_zakoti(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Chorva hayvonlari zakotining shartlari:
1. Yaylovdao‘tlaydigan bo‘lishi.
2. Ishchi hayvonbo‘lmasligi.
Yaylovda o‘tlaydigan bo‘lishi, ya’ni yilningko‘p qismida ommaviy yaylovda o‘tlab, semirib, bolalabyurishi. Yilning ba’zi vaqtida qo‘ldan yem yesa ham bo‘laveradi. Yilning ko‘p qismidaqo‘lda boqilgan hayvonlardan zakot berilmaydi. Chunki ularniboqishga shaxsiy mehnat va sarf-xarajat ko‘p ketganbo‘ladi.
Yilning ko‘p qismida yaylovda boqilgan hayvonlarga esa mehnat ham, sarf-xarajatham juda oz ketadi. Asosan ko‘pchilikning haqqi bo‘lmish yaylovdan foydalaniladi. Shuning uchun ko‘pchilik ichidagi kambag‘al-miskinlarga zakotberish kerak bo‘ladi.
Ishchi hayvon bo‘lmasligi. Chorvahayvonlarining ishchisidan, ya’ni aravaga, omochga qo‘shiladigan, yuk tashishgaishlatiladigan, miniladigan, juvozda, suv chiqarishda yoki shunga o‘xshash ishlarda foydalanib turiladiganidan zakot olinmaydi, chunki bundayhayvonlar hojati asliya va ish vositasi hisoblanadi, o‘suvchi mol emas. Qolaversa, ularni ishga solibtopilgan narsalardan zakot chiqariladi. Ana o‘sha zakotyo‘lida xizmat qilganlari uchun ham ularning o‘zlaridan zakot olinmaydi.
Tuyadan olinadigan zakot miqdori
Tuyaning nisobi beshtadir. To‘rtta tuyasi bor kishiga zakot farz bo‘lmaydi. Lekin egasi o‘zi xohlab, bersa, ixtiyoriga havola. 
Hanafiy mazhabida tuyaning soni bir yuz yigirma bitta bo‘lgandan boshlab buning zakotiga tuyaga zakot berish boshlangan vaqtdagi zakot qo‘shilib, xuddi avvalgidek ortib boraveradi. Tuyalar ikki yuzga yetganda qo‘shimcha qo‘shish yana qaytadan boshlanadi.
Qoramolning zakoti
Qoramoldan zakot berish tartibi:
O‘ttizta qoramoldan bir yoshli erkak yoki urg‘ochi buzoq; 
Qirqta qoramoldan ikki yoshli erkak yoki urg‘ochi buzoq, 
Qirqtadan oshganda to oltmishtagacha ikki yoshli erkak yoki urg‘ochi buzoq hamda qirqtadan oshgan har bir bosh uchun ana shunday sifatli buzoq qiymatining qirqdan biri berib boriladi. 
Oltmishtadan oshganda har o‘ttizta qoramol uchun bir yoshli erkak buzoq, har qirqta qoramol uchun ikki yoshli urg‘ochi buzoq zakot qilib beriladi.
Masalan, qoramollar soni 41 ta bo‘lganda ikki yoshli erkak yoki urg‘ochi buzoq hamda shunday buzoq qiymatining qirqdan biri beriladi. 42 ta bo‘lsa, ikki yoshli erkak yoki urg‘ochi buzoq hamda shunday buzoq qiymatining qirqdan ikkisi beriladi va hokazo.
Qo‘y-echkilarning zakoti
40 ta qo‘y yoki echkidan bitta, 121 dan ikkita, 201 tadan uchta, 400 tadan to‘rtta, so‘ng har yuztadan bitta qo‘y zakot beriladi.
Qo‘ylarning soni qirqtaga yetganda nisobga yetgan bo‘ladi va ulardan bir dona qo‘y zakotga chiqariladi. Qo‘ylarning umumiy soni o‘ttiz to‘qqizta bo‘lsa ham, zakot farz bo‘lmaydi. Bunda zakot berish-bermaslikni egasining o‘zi biladi. Beraman desa, beradi, bermasa, gunohkor bo‘lmaydi. 
Qirqtadan to bir yuz o‘n to‘qqiztagacha bo‘lgan qo‘ylardan bir dona qo‘y zakotga beriladi. Bir yuz yigirmataga yetgandan so‘ng to ikki yuzga yetguncha ikkita qo‘y berilaveradi. Ikki yuzdan o‘tganidan keyin esa uchta qo‘y beriladi. 
Uch yuzdan oshgandan keyin esa har yuztasidan bitta qo‘y zakotga chiqariladi. Bunda qo‘y boqishni ko‘paytirish maqsadida ular qancha ko‘p bo‘lsa, shuncha oz zakot olish yo‘lga qo‘yilgan.
Echki ham qo‘y hisobida bo‘lishini unutmaslik kerak.
Otning zakoti
Quyidagi otlardan zakot olinmaydi:
1. Miniladigan, ishlatiladigan va harbiy xizmatga tayyorlangan otlar.
2. Yem berib boqiladigan otlar.
Demak, tijorat uchun boqiladigan ot, xachir va eshaklardan zakot olinadi.
""",reply_markup=admin_keyboard.zakot_orqa_button)
 

@dp.callback_query(F.data == "naqtdan_olinadigan_zakot")
async def naqtdan_olinadigan_zakot(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Naqd puldan qanday qilib zakot chiqariladi? Uning shartlari qanday?
Naqd puldan zakot chiqarish farz bo‘lishi uchun unda quyidagi shartlar mavjud bo‘lishi lozim:
1. Pul nisobga yetgan bo‘lishi.
2. Bir yil to‘lishi.
3. Qarzdan xoli bo‘lishi.
4. Hojati asliyadan ortiq bo‘lishi.
Pul nisobga yetgan bo‘lishi. Tilla pul bo‘lsa, yigirma dinor, kumush pul bo‘lsa, ikki yuz dirham nisob ekanini yaxshi bilib oldik. Ammo hozir tilla ham, kumush ham pul sifatida ishlatilmaydi. Qog‘oz puldan qanday qilib zakot chiqariladi? Uning nisobi qancha?
Kumush xalqaro miqyosda pul o‘rnida umuman qabul qilinmay qo‘ydi. Tilla esa pul o‘lchovi sifatida dunyo bo‘yicha maqbul bo‘lib turibdi. Shuning uchun ulamolar qog‘oz pulni tillaning qiymati bilan o‘lchash kerak, degan fikrga kelganlar. Payg‘ambar sollallohu alayhi vasallamning vaqtlarida yigirma dinor pulning og‘irligi yigirma misqol bo‘lardi. Yigirma misqol esa sakson besh grammga teng.
Demak, 85 gramm tillaning bahosi qog‘oz pulning nisobi bo‘ladi. Kimda 85 gramm tillaning qiymatiga teng yoki undan ko‘p qog‘oz pul bo‘lsa, zakot berishi farz bo‘ladi. U odam pulini hisoblab turib, ikki yarim foizini, ya’ni qirqdan bir bo‘lagini zakotga berishi kerak.
Bir yil to‘lishi kerak. Naqd pullardan yoki ularning o‘rniga o‘tadigan narsalardan zakot farz bo‘lishi uchun lozim bo‘lgan shartlardan biri – o‘sha pul nisobga yetgan holida to‘liq bir yil turishi kerak. Hanafiy mazhabi bo‘yicha, yilning o‘rtasida pul nisobdan kam bo‘lsa ham, yilning boshida va oxirida to‘liq bo‘lsa, zakot farz bo‘laveradi.
Foydaga kelgan mollardan: oylik maosh, ish haqqi, mukofotlar, hunar qilib topilgan pullar, ijaraga qo‘yilgan imoratlar, mehmonxona, zavod yoki fabrika va mashinalardan tushgan foydalarni ham asl sarmoyaga qo‘shib turib zakot chiqariladi.
Qarzdan xoli bo‘lishi kerak. Puldan zakot farz bo‘lishi uchun u qaytarib berilishi zarur bo‘lgan qarz bo‘lmasligi kerak. Aytaylik, birovning qo‘lida nisobga yetgan puli bor. Shu bilan birga, qarzi ham bor. U avval qarzini berishi kerak. Uni berganidan keyin puli nisobdan kam bo‘lib qolsa, unga zakot farz bo‘lmaydi.
Hojati asliyadan ortiq bo‘lishi kerak.  Deylik, bir kishining qo‘lida nisobga yetgan puli bor. Ammo u o‘ziga va qaramog‘idagi kishilarga qishlik yoki yozlik kiyim olishi kerak. Yoki bir yillik oziq-ovqatining sarf-xarajati ham bor. Uy sotib olishi, uyiga kerakli anjomlar, kasb-hunari uchun asboblar, mingani, zarurat uchun ulov yoki o‘qigani kitob olishi kerak. Ushbu narsalarni yoki ulardan ba’zilarini sotib olganidan keyin puli nisobdan kam bo‘lib qolsa, unga zakot farz bo‘lmaydi. Sotib olishidan oldin esa puli nisobga yetgan bo‘lsa, farz bo‘ladi. Chunki zakot o‘ziga to‘q, o‘z ehtiyojlaridan ortiqcha puli bor boy odamlarga farzdir.
""",reply_markup=admin_keyboard.zakot_orqa_button)
 

@dp.callback_query(F.data == "tijorat_moli")
async def tijorat_moli(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Sotib olingan har bir narsa ham tijorat moli bo‘lavermaydi, chunki ularning orasida shaxsiy va oilaviy foydalanish uchun narsalar ham bo‘ladi. Faqatgina sotish, foyda olish niyatida xarid qilingan narsagina tijorat moli hisoblanadi.
Ulamolarimiz: «Tijoratda ikkita asosiy unsur: niyat va amal bor», deyishadi. Niyat – foyda ko‘rish maqsadi bo‘lsa, amal – oldi-sotdidir. Ushbu ikki unsur bir bo‘lgandagina, tijorat bo‘ladi. Biri bo‘lib, ikkinchisi bo‘lmasa, tijorat bo‘lmaydi.
Shunga ko‘ra, birov o‘zi uchun biror narsa olib, uni ishlatib yursa-yu, yaxshiroq foyda chiqsa sotib ham yuborish maqsadi bo‘lsa, u narsa tijorat moli bo‘lmaydi. Chunki uni aslida o‘zi uchun olgan. Aksincha, sotib, foyda ko‘rish niyatida olgan narsasidan o‘zi vaqtincha, yaxshiroq xaridor chiqquncha foydalanib tursa ham, u narsa tijorat moli hisoblanadi. Ammo ushbu narsani «Sotmayman, o‘zim foydalanaman», deb niyat qilsa-yu, foydalanib yursa, o‘sha mol tijorat moli bo‘lmaydi va undan zakot ham bermaydi.
Tijorat mollaridan zakot farz bo‘lishining shartlari ham xuddi puldagi shartlarga o‘xshaydi, ya’ni buning uchun mol nisobga yetishi, bir yil to‘lishi, qarzdan xoli bo‘lishi va hojati asliyadan ortiq bo‘lishi lozim.
Zakot berish vaqti kelganda tojir qo‘lidagi va hisob raqamidagi pullarini, savdoga qo‘yilgan mollaridan bir yil to‘lganini va odamlarga bergan qarzlaridan qaytib kelishiga ko‘zi yetganlarini jamlab hisoblaydi, so‘ngra buning ikki yarim foizini zakotga chiqaradi.
Hisoblash vaqtida tijorat do‘koni binolari, binoning asbob-anjomlari, tijorat mollari qo‘yiladigan joylar, peshtaxta va shunga o‘xshash sotuvga qo‘yilmagan narsalar hisobga olinmaydi. Tijorat mollarining qiymati zakot chiqarilayotgan kundagi bahosida o‘lchanadi. Zakotni tijorat mollarining o‘zidan yoki qiymatidan chiqarsa ham bo‘ladi. Ammo kambag‘allarga foydaliroq bo‘lgani uchun qiymatidan chiqarilsa, yaxshi bo‘ladi.
Zakot, sadaqai fitr, kafforat, ushr va nazrlarda ularning qiymatini berish ham joiz. Bir yil to‘lgandan keyin kamaysa, zakotning o‘sha kamaygan miqdordagi ulushi soqit bo‘ladi. Zakot nisobdadir, afv qilingan narsada emas. 
Agar qirqta tuyaga bir yil to‘lgandan keyin o‘n beshtasi halok bo‘lsa, binti maxoz berish vojib bo‘ladi.
Yilning o‘rtasida ko‘rilgan foyda o‘z jinsidan bo‘lgan nisobga qo‘shiladi. 
Nisobni mukammal qilish uchun tilla kumushga va tijorat mollari qiymati ila ikkisiga qo‘shiladi. 
Nisobning yil davomida noqis bo‘lgani (kamaygani) hisob emas. Zakotni bir yil va undan ham avvalroq berish joiz.
Shuningdek, bir nisobga sohib bo‘lgan kishi bir necha nisobning zakotini oldindan bersa bo‘ladi («Kifoya»dan).
Bu yerda zakotga oid bir necha masala muolaja qilinmoqda. Avvalo, zakot va unga o‘xshash moliyaviy ibodatda beriladigan narsalarning o‘zini bermay, qiymatini bersa ham bo‘lishi haqida so‘z bormoqda.
Zakot, sadaqai fitr, kafforat, ushr va nazrlarning qiymatini berish ham joizligi haqida hanafiy mazhabining ulamolari: «Qiymatini chiqarsa yaxshi bo‘ladi, ba’zi vaqtlarda qiymatini berish miskin va faqirlar uchun manfaatliroq bo‘ladi», deyishadi. Zamondosh ulamolarimiz bu boradagi barcha ma’lumotlarni to‘liq va atroflicha o‘rganib chiqib, hanafiy mazhabining tutgan yo‘li hozirgi zamon uchun munosib, degan fikrga kelishgan.
Zakotga beriladigan hayvon o‘rniga uning qiymatini bersa bo‘ladimi? Hanafiy mazhabida: «Zakotga beriladigan hayvon o‘rniga uning qiymati berilsa bo‘ladi», deyiladi. Qiymat har yurtning o‘z narxida va zakot berilayotgan kunning bahosiga qarab bo‘ladi.
""",reply_markup=admin_keyboard.zakot_orqa_button)
 

@dp.callback_query(F.data == "taqinchoqlar_zakoti")
async def taqinchoqlar_zakoti(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Ushbu masalada fiqhiy mazhablar ikkiga bo‘linishgan:
1. Hanafiy mazhabi: «Ayollarning taqinchoqlaridan zakot chiqariladi», degan.
2. Molikiy, shofe’iy va hanbaliy mazhablari: «Ayollarning odatdagi tilla va kumush taqinchoqlaridan zakot chiqarish farz emas», degan.
Hanafiy ulamolarimiz tilla-kumush buyumlar, idishlar va taqinchoqlardan zakot berish borasida quyidagi fikrlarni aytishgan:
1. Tilla va kumushdan yasalgan turli buyumlar, idishlar uchun zakot berish farzdir. Avvalo, Islom bu narsalarni isrofgarchilik, manmanlik hamda kambag‘allarning ko‘ngli cho‘kishiga sabab bo‘lgani uchun harom qilgan. Musulmon odam mazkur narsalarni uyida saqlamagani ma’qul. Ammo kim ushbu qoidaga rioya qilmay, ularni o‘ziga mulk qilib olgan bo‘lsa, o‘sha narsalarning o‘zi yoki boshqa mulk bilan qo‘shilganda nisobga yetsa, zakot berishi farz bo‘ladi.
Ulamolarimizdan ba’zilari: «Bunday idish va buyumlarning nisobga yetganini aniqlash uchun ularning og‘irligi e’tiborga olinadi, agar 85 grammga yetsa, nisobga yetgan bo‘ladi», deganlar. Ba’zilari esa: «Qiymati e’tiborga olinadi, chunki bu narsalar san’at asari sifatida bahosi yana ham ortgan bo‘ladi», deyishadi.
2. Erkak kishilarning tilla va kumush taqinchoqlaridan ham zakot olinadi. Erkak kishiga shariatimizda bitta kumush uzuk taqishga ruxsat berilgan. Lekin shunday bo‘lsa ham, o‘sha narsalardan taqinchog‘i bo‘lsa, uni taqish yoki taqmasligidan qat’i nazar, o‘ziga mulk bo‘lib turgani uchun zakot beradi. Uni boshqa mulklarga qo‘shib nisob hisobiga kiritadi. Bu narsalarning hammasi o‘sishi kerak bo‘lgan molni o‘lik mol qilib qo‘yish hisoblanadi va Islomda qoralanadi. Zarurat uchun, kishining sog‘lig‘i uchun qilingan tilla va kumush narsalar, masalan, tish, burun va shunga o‘xshashlardan zakot berilmaydi.
3. Marjon, la’l, zumrad, olmos, yoqut kabi narsalardan zakot berilmaydi. Chunki bu narsalar o‘smaydigan mol hisoblanadi. Faqat ayollarning zebu-ziynati shaklida ishlatiladi.
4. Tilla va kumush taqinchoqlar taqish uchun emas, pulni band qilish uchun, jamg‘arma qilish uchun, sotib-foyda ko‘rish uchun olib qo‘yilgan bo‘lsa, ulardan zakot berish vojib bo‘ladi. Agar shunday qilinmasa, odamlar zakot berishdan qochib, puliga tilla va kumush taqinchoqlar olib qo‘yishga o‘tadi. Qolaversa, bunday taqinchoqlar ayollarning hojati uchun emas, pulni ushlab va uning foydasini olish uchun jamg‘arilgan bo‘ladi.
""",reply_markup=admin_keyboard.zakot_orqa_button)
 

@dp.callback_query(F.data == "toshlar_zakoti")
async def toshlar_zakoti(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Tog‘dan topilgan feruzadan zakot berilmaydi, chunki bunga o‘xshash narsalar tuz kabi yerning bir bo‘lagi hisoblanadi.
Shuningdek, marvarid, la’l, zumrad, olmos, yoqut kabi narsalardan zakot berilmaydi, chunki bu narsalar o‘smaydigan mol hisoblanib, faqat ayollarning zebu ziynati sifatida ishlatiladi.
Odamlar tomonidan yerga ko‘milgan narsa topilsa va unda kalimai shahodat yoki shunga o‘xshash islomiy alomatlar bo‘lsa, uning hukmi tushib qolgandan keyin topib olingan narsaning hukmi kabi bo‘ladi. Albatta, bu kabi narsalar musulmonlarning mulki hisoblanadi. Bu holda xuddi topib olingan narsa kabi mazkur dafinaning ham egasini topib, unga qaytarib berish uchun shariatda qabul qilingan choralar ko‘riladi. Egasi topilmasa, topilmaning hukmida bo‘ladi.
Hanafiy, molikiy va hanbaliy mazhabi ulamolari: «Dafinaning zakoti davlat mulkiga qo‘shiladi», deyishgan. Shofe’iy mazhabida esa: «Dafinaning zakoti boshqa zakotlar beriladigan haqdorlarga beriladi», deyilgan. Nima bo‘lganda ham, dafinaning zakotini berish kerak.
""",reply_markup=admin_keyboard.zakot_orqa_button)

@dp.callback_query(F.data == "olishi_mumkinlar")
async def olishi_mumkinlar(callback: CallbackQuery):
    await callback.message.answer(text="""
Zakot olishi harom bo‘lganlar quyidagilardir:
Orasida tug‘ishganlik va er-xotinlik aloqasi borlar.
Bu toifaga kishining tuqqanlari, ya’ni ota-onasi, bobo-momolari necha pog‘ona yuqori bo‘lsa ham kiradi. Mazkur kishi ana o‘shalarga zakotini berishi mumkin emas.
O‘zining quliga, bir qismini ozod qilgan quliga zakot berilmaydi.
Qul xojaning mulki bo‘ladi. O‘zining mulkiga zakot berish durust emas.
Zimmiyga emas. Unga (zimmiyga) zakotdan boshqasini bersa bo‘ladi.
Zimmiyga zakotdan boshqasini bersa bo‘ladi. Islom davlati soyasida yashayotgan «ahli zimma» deb ataluvchi boshqa din vakillariga zakotdan berib bo‘lmaydi. Chunki zakot musulmonlardan olinib, musulmonlarga berilishi shart. Ammo ahli zimmaga nafl sadaqalardan, sadaqai fitrdan bersa bo‘ladi. Chunki avval aytilganidek, zakot moliyaviy ibodat bo‘lib, uni berish uchun ham, olish uchun ham musulmon bo‘lish kerak.
Fosiq kishiga zakot bersa bo‘ladimi?
«Fosiq» deb ba’zi gunoh ishlarni qilib nomi chiqqan odamga aytiladi. O‘zi musulmon odam-u, lekin gunoh ishlar ham qilgan bo‘ladi. Qadimgi ulamolarimiz bunday odamlarga zakot berish mumkin, deyishgan va zakotni olgandan keyin uni fisq va gunoh ishlarga sarflamasligi aniq bo‘lishi kerak, degan shartni qo‘yishgan.
Kuch-quvvati yetarli, biror kasbga qodir kishilarga zakotdan berilmaydi.
Kasb-korga qodir bo‘lgan, sog‘lom kishiga zakotdan ulush berilmasligi uchun unda quyidagi shartlar mavjud bo‘lishi kerak:
1) O‘z kasbiga yarasha ishi mavjud bo‘lishi;
2) Bu ish halol ish bo‘lishi;
3) Mazkur ish toqatidan tashqari, chidab bo‘lmaydigan darajada bo‘lmasligi;
4) Bu ish unga munosib, o‘ziga o‘xshash kishilarning obro‘sini to‘kmaydigan ish bo‘lishi;
5) O‘zida va qaramog‘idagilarda yetarli kasb qilish imkoni bo‘lishi.
Tarkidunyo qilib, ibodatga berilgan odamga zakotdan ulush berilmaydi.
""",reply_markup=admin_keyboard.zakot_orqa_button) 
    
@dp.callback_query(F.data == "zakot_beruvchi")
async def zakot_beruvchi(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Zakotni ado qiluvchi bandaning zimmasida bajarishi lozim bo‘lgan quyidagi vazifalar bor:
1. Zakotdan murod nimaligini fahmlashi kerak. U uch narsadan iborat: Alloh taoloning muhabbatini da’vo qiluvchini o‘zi muhabbat qo‘ygan narsasini chiqarishi bilan sinash; halokatga olib boruvchi baxillik sifatidan poklanish; mol-mulk ne’matiga shukr qilish.
2. Riyokorlikdan xoli bo‘lish uchun zakotni sir tutish. Uni izhor qilishda faqirni xorlash bor. Agar «zakotni bermadi» degan tuhmatdan qo‘rqsa, faqirlarga jamoat ichida ochiqchasiga beradi. Boshqalarga pinhona ravishda beradi.
3. Zakotini minnat va ozor bilan buzmaydi. Inson faqirga ehson qilayotganida  minnat hosil bo‘lishi mumkin. Aslida esa, uning zakotini olgan faqir kishi Alloh taoloning unga buyurgan haqqini qabul qilib, unga yaxshilik qilayotgan, uning molini birovning haqqidan poklayotgan bo‘ladi. Zakot beruvchi yaxshiroq o‘ylab ko‘rsa, uning zakot chiqarishi u bilan faqir o‘rtasidagi muomala emas, balki mol ne’matiga shukrdir. Shuning uchun faqir odam faqirligi uchun haqoratlanmasligi kerak, chunki fazl mol-mulkning borligi yoki yo‘qligida emas.
4. Berayotgan narsasini kichik sanashi lozim, chunki ishni katta sanagan odam u bilan faxrlanadi. Yaxshi ish uch narsa bilan: uni kichik sanash, tezlatish va sir tutish ila tugal bo‘ladi.
5. Zakot beruvchi molidan eng halolini, eng yaxshisini va o‘ziga eng mahbubini chiqarsin.
6. Sadaqasini berishga loyiq odam topish. Ularda quyidagi sifatlar bo‘lishi kerak:
Birinchi sifat: taqvo.
Ikkinchi sifat: ilmli bo‘lish.
Uchinchi sifat: «Ne’mat berish yolg‘iz Alloh taoloning O‘zidan bo‘ladi», deb e’tiqoddagi odam bo‘lishi.
To‘rtinchi sifat: faqirligini yashiradigan, hojatmandligini bekitadigan va oshkora shikoyat qilmaydigan bo‘lish.
Beshinchi sifat: ayolmand, qarzga duchor bo‘lgan, og‘ir kasallikka chalingan kishilar bo‘lsin.
Oltinchi sifat: qarindosh-urug‘lardan bo‘lsin, chunki ularga qilingan sadaqa – ham sadaqa, ham silai rahmdir. Kimda ushbu sifatlardan ikkitasi yoki ko‘prog‘i jam bo‘lsa, zakotni ana shunday odamga berish afzaldir.
Zakot oluvchining vazifalari
Zakotni oluvchi Qur’onda zikr qilingan sakkiz toifadan biri bo‘lishi lozim. Uning zimmasida bir necha vazifa bor:
1. Alloh taolo uni g‘amga solgan narsani bartaraf qilish uchun zakotni unga berishni buyurganini fahmlasin va barcha g‘amini yig‘ib, bitta g‘amga – Alloh taoloning roziligini topishga aylantirsin.
2. Beruvchiga tashakkur aytib, uning haqqiga duo qilsin. Lekin bu duosi sababning shukri miqdorida bo‘lsin.
3. O‘ziga berilgan narsaga e’tibor bersin, halol bo‘lmagan narsani mutlaqo olmasin, chunki bir kishi birovning molidan zakot chiqarsa, bu narsa zakot bo‘lmaydi. Agar shubhali narsa bo‘lsa, o‘zini olib qochsin. Ilojsiz qolgandagina hojatiga yarashasini olsin.
4. O‘ziga muboh bo‘lgan miqdorda olsin, hojatidan ko‘pini olmasin. Agar qarzdor bo‘lsa, qarzidan ortig‘ini olmasin.
""",reply_markup=admin_keyboard.zakot_orqa_button) 
    