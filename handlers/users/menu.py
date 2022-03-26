from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default import menu
from doc import cv_doc
from states.cv import cv
from data import config


@dp.message_handler(content_types=['text'],state=cv.zero)
async def sign(message: types.Message):
    if message.text == "🧾 Анкета толдириш":
        await message.answer("Фамилия, исм-шарифингиз \n(Икромов Бунёдбек Фарход ўғли):", reply_markup=menu.cancel)
        await cv.name.set()
    if message.text == "Админ":
        await message.answer("Админ: @Business_Amir_brend")
    if message.text == "Биз хақимизда":
        await message.answer(config.textx)
