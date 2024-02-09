from aiogram.dispatcher.filters.state import State, StatesGroup


class CallbackStates(StatesGroup):
    chala = State()
    katalog = State()
    sub_catagory_state = State()
    product_state = State()
