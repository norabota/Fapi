import logging
from aiogram import Bot, Dispatcher, executor, types
import config
import markups as nav
import json

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот успешно запущен!')


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет, {0.first_name}!'.format(message.from_user),
                           reply_markup=nav.mainMenu)


with open('data_file.json', "r") as file:
    data = json.load(file)


@dp.message_handler()
async def bot_message(message: types.Message):
    key = data.get(message.text)
    ss = key["markup"]

    await bot.send_message(message.from_user.id, f'{key["answer"]}', reply_markup=nav.mainMenu)
    if message.text not in nav.ollMenu:
        await message.reply('Выберите пункт меню...')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
