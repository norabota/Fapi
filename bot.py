import logging
from aiogram import Bot, Dispatcher, executor, types
import config
import markups as nav

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот успешно запущен!')


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    markup_menu = nav.menu_id('start')
    await bot.send_message(message.from_user.id, 'Здравствуйте, {0.first_name}!'.format(message.from_user),
                           reply_markup=markup_menu[1])


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text in nav.allMenu:
        markup_menu = nav.menu_id(message.text)
        print(type(markup_menu))
        await bot.send_message(message.from_user.id, f'{markup_menu[0]}', reply_markup=markup_menu[1])
    else:
        await message.reply('Выберите пункт меню...')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
