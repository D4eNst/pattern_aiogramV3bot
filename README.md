# pattern_aiogramV3bot

This is a template for the aiogramV3 bot, which contains the basic structure of the bot. Included: 

Creating a bot and launching it via start polling.
Creating and connecting a Postgresql database, as well as middleware, 
which transmits a database connection to each request. asyncpg is used 
to work with the database.
The Redis that the bot uses (RedisStorage is passed to Dispatcher)
There are some explanatory comments and examples in the code, and a basic handler cmd_start has been created

For the bot to work, you need to add a file to the project .env which will contain the following constants:
POSTGRES_USER        = (for example: postgres)
POSTGRES_PASSWORD    = (for example: qwerty)
REDIS_PASSWORD       = (for example: qwerty)
TOKEN                = (get your token here: https://t.me/BotFather)
ADMIN_ID             = (your telegram id)



Project structure:

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

