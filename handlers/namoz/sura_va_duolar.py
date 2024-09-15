from keyboard_buttons import admin_keyboard
from aiogram import  F
from aiogram.types import Message,CallbackQuery
from loader import dp
from aiogram.fsm.context import FSMContext

# Qo'shimcha suralar va duolar haqida ma'lumot berish
@dp.message(F.text == "SURALAR")
async def massaeg(messaga: Message):
    await messaga.answer("Qo'shimcha suralar", reply_markup=admin_keyboard.qushimcha)

# Callback query uchun sura va duolar
@dp.callback_query(F.data == 'oyat')
async def valyuta_back(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Allohu la ilaha illa huval hayyul qoyyum. La ta'xuzuhu sinatuv-va la nawm. Lahu ma fis-samavati va ma fil arz. Manzallaziy yashfa'u 'indahu illa bi'iznih...

<a href='https://t.me/namoz_uqishni_urganish_Kanal/15'>Bizning kanal📢</a>
""", reply_markup=admin_keyboard.qushimcha)


# Fotiha surasi haqida
@dp.callback_query(F.data == 'fotiha')
async def valyuta_back(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Makkiy, 7 oyatdan iborat
<a href='https://t.me/namoz_uqishni_urganish_Kanal/50'>Bizning kanal📢</a>
""", reply_markup=admin_keyboard.qushimcha)



# Callbacklar uchun handlerlar
@dp.callback_query(F.data == 'kofirun')
async def kofirun_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Makkiy, 6 oyatdan iborat
 <a href='https://t.me/namoz_uqishni_urganish_Kanal/45'>Bizning kanal📢</a>",    
""", reply_markup=admin_keyboard.qushimcha)


@dp.callback_query(F.data == 'ixlos_1')
async def ixlos_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Makkiy, 4 oyatdan iborat                            
    <a href=''>Bizning kanal📢</a> 
""", reply_markup=admin_keyboard.qushimcha)


@dp.callback_query(F.data == 'falaq_sura')
async def falaq_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
 Makkiy, 5 oyatdan iborat                                    
<a href=' '>Bizning kanal📢</a>                                                     
""", reply_markup=admin_keyboard.qushimcha)

@dp.callback_query(F.data == 'nas')
async def nas_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
 Makkiy, 6 oyatdan iborat   
    <a href='https://t.me/namoz_uqishni_urganish_Kanal/37'>Bizning kanal📢</a> 
""", reply_markup=admin_keyboard.qushimcha)

@dp.callback_query(F.data == 'kavsar_qushimcha')
async def kavsar_qushimcha(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
 Makkiy, 3 oyatdan iborat                                      
<a href='https://t.me/namoz_uqishni_urganish_Kanal/65'>Bizning kanal📢</a> 
""", reply_markup=admin_keyboard.qushimcha)



@dp.callback_query(F.data == 'quraysh_')
async def quraysh_(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
 Makkiy, 4 oyatdan iborat   
    <a href='https://t.me/namoz_uqishni_urganish_Kanal/73'>Bizning kanal📢</a> 
""", reply_markup=admin_keyboard.qushimcha)


@dp.callback_query(F.data == 'nasr_')
async def nasr_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
 Makkiy, 3 oyatdan iborat   
<a href='https://t.me/namoz_uqishni_urganish_Kanal/38'>Bizning kanal📢</a> 
""",reply_markup=admin_keyboard.qushimcha)

@dp.callback_query(F.data == 'fil_sura')
async def fil_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
 Makkiy, 5 oyatdan iborat                          
<a href=''>Bizning kanal📢</a> 
""", reply_markup=admin_keyboard.qushimcha)
    

@dp.callback_query(F.data == 'maun_surasi')
async def maun_surasi(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
 Makkiy, 7 oyatdan iborat                          
<a href=''>Bizning kanal📢</a> 
""", reply_markup=admin_keyboard.qushimcha)

@dp.callback_query(F.data == 'masad_surasi')
async def masad_surasi(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
 Makkiy, 5 oyatdan iborat                          
<a href=''>Bizning kanal📢</a> 
""", reply_markup=admin_keyboard.qushimcha)


# duolar ---------=\
@dp.message(F.text=="DUOLAR")
async def message(message:Message):
    await message.answer(text="""
DUOLAR """,reply_markup=admin_keyboard.duolar)

@dp.callback_query(F.data == "orqa_button_duolar")
async def orqa_button_duolar(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
DUOLAR
""", reply_markup=admin_keyboard.duolar)

@dp.callback_query(F.data == "azondan_kiyinduo")
async def azondan_kiyinuo(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Bismillahir Rohmanir Rohiym.
Alloh taologa bitmas-tuganmas hamdu sanolar bo‘lsin.
Payg‘ambarimizga mukammal va batamom salavotu durudlar bo‘lsin.
Azonning hammasini eshitib bo‘lganidan keyin Rasululloh sollallohu alayhi vasallamga salovot aytib, ortidan mana bu duoni o‘qiydi:
اللهُمَّ رَبَّ هَذِهِ الدَّعْوَةِ التَّامَّةِ وَالصَّلاَةِ القَائِمَةِ آتِ مُحَمَّدًا الوَسِيلَةَ وَالفَضِيلَةَ وَابْعَثْهُ مَقَامًا مُحْمُودًا الَّذِي وَعَدْتَهُ
«Allohumma robba hazihid da’vatit tammah vassolatil qoimah, ati Muhammadanil vasiylata val faziylah vab’ashu maqomam mahmudanillaziy va’adtah» (Ey bu komil duoning va qoim bo‘lgan namozning egasi Allohim, Muhammadga vasila va fazilat ber, u zotni va’da qilganing maqtovli maqomda tiriltir). So‘ngra xohlaganicha dunyoviy va uxroviy duolarni qilaveradi.
""", reply_markup=admin_keyboard.duolar)

@dp.callback_query(F.data == "sano_duosi")
async def sano_duosi(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
SANO DUOSI
Subhaanakalloouhumma va bihamdika va tabaaro kasmuka va ta’aalaa jadduka va laa ilaaha g‘oyruk
Ma’nosi: «Allohim! Sening noming muborakdir. Shon sharafing ulug‘dir. Sendan o‘zga iloh yo‘qdir»
                                 
""", reply_markup=admin_keyboard.duolar)

@dp.callback_query(F.data == "rukudan_turkanda")
async def rukudan_turkanda(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Subhana robbiyal 'aziym
Ulug' Robbim nuqsonlarda pikdir                           
""", reply_markup=admin_keyboard.duolar)

@dp.callback_query(F.data == "rukudan_qaytayotganda")
async def rukudan_qaytayotganda(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Sami'allohu liman hamidah
Kim hamd aytsa,Alloh uni eshitadi                                  
""", reply_markup=admin_keyboard.duolar)

@dp.callback_query(F.data == "rukudan_qaytib_turganda")
async def rukudan_qaytib_turganda(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Robbana lakal hamd.
Robbimiz, Senga hamd bo'lsin                              
""", reply_markup=admin_keyboard.duolar)

@dp.callback_query(F.data == "sajdada")
async def sajdada(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Subhana robbiyal a'la
Oliy Robbim nuqsonlardan pokdir                              
""", reply_markup=admin_keyboard.duolar)

@dp.callback_query(F.data == "tashahhud")
async def tashahhud(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
«Attahiyyatu lillahi vassolavatu vat­toy­yibat. Assalamu ’alayka ayyuhan-nabiyyu va rohmatullohi vabarokatuh. Assalamu ’alayna va a’laa ibaadillaahis solihiyn. Ashhadu allaa ilaaha illallohu va ashhadu anna Muhammadan ’abduhu va rosuluh».
Ma’nosi: «Barokatli tabriklar va pokiza salavotlar Alloh uchundir. Ey Nabiy! Senga salom, Allohning rahmati va barakasi bo‘lsin. Bizlarga va Allohning solih bandalariga salom bo‘lsin. Allohdan o‘zga iloh yo‘q deb guvohlik beraman va albatta, Muhammad – Allohning Rasuli deb guvohlik beraman».                             
""", reply_markup=admin_keyboard.duolar)

@dp.callback_query(F.data == "salovatlar")
async def salovatlar(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
«Allohumma solli ’alaa Muhammadiv va ’alaa ali Muhammad. Kama sollayta ’alaa Ibrohima va ’alaa ali Ibrohim. Innaka hamidum majid.
Allohumma barik ’alaa Muhammadiv va ’alaa ali Muhammad. Kama barokta ’alaa Ibrohima va ’alaa ali Ibrohim. Innaka hamidum majid».
Ma’nosi: Allohim! Ibrohimga va Ibrohimning ahli baytlariga O‘z rahmatingni nozil qilganingdek, Muhammadga va Muhammadning oila a’zolariga O‘zingning ziyoda rahmatlaringni nozil qilgin! Albatta, Sen maqtalgan, ulug‘langan Zotsan!
Allohim! Ibrohimga va Ibrohimning ahli baytlariga O‘z barakangni nozil qilganingdek, Muhammadga va Muhammadning oila a’zolariga O‘z barakangni nozil qilgin! Albatta, Sen maqtalgan, ulug‘langan Zotsan!.
""", reply_markup=admin_keyboard.duolar)
    
@dp.callback_query(F.data == "namozdan_kiyin")
async def namozdan_kiyin(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Namoz salom bilan tugaydi. Salomdan keyingi amallar (tasbehotu duolar) majburiy emas, ammo nihoyatda savoblidir.
Farz namozlaridan keyin quyidagi duoni o‘qish sunnatdir:
All`ohumma antas-sal`am va minkas-sal`am. Tab`arokta y`a zaljal`ali val ikr`om.
Mazmuni:
Ey Allohim, Sen barcha ayb-nuqsonlardan poksan. Barcha salomatlik va rahmat Sendandir. Ey azamat va qudrat egasi bo‘lgan Allohim, Sening shoning ulug‘dir.
Umuman, har vaqt namozni tugatgandan so‘ng Oyatal kursi o‘qilsa, tasbehot qilinsa, savobi ulug‘ bo‘ladi.
OYATAL KURSI
A'`uzu bill`ahi minash-shayt`onir roj`iym. Bismill`ahir rohm`anir roh`iym.
All`ohu l`a il`aha ill`a huval hayyul qoyy`um. L`a ta'xuzuh`u sinatuv-va l`a na`vm. Lahu m`a fis-sam`av`ati va m`a fil arz. Manzallaz`iy yashfa'u ‘indah`u ill`a bi'iznih. Ya'lamu m`a bayna ayd`ihim va m`a xolfahum va l`a yux`it`una bi shay'im-min ‘ilmih`i ill`a bima sh`a'a. Vasi'a kursiyyuhus-sam`av`ati val arz. Va l`a ya'`uduh`u hifzuhum`a va huval ‘alliyyul ‘az`iym.
Mazmuni:
Alloh — Undan o‘zga iloh yo‘qdir. (U hamisha) tirik va abadiy turuvchidir. Uni na mudroq tutar va na uyqu. Osmonlar va Yerdagi (barcha) narsalar Unikidir. Uning huzurida hech kim (hech kimni) Uning ruxsatisiz shafoat qilmas. ( U ) ular (odamlar)dan oldingi (bo‘lgan) va keyingi (bo‘ladigan) narsani bilur. (Odamlar) Uning ilmidan faqat ( U ) istagancha o‘zlashtirurlar. Uning Kursiysi osmonlar va Yerdan (ham) kengdir. U ikkisining hifzi (tutib turishi) Uni toliqtirmas. U oliy va buyukdir.
TASBEH
Subhanalloh
(33 marta)
Alhamdulillah
(33 marta)
Allohu akbar
(33 marta)
KALIMAI TAVHID
L`a il`aha illall`ohu vahdah`u l`a shar`ika lah, lahul mulku va lahul hamd. Va huva ‘al`a kulli shay'in qod`ir.
Mazmuni:
Allohdan o‘zga iloh yo‘q. U yagonadir, sherigi yo‘q, butun mulk Unikidir. Hamd-maqtov Unga xosdir. Va U har narsaga qodir zotdir.
""", reply_markup=admin_keyboard.duolar)


@dp.callback_query(F.data == "qunut")
async def qunut(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
«Allohumma innaa nasta’iynuka va nastag‘firuka. Va nu’minu bika va natavakkalu alayka. Va nusniy alaykal xoyro kullahu. Nashkuruka va laa nakfuruk. Va naxla’u va natruku man yafjuruk. Allohumma iyyaaka na’budu va laka nusolliy va nasjudu va ilayka nas’aa va nahfidu. Narjuu rohmataka va naxshaa azaabaka. Inna azaabaka bil kuffaari mulhiq».
Duoning ma’nosi: «Allohim, albatta, biz Sendan yordam so‘raymiz, senga istig‘for aytamiz va senga iymon keltiramiz, senga tavakkul qilamiz va senga shukr keltiramiz, kufr keltirmaymiz. Kim senga fojirlik qilsa, uni ajratamiz va tark qilamiz. Allohim, sengagina ibodat qilamiz, sengagina namoz o‘qiymiz va sajda qilamiz, Sengagina intilamiz va shoshilamiz. Sening rahmatingni umid qilamiz va azobingdan qo‘rqamiz. Albatta, Sening haq azobing kofirlarga yetguvchidir».  (“Kifoya” kitobidan). Vallohu a’lam!
""", reply_markup=admin_keyboard.duolar)

@dp.callback_query(F.data == "istihora_namozi_duosi")
async def istihora_namozi_duosi(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Allohumma inniy astaxīruka biʿilmika va astaqdiruka biqudratika, va asʾaluka min faḍlika (a)l-ʿaẓīm fainnaka taqdiru valā aqdiru va taʿlamu valā aʿlamu va anta ʿallāmu (a)l-g’uyūb. Allohumma, in kunta taʿlamu anna hāza (a)l-amra xoyrul lī fī dīnī va maʿāshī vaʿāqibati amrī faqdurhu lī va yassirhu lī thumma barik lī fīhi. Va in kunta taʿlamu anna haza (a)l-amra sharrun lī fī dīnī va maʿāshī va ʿāqibati amri faṣrifhu ʿannī va (a)ṣrifni ʿanhu vaqdir lī(ya) (a)l-xoyro haysu kāna summa arḍīnī bihi.
Allohim, ilming bilan Sendan yaxshilik so’rayman. Qudrating bilan Sendan qodirlik va ulug’ fazlingni so’rayman. Zero, Sen qodirsan, men ojizman. Sen biluvchisan, men bilmayman. Sen g’aybni biluvchisan. Allohim, agar mana shu ishim dinimda, hayotimda, ishlarimning oqibatida, dunyo va ohiratimda men uchun yaxshi bo’lsa, uni menga nasib et. Agar mana shu ishim dinimda, hayotimda, ishlarimning oqibatida, dunyo va ohiratimda men uchun yomon bo’lsa, uni mendan va meni undan uzoqlashtir. Qayerda bo’lsa ham, men uchun yaxshilikni taqdir qil va meni undan rozi qil.                                  
""", reply_markup=admin_keyboard.duolar)


@dp.callback_query(F.data == "hojat_namozi_duosi")
async def hojat_namozi_duosi(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="""
Hojat namozi o‘qib bo‘lingach, salomdan keyin quyidagi duo o‘qiladi:
ا إِلَهَ إِلَّا اللهُ الْحَلِيمُ الْكَرِيمُ، سُبْحَانَ اللهِ رَبِّ الْعَرْشِ الْعَظِيمِ، الْحَمْدُ لِلَّه رَبِّ الْعَالَمِينَ: أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ، وَعَزَائِمَ مَغْفِرَتِكَ، وَالْغَنِيمَةَ مِنْ كُلِّ بِرٍّ، وَالسَّلَامَةَ مِنْ كُلِّ إِثْمٍ، لَا تَدَعْ لِي ذَنْبًا إِلَّا غَفَرْتَهُ، وَلَا هَمًّا إِلَّا فَرَّجْتَهُ، وَلَا حَاجَةً هِيَ لَكَ رِضًا إِلَّا قَضَيْتَهَا يَا أَرْحَمَ الرَّاحِمِينَ.
«Laa ilaaha illallohul haliymul kariym. Subhaanallohi robbil ’arshil ’aziym. Alhamdu lillaahi robbil ’aalamiyn. As’aluka mujibaati rohmatika va ’azoima mag‘firotika val g‘oniymata min kulli birrin, vas-salaamata min kulli ismin, laa tada’ liy zanban illa g‘ofartahu, va laa hamman illa farrojtahu, va laa haajatan hiya laka rizon illa qozoytaha, yaa arhamar rohimiyn!» deb, hojati aytib duo qilinadi.
""", reply_markup=admin_keyboard.duolar)
