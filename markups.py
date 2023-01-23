from aiogram.types import ReplyKeyboardMarkup
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
        for i in items_main_menu:
            list_buttons.append(i["menuItem"]["description"])
        return {"answer": msg_answer, "submenu": ReplyKeyboardMarkup(resize_keyboard=True).add(*list_buttons)}


def menu_id(msg, submenu_with_msg=data["menu"]):
    list_buttons = []
    print(1, submenu_with_msg)
    for i in submenu_with_msg:
        if i["menuItem"]["menuItems"] == []:
            continue
        elif i["menuItem"]["description"] == msg:
            msg_answer = i["menuItem"]["answer"]
            for key in i["menuItem"]["menuItems"]:
                if not key["menuItem"].get("callback_data", 0):
                    list_buttons.append(key["menuItem"]["description"])
            if list_buttons:
                return {"answer": msg_answer, "submenu": ReplyKeyboardMarkup(resize_keyboard=True).add(*list_buttons)}
        else:
            answer_submenu = menu_id(msg, i["menuItem"]["menuItems"])
            if answer_submenu != False:
                return answer_submenu
    return False
