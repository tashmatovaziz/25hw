from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import ADMIN
from keyboards import client_kb
from database.bot_db_mentors import sql_command_find_id_mentors, sql_command_find_name_mentors, \
    sql_command_find_direction_mentors, sql_command_find_age_mentors, sql_command_find_group_mentors


class FSMFindId(StatesGroup):
    Id = State()


async def fsm_id_m(message: types.Message):
    if message.from_user.id not in ADMIN:
        await message.answer("Доступ ограничен!")
    if message.chat.type == "private":
        await FSMFindId.Id.set()
        await message.answer("Id ментора?", reply_markup=client_kb.cancel_markup)
    else:
        await message.answer("Пиши в личке!")


async def find_id(message: types.Message, state: FSMContext):
    read = await sql_command_find_id_mentors(message.text)
    for res in read:
        await message.answer(f"ID = {res[0]},Name {res[1]}, Direction {res[2]}, Age {res[3]}, Group {res[4]}")
    await state.finish()


class FSMFindName(StatesGroup):
    Name = State()


async def fsm_name_m(message: types.Message):
    if message.from_user.id not in ADMIN:
        await message.answer("Доступ ограничен!")
    if message.chat.type == "private":
        await FSMFindName.Name.set()
        await message.answer("Имя ментора?", reply_markup=client_kb.cancel_markup)
    else:
        await message.answer("Пиши в личке!")


async def find_name(message: types.Message, state: FSMContext):
    read = await sql_command_find_name_mentors(message.text)
    for res in read:
        await message.answer(f"ID = {res[0]},Name {res[1]}, Direction {res[2]}, Age {res[3]}, Group {res[4]}")
    await state.finish()


class FSMFindDirection(StatesGroup):
    direction = State()


async def fsm_direction_m(message: types.Message):
    if message.from_user.id not in ADMIN:
        await message.answer("Доступ ограничен!")
    if message.chat.type == "private":
        await FSMFindDirection.direction.set()
        await message.answer("Напрвление ментора?", reply_markup=client_kb.cancel_markup)
    else:
        await message.answer("Пиши в личке!")


async def find_direction(message: types.Message, state: FSMContext):
    read = await sql_command_find_direction_mentors(message.text)
    for res in read:
        await message.answer(f"ID = {res[0]},Name {res[1]}, Direction {res[2]}, Age {res[3]}, Group {res[4]}")
    await state.finish()


class FSMFindAge(StatesGroup):
    age = State()


async def fsm_age_m(message: types.Message):
    if message.from_user.id not in ADMIN:
        await message.answer("Доступ ограничен!")
    if message.chat.type == "private":
        await FSMFindAge.age.set()
        await message.answer("Напрвление ментора?", reply_markup=client_kb.cancel_markup)
    else:
        await message.answer("Пиши в личке!")


async def find_age(message: types.Message, state: FSMContext):
    read = await sql_command_find_age_mentors(message.text)
    for res in read:
        await message.answer(f"ID = {res[0]},Name {res[1]}, Direction {res[2]}, Age {res[3]}, Group {res[4]}")
    await state.finish()


class FSMFindGroup(StatesGroup):
    group = State()


async def fsm_group_m(message: types.Message):
    if message.from_user.id not in ADMIN:
        await message.answer("Доступ ограничен!")
    if message.chat.type == "private":
        await FSMFindGroup.group.set()
        await message.answer("Напрвление ментора?", reply_markup=client_kb.cancel_markup)
    else:
        await message.answer("Пиши в личке!")


async def find_group(message: types.Message, state: FSMContext):
    read = await sql_command_find_group_mentors(message.text)
    for res in read:
        await message.answer(f"ID = {res[0]},Name {res[1]}, Direction {res[2]}, Age {res[3]}, Group {res[4]}")
    await state.finish()


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Canceled")


def register_handlers_find_mentors(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_reg,
                                Text(equals="cancel", ignore_case=True),
                                state="*")

    dp.register_message_handler(fsm_id_m, commands=['id'])
    dp.register_message_handler(find_id, state=FSMFindId.Id)

    dp.register_message_handler(fsm_name_m, commands=['name'])
    dp.register_message_handler(find_name, state=FSMFindName.Name)

    dp.register_message_handler(fsm_direction_m, commands=['direction'])
    dp.register_message_handler(find_direction, state=FSMFindDirection.direction)

    dp.register_message_handler(fsm_age_m, commands=['age'])
    dp.register_message_handler(find_age, state=FSMFindAge.age)

    dp.register_message_handler(fsm_group_m, commands=['group'])
    dp.register_message_handler(find_group, state=FSMFindGroup.group)