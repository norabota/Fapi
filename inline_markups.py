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

def menu_id_links(msg, submenu_with_msg=data["menu"]):
    list_buttons = []
    print(1, submenu_with_msg)
    for i in submenu_with_msg:
        # if i["menuItem"]["menuItems"] == []:
        #     print("TEST")
        #     continue
        if i["menuItem"]["description"] == msg:
            print(2, i)
            print(3, i["menuItem"].get("menuItems"))
            msg_answer = i["menuItem"]["answer"]
            if "links" in i["menuItem"]:
                list_buttons = [InlineKeyboardButton(text=key, url=values) for key,values in i["menuItem"]["links"].items()]
            return {"answer": msg_answer, "submenu": InlineKeyboardMarkup(row_width=2).add(*list_buttons)}
        else:
            answer_submenu = menu_id_links(msg, i["menuItem"]["menuItems"])
            if answer_submenu != False:
                return answer_submenu
    return False






# кнопки из списка
l = ['Яблоко', 'Груша']
keyboard = InlineKeyboardMarkup(row_width=1)
backbutton = InlineKeyboardButton(text="Back", callback_data="MainMenu")
button_list = [InlineKeyboardButton(text=x, callback_data=x) for x in l]
keyboard.add(*button_list, backbutton)

