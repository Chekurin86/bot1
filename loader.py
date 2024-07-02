from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config import TOKEN
from aiogram.client.bot import DefaultBotProperties

bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


