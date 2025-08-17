# SIMtastic!
SIMtastic! - Телеграм-бот на aiogram3 для коммуникации и совместных поездок пользователей СИМ (средств индивидуальной мобильности)

# Установка зависимостей для бота
## Установка пакетного менеджера uv
Установить пакетный менеджер __uv__ в операционную систему, если он ещё не установлен:  
__Windows__: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`  
__macOS и Linux__: `curl -LsSf https://astral.sh/uv/install.sh | less`  
__Также можно через pip__: `pip install uv`  
_Помимо этого, есть и другие способы установки. Подробнее на оф. сайте с документацией:_ `https://docs.astral.sh/uv/getting-started/installation/`  
Проверить, установлен ли uv, можно командой: `uv --version`
## Установка утилиты make
Установить утилиту __make__, если она ещё не установлена:  

__Windows__:  
Установить __scoop__ (если ещё не установлен) для возможности в дальнейшем установить __make__:  
Открыть терминал __powershell__ и ввести команды:  
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`  
`Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression`  
1.2 Так же через терминал установить __make__: `scoop install make`  

__macOS__:  
_Вариант 1_: В терминале ввести команду: `xcode-select --install`  
_Вариант 2_: Если установлен Homebrew: `brew install make`  

__Linux__:  
В большинстве дистрибутивов Linux __make__ уже предустановлен. Проверить наличие __make__ можно командой: `make --version`  
Если же __make__ не был обнаружен в системе, установить его командами:  
`sudo apt update`  
`sudo apt install make`
## Добавление токена бота
1. Перейти в корневую директорию с проектом через терминал: `cd {путь/до/директории/c/ботом/simtastic_bot}`
2. В корень проекта добавить файл `.env`, внутри которого необходимо прописать токен бота в формате: `BOT_TOKEN='токен_бота'`

# Запуск бота
Запустить бота командой: `make run`