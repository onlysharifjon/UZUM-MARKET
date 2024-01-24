import logging
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.default import keyboard
from keyboards.inline import Katalog1, Katalog2, kiyimlar
import os

# ------------------------DATABASE--------------------
import sqlite3

connect = sqlite3.connect('C:/Users/momin/PycharmProjects/UZUM-MARKET/db.sqlite3', check_same_thread=False)
cursor = connect.cursor()
# ------------------------DATABASE--------------------


API_TOKEN = '6586939529:AAF8J4lGLyO0LSCmpKHnBj14OkuvwgD76jc'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands="start")
async def startt(message: types.Message):
    await message.answer("Assalomu aleykum uzum marketga xush kelibiz! ", reply_markup=keyboard)


@dp.message_handler(text='Katalog')
async def katalog(message: types.Message):
    await message.answer('KATALOG', reply_markup=Katalog1)


@dp.callback_query_handler(text='Kiyim')
async def kiyimlar_handler(call: types.CallbackQuery):
    try:
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=kiyimlar)
    except:
        await call.answer('Boshqa menyu mavjud emas')


@dp.callback_query_handler(text='oldinga')
async def oldinga_inline(call: types.CallbackQuery):
    try:
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=Katalog2)
    except:
        await call.answer('Boshqa menyu mavjud emas')


@dp.callback_query_handler(text='orqaga')
async def orqaga_inline(call: types.CallbackQuery):
    try:
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=Katalog1)
    except:
        await call.answer('Boshqa menyu mavjud emas')


from channels.db import database_sync_to_async

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@dp.callback_query_handler(text='orqaga_katalog')
async def orqaga_kala(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('KATALOG', reply_markup=Katalog1)


@dp.callback_query_handler()
async def catalog_oladi(call: types.CallbackQuery):
    await call.message.delete()
    filters = cursor.execute("SELECT category FROM ProductAPP_katalogmodel WHERE katalog = ?", (call.data,)).fetchall()
    buttons_list = []
    button = InlineKeyboardMarkup()
    for i in filters:
        buttons_list.append(i[0])
    for d in buttons_list:
        button.add(InlineKeyboardButton(text=d, callback_data=d))
    button.add(InlineKeyboardButton(text='<<', callback_data="orqaga_katalog"))
    await call.message.answer(f'{call.data}', reply_markup=button)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
