# pattern_aiogramV3bot

Это шаблон для бота aiogramV3, который содержит базовую структуру бота. Включает:

- Создание бота и запуск через polling.
- Создание и подключение базы данных Postgresql, а также middleware,
- которое передает подключение к базе данных для каждого запроса.
- для работы с базой данных используется asyncpg.
- Использование Redis (RedisStorage)
- Использование Docker / Docker-compose
- В коде есть несколько пояснительных комментариев и примеров, также создан базовый обработчик cmd_start

Чтобы всё работало, необходимо добавить .env файл, который будет содержать следующие константы:
POSTGRES_USER        = (for example: postgres)
POSTGRES_PASSWORD    = (for example: qwerty)
REDIS_PASSWORD       = (for example: qwerty)
TOKEN                = (get your token here: https://t.me/BotFather)
ADMIN_ID             = (your telegram id)

Это не конечная версия шаблона и в дальнейшем она будет дорабатываться или изменяться


Структура проекта:
```
path/to/the/project:.
│   .dockerignore
│   .env
│   .gitignore
│   docker-compose.yml
│   dockerfile
│   requirements.txt
│   
├───bot
│   │   bot.py
│   │   utils.py
│   │   __init__.py
│   │   __main__.py
│   │
│   ├───content
│   │   │   __init__.py
│   │   │
│   │   ├───handlers
│   │   │   │   basic_handlers.py
│   │   │   │   __init__.py
│   │   │   │
│   │   │   ├───keyboards
│   │   │   │   │   ikb.py
│   │   │   │   │   kb.py
│   │   │   │   │   __init__.py
│   │   │
│   │   ├───middlewares
│   │   │   │   db_session.py
│   │   │   │   __init__.py
│   │   │
│   │   ├───states
│   │   │   │   states.py
│   │   │   │   __init__.py
│   │   │
│
├───data
│   │   config.py
│   │   __init__.py
│   │
│
├───database
│   │   db.py
│   │   models.py
│   │   __init__.py
│   │
```
