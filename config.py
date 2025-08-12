from dotenv import load_dotenv
import os


load_dotenv()  # парсим .env-файл
BOT_TOKEN = os.getenv('BOT_TOKEN')  # получаем ключ бота из .env