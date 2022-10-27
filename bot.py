import logging

from aiogram import Bot, Dispatcher, executor, types
from buttons import *
from aiogram.types import Message,CallbackQuery

API_TOKEN = '5483740166:AAFudYInJWgnNLN-1xeGN6YFrng1rOKUt3U'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Tilni Tanlang/Choiose language",reply_markup=til)

#=========================================================================================================

@dp.callback_query_handler(text="uz")
async def echo(call: CallbackQuery):
    await call.message.answer("""👋Assalomu alaykum!

Sizni kuzatuvchilarimiz safida ko'rganimizdan mamnunmiz!
    
Yosh menejerlar dasturi Besh tashabbus loyihasi hamda MBM IT kompaniyasi vakillari hamkorligida tashkil etilgan maxsus dastur hisoblanadi!
    
Ushbu loyiha orqali xalqaro doirada boshqaruv qobiliyatiga ega kadrlar tizimi shakllantiriladi.""",reply_markup=menu)
#=========================================================================================================

@dp.callback_query_handler(text="loyiha")
async def echo(call: CallbackQuery):
    await call.message.answer("Loyiha haqida",reply_markup = loyiha_menu)

# Loyiha menudan chiqish
@dp.callback_query_handler(text="ortga")
async def echo(call: CallbackQuery):
    await call.message.answer("""👋Assalomu alaykum!

Sizni kuzatuvchilarimiz safida ko'rganimizdan mamnunmiz!
    
Yosh menejerlar dasturi Besh tashabbus loyihasi hamda MBM IT kompaniyasi vakillari hamkorligida tashkil etilgan maxsus dastur hisoblanadi!
    
Ushbu loyiha orqali xalqaro doirada boshqaruv qobiliyatiga ega kadrlar tizimi shakllantiriladi.""",reply_markup=menu)

#=========================================================================================================

# Inline knopkalarni ishlatish
# Loyiha maqsadi
@dp.callback_query_handler(text="vazifa")
async def echo(call: CallbackQuery):
    await call.message.answer("""🔰 Loyihaning vazifalari nimalardan iborat?

• Boshqaruv sohasida malakaga ega, xalqaro doirada faoliyat yurita oladigan mutaxassislar tayyorlab, davlat va nodavlat sektoridagi subyekt/obyektlar uchun salohiyatli kadrlar tizimini yaratib berish;

• Yoshlarning bilim va ko'nikmasini oshirib, yuqori daromad keltiradigan ish bilan ta'minlash;

• Kattalar va yoshlar orasida kommunikatsiya jarayonini shakllantirib, o'rtadagi "jarlik"ka ma'lum ma'noda chek qo'yish, ularning o'zaro hamkorligini ta'minlashga ko'maklashish.""",reply_markup = vazifa)

# Loyiha Vazifasidan chiqish
@dp.callback_query_handler(text="ortga_2")
async def echo(call: CallbackQuery):
    await call.message.answer("Loyiha haqida",reply_markup = loyiha_menu)
#=========================================================================================================

@dp.callback_query_handler(text="maqsadi")
async def echo(call: CallbackQuery):
    await call.message.answer("""🔰 Yosh Menejerlar dasturi nima maqsadda tashkil etilmoqda?

Mazkur loyiha 17 yoshdan 25 yoshgacha bo'lgan
yoshlar qatlamini loyihalar boshqaruvi bo'yicha 
nazariy jihatdan o'qitish, amaliy jihatdan yoshlarga
ish tajribasini ulashish, turli fikr va dunyoqarashga
ega shaxslar orasida muloqot almashinuvini yo'lga
qo'yish maqsadida tashkil etilgan.""",reply_markup=maqsadi)

# Loyiha maqsadidan chiqish
@dp.callback_query_handler(text="ortga_1")
async def echo(call: CallbackQuery):
    await call.message.answer("Loyiha haqida",reply_markup = loyiha_menu)

#=========================================================================================================

@dp.callback_query_handler(text="tartibi")
async def echo(call: CallbackQuery):
    await call.message.answer("""🔰 Loyiha qancha vaqt davom etadi va o'tkazilish tartibi qanday?

 📝Yosh menejerlar dasturining o’tkazilish tartibi:

 Loyiha 10 hafta davomida bo'lib o'tadi: amaliy va nazariy darslar olib boriladi.

 📋 Avgust oyining 25-sanasidan boshlab 10-Sentabr kuniga qadar loyihada ishtirok etishga nomzod shaxslarni ro'yxatdan o'tkazish va saralash jarayoni tashkil etiladi:

• 1-bosqichi saralashdan o’tganlar: 13 Sentabr e’lon qilinadi. (100 ta ishtirokchi);
• 2-saralash bosqichi: 15-16 Sentabr kuni bo’lib o’tadi;
• Javoblar: 18 Sentabr kuni e’lon qilinadi (50 ta ishtirokchi).

 💡 Nomzodlar ichidan 50 nafar kuchga to'la, ingliz tilini yaxshi biluvchi, o'z ambitsiyalariga ega va kelajakda katta maqsadlari bor yoshlar tanlab olinadi.""",reply_markup=tartibi)

# Loyiha Tartibidan chiqish
@dp.callback_query_handler(text="ortga_3")
async def echo(call: CallbackQuery):
    await call.message.answer("Loyiha haqida",reply_markup = loyiha_menu)
#=========================================================================================================


@dp.callback_query_handler(text="talabi")
async def echo(call: CallbackQuery):
    await call.message.answer("""🔰 Loyihada qatnashish uchun nomzodlarga qanday talablar qo'yiladi?

 — ingliz, rus, o'zbek tilida ish yuritish: erkin so'zlashish va yoza olish;
 — IT texnologiyalari hamda mediasavodxonlik bo'yicha bilimga egalik;
 — 17-25 yosh orasida bo'lish;
 — Toshkent shahri va viloyati hududida istiqomat qilish.""",reply_markup=talabi)

# Loyiha Talabidan chiqish
@dp.callback_query_handler(text="ortga_4")
async def echo(call: CallbackQuery):
    await call.message.answer("Loyiha haqida",reply_markup = loyiha_menu)

#=========================================================================================================
#=========================================================================================================
#=========================================================================================================
# Savollar uchun menyu
@dp.callback_query_handler(text="savollar0")
async def echo(call: CallbackQuery):
    await call.message.answer("""Assalomu alaykum!

Savollaringizni @https://t.me/djuraev_721 ga yo'llashingiz mumkin. Sizga tez orada javob beramiz!

E'tiboringiz uchun rahmat.""",reply_markup = savollar)

# Loyiha Talabidan chiqish
@dp.callback_query_handler(text="ortga_5")
async def echo(call: CallbackQuery):
    await call.message.answer("""👋Assalomu alaykum!

 Sizni kuzatuvchilarimiz safida ko'rganimizdan mamnunmiz!
    
 Yosh menejerlar dasturi Besh tashabbus loyihasi hamda MBM IT kompaniyasi vakillari hamkorligida tashkil etilgan maxsus dastur hisoblanadi!
    
 Ushbu loyiha orqali xalqaro doirada boshqaruv qobiliyatiga ega kadrlar tizimi shakllantiriladi.""",reply_markup = menu)
#=========================================================================================================

@dp.callback_query_handler(text="royxat")
async def echo(call: CallbackQuery):
    await call.message.answer("Loyiha haqida",reply_markup=royxat)





# ENGLISH VERSION
#=========================================================================================================

@dp.callback_query_handler(text="en")
async def echo(call: CallbackQuery):
    await call.message.answer("""👋Hello!

 We are glad to see you among our observers! 
    
 The Young Managers Program is a special project organized in collaboration with the Five Initiative Project and representatives of MBM IT Company! 
    
 Through this program personnel management skills system will be formed in the international arena.""",reply_markup=menu_1)
#=========================================================================================================

@dp.callback_query_handler(text="project_menu")
async def echo(call: CallbackQuery):
    await call.message.answer("About the project",reply_markup = project_menu)

# Loyiha menudan chiqish
@dp.callback_query_handler(text="back")
async def echo(call: CallbackQuery):
    await call.message.answer("""👋Hello!

 We are glad to see you among our observers! 
    
 The Young Managers Program is a special project organized in collaboration with the Five Initiative Project and representatives of MBM IT Company! 
    
 Through this program personnel management skills system will be formed in the international arena.""",reply_markup=menu_1)

#=========================================================================================================

# Inline knopkalarni ishlatish:

# Task
@dp.callback_query_handler(text="task")
async def echo(call: CallbackQuery):
    await call.message.answer("""🔰 What are the objectives of project? 

 • Training of specialists with international qualifications in the field of management and creation of a potential human resources system for entities and objects in the public and private sectors;

 • Providing high-paid jobs to increase the knowledge and skills of youth; 

 • To form a process of communication between the older and younger generations, to put an end to the "cliff" between them, to help them to ensure their interaction;""",reply_markup = task)

# Back to Project Menu from Task
@dp.callback_query_handler(text="back_2")
async def echo(call: CallbackQuery):
    await call.message.answer("About the project",reply_markup = project_menu)
#=========================================================================================================

@dp.callback_query_handler(text="aim")
async def echo(call: CallbackQuery):
    await call.message.answer("""🔰 What is the main purpose of the Young Managers Program?

Project is designed to provide theoretical
training in project management to young
people from aged 17 to 25, to share practical
work experience with young people, and to
establish a community between people with
different ideas and worldviews.""",reply_markup=aim)

# Loyiha maqsadidan chiqish
@dp.callback_query_handler(text="back_1")
async def echo(call: CallbackQuery):
    await call.message.answer("About the project",reply_markup = project_menu)

#=========================================================================================================

@dp.callback_query_handler(text="process")
async def echo(call: CallbackQuery):
    await call.message.answer("""🔰 How long will the project last and what is the procedure?

  📝 Procedure for the Young Managers Program:

  The project will last for 10 weeks: practical and theoretical lessons will be conducted.

  📋 From August 25 to September 10, the process of registration and selection of candidates for participation in the project will be organized:

• Round 1 qualifiers: September 13 will be announced. (100 participants);
• Qualifying Round 2: September 15-16;
• Answers: to be announced on September 18 (50 participants).

  💡 Out of the candidates, 50 young people who are strong, fluent in English, have their own ambitions and have big goals for the future will be selected.""",reply_markup=process)

# Loyiha Tartibidan chiqish
@dp.callback_query_handler(text="back_3")
async def echo(call: CallbackQuery):
    await call.message.answer("About the project",reply_markup = project_menu)
#=========================================================================================================


@dp.callback_query_handler(text="require")
async def echo(call: CallbackQuery):
    await call.message.answer("""🔰 What are the requirements for candidates to participate?

 — Office work in English, Russian, Uzbek: fluent speaking and writing skills;
 — Knowledge of IT and media; 
 — 17-25 years old;
 — Resident of Tashkent city and region.""",reply_markup=require)

# Loyiha Talabidan chiqish
@dp.callback_query_handler(text="back_4")
async def echo(call: CallbackQuery):
    await call.message.answer("About the project",reply_markup = project_menu)

#=========================================================================================================
#=========================================================================================================
#=========================================================================================================
# Savollar uchun menyu
@dp.callback_query_handler(text="questions")
async def echo(call: CallbackQuery):
    await call.message.answer("""Assalamu alaikum!

You can send your questions to  @https://t.me/djuraev_721. We will reply you soon.

Thank you for your attention.""",reply_markup = questions)

# Loyiha Talabidan chiqish
@dp.callback_query_handler(text="ortga_5")
async def echo(call: CallbackQuery):
    await call.message.answer("""👋Hello!

 We are glad to see you among our observers! 
    
 The Young Managers Program is a special project organized in collaboration with the Five Initiative Project and representatives of MBM IT Company! 
    
 Through this program personnel management skills system will be formed in the international arena.""",reply_markup = menu)
#=========================================================================================================

@dp.callback_query_handler(text="registration")
async def echo(call: CallbackQuery):
    await call.message.answer("About the project",reply_markup=registration)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)