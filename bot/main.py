import logging
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.default import keyboard
from keyboards.inline import Katalog1,Katalog2

API_TOKEN = '6029555538:AAGZVSM6OIOoomI92pIcy5Zm7tk4MtFR_Ys'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands="start")
async def startt(message: types.Message):
    await message.answer("Assalomu aleykum uzum marketga xush kelibiz! ", reply_markup=keyboard)


@dp.message_handler(text='Katalog')
async def katalog(message: types.Message):
    await message.answer('KATALOG', reply_markup=Katalog1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
