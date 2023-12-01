from aiogram import filters, Dispatcher, F
import bot.content.states as states

from .basic_handlers import *


def rg_msg_hd(dp: Dispatcher) -> None:
    dp.message.register(cmd_start, filters.Command(commands=['start']))
    # dp.message.register(set_state, filters.Command(commands=['set_state']))
