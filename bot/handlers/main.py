from aiogram import Dispatcher

from bot.handlers.users.main import register_users_handlers
from bot.handlers.admin.main import register_admins_handlers


def register_all_handlers(dp: Dispatcher):
    handlers = [
        register_users_handlers,
        register_admins_handlers,
    ]
    for handler in handlers:
        handler(dp)
