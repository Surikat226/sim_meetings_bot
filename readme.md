# SIMtastic!
SIMtastic! - Телеграм-бот на aiogram3 для коммуникации и совместных поездок пользователей СИМ (средств индивидуальной мобильности)

# Развёртывание и запуск бота
1. Установить пакетный менеджер uv в операционную систему:  
__Windows__: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`  
__macOS и Linux__: `curl -LsSf https://astral.sh/uv/install.sh | less`  
__Также можно через pip__: `pip install uv`
Помимо этого, есть и другие способы установки. Подробнее на оф. сайте с документацией: `https://docs.astral.sh/uv/getting-started/installation/`
2. Перейти в корневую директорию с проектом через терминал: `cd {путь/до/директории/c/ботом/simtastic_bot}`
3. Установить все зависимости командой: `uv sync`
4. В корень проекта добавить файл `.env`, внутри которого необходимо прописать токен бота в формате: `BOT_TOKEN='токен_бота'`
5. Запустить бота командой: `uv run python -m app.main`