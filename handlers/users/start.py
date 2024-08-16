from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.startMenu import startMenu_Keyboard
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name} botimizga xush kelibsiz!")
    await message.answer(f"Menyuni tanlang ⤵️", reply_markup=startMenu_Keyboard)
    