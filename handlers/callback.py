from aiogram import types, Dispatcher
from config import bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT>>>", callback_data='button_call_2')
    markup.add(button_call_2)

    question = "Лучшие фильмы про супергероев?"
    answers = [
        '[1]',
        '[2]',
        '[3]',
        '[4]',
    ]

    photo = open("media/img_1.png", 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        open_period=15,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    question = "Лучший спорт?"
    answers = [
        'волейбол',
        'футбол',
        'баскетбол',
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        open_period=10,
    )


async def photo_mem2(call: types.CallbackQuery):
    photo2 = open("media/img.jpg", 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo2)


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")
    dp.register_callback_query_handler(photo_mem2, text="button_call_3")
    dp.register_callback_query_handler(quiz_3, text="button_call_2")