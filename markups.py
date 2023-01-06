from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btnMain = KeyboardButton('Главное меню')

# ---Main Menu---
buttons_Main = ['Продукты', 'Скачать бесплатно', 'Контакты']
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(*buttons_Main)

# ---Products Menu---
buttons_Products = ['База кроссов FAPI', 'Каталог  по маркам', 'База фото автозапчастей', 'Штрих-коды автозапчастей',
                    'База артикулов автозапчастей', '1С: Автобизнес', 'API интеграция', 'База кроссов онлайн',
                    'База автовладельцев ВКонтакте', 'Фото логотипов автомобилей']
productsMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(*buttons_Products, btnMain)
dict_buttons_Products = {'Продукты': 'Вы перешли в меню "Продукты"',
                         'База кроссов FAPI': 'Потом здесь будет описание базы и способ оплаты',
                         'Каталог  по маркам': 'Потом здесь будет описание базы и способ оплаты',
                         'База фото автозапчастей': 'Потом здесь будет описание базы и способ оплаты',
                         'Штрих-коды автозапчастей': 'Потом здесь будет описание базы и способ оплаты',
                         'База артикулов автозапчастей': 'Потом здесь будет описание базы и способ оплаты',
                         '1С: Автобизнес': 'Потом здесь будет описание базы и способ оплаты',
                         'API интеграция': 'Потом здесь будет описание базы и способ оплаты',
                         'База кроссов онлайн': 'Потом здесь будет описание базы и способ оплаты',
                         'База автовладельцев ВКонтакте': 'Потом здесь будет описание базы и способ оплаты',
                         'Фото логотипов автомобилей': 'Потом здесь будет описание базы и способ оплаты'}

# ---Download Menu---
buttons_Download = ['Ссылки для скачивания']
downloadMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(*buttons_Download, btnMain)
dict_buttons_Download = {'Скачать бесплатно': 'Вы перешли в меню "Скачать бесплатно"',
                         'Ссылки для скачивания': 'Потом здесь будут ссылки на скачивание'}
# ---Contacts Menu---
buttons_Contacts = ['Email']
contactsMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(*buttons_Contacts, btnMain)
dict_buttons_Contacts = {'Контакты': 'Вы перешли в меню "Контакты"',
                         'Email': 'Потом здесь будет адрес и переход на почту'}

ollMenu = buttons_Main + buttons_Contacts + buttons_Download + buttons_Products + ['Главное меню']

