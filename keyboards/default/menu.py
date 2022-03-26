from aiogram import types


markup_menu = types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [types.KeyboardButton("🧾 Анкета толдириш")],
        [types.KeyboardButton("Админ"), types.KeyboardButton("Биз хақимизда")]
    ]
)
is_married = types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [types.KeyboardButton("Ха"), types.KeyboardButton("Йўқ")]
    ]
)
cancel = types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [types.KeyboardButton("❌bekor")]
    ]
)
Phone_number = types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [types.KeyboardButton(request_contact=True, text="Telefon Raqamingiz")]
    ]
)