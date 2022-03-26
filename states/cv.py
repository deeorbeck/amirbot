from aiogram.dispatcher.filters.state import State, StatesGroup

class cv(StatesGroup):
    zero = State()
    name = State()
    birth = State()
    nation = State()
    address = State()
    number = State()
    is_married = State()
    edu = State()

    drive_passport = State()
    lang = State()
    computer_programs = State()
    marketing = State()
    previous_job = State()
    cause = State()
    previous_price = State()

    job = State()
    price = State()

    work_timeoff = State()
    transport = State()
    about_me = State()

    photo = State()

