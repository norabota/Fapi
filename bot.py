import logging
from aiogram import Bot, Dispatcher, executor, types
import config
import inline_markups as nav

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот успешно запущен!')


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    inline_menu = nav.menu_commands('start')
    print(inline_menu)
    await bot.send_message(message.from_user.id,
                           '.           Здравствуйте, {0.first_name}!         .'.format(message.from_user),
                           reply_markup=inline_menu["submenu"])


@dp.callback_query_handler(lambda call: True)
async def process_callback(callback_query: types.CallbackQuery):
    code = callback_query.data
    print(1, code)
    inline_menu = nav.menu_inline(callback_query.data)
    if inline_menu:
        await bot.send_message(callback_query.from_user.id, f'{inline_menu["answer"]}',
                               reply_markup=inline_menu["submenu"],
                               parse_mode="MarkdownV2")
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
