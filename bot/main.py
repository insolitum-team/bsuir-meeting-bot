from aiogram import Dispatcher, Bot, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.misc import config
from bot.handlers.main import register_all_handlers


def __on_startup(dp: Dispatcher):
    register_all_handlers(dp)


def start_bot():
    bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot=bot, storage=MemoryStorage())
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=__on_startup(dp))
