from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

find_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton('/id'),
    KeyboardButton('/name'),
    KeyboardButton('/direction'),
    KeyboardButton('/age'),
    KeyboardButton('/group'),
)