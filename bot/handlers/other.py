from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from bot.keyboards import menu_inline, menu_commands


async def command_start(message: Message):
    inline_menu = menu_commands('start')
    print(1, inline_menu)
    await message.bot.send_message(message.from_user.id,
                                   '.           Здравствуйте, {0.first_name}!         .'.format(message.from_user),
                                   reply_markup=inline_menu["submenu"])


async def process_callback(callback_query: CallbackQuery):
    code = callback_query.data
    print(2, code)
    inline_menu = menu_inline(callback_query.data)
    if inline_menu:
        await callback_query.bot.send_message(callback_query.from_user.id, f'{inline_menu["answer"]}',
                                              reply_markup=inline_menu["submenu"],
                                              parse_mode="MarkdownV2")
        await callback_query.bot.delete_message(chat_id=callback_query.from_user.id,
                                                message_id=callback_query.message.message_id)


def register_other_handlers(dp: Dispatcher) -> None:
    # todo: register all other handlers
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_callback_query_handler(process_callback, lambda call: True)
