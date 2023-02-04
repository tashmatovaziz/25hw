from config import bot, PAYMENTS_TOKEN, ADMIN
import logging
from aiogram import Dispatcher, types
from aiogram.types.message import ContentType


logging.basicConfig(level=logging.INFO)


PRICE = types.LabeledPrice(label="Подписка на 1 месяц", amount=500 * 100)


async def buy(message: types.Message):
    if PAYMENTS_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, "Тестовый платеж!!!")

    await bot.send_invoice(message.chat.id,
                           title="Подписка на бота",
                           description="Активация подписки на бота на 1 месяц",
                           provider_token=PAYMENTS_TOKEN,
                           currency="KGS",
                           photo_url="https://marketplace.cs-cart.com/images/logos/3/Pay_Logo_-_RGB_Primary_Logo.png",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter="one-month-subscription",
                           payload="some-invoice-payload-for-our-internal-use")


async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


async def successful_payment(message: types.Message):
    await bot.send_message(ADMIN, f"SUCCESSFUL PAYMENT:{message.chat.id}")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        await bot.send_message(ADMIN, f"{k} = {v}")

    await bot.send_message(message.chat.id,
                           f"Платёж на сумму {message.successful_payment.total_amount // 100}"
                           f" {message.successful_payment.currency} прошел успешно!!!")


def register_handlers_pay(dp: Dispatcher):
    dp.register_message_handler(buy, commands=['buy'])
    dp.register_message_handler(successful_payment, content_types=ContentType.SUCCESSFUL_PAYMENT)
    dp.pre_checkout_query_handler(pre_checkout_query, lambda query: True)