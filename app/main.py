import asyncio
from app.create_bot import bot, dp
from app.handlers.main_handlers import start_router, riding_now_router, get_location_router, who_is_near_router
from app.handlers.return_handlers.back_to_main_from_sub import back_to_main_from_sub_router
from loguru import logger


# TODO Подключить пакетный менеджер (poetry/uv), если целесообразно
# TODO Реализоать загрузку фото себя и своего транспорта
# TODO Реализоать хранение пользователей
# TODO Доработать геолокацию
# TODO Подключить линтер
# TODO Реализовать обратную связь пользователей со мной (вопросы/пожелания/предложения)
async def main():
    logger.info("Бот запущен")
    dp.include_router(start_router)
    dp.include_router(riding_now_router)
    dp.include_router(get_location_router)
    dp.include_router(who_is_near_router)
    dp.include_router(back_to_main_from_sub_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
