from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = config("TOKEN")
AD = config("ADMIN")
PAYMENTS_TOKEN = config("PAYMENTS_TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMIN = (5742796974, )