from aiogram import Bot, Dispatcher, types, executor
from aiogram.utils.markdown import link
import aiogram.utils.markdown as fmt

import keys
import keyboard
from parser import Parser

bot = Bot(keys.API)
disp = Dispatcher(bot)
Parser = Parser()


@disp.message_handler(commands=['start'])
async def process_command_start(message: types.message):
    await bot.send_message(message.from_user.id, keyboard.startText, reply_markup=keyboard.main_keyboard)


@disp.callback_query_handler(text=['il1'])
async def get_news(call: types.CallbackQuery):
    Parser.count_n = 0
    article = Parser.get_news()
    await bot.send_message(call.message.chat.id,
                           fmt.text(fmt.hbold(article['title']), fmt.text(article['text']),
                                    fmt.hide_link(article['link'])),
                           parse_mode='HTML',
                           reply_markup=keyboard.moveBack_keyboard
                           )


@disp.callback_query_handler(text=['il2'])
async def get_link(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, link('Сайт ДВФУ', 'https://www.dvfu.ru/'))


@disp.callback_query_handler(text=['il3'])
async def get_news(call: types.CallbackQuery):
    article = Parser.get_news('next')
    await bot.send_message(call.message.chat.id,
                           fmt.text(fmt.hbold(article['title']), fmt.text(article['text']),
                                    fmt.hide_link(article['link'])),
                           parse_mode='HTML',
                           reply_markup=keyboard.move_keyboard
                           )


@disp.callback_query_handler(text=['il4'])
async def get_news(call: types.CallbackQuery):
    article = Parser.get_news('prev')
    await bot.send_message(call.message.chat.id,
                           fmt.text(fmt.hbold(article['title']), fmt.text(article['text']),
                                    fmt.hide_link(article['link'])),
                           parse_mode='HTML',
                           reply_markup=keyboard.move_keyboard
                           )

@disp.callback_query_handler(text=['il5'])
async def get_news(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id,
                           text=keyboard.descryptionText,
                           reply_markup=keyboard.main_keyboard
                           )

if __name__ == '__main__':
    executor.start_polling(disp)
