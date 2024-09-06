from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart
from keyboard_buttons import admin_keyboard
from filterss.check_sub_channel import IsCheckSubChannels
from loader import bot,dp,CHANNELS
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message,InlineKeyboardButton
@dp.message(CommandStart())

async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
        await message.answer(text="Assalomu alaykum",reply_markup=admin_keyboard.start_buttonnew)
    except:
        await message.answer(text="Assalomu alaykum",reply_markup=admin_keyboard.start_buttonnew)





@dp.message(IsCheckSubChannels())
async def kanalga_obuna(message:Message):
    text = ""
    inline_channel = InlineKeyboardBuilder()
    for index,channel in enumerate(CHANNELS):
        ChatInviteLink = await bot.create_chat_invite_link(channel)
        inline_channel.add(InlineKeyboardButton(text=f"{index+1}-kanal",url=ChatInviteLink.invite_link))
    inline_channel.adjust(1,repeat=True)
    button = inline_channel.as_markup()
    await message.answer(f"{text} kanallarga azo bo'ling",reply_markup=button)
