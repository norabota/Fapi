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
    # await bot.send_message(message.from_user.id, message.text)
    if message.text == 'Продукты':
        await bot.send_message(message.from_user.id, 'Меню "Продукты"', reply_markup=nav.productsMenu)
    elif message.text == 'Скачать бесплатно':
        await bot.send_message(message.from_user.id, 'Меню "Скачать бесплатно"', reply_markup=nav.downloadMenu)
    elif message.text == 'Контакты':
        await bot.send_message(message.from_user.id, 'Меню "Контакты"', reply_markup=nav.contactsMenu)
    elif message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'Главное меню', reply_markup=nav.mainMenu)
    elif message.text == 'База кроссов FAPI':
        await bot.send_message(message.from_user.id, 'Потом здесь будет описание базы и способ оплаты',
                               reply_markup=nav.productsMenu)
    elif message.text == 'Каталог  по маркам':
        await bot.send_message(message.from_user.id, 'Потом здесь будет описание базы и способ оплаты',
                               reply_markup=nav.productsMenu)
    elif message.text == 'База фото автозапчастей':
        await bot.send_message(message.from_user.id, 'Потом здесь будет описание базы и способ оплаты',
                               reply_markup=nav.productsMenu)
    elif message.text == 'Штрих-коды автозапчастей':
        await bot.send_message(message.from_user.id, 'Потом здесь будет описание базы и способ оплаты',
                               reply_markup=nav.productsMenu)
    elif message.text == 'База артикулов автозапчастей':
        await bot.send_message(message.from_user.id, 'Потом здесь будет описание базы и способ оплаты',
                               reply_markup=nav.productsMenu)
    elif message.text == '1С: Автобизнес':
        await bot.send_message(message.from_user.id, 'Потом здесь будет описание базы и способ оплаты',
                               reply_markup=nav.productsMenu)
    elif message.text == 'API интеграция':
        await bot.send_message(message.from_user.id, 'Потом здесь будет описание базы и способ оплаты',
                               reply_markup=nav.productsMenu)
    elif message.text == 'База кроссов онлайн':
        await bot.send_message(message.from_user.id, 'Потом здесь будет описание базы и способ оплаты',
                               reply_markup=nav.productsMenu)
    elif message.text == 'База автовладельцев ВКонтакте':
        await bot.send_message(message.from_user.id, 'Потом здесь будет описание базы и способ оплаты',
                               reply_markup=nav.productsMenu)
    elif message.text == 'Фото логотипов автомобилей':
        await bot.send_message(message.from_user.id, 'Потом здесь будет описание базы и способ оплаты',
                               reply_markup=nav.productsMenu)
    elif message.text == 'Ссылки для скачивания':
        await bot.send_message(message.from_user.id, 'Потом здесь будут ссылки на скачивание',
                               reply_markup=nav.downloadMenu)
    elif message.text == 'Email':
        await bot.send_message(message.from_user.id, 'Потом здесь адрес и переход на почту',
                               reply_markup=nav.contactsMenu)
    else:
        await message.reply('Выберите пункт меню')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
