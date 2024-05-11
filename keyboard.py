from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


startText = 'Привет, я бот, который показывает новости с сайта Дальневосточного Федерального Университета.' \
            ' Ссылку на сайт можно получить, нажав на соответствующую кнопку'

news_button = InlineKeyboardButton('Узнать последнюю новость', callback_data='il1')
link_button = InlineKeyboardButton('Сайт портала ДВФУ', callback_data='il2', url='https://www.dvfu.ru/')

next_button = InlineKeyboardButton('Следующая новость', callback_data='il3')
prev_button = InlineKeyboardButton('Предыдущая новость', callback_data='il4')

main_keyboard = InlineKeyboardMarkup()
move_keyboard = InlineKeyboardMarkup()
moveBack_keyboard = InlineKeyboardMarkup()

main_keyboard.row(link_button, news_button)
move_keyboard.row(prev_button, next_button)
moveBack_keyboard.add(prev_button)
