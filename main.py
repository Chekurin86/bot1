import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.enums import ParseMode

from handlers import command_start_handler, echo_handler
from loader import dp
from loader import TOKEN
from aiogram.client.bot import DefaultBotProperties


async def main() -> None:
    dp.message.register(command_start_handler)
    dp.message.register(echo_handler)
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())