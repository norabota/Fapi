from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import json

try:
    with open('data_file.json', "r", encoding="utf-8") as file:
        data = json.load(file)
except FileNotFoundError:
    print("The data file is missing")
except PermissionError:
    print("This is not allowed")
except Exception as err:
    print("Some other error occurred", str(err))


def menu_commands(msg):
    if msg == 'start':
        return create_inline_keyboard_buttons(data["menu"][0]["menuItem"]["answer"],
                                              data["menu"][0]["menuItem"]["menuItems"])


def menu_inline(msg, menu_item=data["menu"]):
    print("Ветка JSON ", menu_item)
    for item in menu_item:
        if item["menuItem"]["callback_data"] == msg:
            return create_inline_keyboard_buttons(item["menuItem"]["answer"], item["menuItem"]["menuItems"])
        else:
            menu = menu_inline(msg, item["menuItem"]["menuItems"])
            if menu is not None:
                return menu
    return None


def create_inline_keyboard_buttons(msg_answer, menu_items):
    list_buttons = []
    for item in menu_items:
        if item["menuItem"]["id"].startswith('link'):
            button = InlineKeyboardButton(text=item["menuItem"]["description"],
                                          url=item["menuItem"]["callback_data"])
            list_buttons.append(button)
        else:
            button = InlineKeyboardButton(text=item["menuItem"]["description"],
                                          callback_data=item["menuItem"]["callback_data"])
            list_buttons.append(button)
    if list_buttons:
        return {"answer": msg_answer, "submenu": InlineKeyboardMarkup(row_width=1).add(*list_buttons)}
