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
    await bot.send_message(message.from_user.id, 'Привет, {0.first_name}!'.format(message.from_user),
                           reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    for key, value in nav.dict_buttons_Contacts.items():
        if message.text == key:
            await bot.send_message(message.from_user.id, f'{value}', reply_markup=nav.contactsMenu)
    for key, value in nav.dict_buttons_Products.items():
        if message.text == key:
            await bot.send_message(message.from_user.id, f'{value}', reply_markup=nav.productsMenu)
    for key, value in nav.dict_buttons_Download.items():
        if message.text == key:
            await bot.send_message(message.from_user.id, f'{value}', reply_markup=nav.downloadMenu)
    if message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'Главное меню', reply_markup=nav.mainMenu)
    if message.text not in nav.ollMenu:
        await message.reply('Выберите пункт меню')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
