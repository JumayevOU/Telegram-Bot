from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


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
            InlineKeyboardButton(text=' 🐙 GitHub', callback_data='github', url="https://github.com/otajonbozorboyev"),
            InlineKeyboardButton(text='🔗  LinkedIn',callback_data='linkedin', url="https://www.linkedin.com/in/otajonbozorboyev"),
        ],
        [
            InlineKeyboardButton(text="💡 Leetcode",callback_data='leetcode',url="https://leetcode.com/u/otajonbozorboyev571"),
            InlineKeyboardButton(text="🔵 Telegram",callback_data='telegram',url="https://t.me/otajonbozorboyev"),
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



back_button_network = InlineKeyboardMarkup(
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


back_button_resume = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_resume")]  
    ]
)
