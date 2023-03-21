from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from bot.keyboards import menu_inline, menu_commands
from bot.database.models.main import create_db, DBCommands

db = DBCommands()


async def command_start(message: Message):
    inline_menu = menu_commands('start')
    await create_db()
    await db.add_new_user()
    count_users = await db.count_users()
    all_users = await db.select_all_users()
    print(f'Количество пользователей в базе: {count_users}')
    print(all_users)
    await message.bot.send_message(message.from_user.id,
                                   '.           Здравствуйте, {0.first_name}!         .'.format(message.from_user),
                                   reply_markup=inline_menu["submenu"])


async def process_callback(callback_query: CallbackQuery):
    code = callback_query.data
    print("Callback =", code)
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
