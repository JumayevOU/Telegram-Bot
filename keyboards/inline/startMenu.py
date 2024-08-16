from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

startMenu_Keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✍️  Bio",callback_data="bio"),
        ],
        [
            InlineKeyboardButton(text="📝   Resume",callback_data="resume"),
        ],
        [
            InlineKeyboardButton(text="🌐   Social networks",callback_data="social_networks"),
        ],
        
    ])