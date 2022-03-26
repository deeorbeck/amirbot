from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default import menu
from doc import cv_doc
from states.cv import cv
from data import config, database
import os
from handlers.users.transliterate import to_latin
from functions.doc import get_quant



@dp.message_handler(content_types=['text'], state=cv.name)
async def name(message: types.Message, state: FSMContext):
    if message.text == "❌bekor":
        await message.answer("Tanlang", reply_markup=menu.markup_menu)
        await cv.zero.set()
        return False
    await message.answer("Тугилган санангиз:\nМисол учун: 01.03.1999")
    await state.update_data(name=message.text)
    await cv.next()
@dp.message_handler(content_types=['text'], state=cv.birth)
async def name(message: types.Message, state: FSMContext):
    if message.text == "❌bekor":
        await message.answer("Tanlang", reply_markup=menu.markup_menu)
        await cv.zero.set()
        return False
    await state.update_data({"Tug'ilgan sana":message.text})
    await message.answer("Миллатингиз:")
    await cv.next()
@dp.message_handler(content_types=['text'], state=cv.nation)
async def name(message: types.Message, state: FSMContext):
    if message.text == "❌bekor":
        await message.answer("Tanlang", reply_markup=menu.markup_menu)
        await cv.zero.set()
        return False
    await state.update_data({"Millati":message.text})
    await message.answer("Яшаш манзилингиз ( Вилоят,туман, кўча):")
    await cv.next()
@dp.message_handler(content_types=['text'], state=cv.address)
async def name(message: types.Message, state: FSMContext):
    if message.text == "❌bekor":
        await message.answer("Tanlang", reply_markup=menu.markup_menu)
        await cv.zero.set()
        return False
    await state.update_data({"Yashash manzili":message.text})
    await message.answer("Телефон ракамингиз:\n\nМисол учун: +998997270657")
    await cv.next()

@dp.message_handler(content_types=['text'], state=cv.number)
async def name(message: types.Message, state: FSMContext):
    phone_number = message.text
    if message.text == "❌bekor":
        await message.answer("Tanlang", reply_markup=menu.markup_menu)
        await cv.zero.set()
        return False
    elif phone_number[:4] == "+998" and len(phone_number) == 13 or phone_number[:2] in config.code_list  and len(phone_number) == 9 :
        await state.update_data({"Telefon raqami" : message.text})
    else:
        await message.answer("Телефон ракамингиз:\n\nМисол учун: +998997270657")
        return False
    await message.answer("Оилавий аxволи (турмуш курган(нечта фарзандингиз бор), турмуш курмаган, ):")
    await cv.next()
@dp.message_handler(content_types=['text'], state=cv.is_married)
async def name(message: types.Message, state: FSMContext):
    if message.text == "❌bekor":
        await message.answer("Tanlang", reply_markup=menu.markup_menu)
        await cv.zero.set()
        return False
    await state.update_data({"Oilaviy ahvoli" : message.text})
    await message.answer("Маълумотингиз (урта, олий)", reply_markup=menu.cancel)
    await cv.next()

@dp.message_handler(content_types=['text'], state=cv.edu)
async def name(message: types.Message, state: FSMContext):
    if message.text == "❌bekor":
        await message.answer("Tanlang", reply_markup=menu.markup_menu)
        await cv.zero.set()
        return False
    await state.update_data({"Ma'lumoti" : message.text})
    await message.answer("Хайдовчилик гувохномангиз борми (кайси класс: А, В, С, D, Е):", reply_markup=menu.cancel)
    await cv.next()
#####
@dp.message_handler(content_types=['text'], state=cv.drive_passport)
async def name(message: types.Message, state: FSMContext):
    if message.text == "❌bekor":
        await message.answer("Tanlang", reply_markup=menu.markup_menu)
        await cv.zero.set()
        return False
    await state.update_data({"Xaydovchilik guvohnomasi":message.text})
    await message.answer("""Хорижий тилларни билишингиз даражаси \n("аъло", "яхши" "паст" каби кoринишда, тулдиринг):""")
    await cv.next()
@dp.message_handler(content_types=['text'], state=cv.lang)
async def name(message: types.Message, state: FSMContext):
    if message.text == "❌bekor":
        await message.answer("Tanlang", reply_markup=menu.markup_menu)
        await cv.zero.set()
        return False
    await state.update_data({"Xorojiy tillarni bilishi" : message.text})
    await message.answer("""Kайси компьютер дастурларида илгари ишлагансиз\n( фоизда % да курсатинг агар
компьютерни билмасангиз буш колдиринг):""")
    await cv.next()
@dp.message_handler(content_types=['text'], state=cv.computer_programs)
async def name(message: types.Message, state: FSMContext):
    if message.text == "❌bekor":
        await message.answer("Tanlang", reply_markup=menu.markup_menu)
        await cv.zero.set()
        return False
    await state.update_data({"Komputer dasturlarni bilishi": message.text})
    await message.answer("""Бизнинг корхона хакида каердан маълумот олдингиз ёки ким сизга таклиф килди: """)
    await cv.next()
@dp.message_handler(content_types=['text'], state=cv.marketing)
async def name(message: types.Message, state: FSMContext):
    if message.text == "❌bekor":
        await message.answer("Tanlang", reply_markup=menu.markup_menu)
        await cv.zero.set()
        return False
    await state.update_data({"Bizning korxona haqida qayerdan ma'lumot olgani" : message.text})
    await message.answer("""Охирги иш жойингиз хакида маълумот берсангиз""")
    await cv.next()
@dp.message_handler(content_types=['text'], state=cv.previous_job)
async def name(message: types.Message, state: FSMContext):
    if message.text == "❌bekor":
        await message.answer("Tanlang", reply_markup=menu.markup_menu)
        await cv.zero.set()
        return False
    await state.update_data({"Oxirgi ish joyi" : message.text})
    await message.answer("""Охирги иш жойингизда ишдан бушаш сабабингиз:""")
    await cv.next()


@dp.message_handler(content_types=['text'], state=cv.cause)
async def name(message: types.Message, state: FSMContext):
    if message.text == "❌bekor":
        await message.answer("Tanlang", reply_markup=menu.markup_menu)
        await cv.zero.set()
        return False
    await state.update_data({"Ishdan ketish sababi" : message.text})
    await message.answer("""Охирги иш урнингиздаги ойлик маошингиз канча булган: """)
    await cv.next()
@dp.message_handler(content_types=['text'], state=cv.previous_price)
async def name(message: types.Message, state: FSMContext):
    if message.text == "❌bekor":
        await message.answer("Tanlang", reply_markup=menu.markup_menu)
        await cv.zero.set()
        return False
    await state.update_data({"Avvalgi maoshi":  message.text})
    await message.answer("Кайси йуналишда (Оддий ходим, Сотув, Бошкарув, Хисоб-китоб, Бухгалтерия, Косиб, Кройчи, Загатофкачи) бемалол кийналмай ишлай оласиз?")
    await cv.next()

@dp.message_handler(content_types=['text'], state=cv.job)
async def name(message: types.Message, state: FSMContext):
    if message.text == "❌bekor":
        await message.answer("Tanlang", reply_markup=menu.markup_menu)
        await cv.zero.set()
        return False
    await state.update_data({"Yo'nalishi" : message.text})
    await message.answer("Бизда канча микдорли маошга ишламокчисиз (ёзишингиз шарт):")
    await cv.next()

@dp.message_handler(content_types=['text'], state=cv.price)
async def name(message: types.Message, state: FSMContext):
    if message.text == "❌bekor":
        await message.answer("Tanlang", reply_markup=menu.markup_menu)
        await cv.zero.set()
        return False
    await state.update_data({"Maoshi" : message.text})
    await message.answer("Бизнинг корхонада канча муддат ишламокчисиз:")
    await cv.next()


@dp.message_handler(content_types=['text'], state=cv.work_timeoff)
async def name(message: types.Message, state: FSMContext):
    if message.text == "❌bekor":
        await message.answer("Tanlang", reply_markup=menu.markup_menu)
        await cv.zero.set()
        return False
    await state.update_data({"Ishlash muddati" : message.text})
    await message.answer("Ишга бориб келгани кийинчилик булмайдими? (узим бора оламан, транспорт зарур, колиб ишламокчиман)")
    await cv.next()


@dp.message_handler(content_types=['text'], state=cv.transport)
async def name(message: types.Message, state: FSMContext):
    if message.text == "❌bekor":
        await message.answer("Tanlang", reply_markup=menu.markup_menu)
        await cv.zero.set()
        return False
    await state.update_data({"Ishga borib kelishdagi qiyinchiliklar" : message.text})
    await message.answer(
        "Узингиз хакингизда нималар кушмокчисиз: ")
    await cv.next()


@dp.message_handler(content_types=['text'], state=cv.about_me)
async def name(message: types.Message, state: FSMContext):
    if message.text == "❌bekor":
        await message.answer("Tanlang", reply_markup=menu.markup_menu)
        await cv.zero.set()
        return False
    await state.update_data({"O'zi haqda" : message.text})
    await message.answer(
        "Расмингизни жўнатинг (3х4 ёки селфи тариқасида расмингизни жўнатинг (3х4 ёки селфи тариқасида)"
    )
    await cv.next()
@dp.message_handler(content_types=['photo'], state=cv.photo)
async def name(message: types.photo_size, state: FSMContext):
    if message.text == "❌bekor":
        await message.answer("Tanlang", reply_markup=menu.markup_menu)
        await cv.zero.set()
        return False
    id = message.from_user.id
    data  = os.listdir("handlers/users/images")
    quant = get_quant(id,data)+1
    await message.photo[-1].download(f'handlers/users/images/{id}_{quant}.jpg')
    data = await state.get_data()
    number = int(database.db().filter("bot",'company', 'amir')[0][1])
    database.db().update("bot", "no",number + 1, "company", 'amir')
    translate_data = {}
    translate_data['name']  = to_latin(data['name'])
    translate_data['Oilaviy ahvoli'] = to_latin(data['Oilaviy ahvoli'])
    del data['name']
    del data['Oilaviy ahvoli']
    for i in data.keys():
        translate_data[i] = to_latin(data[i])
    cv_doc(id,translate_data, quant)
    doc = open(f'handlers/users/pdfs/{id}.pdf', 'rb')
    job = ""
    for i in translate_data["Yo'nalishi"].split():
        job += f"#{i} "
    await dp.bot.send_document(chat_id=config.kanal,  document=doc, caption=f"<b>Yangi Zayavka № {number + 1}</b>  \n<a href='tg://user?id={id}'>{message.from_user.first_name}</a> \n\n\n{job}", parse_mode="html")
    # await dp.bot.send_document(chat_id=id,  document=doc, caption=f"<b>Yangi Zayavka № {len(os.listdir('handlers/users/images'))}</b>  \n<a href='tg://user?id={id}'>{message.from_user.first_name}</a>\n\n\n#{job}", parse_mode="html")
    await dp.bot.send_message(id, "✔️ Рахмат, аризангиз кабул килинди!Қисқа вақт ичида кўриб чиқиб сизга алоқага чиқамиз.Эътиборингиз учун раҳмат!",reply_markup=menu.markup_menu)
    os.remove(f'handlers/users/pdfs/{id}.pdf')
    os.remove(f'handlers/users/images/{id}_{1}.jpg')

    await cv.zero.set()
