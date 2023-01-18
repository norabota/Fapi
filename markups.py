from aiogram.types import ReplyKeyboardMarkup
import json

with open('data_file.json', "r", encoding="utf-8") as file:
    data = json.load(file)

allMenu = ['База кроссов FAPI', 'Каталог  по маркам', 'База фото автозапчастей', 'Штрих-коды автозапчастей',
           'База артикулов автозапчастей', '1С: Автобизнес', 'API интеграция', 'База кроссов онлайн',
           'База автовладельцев ВКонтакте', 'Фото логотипов автомобилей', 'Главное меню', 'Продукты',
           'Скачать бесплатно', 'Ссылки для скачивания', 'Email', 'Контакты']


def menu_commands(msg):
    list_buttons = []
    if msg == 'start':
        items_main_menu = data["menu"][0]["menuItem"]["menuItems"]
        msg_answer = data["menu"][0]["menuItem"]["answer"]
        for i in items_main_menu:
            list_buttons.append(i["menuItem"]["description"])
        return [msg_answer, ReplyKeyboardMarkup(resize_keyboard=True).add(*list_buttons)]


def menu_id(msg, submenu_with_msg=data["menu"]):
    list_buttons = []
    print(1, submenu_with_msg)
    for i in submenu_with_msg:
        if i["menuItem"]["description"] == msg:
            print(2, i)
            print(3, i["menuItem"].get("menuItems"))
            msg_answer = i["menuItem"]["answer"]
            for key in i["menuItem"]["menuItems"]:
                list_buttons.append(key["menuItem"]["description"])
            return [msg_answer, ReplyKeyboardMarkup(resize_keyboard=True).add(*list_buttons)]
        # elif i["menuItem"]["description"] == msg and i["menuItem"]["menuItems"] is type(None):
        #     return ["Раздел меню сейчас в разработке-выберите другой пункт меню;))", None]
        # elif i["menuItem"]["description"] != msg and i["menuItem"]["menuItems"] is type(None):
        #     continue
        else:
            return menu_id(msg, i["menuItem"]["menuItems"])
