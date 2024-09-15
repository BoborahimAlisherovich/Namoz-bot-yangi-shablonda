ITEMS_PER_PAGE = 20

def get_paginated_keyboard(page=0):
    start = page * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    surah_page = admin_keyboard.SURAH_NAMES[start:end]

    keyboard_builder = InlineKeyboardBuilder()

    # Har bir qator uchun 2 ta Surah tugmasi qo'shish
    for name, callback_data in surah_page:
        keyboard_builder.button(text=name, callback_data=callback_data)
    
    keyboard_builder.adjust(2)  # Tugmalarni 2 tadan qator qilib joylashtirish

    # "Orqaga" va "Keyingi" tugmalari qo'shish
    pagination_buttons = []
    if page > 0:
        pagination_buttons.append(InlineKeyboardButton(text="⬅️ Orqaga", callback_data=f"page_{page-1}"))
    if end < len(admin_keyboard.SURAH_NAMES):
        pagination_buttons.append(InlineKeyboardButton(text="➡️ Keyingi", callback_data=f"page_{page+1}"))

    # Agar pagination tugmalari bo'lsa, ularni qator sifatida qo'shish
    if pagination_buttons:
        keyboard_builder.row(*pagination_buttons)

    # "Bosh menyu" tugmasini pagination tugmalarining ostida qo'shish
    keyboard_builder.row(InlineKeyboardButton(text="🏠 Bosh menyu", callback_data="qaytish"))

    return keyboard_builder.as_markup()

# Ushbu qism o'zgarmaydi
@dp.message(F.text == "QURON")
async def show_surah_list(message: Message):
    keyboard = get_paginated_keyboard(page=0)
    await message.answer("Tanlang:", reply_markup=keyboard)

# Pagination callback funksiyasi o'zgarmaydi
@dp.callback_query(F.data.startswith("page_"))
async def paginate_callback(query: CallbackQuery):
    page = int(query.data.split("_")[1])
    keyboard = get_paginated_keyboard(page)
    await query.message.edit_reply_markup(reply_markup=keyboard)

