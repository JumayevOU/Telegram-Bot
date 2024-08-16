from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from keyboards.inline.Social_networks import course_callback, book_callback


resume_Keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=' 📥 Download', callback_data='download'),
        ],    
        [
            InlineKeyboardButton(text="🔝 Asosiy menyu",callback_data="back"),
        ],
    ])


social_network_Keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=' 🐙 GitHub', callback_data='github'),
        ],
        [
            InlineKeyboardButton(text='🔗  LinkedIn',callback_data='linkedin'),
        ],
        [
            InlineKeyboardButton(text="💡 Leetcode",callback_data='leetcode'),
        ],
        [
            InlineKeyboardButton(text="🔵 Telegram",callback_data='telegram'),
        ],
        [
            InlineKeyboardButton(text="🔝 Asosiy menyu",callback_data="back"),
        ],
    ])




back_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back")]  
    ]
)



back_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_network")]  
    ]
)



main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔝 Asosiy menyu", callback_data="main_menu")]  
    ]
)



back_button_bio = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_bio")]  
    ]
)
