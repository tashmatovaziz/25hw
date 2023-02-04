from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

start_button = KeyboardButton("/start")
info_button = KeyboardButton("game")
quiz_button = KeyboardButton("/quiz")

start_markup.add(start_button, info_button, quiz_button)

game_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

a_button = KeyboardButton('⚽')
b_button = KeyboardButton('🏀')
c_button = KeyboardButton('/🎳')

game_markup.add(a_button, b_button, c_button)

cancel_button = KeyboardButton("CANCEL")

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton("ДА"),
    KeyboardButton("ЗАНОВО"),
    cancel_button
)

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    cancel_button
)