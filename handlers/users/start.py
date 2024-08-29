from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from keyboards.inline.startMenu import Menu_Keyboard
from aiogram.types import InputFile
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    photo_file = InputFile(path_or_bytesio="photos/O.B.jpg")
    await message.answer_photo( photo=photo_file,caption=f"Assalomu aleykum, {message.from_user.full_name}\n botimizga xush kelibsiz!\nBu <b>Otajon Bozorboyev</b>ning shaxsiy boti\nqo'shimcha ma'lumot olish uchun <b>Menu</b> tugmasini bosing ⤵️", reply_markup=Menu_Keyboard)
    await message.delete()


          
   




    