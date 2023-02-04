from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import client_kb
from config import ADMIN
from database.bot_db_mentors import sql_command_insert


class FSMAdmin(StatesGroup):
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.from_user.id not in ADMIN:
        await message.answer("Доступ ограничен!")
    else:
        if message.chat.type == "private":
            await FSMAdmin.name.set()
            await message.answer("Имя ментора?", reply_markup=client_kb.cancel_markup)
        else:
            await message.answer("Пиши в личке!")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Id'] = message.message_id
        data['name'] = message.text
    await FSMAdmin.direction.set()
    await message.answer("Напрвление?")


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числа!")
    elif not 13 < int(message.text) < 70:
        await message.answer("Доступ ограничен!")
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMAdmin.next()
        await message.answer("Группа?", reply_markup=client_kb.cancel_markup)


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer("Возраст ментора?")


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await message.answer(f"ID Mentor = {data['Id']}\n"
            f"{data['name']}, {data['direction']}, {data['age']}, {data['group']}"
        )
    await FSMAdmin.next()
    await message.answer("Все верно?",
                         reply_markup=client_kb.submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        async with state.proxy() as data:
            data['data'] = message.date
        await sql_command_insert(state)
        await state.finish()
    elif message.text.lower() == "заново":
        await FSMAdmin.name.set()
        await message.answer("Имя ментора?", reply_markup=client_kb.cancel_markup)
    else:
        await message.answer('Нипонял!?')


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Canceled")


def register_handlers_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_reg,
                                Text(equals="cancel", ignore_case=True),
                                state="*")

    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)