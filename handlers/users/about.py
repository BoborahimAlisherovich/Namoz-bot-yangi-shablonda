from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("""  
🕌 Mukammal Namoz – Namozni to‘g‘ri va mukammal ado eting! 
📖 Islomiy bilimlar, namoz qo‘llanmalari, va ruhiy o‘sish uchun foydali maslahatlar – barchasi bu yerda. Iymoningizni mustahkamlash uchun bizga qo‘shiling! 🤲
""")

