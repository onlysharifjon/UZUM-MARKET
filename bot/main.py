import logging
from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards.default import keyboard
from keyboards.inline import Katalog1, Katalog2
from states import CallbackStates
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
# ------------------------DATABASE--------------------
from aiogram.dispatcher import FSMContext
import sqlite3
from aiogram.types import InputMedia

connect = sqlite3.connect(
    'C:/Users/Sharifjon/PycharmProjects/UZUM-MARKET/db.sqlite3', check_same_thread=False)
cursor = connect.cursor()

# ------------------------DATABASE--------------------
API_TOKEN = '5118382129:AAGNQiGeZEKB6tSy846WrWOh7v1ftBCtSZ4'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands="start")
async def startt(message: types.Message):
    await message.answer("Assalomu aleykum uzum marketga xush kelibiz! ", reply_markup=keyboard)


@dp.message_handler(text='Katalog')
async def katalog(message: types.Message):
    await message.answer('Kataloglardan Birini tanlang', reply_markup=ReplyKeyboardRemove())
    await message.answer('KATALOG', reply_markup=Katalog1)
    await CallbackStates.chala.set()


@dp.callback_query_handler(text='edit_orqa', state=CallbackStates.chala)
async def orqaga_inline(call: types.CallbackQuery):
    try:
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=Katalog1)
    except:
        await call.answer('Boshqa menyu mavjud emas')


@dp.callback_query_handler(text='edit_oldin', state=CallbackStates.chala)
async def oldinga_inline(call: types.CallbackQuery):
    try:
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=Katalog2)
    except:
        await call.answer('Boshqa menyu mavjud emas')


@dp.callback_query_handler(state=CallbackStates.chala)
async def kiyimlar_handler(call: types.CallbackQuery):
    print('Chala ishladi')
    try:
        categorylar = cursor.execute(f'SELECT category FROM ProductAPP_katalogmodel WHERE katalog=?',
                                     (call.data,)).fetchall()
        a = []
        if categorylar == a:
            await call.answer('Boshqa menyu mavjud emas')
        else:
            kiyimlar = InlineKeyboardMarkup()
            for i in categorylar:
                kiyimlar.add(InlineKeyboardButton(
                    text="🛍" + i[0], callback_data=i[0]))
            kiyimlar.add(InlineKeyboardButton(
                text='<<', callback_data="orqaga"))
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                reply_markup=kiyimlar)
            await CallbackStates.katalog.set()
    except:
        await call.answer('Boshqa menyu mavjud emas')


@dp.callback_query_handler(text='orqaga_katalog')
async def orqaga_kala(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('KATALOG', reply_markup=Katalog1)


@dp.callback_query_handler(text='orqaga', state=CallbackStates.katalog)
async def mainer(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('KATALOG', reply_markup=Katalog1)
    await CallbackStates.chala.set()


@dp.callback_query_handler(state=CallbackStates.katalog)
async def catalog_oladi(call: types.CallbackQuery):
    print('Katalog ishladi')
    filters = cursor.execute(
        "SELECT id FROM ProductAPP_katalogmodel WHERE category = ?", (call.data,)).fetchall()
    category_id = filters[0][0]
    filter_sub_category = cursor.execute('SELECT sub_category FROM ProductAPP_categorymodel WHERE category_id = ?',
                                         (category_id,)).fetchall()
    buttons_list = []
    a = []
    print(filters)
    if filter_sub_category == a:
        print('Ishladi')
        await call.answer('Mahsulot Topilmadi')
    else:
        print('Else')
        button = InlineKeyboardMarkup()
        for i in filter_sub_category:
            buttons_list.append(i[0])
        for d in buttons_list:
            button.add(InlineKeyboardButton(text=d + "🛍", callback_data=d))
        button.add(InlineKeyboardButton(
            text='<<', callback_data="orqaga_katalog"))
        # await call.message.answer(f'{call.data}', reply_markup=button)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.data)
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=button)
        print(True)
        await CallbackStates.sub_catagory_state.set()


@dp.callback_query_handler(text='orqaga_katalog', state=CallbackStates.sub_catagory_state)
async def orqaga_katalog(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('KATALOG', reply_markup=Katalog1)
    await CallbackStates.chala.set()


@dp.callback_query_handler(state=CallbackStates.sub_catagory_state)
async def sub_category(call: types.CallbackQuery, state: FSMContext):
    id_subcategory = cursor.execute(f'SELECT id FROM ProductAPP_categorymodel WHERE sub_category = ?',
                                    (call.data,)).fetchone()
    print(id_subcategory)

    mahsulotlar = cursor.execute('SELECT name FROM ProductAPP_productmodel WHERE sub_category_id = ?',
                                 (id_subcategory[0],)).fetchall()
    print(mahsulotlar)
    a = []
    if id_subcategory == a:
        await call.answer('Bu Bo`limda Mahsulotlarimiz Mavjud emas')
    else:
        inline_keyboard_mahsulotlar = InlineKeyboardMarkup()
        for i in mahsulotlar:
            inline_keyboard_mahsulotlar.add(
                InlineKeyboardButton(text="🛍" + i[0], callback_data=i[0]))
        inline_keyboard_mahsulotlar.add(InlineKeyboardButton(
            text='<<', callback_data="orqaga_sub"))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.data)
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=inline_keyboard_mahsulotlar)
        await state.finish()
        await CallbackStates.product_state.set()


@dp.callback_query_handler(state=CallbackStates.product_state, text="orqaga_sub")
async def sub_orqaga(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('KATALOG', reply_markup=Katalog1)
    await CallbackStates.chala.set()


@dp.callback_query_handler(state=CallbackStates.product_state)
async def product_aywdfiawd(call: types.CallbackQuery):
    if call.data != 'ha':
        mahsulot_nomi = call.data
        global a
        a = cursor.execute(
            f"SELECT * FROM ProductAPP_productmodel WHERE name=?", (mahsulot_nomi,)).fetchall()
        saler_name = cursor.execute(
            f"SELECT name FROM SalerApp_salerregister WHERE id = {a[0][-2]}").fetchone()
        sub_category = cursor.execute(
            f"SELECT sub_category FROM ProductAPP_categorymodel WHERE category_id = {a[0][-1]}").fetchone()
        description = f'''
🆔Mahsulot id: {a[0][0]}
✒️Mahsulot nomi: {a[0][1]}
💸Mahsulot narxi: {a[0][5]}
🔮Mahsulot rangi: {a[0][6]}
📄Mahsulot haqida : {a[0][7]}
📌Mahsulot o`lchami : {a[0][8]}
🛒Mahsulot qoldiqi : {a[0][9]}
👱‍♂️Sotuvchi : {saler_name[0]}    
📎Mahsulot kategoriyasi: {sub_category[0]}
    '''
        media_group = [
            InputMediaPhoto(media=open(
                f'C:/Users/Sharifjon/PycharmProjects/UZUM-MARKET/{a[0][2]}', 'rb')),
            InputMediaPhoto(media=open(
                f'C:/Users/Sharifjon/PycharmProjects/UZUM-MARKET/{a[0][3]}', 'rb')),
            InputMediaPhoto(media=open(
                f'C:/Users/Sharifjon/PycharmProjects/UZUM-MARKET/{a[0][4]}', 'rb'), caption=description)
        ]
        
        
        mahsulot_n = a[0][1]
        await call.message.answer_media_group(media=media_group)
        button = InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(text='Ha', callback_data='ha'),
                InlineKeyboardButton(text='Yoq', callback_data='yoq'),
            ]
            ]
        )
        await call.message.answer("Sotib Olmoqchimisiz", reply_markup=button)

    elif call.data == 'ha':
        await call.message.answer(f'Korzinkaga {a[0][1]} qo`shildi!')

        


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
