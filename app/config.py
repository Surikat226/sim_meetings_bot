from dotenv import load_dotenv
import os


load_dotenv()  # парсим .env-файл
BOT_TOKEN = os.getenv('BOT_TOKEN')  # получаем ключ бота из .env
GEO_SERVICE_URL = os.getenv('GEO_SERVICE_URL')  # получаем url сервиса, обрабатывающего геолокацию пользователей