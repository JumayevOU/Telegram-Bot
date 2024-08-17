from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# check_button = InlineKeyboardMarkup(
#     inline_keyboard=[[
#         InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="check_subs")
#     ]]
# )


channel_button = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="➕ Obuna bo'lish", callback_data="check_channel", url="https://t.me/turnerlar_N_1"),
    ],
    [
        InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="check_subs")
    ]]
)

