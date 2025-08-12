import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from config import BOT_TOKEN


# TODO Разбить всё на модули
def get_main_menu() -> ReplyKeyboardMarkup:
    keyboard_buttons = [
        [KeyboardButton(text="🚴 Я катаюсь")],
        [KeyboardButton(text="📍 Кто рядом")]
    ]
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=keyboard_buttons
    )
    return keyboard


async def cmd_start(message: types.Message):
    """
    /start — приветственное сообщение
    """
    await message.answer(
        f"Привет, {message.from_user.first_name}! 🚀\n"
        "Я помогу тебе находить других райдеров поблизости.\n"
        "Выбери действие ниже:",
        reply_markup=get_main_menu()
    )


async def riding_now(message: types.Message):
    """
    Кнопка "🚴 Я катаюсь"
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📍 Отправить геопозицию", request_location=True)]
        ],
        resize_keyboard=True
    )
    await message.answer(
        "Отправь свою геопозицию (можно в реальном времени), чтобы другие могли тебя найти.",
        reply_markup=keyboard
    )


async def handle_location(message: types.Message):
    """
    Принимает геопозицию от пользователя
    """
    lat = message.location.latitude
    lon = message.location.longitude
    await message.answer(
        f"✅ Я получил твоё местоположение!\n"
        f"Широта: {lat}\nДолгота: {lon}",
        reply_markup=get_main_menu()
    )


async def who_is_near(message: types.Message):
    """
    Кнопка "📍 Кто рядом"
    """
    await message.answer("Функция 'Кто рядом' скоро будет доступна! 😉")


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Регистрируем обработчики
    dp.message.register(cmd_start, Command("start"))
    dp.message.register(riding_now, F.text == "🚴 Я катаюсь")
    dp.message.register(handle_location, F.location)
    dp.message.register(who_is_near, F.text == "📍 Кто рядом")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
