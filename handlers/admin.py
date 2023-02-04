from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, ADMIN
from database.bot_db_mentors import sql_command_delete, sql_command_list_mentors
from keyboards.admin_cd import find_markup


async def find_mentors(message: types.Message):
    if message.from_user.id not in ADMIN:
        await message.answer("Доступ ограничен!")
    if message.chat.type == "private":
        await message.answer('по каким данным искать?', reply_markup=find_markup)
    else:
        await message.answer("Пиши в личке!")


async def get_list_mentors(message: types.Message):
    if message.from_user.id in ADMIN:
        read = await sql_command_list_mentors(message)
        for res in read:
            await message.answer(f"ID = {res[0]},Name {res[1]}, Direction {res[2]}, Age {res[3]}, Group {res[4]}",
                                 reply_markup=InlineKeyboardMarkup().
                                 add(InlineKeyboardButton(f"delete {res[1]}",
                                                          callback_data=f"delete {res[0]}"),
                                     InlineKeyboardButton(f"change {res[1]}",
                                                          callback_data=f"change {res[0]}")))


async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace("delete ", ""))
    await call.answer(text="Deleted!", show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(get_list_mentors, commands=['list'])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith("delete "))
    dp.register_message_handler(find_mentors, commands=['find'])
