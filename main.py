import asyncio
from create_bot import bot, dp
from aiogram import F
from aiogram.filters import Command
from handlers import cmd_start, riding_now, get_location, who_is_near


# TODO Добавить логирование
# TODO Реализовать переход между состояниями в меню
# TODO Реализоать загрузку фото себя и своего транспорта
# TODO Реализоать хранение пользователей
# TODO Доработать геолокацию
async def main():
    print("Бот запущен")
    # Регистрируем обработчики
    dp.message.register(cmd_start, Command("start"))
    dp.message.register(riding_now, F.text == "🚴 Я катаюсь")
    dp.message.register(get_location, F.location)
    dp.message.register(who_is_near, F.text == "📍 Кто рядом")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
