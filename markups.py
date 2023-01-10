from aiogram.types import ReplyKeyboardMarkup
import json

with open('data_file.json', "r", encoding="utf-8") as file:
    data = json.load(file)

allMenu = ['База кроссов FAPI', 'Каталог  по маркам', 'База фото автозапчастей', 'Штрих-коды автозапчастей',
           'База артикулов автозапчастей', '1С: Автобизнес', 'API интеграция', 'База кроссов онлайн',
           'База автовладельцев ВКонтакте', 'Фото логотипов автомобилей', 'Главное меню', 'Продукты',
           'Скачать бесплатно', 'Ссылки для скачивания', 'Email', 'Контакты']


def menu_id(msg):
    # Проверка входящего сообщения на соответствие значению ключа
    # Перебор словаря, создание клавиатуры меню
    list_buttons = []
    if msg == data["menu"][0]["menuItem"]["description"] or msg == 'start':
        items_main_menu = data["menu"][0]["menuItem"]["items"]
        msg_answer = data["menu"][0]["menuItem"]["answer"]
        for i in items_main_menu:
            list_buttons.append(i["description"])
        return [msg_answer, ReplyKeyboardMarkup(resize_keyboard=True).add(*list_buttons)]
    else:
        items_msg_menu = data["menu"]
        for i in items_msg_menu:
            if i["menuItem"]["description"] == msg:
                msg_answer = i["menuItem"]["answer"]
                for key in i["menuItem"]["items"]:
                    list_buttons.append(key["description"])
                return [msg_answer, ReplyKeyboardMarkup(resize_keyboard=True).add(*list_buttons)]
