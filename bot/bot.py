from aiogram import Dispatcher, Bot
from database import storage
from data.config import token


bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher(storage=storage)
