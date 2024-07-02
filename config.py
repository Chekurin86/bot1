import os
from dotenv import load_dotenv

# Загрузка переменных щкружения из .env файла
load_dotenv()

# Извлекаем из .env Токен Бота
TOKEN = str(os.getenv("BOT_TOKEN"))