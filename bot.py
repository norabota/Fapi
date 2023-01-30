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
    markup_menu = inav.menu_commands('start')
    print(markup_menu)
    await bot.send_message(message.from_user.id, '.          Здравствуйте, {0.first_name}!          .'.format(message.from_user),
                           reply_markup=markup_menu["submenu"])


@dp.callback_query_handler(lambda call: True)
async def process_callback(callback_query: types.CallbackQuery):
    code = callback_query.data
    print(6666666,code)
    inline_callback_menu = inav.menu_inline(callback_query.data)
    if inline_callback_menu:
        await bot.send_message(callback_query.from_user.id, f'{inline_callback_menu["answer"]}',
                           reply_markup=inline_callback_menu["submenu"],
                           parse_mode="MarkdownV2")
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)


# @dp.message_handler()
# async def bot_message(message: types.Message):
#     markup_menu = nav.menu_id(message.text)
#     inline_links_menu = inav.menu_id_links(message.text)
#     inline_callback_menu = inav.menu_inline(message.text)
#     print(99, inline_callback_menu)
#     print(65, inline_links_menu)
#     print(67, markup_menu)
#     if inline_links_menu:
#         await message.answer("Перейдите по ссылке", reply_markup=inline_links_menu["submenu"], parse_mode="MarkdownV2")
#     if markup_menu:
#         await bot.send_message(message.from_user.id, f'{markup_menu["answer"]}', reply_markup=markup_menu["submenu"],
#                                parse_mode="MarkdownV2")
#     if inline_callback_menu:
#         await message.answer(f'{inline_callback_menu["answer"]}', reply_markup=inline_callback_menu["submenu"],
#                              parse_mode="MarkdownV2")
#     if markup_menu is False and inline_links_menu is False and inline_callback_menu is False:
#         await message.reply(
#             'Выбранный  пункт меню сейчас в разработке, выберите другой пункт меню из предложенной клавиатуры')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
