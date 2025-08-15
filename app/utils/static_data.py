from enum import StrEnum


class FilterTexts(StrEnum):
    """
    Перечисления всех текстов, которые обрабатываются фильтрами
    """
    im_riding = "🚴 Я катаюсь"
    whos_near = "📍 Кто рядом"
    send_geo = "📍 Отправить геопозицию"
    back = "⬅️ Назад"
