import os
# Needed adding .env file with 5 constants:
# POSTGRES_USER
# POSTGRES_PASSWORD
# REDIS_PASSWORD
# TOKEN
# ADMIN_ID

token = os.environ["TOKEN"]
payment_token = os.environ["PAYMENT_TOKEN"]
admin_id = int(os.environ["ADMIN_ID"])

redis_host = "redis"
redis_password = os.environ["REDIS_PASSWORD"]
redis_port = 6379
redis_url = f"redis://:{redis_password}@{redis_host}:{redis_port}"

postgres_password = os.environ["POSTGRES_PASSWORD"]
postgres_user = os.environ["POSTGRES_USER"]
postgres_db = postgres_user
postgres_app_db = "db_name"
postgres_host = "postgres_db"


db_connection_data = {
    "user": postgres_user,
    "password": postgres_password,
    "database": postgres_app_db,
    "host": postgres_host,
    "port": 5432,
    "command_timeout": 60
}
