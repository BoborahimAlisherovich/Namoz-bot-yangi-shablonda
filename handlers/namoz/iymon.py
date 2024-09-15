from keyboard_buttons import admin_keyboard
from aiogram import  F,types
from loader import dp
from aiogram.types import Message,CallbackQuery


#Iymon ----------------===========
@dp.message(F.text=="IYMON")
async def message(message:Message):
    await message.answer(text="IYMON  <a href='https://t.me/mukammal_namoz/85'>.</a>                                    ",reply_markup=admin_keyboard.iymon)

@dp.callback_query(F.data == "orqaga_button")
async def orqaga_button(callback: CallbackQuery):
    await callback.message.delete()

    await callback.message.answer(text="""IYMON  <a href='https://t.me/mukammal_namoz/85'>.</a>                                    """,reply_markup=admin_keyboard.iymon)

@dp.callback_query(F.data == "shariat")
async def shariat(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Alhamdulillah, barchalarimiz musulmonlarmiz, suyukli Payg‘ambarimiz Muhammad alayhissalom keltirgan Islom dinining haq ekanligiga e’tiqod qilamiz, uning ahkomlarini ado etamiz. Gohida shunday savol ham tug‘ilib qoladi: «Din nima o‘zi?»
«Din» so‘zi «itoat, parhez, e’tiqod, hisob, ishonch, mukofot, hukm, yo‘l tutish» degan ma’nolarni bildiradi. Din ilohiy yo‘l-yo‘riqlar, Alloh taolo buyurgan hukmlar, ibodatlar va aqidalar majmuidir. Din aqlli insonlarni xayrli va ezgu ishlarga yetaklaydi, faqat yaxshilikka boshlaydi. Yeyish, ichish, uxlash moddiy ehtiyoj bo‘lganidek, din ham ma’naviy ehtiyojdir. 
Barcha payg‘ambarlar alayhimussalom da’vat etgan dinlarning asosi bittadir: payg‘ambarlar insonlarni olamni yagona Alloh taolo yaratganiga iqror bo‘lishga va faqat Unga ibodat qilishga da’vat etishgan. Ular yetkazgan hukmlardagina farq bor, asosiy da’vatlarida esa farq yo‘q. Dunyoda dini, ishonchi bo‘lmagan biror millat yoki xalq yo‘q. Chunki hech bir millat, xalq dinsiz yashay olmaydi. Dinsizlik, Allohga, Uning vahiylariga, oxiratga ishonmaslik (ya’ni kufr keltirish) insoniyatning eng katta kulfatidir. «Kufr» so‘zi lug‘atda «inkor etish», «rad qilish», «berkitish» ma’nolarini bildiradi. Shar’iy hukmlarni inkor etuvchi odam «kofir», uning qilmishlari «kofirlik» deyiladi. Allohning borligini va birligini, Muhammad alayhissalom yetkazgan xabarlarni inkor, rad etganlar kofir sanaladi. Yana inson o‘zining asl tabiati tasdiqlaydigan haq yo‘lni tan olmasa, ichki tuyg‘u haqiqatini berkitsa, haqni berkitgan bo‘ladi. 
«Islom» – «bo‘ysunish, toat, ixlos, tinchlik, sulh» demakdir. Islom tavhid (yakkaxudolik) dinidir. Alloh taolo yuborgan barcha payg‘ambarlar insoniyatni asosi bir dinga – Alloh taoloning borligi va birligiga, Uning kitoblariga, farishtalariga, payg‘ambarlariga va Qiyomat kuniga iymon keltirishga, faqat Unga ibodat qilishga da’vat etishgan. Islom dinidagi kishilar «musulmon-muslim» deb ataladi. Hozir yer yuzida salkam bir yarim milliard nafar musulmon bor. 
Musulmonlar Islom shariatiga muvofiq hayot kechiradilar. «Shariat» so‘zi lug‘atda «izhor qilmoq, bayon etmoq, yo‘l» ma’nosida bo‘lib, «to‘g‘ri yo‘l, ilohiy yo‘l, qonunchilik»ni anglatadi. Shar’iy istilohda Islom dinining hukmlar to‘plami, Alloh taoloning amr va taqiqlari «shariat» deyiladi. Payg‘ambarlar da’vat etgan dinlarning asosi bir bo‘lsa-da, ular yetkazgan hukmlar, ya’ni shariatlar turlichadir. Shuning uchun keyin kelgan payg‘ambar davrida avvalda o‘tgan payg‘ambar yetkazgan hukmlar (shariat) bekor bo‘lgan. Payg‘ambarimiz yetkazgan hukmlar, ya’ni Islom shariati qiyomatgacha boqiydir. Insonlar manfaatini ta’minlash va uni himoya qilish shariatning asosiy maqsadidir. Bu yerdagi manfaatdan inson xohish-istagiga mos manfaat tushunilmaydi, balki insonning shar’iy mezondagi haqiqiy manfaati tushuniladi. Kundalik hayot tarzining Islom shariatiga muvofiq bo‘lishini ta’minlovchi qonunlar va mezonlar «fiqh» deyiladi. «Shar’iy ahkom» – Allohning buyurgan, qaytargan yoki ixtiyor etgan qat’iy ko‘rsatmalaridir. Alloh taolo Shori’, ya’ni shariat asoschisidir. 
Musulmonlik ikki buyuk ishonch asosiga qurilgan: 
1. Allohdan o‘zga ibodat qilishga loyiq iloh yo‘qligi («Laa ilaaha illalloh»);
2. Muhammad alayhissalom Alloh taoloning barcha insonlarga yuborgan elchisi (payg‘ambari) ekanlari («Muhammadur Rasululloh»). 
Bu muborak jumlalarni qalbidan tasdiqlab, iqror bo‘lib, tilida izhor qilgan kishi Islom dinida bo‘ladi. Bu ishonch «iymon», iymon keltirgan kishi esa «mo‘min» deb ataladi. 
Islom dini quyidagi besh asos (ustun) ustiga qurilgan: 
1. Iymon («Laa ilaaha illalloh, Muhammadur rasululloh» deb dil bilan iqror bo‘lish va tilda aytish);
2. Namoz (kuniga besh vaqt namoz o‘qish);
3. Zakot (moli ma’lum hisobga yetsa, qirqdan bir ulushini Alloh ta’yin qilgan muhtojlarga ajratish);
4. Ro‘za (Ramazon oyida bir oy ro‘za tutish);
5. Haj (qodir bo‘lsa, umrida bir marta haj qilish).
""",reply_markup=admin_keyboard.iymon_orqaga_button)

@dp.callback_query(F.data == "iymon_nima")
async def iymon_nima(callback: CallbackQuery):
    await callback.message.delete()

    await callback.message.answer(text="""
«Iymon»ning ma’nosi tasdiq etish, ishonishdir. Payg‘ambarimiz Muhammad alayhissalomga Alloh taolo tomonidan yetkazilgan barcha narsalarni dil bilan tasdiqlab, ularga til bilan iqror bo‘lish «iymon» deyiladi.
Iymon bunday izhor qilinadi:
أَشْهَدُ أَنْ لَا إِلَهَ إِلَّا اللهُ، وَأَشْهَدُ أَنَّ مُحَمَّدًا عَبْدُهُ وَرُسُولُهُ.
«Ashhadu allaa ilaaha illallohu va ashhadu anna Muhammadan ’abduhu va rosuluh» (ya’ni «Guvohlik beramanki, Alloh taolodan o‘zga iloh yo‘qdir va guvohlik beramanki, Muhammad alayhissalom Uning bandasi va Rasulidir).
Kim bu kalimani tili bilan aytib, dili bilan uning ma’nosini tasdiq va qabul qilsa, ya’ni Alloh taolo yagona sig‘iniladigan Zotdir, Undan o‘zga sig‘inishga loyiq hech mavjudot yo‘q, Muhammad alayhissalom Alloh taoloning bandasi va rasulidir, Muhammad alayhissalom Alloh taolo tomonidan yetkazgan barcha narsa haq-rostdir, deb qalbi bilan tasdiq va qabul qilsa hamda tili bilan shunga iqror bo‘lsagina iymonli sanaladi. Ibodat va solih amallarning qabul bo‘lishi uchun iymon shartdir.
Shu o‘rinda Islom va iymonning asl mohiyatini bayon etuvchi bir mashhur hadisi sharif bilan tanishib o‘tish foydadan xoli bo‘lmas edi.
Umar ibn Xattob roziyallohu anhudan rivoyat qilinadi:
«Bir kuni Rasululloh sollallohu alayhi vasallamning huzurlarida edik. Birdan oldimizda oppoq kiyimli, sochlari qop-qora odam paydo bo‘ldi. Unda safarning asari ko‘rinmas edi. Uni birortamiz tanimas ham edik. U kelib Rasululloh sollallohu alayhi vasallamning to‘g‘rilariga o‘tirdi. Ikki tizzasini u zotning ikki tizzalariga tiradi. Ikki kaftini sonlari ustiga qo‘ydi va: «Ey Muhammad, menga Islom haqida xabar ber», dedi.
Rasululloh sollallohu alayhi vasallam: «Islom: «Laa ilaha illallohu Muhammadur Rasululloh» deb shahodat keltirmog‘ing, namozini to‘kis ado qilmog‘ing, zakot bermog‘ing, Ramazon ro‘zasini tutmog‘ing, agar yo‘lga qodir bo‘lsang, Baytni haj qilmog‘ing», dedilar.
«To‘g‘ri aytding», dedi u. Biz undan ajablandik. O‘zi so‘raydi, o‘zi tasdiqlaydi. «Menga iymon haqida xabar ber», dedi.
U zot sollallohu alayhi vasallam: «Allohga, Uning farishtalariga, kitoblariga, payg‘ambarlariga va oxirat kuniga iymon keltirmog‘ing, yaxshiyu yomon qadarga iymon keltirmog‘ing», dedilar.
«To‘g‘ri aytding», deb tasdiqladi va: «Menga ehson haqida xabar ber», dedi.
U zot sollallohu alayhi vasallam: «Allohga xuddi Uni ko‘rib turganingdek, agar sen Uni ko‘rmasang, U seni ko‘rib turgandek ibodat qilmog‘ing», dedilar.
«Menga (qiyomat) soatidan xabar ber», dedi.
U zot sollallohu alayhi vasallam: «So‘raluvchi bu haqda so‘rovchidan bilimliroq emas», dedilar.
«Uning alomatlaridan xabar ber», dedi.
U zot sollallohu alayhi vasallam: «Cho‘ri o‘z xojasini tug‘mog‘ligi, yalangoyoq, yalan­g‘och, kambag‘al cho‘ponlarning bino qurishda bir-birlaridan o‘zishga urinishlarini ko‘rmog‘ing», dedilar.
So‘ngra u qaytib ketdi. Shunda men birmuncha vaqt (o‘sha yerdan) g‘oyib bo‘ldim. Keyinroq u zot sollallohu alayhi vasallam menga: «Ey Umar, so‘rovchi kimligini bildingmi?» dedilar. «Alloh va Uning Rasuli biluvchiroq», dedim. U zot sollallohu alayhi vasallam: «Albatta, u Jabroildir. Sizlarga dinlari­ngizdan ta’lim bergani kelibdi», dedilar».
""",reply_markup=admin_keyboard.iymon_orqaga_button)
    
@dp.callback_query(F.data == "Allohga_iymon")
async def Allohga_iymon(callback: CallbackQuery):
    await callback.message.delete()
   
    await callback.message.answer(text="""
Inson uchun eng birinchi vazifa va burch Alloh taologa iymon keltirishdir. Allohga iymon keltirish bo‘lmas ekan, iymon keltirish lozim bo‘lgan boshqa narsalarga ham iymon bo‘lmaydi. Kishi hamma narsani yolg‘iz Alloh taolo yaratganini, Undan o‘zgaga sig‘inib bo‘lmasligini, U komil sifatlar bilan sifatlanganini, ayb-nuqsondan pokligini qalbi bilan tasdiqlab, tili bilan iqror bo‘lsagina Alloh taologa iymon keltirgan bo‘ladi. 
Alloh taolo zoti va sifatlarida yagonadir, qadimdir (mavjudligining avvali yo‘q), doimdir (mavjudligining nihoyasi yo‘q), tirikdir, biluvchidir, qodirdir, ixtiyorlidir (istaganini qiladi), so‘zlaguvchidir, eshituvchidir, ko‘ruvchidir. Alloh taolo jism ham, javhar (ya’ni modda) ham, araz (rang, hid kabi) ham emas. Uning surati va shakli yo‘q. Alloh taolo biror tomonda va makonda emas. Zero, U Zot makon va tomonni O‘zi yaratgan. Alloh taoloning borligi zamon bilan belgilanmaydi. Alloh taolo ismlari, zotiy va fe’liy sifatlari bilan hamisha bo‘lgan va bo‘ladi. Alloh taoloning birorta ismi va sifati yangi paydo bo‘lmagan. 
Alloh taoloning zoti va sifatlarida o‘xshashi, aksi, tengi yo‘q. Alloh taolo hech bir narsaga muhtoj emas. Alloh taolo oxiratda mo‘minlarga O‘z zotiga munosib, kayfiyatsiz ravishda ko‘rinadi. Hamma narsa Alloh taoloning xohishi, hukmi va taqdiri bilan bo‘ladi. Alloh taolo barcha narsani biladi, hamma narsaga qodirdir. 
Alloh taoloning sifatlari azaliy va abadiydir. Alloh taoloning sifatlari sakkizta: 
Hayot – tiriklik. Alloh taolo tirikdir. 
Ilm – bilish. Alloh taolo hamma narsani biluvchidir. 
Qudrat – qodirlik. Alloh taolo hamma narsaga qodirdir. 
Sam’a – eshitish. Alloh taolo oshkor va pinhonni eshituvchidir, hech narsa Unga maxfiy emasdir. 
Basar – ko‘rish. Alloh taolo hamma narsani ko‘radi, hech narsa Undan yashirin emasdir. 
Iroda – xohish. Alloh taolo xohlagan narsa bo‘ladi, xohlamagan narsa bo‘lmaydi. 
Kalom – so‘zlash. Alloh taolo so‘zlaguvchidir. 
Takvin – yo‘qdan yaratish. Alloh taolo olamni yo‘qdan yaratgan, hamma narsaning yaratuvchisi Alloh taolodir. 
Bu sifatlardan hayot, ilm, qudrat, sam’a, basar, iroda va kalom sifatlari Alloh taoloning zotiy sifatlaridir. Takvin sifati ham Alloh taoloning zotiy sifati bo‘lib, barcha fe’liy sifatlar Alloh taoloning «takvin» sifati ostiga kiradi. Alloh taoloning hech bir sifati maxluqlarning sifatiga aslo o‘xshamaydi.
""",reply_markup=admin_keyboard.iymon_orqaga_button)
    
@dp.callback_query(F.data == "farishtalarga_iymon")
async def farishtalarga_iymon(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Farishtalarga iymon keltirish iymon arkonlaridan biridir. Farishta arab tilida «malak» deyiladi, uning ko‘pligi «maloika»dir. Alloh taolo farishtalarni nurdan yaratgan. Farishtalar borligiga hamda Qur’oni Karim va Payg‘ambarimizning muborak hadislarida bayon etilgan ularning sifatlari va vazifalariga ishonish iymon shartlaridan bo‘lib, inson ularga ham iymon keltirmagunicha mo‘min bo‘la olmaydi. 
Farishtalar Alloh taoloning maxluqi, bandasidir. Ular kufr va gunohlardan pokdir. Ular har doim Alloh taologa toat-ibodatda bo‘lishadi. Ular erlik va ayollik sifatlari bilan sifatlanmaydi. Farishtalar insonlar kabi yeb-ichishmaydi, uxlashmaydi, ularda shahvat bo‘lmaydi. Farishtalar Alloh taoloning izni bilan turli shakllarda ko‘rina olishadi. Alloh taolo farishtalarni ko‘p qanotli qilib yaratgan, ularning ba’zilarida ikkitadan, ayrimlarida uchtadan, ba’zilarida to‘rttadan, ayrimlarida esa bundan ham ko‘p qanot bor. 
  Farishtalar Alloh taoloning hukmini bandalarga yetkazish, Arshni ko‘tarib turish, jannat va do‘zax ishlarini bajarish, odamlarning ishlarini kuzatib, amallarini yozib yurish, insonni doimiy muhofaza qilish, ruhlarni qabz qilish va boshqa vazifalarga biriktirilgan. Jabroil, Mikoil, Isrofil, Malakul mavt (Azroil) alayhimussalomlar farishtalarning ulug‘laridir. Jabroil alayhissalom vahiy yetkazishga, Mikoil alayhissalom Alloh bergan rizqlarni tasarruf qilishga, Isrofil alayhissalom qiyomatdan ogoh etuvchi surni chalishga, Azroil alayhissalom jonlarni qabz qilish vazifasidadirlar.
""",reply_markup=admin_keyboard.iymon_orqaga_button)
    
@dp.callback_query(F.data == "ilohiy_kitobga_iymon")
async def ilohiy_kitobga_iymon(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Iymonning yana bir sharti Alloh taoloning O‘z payg‘ambarlariga (rasullari va nabiylariga) nozil qilgan kitoblariga ishonishdir. Alloh taoloning hamma kitoblari Uning kalomi (so‘zi) va vahiysidir. Alloh taolo ushbu kalomni yaratgan emasdir, balki bu Allohning azaliy sifatlaridandir. Ularning hammasi bir kalomdir, ibron, arab va boshqa tillarda nozil qilinganligi, jumlalarining tuzilishi jihatidan, o‘qish va eshitish jihatidan bir nechtadir. Shunga ko‘ra nozil bo‘lgan kitoblarning eng afzali Tavrot, Injil, Zabur va Qur’oni Karimdir. Bu to‘rt kitobning eng afzali Qur’oni Karimdir. Qur’oni Karim nozil bo‘lgach qolgan barcha kitoblarni o‘qish va yozish bekor bo‘lgan. Chunki ulardagi hukmlar muayyan xalqqa yo‘llangan edi. Qur’oni Karim hukmlari esa butun insoniyatga qaratilgan. Tavrot Muso alayhissalomga, Zabur Dovud alayhissalomga, Injil Iso alayhissalomga, Qur’oni Karim esa Payg‘ambarimiz Muhammad alayhissalomga yuborilgan. Qur’oni Karim hukmlari qiyomatgacha o‘zgarmaydi, biror harfi ziyoda yoki kam bo‘lmaydi, tillarda va dillarda saqlanib boradi. Qur’oni Karimni o‘qish ibodat hisoblanadi.
""",reply_markup=admin_keyboard.iymon_orqaga_button)


@dp.callback_query(F.data == "Payg'ambarlarga_iymon")
async def ambarlarga_iymon(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Payg‘ambar» forscha so‘z bo‘lib, «xabar yetkazuvchi» degan ma’nodadir. Arabchada «rasul, nabiy» deb ataladi. Iymonning shartlaridan yana biri Alloh taoloning barcha payg‘ambarlariga istisnosiz ishonishdir. Payg‘ambarlarning vazifasi iymon keltirib, toat-ibodat qilgan insonlarga jannat bashoratini qilish, kufr va isyonda bo‘lgan insonlarni do‘zax azobidan ogoh etish, insonlarga dunyo va din ishlarida ular muhtoj bo‘lgan narsalarni bayon etishdir. Payg‘ambarlarning barchasi Odam naslidan, gunoh, kufr, tug‘yondan saqlangan, pok, aql va ibodatda komildirlar. Ularning barchasi bir dinda – Islom dinidadir. Zero, ular o‘z qavmlarini faqat Alloh taologa ibodat qilishga, Uning uluhiyatiga, rububiyatiga, ism va sifatlariga shirk keltirmaslikka chaqirganlar. Payg‘ambarlar rasul va nabiyga ajraladi. Ular olib kelgan yo‘lning asosi bir bo‘lsa-da, rasullar nabiylardan yuqori darajada turadilar. Rasullarning ba’zilari ham ba’zilaridan fazl jihatidan ustun bo‘ladi. Ular zimmalariga yuklangan vazifalarni to‘la ado etishgan. Payg‘ambarlarning avvali Odam alayhissalom, oxirlari Muhammad sollallohu alayhi va sallamdirlar. Odam va Muhammad alayhimussalomlar oralaridagi davrda o‘tgan payg‘ambarlarning adadi haqida ­qat’iy dalil bo‘lmaganidan ularning umumiy sanog‘i aniq emas. Shuning uchun ular adadini ma’lum bir son bilan chegaralash joiz bo‘lmaydi. Qur’oni Karimda yigirma besh payg‘ambarning nomi zikr etilgan: bular Odam, Idris, Nuh, Hud, Solih, Ibrohim, Lut, Ismoil, Ishoq, Ya’qub, Yusuf, Ayyub, Zulkifl, Shuayb, Muso, Xorun, Dovud, Sulaymon, Ilyos, Alyasa’, Yunus, Zakariyo, Yahyo, Iso va oxirgi payg‘ambar Muhammad alayhimussalomlardir. Qur’onda Uzayr, Luqmon, Zulqarnayn degan ismlar ham kelgan, ulardan ba’zilari nabiy, ba’zilari valiydir. Odam, Nuh, Ibrohim, Muso, Iso, Muhammad alayhimussalom shariat sohiblari bo‘lishgani uchun «ulul-azm» payg‘ambarlar deyiladi. Kitob va shariat berilgan payg‘ambarlar «rasul», o‘zidan oldingi payg‘ambarning shariatini davom ettiruvchi bo‘lib kelgan payg‘ambarlar «nabiy» deyiladi. Mashhur qavlga binoan, Payg‘ambarimiz Muhammad ibn Abdulloh ibn Abdulmuttalib ibn Hoshim ibn Abdumanof sollallohu alayhi vasallam fil yilida, rabi’ul-avval oyining 12-kechasida Makkada tug‘ildilar. Otalarining ismi Abdulloh, onalarining ismi Ominadir. Quraysh qabilasidanlar. Otalari Abdulloh tijorat uchun Shomga boradi va qaytishda Madinada vafot etadi. Muhammad alayhissalom olti yoshga kirganlarida onalari ham vafot etadi va bobolari Abdulmuttolib tarbiyasida qoladilar. Uch yildan so‘ng bobolari ham vafot etadi va Rasululloh sollallohu alayhi vasallam milodiy 579-595 yillari amakilari Abu Tolib tarbiyasida bo‘ladilar. Amakilarining qo‘y-echkilarini boqadilar, tijorat safarlariga ham borib turadilar. Xadicha ismli Makkaning boy va baobro‘ ayoliga tegishli tijorat mollarini Shomga olib boradilar. U kishi ishonchli, yaxshi xulqli bo‘lganlari uchun Xadicha onamiz o‘zlari sovchi qo‘yib, Rasululloh sollallohu alayhi vasallam bilan turmush qurishadi. Bu paytda janob Payg‘ambarimiz yigirma besh yoshda, Xadicha onamiz esa qirq yoshda edilar. 610 yili ramazon oyining qadr kechasida janob Rasululloh sollallohu alayhi vasallam Makka yaqinidagi Hiro g‘orida ibodat qilayotganlarida Alloh taolo Jabroil alayhissalom orqali ilk vahiy – Qur’oni Karimning Alaq surasidagi avvalgi besh oyatni nozil etadi va shu tariqa bu zotning payg‘ambarlik risolatlari boshlanadi. Rasululloh sollallohu alayhi vasallam oltmish uch yil umr ko‘rib, hijratning o‘n birinchi yili robi’ul avval oyining o‘n ikkinchi, dushanba kuni (milodiy 632 yil) vafot etdilar. Hujrai saodatga, ya’ni Oisha onamizning hujralariga dafn etilganlar. Hozir maqbaralari Madinadagi Masjidun nabaviy ichidadir. Payg‘ambarimiz Muhammad sollallohu alayhi vasallamning shariatlari qiyomatgacha davom etadi. U zotdan so‘ng hech bir payg‘ambar bo‘lmaydi. Bu zot butun insoniyatga va jinlarga rasul etib yuborilganlar.
""",reply_markup=admin_keyboard.iymon_orqaga_button)
    

@dp.callback_query(F.data == "oxirat_kuniga_iymon")
async def oxirat_kuniga_iymon(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Oxiratga, ya’ni qiyomat kuniga ishonish iymonning yana bir shartidir. Bu haqiqatni tasdiq qilmagan inson mo‘min bo‘la olmaydi. Qur’oni Karimning juda ko‘p oyatlarida mo‘min va taqvodorlarning sifatlari zikr etilganida «va ular oxiratga ishonadilar» deb vasflanadi. Imom Buxoriy rivoyat qilgan hadisda: «Jabroil alayhissalom u zot sollallohu alayhi vasallamga «Menga iymonning xabarini bering», deganlarida Payg‘ambarimiz: «Allohga, Uning farishtalariga, kitoblariga, payg‘ambarlariga, oxirat kuniga va yaxshi-yomon qadarga iymon keltirish» deb javob berganlar. Oxiratga ishonish Qur’oni Karim va hadisi shariflarda oxirat haqida kelgan barcha narsalarga: qabrda ikki farishtaning savol qilishiga, qabr azobi va ne’matiga, oxirat kuni oldidan bo‘ladigan alomatlarga, qayta tirilishga va hammaning to‘planishiga (hashrga), nomai a’mollarning berilishiga, kishining savob va gunohlari hisob qilinishiga, mezonga (tarozuga), havzga, sirotga, shafoatga, jannat va do‘zaxga, ularning ahllariga hozirlangan ne’mat va azoblarga ishonish, demakdir. Qiyomat Isrofil alayhissalomning birinchi sur tortishlari bilan boshlanadi va dunyo hayoti tugaydi. Qiyomat kuniga iymon keltirmagan kishi bu dunyoga nimaga kelganini bilmay, hayvon kabi yashab o‘tadi. Chunki bu dunyoda yashashdan maqsad nimaligini bilmay o‘tadi. Shuning uchun u goh mol-dunyo to‘playdi, goh shahvatlarga beriladi, hayotini bemaqsad sovuradi. Qiyomat kuniga iymoni bor kishi esa dunyo hayoti insonlarning oxiratdagi abadiy hayotining muqaddimasi ekanini yaxshi biladi. Shuning uchun bu dunyoda oxirati uchun tayyorgarlik ko‘radi, hayotini solih amallar va ezgu ishlar bilan bezaydi.
""",reply_markup=admin_keyboard.iymon_orqaga_button)
    

@dp.callback_query(F.data == "limdan_sung_tirilish")
async def limdan_sung_tirilish(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
O‘lim, undan keyingi qabr sinovi va undagi azob yoki rohatga ishonish ham qiyomat kuniga iymon keltirishning bir qismidir. O‘lim haq, kattayu kichik, boyu kambag‘al, kuchliyu kuchsiz ajali yetib bir kuni o‘ladi. Musulmon inson o‘lganidan keyin qabrda ikki farishtaning so‘roq qilishiga, so‘ng natijaga qarab qabr azobi yoki undagi huzur bo‘lishiga sidqidildan ishonadi. Bu dunyo bilan oxirat dunyosi orasidagi, ya’ni o‘lgandan so‘ng to qiyomat qoim bo‘lguncha davrdagi hayotni «barzax hayoti» deyiladi. Alloh taoloning amri bilan Isrofil alayhissalom ikkinchi bor sur tortganlaridan so‘ng barcha jonzotlar, jumladan insonlar tiriladi. Ularning asl jasadlariga ruhlari qaytariladi va ular qabrlaridan chiqib Mahshargohga to‘planadi hamda hisobga tortiladi. 
O‘lim – insonning dunyo hayotidagi faoliyatiga nuqta qo‘yuvchi va oxirat hayotining boshlanishini bildiruvchi bir marradir. Inson o‘lishi bilan uning oxirat hayoti boshlanadi. Mo‘minlar o‘limdan keyin tirilib mahshargohda to‘planishlariga, qilgan yaxshi va yomon amallardan hisob berishlariga iymon keltirishlari vojibdir. Amallar Haq tarozusida – Mezonda tortilib, yaxshi amalli, iymonlilar abadiy orom-farog‘at maskani – jannatga kiradi, iymonsizlar va ayrim gunohkorlar do‘zaxga tashlanadi. 
O‘lishdan keyin tirilishning muhim hikmati bor. Modomiki, dunyoga kelgan ekanmiz, bu yerda bir qancha islomiy, insoniy vazifalarimizni o‘tashimiz, Alloh buyurganlarini bajarishimiz kerak bo‘ladi. Bunga osiylik qilganlar esa Allohning g‘azabi va jazosiga duchor bo‘ladi. Oxiratdagi baxtli-saodatli va osoyishta hayot iymonimizga bu dunyodagi qilgan amallarimizga, savobli, xayrli ishlarimizga bog‘liq. 
Qur’oni Karimda «Sizlarni undan yaratdik, unga qaytarurmiz va yana bir bor undan chiqarib olurmiz», deyilgan (Toha surasi, 55-oyat). Buni inkor qilish ­Qur’onni inkor etishdir, bu esa aniq kufrdir. O‘limdan so‘ng qayta tirilishga ishonish iymon shartlaridan biridir. Mo‘minning aqli bilan kofirning aqli shu nuqtada farqlanadi. Hozirgi kunda dunyo bo‘ylab tanosux (inson vafot topgandan keyin uning ruhi yangi tug‘iladigan chaqaloqqa kirishi, ba’zi bir millatlardagi inson yetti bor hayot kechirishi) aqidasi keng targ‘ib qilinmoqda. Bu aqida iymonga zid bo‘lib, bunday deb e’tiqod qilish kufr hisoblanadi. Chunki inson vafot topgach, hadisda kelgan xabarlarga ko‘ra, solih bandalarning ruhlari ma’lum bir joyga, kofir va fosiqlarning ruhlari esa boshqa bir joyga qo‘yiladi. Solihlarning ruhlari jasadlari kabi rohat-farog‘atda bo‘ladi, kofir va fosiqlarning ruhlari esa jasadlari kabi azobga duchor bo‘ladi. Ba’zi bir jinlar bilan do‘st bo‘lgan kishilarni «bobolarim, momolarimning arvohlari meni qo‘llab-quvvatlab turadi», deyishlari safsatadan o‘zga narsa emas. Ularga hamroh bo‘layotganlar jinlardir.
""",reply_markup=admin_keyboard.iymon_orqaga_button)

@dp.callback_query(F.data == "aqida")
async def aqida(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
«Ақида» сўзи арабча «ақада» феълидан олинган бўлиб, «бир нарсани иккинчисига маҳкам боғлаш» маъносини англатади. Истилоҳда Пайғамбаримиз соллаллоҳу алайҳи васаллам етказган барча нарсаларнинг ростлигини тасдиқлаб, қалб ва кўнгил боғлаб ишонилиши лозим бўлган нарсалар «ақида» дейилади. Бу сўзнинг жаъми (кўплик шакли) «ақоид» бўлади. Ислом ақидаси мусулмон инсонни маълум бир нарсалар билан маҳкам боғлаб турадиган эътиқодлар мажмуасидир. 
Аслида, бирор нарсага эътиқод қилиш учун уни ҳеч қандай шубҳа қолдирмайдиган даражада яхши билиш керак. Бунинг учун, аввало, ўша нарсани идрок қилиш керак. Кейин эса, ўша ҳиссий идрок илмий маърифатга айланиши лозим. Сўнгра, замон ўтиши, бошқа далилларнинг собит бўлиши ила ўша илмимиз тасдиқланади ва унга бўлган ишончимиз кучли бўлади. Мазкур илмга бўлган ишонч онгимизда мустаҳкам равишда қарор топганидан сўнг, у бизнинг ақлимизга ва қиладиган ишларимизга ўз таъсирини ўтказадиган бўлади. Қачон маълум бир илм бизнинг фикримизга айланиб, ҳис-туйғуларимизни йўллайдиган ва ҳаракатларимизни бошқарадиган ҳолга етганда ақидага айланган бўлади. Демак, ақида илмга асосланган бўлиши лозим. 
Ақида илмининг мақсади – динга бўлган ишончни, диний ақидаларни қатъий далиллар билан исботлаш ва улар тўғрисидаги шубҳаларни рад қилишдир; кишини ақидада тақлидчи бўлишдан далил келтириш ва ишончли бўлиш чўққисига кўтаришдир; тўғри йўлни изловчиларга очиқ-ойдин ҳақни баён қилиш билан йўл кўрсатиш, аксинча, бўйин товловчиларга эса, далил ва ҳужжатларни исбот қилишдир; дин асосларини аҳли ботилнинг шубҳаларидан ва адаштиришларидан муҳофаза қилишдир; бу илмнинг асосий мақсади эса, барча шаръий илмлар каби, икки дунё саодатини ҳосил қилишдир. 
Ақидани тўғрилаш ва уни мустаҳкамлаш ҳақида Сўфи Оллоҳёр шундай ёзганлар: 
Ақида билмаган шайтона элдур,
Агар минг йил амал деб қилса – елдур.
Ақида масалалари замон, макон, шахс ва жамият ҳаётига кўра ўзгармайди. Ақида масалалари яхлит бўлиб, бир қисмига ишониш, бошқа қисмига ишонмаслик мумкин эмас. Ақидага доир илк асар ёзган ва асарлари шу кунгача етиб келган зот Абу Ҳанифадир. У кишининг «Ал-Фиқҳул-акбар», «Ал-Фиқҳул-абсат», «Ар-Рисола», «Ал-Олим вал-мутаъаллим» ва «Ал-Васиййа» дея танилган беш асарида ақоид масалаларидан баҳс юритилади. 
""",reply_markup=admin_keyboard.iymon_orqaga_button)

@dp.callback_query(F.data == "ahli_sunna_val_jmoa")
async def ahli_sunna_val_jmoa(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
To‘g‘ri yo‘ldagi xalifalar davridan keyin Islom dinidan turli adashgan mazhab, oqim va firqalar paydo bo‘ldiki, bulardan xavorijlar, moʻtaziliylar, murjialar kabilar Islom birligi va birdamligiga jiddiy zarar keltirdi, turli fitna va tafriqalarga (bo‘linishlarga) sabab bo‘ldi. Ana shunday og‘ir bir paytda sof Islom aqidasini saqlab qolish uchun harakat qiladigan ulamolar yetishib chiqdilar. Ular Qur’oni Karim va Sunnat ta’limotlari asosida, Nabiy sollallohu alayhi vasallamning sahobalari uslubida aqida masalalarini yorita boshladilar. Ularga «Ahli sunna val jamoa» nomi berildi. 
Keyinroq, odamlarga tushunarli bo‘lishi uchun, matnlarni ta’vil qilishga ham majbur bo‘lindi. Turli kitoblar bitildi. Ahli sunna val jamoaning aqida bobidagi ta’limotlari to‘planib, tartibga solindi. Nihoyat, aqidaviy mazhab bo‘lib shakllandi va o‘z imomlariga ham ega bo‘ldi. 
«Ahli sunna val jamoa» ismi bundan avval ham bor edi. Ammo keyinroq, yuqorida nomlari aytib o‘tilgan turli firqalarga muqobil o‘laroq, ayni shu ismni ishlatila boshlandi. «Ahli sunna» deganda «sunnatga yurganlarning yo‘li va hadisga amal qiladiganlar» degan ma’nolar ko‘zda tutilgan. Bu borada imom al-Ash’ariy va al-Moturidiy Ahli sunna val jamoaning aqida bo‘yicha imomlari deb tan olindilar. Bu ikki imom Islom olamining ikki tarafida – Ash’ariy basralik, Moturidiy samarqandlik bo‘lsa ham va bir-birlari bilan ko‘rishmagan bo‘lsalar ham, bir xil ishni bir xil vaqtda, bir xil tarzda ado etganlari hamda ikkovlarining birdaniga Ahli sunna val jamoa mazhabining imomi deb e’tirof qilinishi bu mazhabning aqidasi doimo barcha yurtlarda ma’lum va mashhur ekaniga yorqin dalildir. 
Islom ummati ichida Haqni topgan va unga ergashgan firqa Payg‘ambarimiz alayhissalom va u zotning sahobalari amal qilgan yo‘lda sobit qolgan musulmonlardir. Qolgan yetmish ikki firqa Haqni topmagan bo‘lsa-da, Islom dinining qat’iy hukmlarini inkor qilmagani uchun Islom doirasida hisoblanadi. Islom ummati ichida Haqni topgan va unga ergashgan firqa «Ahli sunna val jamoa» deb ataladi. Ahli sunna val jamoa firqasi amaliyotda to‘rt mazhabga bo‘lingan: 
1. Hanafiy mazhabi. Imom Abu Hanifa Noʻmon ibn Sobit. 
2. Molikiy mazhabi. Imom Molik ibn Anas. 
3. Shofe’iy mazhabi. Imom Muhammad ibn Idris ash-Shofe’iy. 
4. Hanbaliy mazhabi. Imom Ahmad ibn Hanbal. 
Bugungi kunda dunyodagi musulmonlarning 92,5 foizi Ahli sunna val jamoa mazhabidadir. Ulardan hanafiylar 47 foizni, shofe’iylar – 27, molikiylar – 17, hanbaliylar – 1,5 foizni tashkil etadi.
""",reply_markup=admin_keyboard.iymon_orqaga_button)
    
@dp.callback_query(F.data == "halol_va_harom")
async def halol_va_harom(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Alloh taolo ruxsat etgan narsalar shariatda «halol» deyiladi. Mo‘min-musulmonlarga halol rizq topish, halol kasb bilan ro‘zg‘or tebratish, halol taom-ichimliklarni iste’mol qilish buyurilgan. Shariatimizda ijozat etilgan hamma narsa, yeyiladigan taomlar yoki qilinadigan ishlar halol sanaladi. Alloh taolo halol qilgan narsalar inson uchun moddiy va ma’naviy foydalardan xoli emas. 
Alloh taolo man qilgan narsalar va ishlar shariatda harom hisoblanadi. Harom ishga o‘tish yoki harom taom yeyish og‘ir gunoh sanaladi (Biroq, ba’zan zarurat tufayli harom narsalar muboh qilinadi, masalan, ochdan o‘layotgan odam jonini saqlab qoladigan miqdorda harom iste’mol qilishi, dushmanga nisbatan yolg‘on ishlatish mumkinligi kabi). Harom ish va narsalar sanoqlidir. Quyida ulardan ayrimlarini keltiramiz: to‘ng‘iz, vahshiy hayvonlar, harom o‘lgan (o‘zi o‘lib qolgan) halol hayvonlarning go‘shtlari, so‘yganda chiqqan qon, «Bismillah»siz so‘yilgan halol hayvonlarning go‘shti, dinsizlar (majusiylar) so‘ygan hayvon go‘shti, mast qiluvchi ichimlik va giyohlarning barcha turlari, erkaklarga ipak va tilla ishlatish, tilla-kumush idishda ovqat yeyish, zinokorlik, sudxo‘rlik, o‘g‘rilik, qaroqchilik, g‘iybat, tuhmat, bo‘hton, yolg‘onchilik kabi narsalar musulmonlarga harom qilingan.
""",reply_markup=admin_keyboard.iymon_orqaga_button)
    
