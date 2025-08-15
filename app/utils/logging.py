from functools import wraps
from loguru import logger
from aiogram import types


def log_handler(func):
    """
    Декоратор, который добавляет логирование хендлеров
    """

    @wraps(func)
    async def wrapper(message: types.Message, *args, **kwargs):
        user = message.from_user
        logger.info(
            f"Хендлер: {func.__name__} | "
            f"ID: {user.id} | "
            f"Username: @{user.username} | "
            f"Имя: {user.first_name} | "
            f"Сообщение: {message.text}"
        )
        return await func(message, *args, **kwargs)
    return wrapper
