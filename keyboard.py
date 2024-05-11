from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


startText = 'Привет, я бот, который показывает новости с сайта Дальневосточного Федерального Университета.' \
            ' Ссылку на сайт можно получить, нажав на соответствующую кнопку'

descryptionText = 'Этот бот был создан в рамках практического занятия №11 по теме «Цифровой контент и его свойства»\n \
Выполнили: \n \
Ведёхин Никита Васильевич Группа:Б9123-01.03.02-ии 2 \n \
Ча Эрнест Ирдеевич Группа:Б9123-01.03.02-ии 1 \n \
Выбранный кейс: Кейс 27: Как эффективно фильтровать информацию, получаемую через новостные ленты и социальные сети?'

news_button = InlineKeyboardButton('Узнать последнюю новость🙄', callback_data='il1')
link_button = InlineKeyboardButton('Сайт портала ДВФУ🤖', callback_data='il2', url='https://www.dvfu.ru/')
descryption_button = InlineKeyboardButton('Кто выполнил💬', callback_data='il5')

next_button = InlineKeyboardButton('Следующая новость👉', callback_data='il3')
prev_button = InlineKeyboardButton('👈Предыдущая новость', callback_data='il4')

main_keyboard = InlineKeyboardMarkup()
move_keyboard = InlineKeyboardMarkup()
moveBack_keyboard = InlineKeyboardMarkup()

main_keyboard.row(link_button, news_button)
main_keyboard.add(descryption_button)
move_keyboard.row(prev_button, next_button)
moveBack_keyboard.add(prev_button)
