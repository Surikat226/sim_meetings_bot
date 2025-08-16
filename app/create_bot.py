from app.config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
