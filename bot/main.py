from aiogram.utils import executor
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types

from bot.filters import register_all_filters
from bot.misc import TgKeys
from bot.handlers import register_all_handlers
from bot.database.models import register_models
from bot.database.models.main import create_db

import logging

logging.basicConfig(level=logging.INFO)

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


async def __on_start_up(dp: Dispatcher) -> None:
    await create_db()
    register_all_filters(dp)
    register_all_handlers(dp)
    register_models()
    logging.info('Start bot')
    print('Бот успешно запущен !')
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Запустить бота'),  # пока добавляем только одну команду
        ]
    )


def start_bot():
    bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot, storage=MemoryStorage())
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)
