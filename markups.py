from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Главное меню')

# ---Main Menu---
btn1 = KeyboardButton('Продукты')
btn2 = KeyboardButton('Скачать бесплатно')
btn3 = KeyboardButton('Контакты')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1, btn2, btn3)

# ---Products Menu---
btn11 = KeyboardButton('База кроссов FAPI')
btn12 = KeyboardButton('Каталог  по маркам')
btn13 = KeyboardButton('База фото автозапчастей')
btn14 = KeyboardButton('Штрих-коды автозапчастей')
btn15 = KeyboardButton('База артикулов автозапчастей')
btn16 = KeyboardButton('1С: Автобизнес')
btn17 = KeyboardButton('API интеграция')
btn18 = KeyboardButton('База кроссов онлайн')
btn19 = KeyboardButton('База автовладельцев ВКонтакте')
btn110 = KeyboardButton('Фото логотипов автомобилей')
productsMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18,
                                                             btn19, btn110, btnMain)

# ---Download Menu---
btn21 = KeyboardButton('Ссылки для скачивания')
downloadMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn21, btnMain)

# ---Contacts Menu---
btn31 = KeyboardButton('Email')
contactsMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn31, btnMain)
