from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
from aiogram.utils import executor
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
    list_buttons = []
    if msg == 'start':
        items_main_menu = data["menu"][0]["menuItem"]["menuItems"]
        msg_answer = data["menu"][0]["menuItem"]["answer"]
        for key in items_main_menu:
            if key["menuItem"].get("callback_data", 0):
                b = InlineKeyboardButton(text=key["menuItem"]["description"],
                                         callback_data=key["menuItem"]["callback_data"])
                list_buttons.append(b)
        if list_buttons:
            return {"answer": msg_answer, "submenu": InlineKeyboardMarkup(row_width=1).add(*list_buttons)}
        # for i in items_main_menu:
        #     list_buttons.append(i["menuItem"]["description"])
        # return {"answer": msg_answer, "submenu": InlineKeyboardMarkup(row_width=1).add(*list_buttons)}


def menu_id_links(msg, submenu_with_msg=data["menu"]):
    list_buttons = []
    for i in submenu_with_msg:
        if i["menuItem"]["description"] == msg:
            msg_answer = i["menuItem"]["answer"]
            if "links" in i["menuItem"]:
                list_buttons = [InlineKeyboardButton(text=key, url=values) for key, values in
                                i["menuItem"]["links"].items()]
                return {"answer": msg_answer, "submenu": InlineKeyboardMarkup(row_width=1).add(*list_buttons)}
        else:
            answer_submenu = menu_id_links(msg, i["menuItem"]["menuItems"])
            if answer_submenu != False:
                return answer_submenu
    return False


def menu_inline(msg, submenu_with_msg=data["menu"]):
    list_buttons = []
    print(1, submenu_with_msg)
    for i in submenu_with_msg:
        if i["menuItem"]["menuItems"] == []:
            continue
        elif i["menuItem"]["callback_data"] == msg:
            print(2, i)
            print(3, i["menuItem"].get("menuItems"))
            msg_answer = i["menuItem"]["answer"]
            for key in i["menuItem"]["menuItems"]:
                if key["menuItem"].get("callback_data", 0):
                    if key["menuItem"]["id"].startswith('link'):
                        b = InlineKeyboardButton(text=key["menuItem"]["description"],
                                                 url=key["menuItem"]["callback_data"])
                        list_buttons.append(b)
                    else:
                        b = InlineKeyboardButton(text=key["menuItem"]["description"],
                                         callback_data=key["menuItem"]["callback_data"])
                        list_buttons.append(b)
            if list_buttons:
                return {"answer": msg_answer, "submenu": InlineKeyboardMarkup(row_width=1).add(*list_buttons)}
        else:
            answer_submenu = menu_inline(msg, i["menuItem"]["menuItems"])
            if not answer_submenu == False:
                return answer_submenu
    return False


# # кнопки из списка
# l = ['Яблоко', 'Груша']
# keyboard = InlineKeyboardMarkup(row_width=1)
# backbutton = InlineKeyboardButton(text="Back", callback_data="MainMenu")
# button_list = [InlineKeyboardButton(text=x, callback_data=x) for x in l]
# keyboard.add(*button_list, backbutton)
