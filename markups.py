from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ollMenu = ['База кроссов FAPI', 'Каталог  по маркам', 'База фото автозапчастей', 'Штрих-коды автозапчастей',
           'База артикулов автозапчастей', '1С: Автобизнес', 'API интеграция', 'База кроссов онлайн',
           'База автовладельцев ВКонтакте', 'Фото логотипов автомобилей', 'Главное меню', 'Продукты',
           'Скачать бесплатно', 'Ссылки для скачивания', 'Email', 'Контакты']


def menu_id(list_buttons):
    return ReplyKeyboardMarkup(resize_keyboard=True).add(*list_buttons)


