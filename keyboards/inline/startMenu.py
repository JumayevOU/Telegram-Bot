from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



Menu_Keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=" Menu",callback_data="menu"),
        ],
     
        
    ])

startMenu_Keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✍️  Bio",callback_data="bio"),
            InlineKeyboardButton(text="📝   Resume",callback_data="resume"),
        ],
        [
            InlineKeyboardButton(text="🌐   Social networks",callback_data="social_networks"),
            InlineKeyboardButton(text="ℹ️  Murojaat uchun",callback_data="problem", url="https://t.me/obozorboyev_bot"),
        ],
              
    ])