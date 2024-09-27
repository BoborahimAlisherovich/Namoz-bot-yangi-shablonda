from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#help commands
@dp.message(Command("help"))
async def help_commands(message:Message):
    await message.answer("""   
Salom!  Ushbu bot orqali namoz vaqtlarini, namozni qanday o‘qishni, va boshqa muhim ma'lumotlarni topishingiz mumkin.:
Namoz Vaqtlari: O'z hududingizda namoz vaqtlarini bilib oling. Faqatgina joyingizni kiriting.
Namoz O‘qish Qoidalari: Har bir namozni qanday o‘qish kerakligini o‘rganing. Har bir namozning qoidalari, ruknlar va tilovatlarini toping.
Duolar: Har bir namoz uchun tavsiya etilgan duolarni o‘rganing. 
                         
""")
