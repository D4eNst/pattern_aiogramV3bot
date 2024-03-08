# pattern_aiogramV3bot

Это шаблон для бота aiogramV3, который содержит базовую структуру бота. Включает:

- Создание бота и запуск через polling.
- Создание и подключение базы данных Postgresql, а также middleware,
- которое передает подключение к базе данных для каждого запроса.
- для работы с базой данных используется asyncpg.
- Использование Redis (RedisStorage)
- Использование Docker / Docker-compose
- В коде есть несколько пояснительных комментариев и примеров, также создан базовый обработчик cmd_start

Чтобы всё работало, необходимо добавить .env файл. Пример заполнения находится в .env.example

Это не конечная версия шаблона и в дальнейшем она будет дорабатываться или изменяться


Структура проекта:
```
.
├── README.md
├── bot
│   ├── __init__.py
│   ├── __main__.py
│   ├── bot.py
│   ├── content
│   │   ├── __init__.py
│   │   ├── handlers
│   │   │   ├── __init__.py
│   │   │   ├── basic_handlers.py
│   │   │   ├── keyboards
│   │   │   │   ├── __init__.py
│   │   │   │   ├── ikb.py
│   │   │   │   └── kb.py
│   │   │   └── routs.py
│   │   ├── middlewares
│   │   │   ├── __init__.py
│   │   │   ├── db_session.py
│   │   │   └── middleware.py
│   │   └── states
│   │       ├── __init__.py
│   │       └── states.py
│   └── utils.py
├── data
│   ├── __init__.py
│   └── config.py
├── database
│   ├── __init__.py
│   ├── db.py
│   └── models.py
├── docker-compose.yml
├── dockerfile
├── requirements.txt

```
