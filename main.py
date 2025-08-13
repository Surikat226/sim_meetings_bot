import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from config import BOT_TOKEN
from handlers.start import cmd_start
from handlers.riding_now import riding_now
from handlers.get_location import get_location
from handlers.who_is_near import who_is_near


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Регистрируем обработчики
    dp.message.register(cmd_start, Command("start"))
    dp.message.register(riding_now, F.text == "🚴 Я катаюсь")
    dp.message.register(get_location, F.location)
    dp.message.register(who_is_near, F.text == "📍 Кто рядом")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
