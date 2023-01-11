from aiogram.types import ReplyKeyboardMarkup
import json

with open('data_file.json', "r", encoding="utf-8") as file:
    data = json.load(file)

allMenu = ['База кроссов FAPI', 'Каталог  по маркам', 'База фото автозапчастей', 'Штрих-коды автозапчастей',
           'База артикулов автозапчастей', '1С: Автобизнес', 'API интеграция', 'База кроссов онлайн',
           'База автовладельцев ВКонтакте', 'Фото логотипов автомобилей', 'Главное меню', 'Продукты',
           'Скачать бесплатно', 'Ссылки для скачивания', 'Email', 'Контакты']


# def menu_id(msg):
#     # Проверка входящего сообщения на соответствие значению ключа
#     # Перебор словаря, создание клавиатуры меню
#     list_buttons = []
#     if msg == data["menu"][0]["menuItem"]["description"] or msg == 'start':
#         items_main_menu = data["menu"][0]["menuItem"]["items"]
#         msg_answer = data["menu"][0]["menuItem"]["answer"]
#         for i in items_main_menu:
#             list_buttons.append(i["description"])
#         return [msg_answer, ReplyKeyboardMarkup(resize_keyboard=True).add(*list_buttons)]
#     else:
#         items_msg_menu = data["menu"]
#         for i in items_msg_menu:
#             if i["menuItem"]["description"] == msg:
#                 msg_answer = i["menuItem"]["answer"]
#                 for key in i["menuItem"]["items"]:
#                     list_buttons.append(key["menuItem"]["description"])
#                 return [msg_answer, ReplyKeyboardMarkup(resize_keyboard=True).add(*list_buttons)]

def memu_id_id(msg, items_msg_menu):
    list_buttons = []
    for i in items_msg_menu:
        if i["menuItem"]["description"] == msg:
            # and i["menuItem"].get("items") is not None
            print(i)
            print(i["menuItem"].get("items"))
            msg_answer = i["menuItem"]["answer"]
            for key in i["menuItem"]["items"]:
                list_buttons.append(key["menuItem"]["description"])
            return [msg_answer, ReplyKeyboardMarkup(resize_keyboard=True).add(*list_buttons)]
        else:
            for ints in range(len(items_msg_menu)):
                if items_msg_menu[ints]["menuItem"]["items"] == type(list):
                    memu_id_id(msg, items_msg_menu[ints]["menuItem"]["items"])


    # for i in items_msg_menu:
    #     if  i["menuItem"]["id"] != "mainMenu":
    #         msg_answer = i["menuItem"]["answer"]
    #         for key in i["menuItem"]["items"]:
    #             if key["menuItem"].get("items") is None:
    #                 print(9999999)
    #         # return [msg_answer, ReplyKeyboardMarkup(resize_keyboard=True).add(*list_buttons)]
    #                 return ["11111111", ReplyKeyboardMarkup(resize_keyboard=True).add("22222222")]
    # else:
    #     for key in i["menuItem"]["items"]:
    #         # print(key["menuItem"]["description"])
    #         list_buttons2.append(key["menuItem"]["items"])
    #         print( list_buttons2)
    #         if key.get("menuItem").get("items") is not None:
    #             memu_id_id(msg, items_msg_menu= items_msg_menu[key].get("menuItem").get("description"))

    # elif i["menuItem"]["items"][0]["menuItem"]["items"] != None:
    # #     for menu in range(len(i["menuItem"]["items"])):
    # #         memu_id_id(msg,items_msg_menu=i["menuItem"]["items"][menu])


def menu_id(msg):
    # Проверка входящего сообщения на соответствие значению ключа
    # Перебор словаря, создание клавиатуры меню
    list_buttons = []
    if msg == data["menu"][0]["menuItem"]["description"] or msg == 'start':
        items_main_menu = data["menu"][0]["menuItem"]["items"]
        msg_answer = data["menu"][0]["menuItem"]["answer"]
        for i in items_main_menu:
            list_buttons.append(i["menuItem"]["description"])
        return [msg_answer, ReplyKeyboardMarkup(resize_keyboard=True).add(*list_buttons)]
    else:

        return memu_id_id(msg, items_msg_menu=data["menu"])
