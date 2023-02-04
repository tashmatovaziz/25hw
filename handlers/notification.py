import aioschedule
import asyncio
from aiogram import types, Dispatcher
from config import bot
from Parssss.weath import parser


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = list()
    chat_id.append(message.from_user.id)
    await message.answer("Ok")


async def go_to_study():
    for id in chat_id:
        await bot.send_message(id, "сегодня занятие в 8 часов вечера!")


async def get_weather():
    weather = parser()
    for id in chat_id:
        await bot.send_message(id, f"{weather['link']}\n{weather['date']}\ntemp {weather['now-weather']}\n"
                                   f"{weather['now-feel']}\n"f"{weather['now-desc']}\n"
                                   f"Заход {weather['astro-sunrise'][5:]}\nВосход "f"{weather['astro-sunset'][6:]}\n"
                                   f"Ветер {weather['now-info-item wind'][5:9]}\n"
                                   f"Влажность {weather['now-info-item humidity'][9:]}")


async def scheduler():
    aioschedule.every().monday.at("13:32").do(go_to_study)
    aioschedule.every().thursday.at("14:24").do(go_to_study)
    aioschedule.every().day.at("08:01").do(get_weather)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: "напомни" in word.text)