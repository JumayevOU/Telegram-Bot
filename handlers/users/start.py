from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import CHANNELS
from keyboards.inline.subscription import channel_button
from keyboards.inline.startMenu import Menu_Keyboard
from aiogram.types import InputFile
from loader import dp, bot
from utils.misc import subscription
import asyncio

@dp.message_handler(commands=['start'])
async def show_channels(message: types.Message):
    channels_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
      
    await message.answer(f"❗️ Bot to'liq ishlashi uchun quyidagi kanalimizga obuna bo'ling 👇 \n"
                         f"{channels_format}",
                         reply_markup=channel_button,
                         disable_web_page_preview=True)


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        print(status)
        channel = await bot.get_chat(channel)
        if status:
            initial_message = await call.message.answer("🎉 Obuna bo’ldingiz. Endi botni bemalol ishlatishingiz mumkun.")
            await call.message.delete()
            await asyncio.sleep(1)
            await initial_message.delete()
            photo_file = InputFile(path_or_bytesio="/home/acer/Downloads/Telegram Desktop/photo_2024-04-07_18-13-25.jpg")
            await call.message.bot.send_photo(chat_id=call.message.chat.id, photo=photo_file,caption=f"Salom {call.message.from_user.full_name} botimizga xush kelibsiz!\nBu <b>Otajon Bozorboyev</b>ning shaxsiy boti\nqo'shimcha ma'lumot olish uchun <b>Menu</b> tugmasini bosing ⤵️", reply_markup=Menu_Keyboard)
            await call.message.answer(result, disable_web_page_preview=True)
          
        else:
            result += "Iltimos, kanallarimizga obuna bo'ling, \nKeyin botni ishlatishingiz mumkin❗️"
            await call.answer(result, show_alert=True)





    