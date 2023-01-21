import logging
from aiogram import Bot, Dispatcher, executor, types
import config
import markups as nav
import inline_markups as inav
logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот успешно запущен!')


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    markup_menu = nav.menu_commands('start')
    await bot.send_message(message.from_user.id, 'Здравствуйте, {0.first_name}!'.format(message.from_user),
                           reply_markup=markup_menu["submenu"])


@dp.message_handler()
async def bot_message(message: types.Message):
    markup_menu = nav.menu_id(message.text)
    inline_markup_menu = inav.menu_id_links(message.text)
    print(65, inline_markup_menu)
    print(655, inline_markup_menu["submenu"]["inline_keyboard"])
    print(66, type(markup_menu))
    print(67, markup_menu)
    # if markup_menu is False:
    #     await message.reply(
    #         'Выбранный  пункт меню сейчас в разработке, выберите другой пункт меню из предложенной клавиатуры')
    if markup_menu is False and inline_markup_menu["submenu"] != []:
        await message.answer("guyguyfyfyfy", reply_markup=inline_markup_menu["submenu"])
    else:
        await bot.send_message(message.from_user.id, f'{markup_menu["answer"]}', reply_markup=markup_menu["submenu"])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
