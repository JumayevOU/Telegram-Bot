import logging 
from aiogram.types import Message, CallbackQuery
from loader import dp
from keyboards.inline.Social_networks import back_button, social_network_Keyboard, main_menu, back_button_bio, resume_Keyboard
from keyboards.inline.startMenu import startMenu_Keyboard
from aiogram.types import InputFile




@dp.callback_query_handler(text='bio')
async def select_category(call: CallbackQuery):
  
    photo_file = InputFile(path_or_bytesio="/home/acer/Downloads/Telegram Desktop/photo_2024-04-07_18-13-25.jpg")
    msg = "<b>Ismi-sharifi:</b>\nOtajon Bozorboyev\n\n"
    msg += "<b>Tug'ilgan yili va joyi: </b>\n08-yanvar 1999-yil; \nJizzax viloyati, Jizzax shahri.\n\n"
    msg += "<b>Ta'limi:</b>\nToshkent temir yo'l transport kasb-hunar kolleji (2018)\n\n"
    msg += "<b>Ish tajribasi: :</b>\n-O'zbekiston temir yo\'llari AJ tashkiloti Jizzax temir yo'l masofasi xodimlar bo\'limi nazoratchisi (HR) (2018-2023);Astro Education Python Beckend Mentor(2023-2024);Tramplin IT Academy Backend dasturchi va Python backend mentor (2024-hozirgacha)\n\n"
    msg += "<b>Texnik ko'nikmalari: </b>\nC, Python, Django, Django Rest, SQLite, MySQL, PostgreSQL, Git, GitHub, HTML, CSS, Java Script, Telegram Bot, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)n\n"
    msg += "<b>Tillar: </b>\nO'zbek tili (Ona tili);\nIngliz tili (B2);\nArab tili (O'qiy olish);\nYapon tili (N3).\n\n"
    await call.message.reply_photo(photo_file, caption=msg, reply_markup=back_button_bio)
    await call.message.delete()



@dp.callback_query_handler(text='resume')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"Bo'limni tanlang ⤵️", reply_markup=resume_Keyboard)


@dp.callback_query_handler(text='download')
async def select_category(call: CallbackQuery):
    with open("/home/acer/Downloads/Telegram Desktop/Otajon-Bozorboev-FlowCV-Resume-20240815.pdf", 'rb') as pdf_file:
        await call.message.answer_document(pdf_file, caption="Bu Otajon Bozorboyevning resumesi! ")
    await call.message.delete()



@dp.callback_query_handler(text='social_networks')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"Sahifani tanlang ⤵️", reply_markup=social_network_Keyboard)




@dp.callback_query_handler(text='github')
async def select_category(call: CallbackQuery):
    await call.message.answer("""<b>GitHub:</b>"""f"https://github.com/otajonbozorboyev", reply_markup=back_button)
    await call.message.delete()



@dp.callback_query_handler(text='linkedin')
async def select_category(call: CallbackQuery):
    await call.message.answer("""<b>LinkedIn:</b>"""f"https://www.linkedin.com/in/otajonbozorboyev", reply_markup=back_button)
    await call.message.delete()    


@dp.callback_query_handler(text='leetcode')
async def select_category(call: CallbackQuery):
    await call.message.answer("""<b>Leetcode:</b>"""f"https://leetcode.com/u/otajonbozorboyev571", reply_markup=back_button)
    await call.message.delete()    



@dp.callback_query_handler(text='telegram')
async def select_category(call: CallbackQuery):
    await call.message.answer("""<b>Telegram kanal:</b>"""f"https://t.me/otajonbozorboyev", reply_markup=back_button)
    await call.message.delete()      




@dp.callback_query_handler(text='back')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"Sahifani tanlang ⤵️", reply_markup=startMenu_Keyboard)


@dp.callback_query_handler(text='back_network')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"Sahifani tanlang ⤵️", reply_markup=social_network_Keyboard)



@dp.callback_query_handler(text='back_bio')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"Sahifani tanlang ⤵️", reply_markup=startMenu_Keyboard)
