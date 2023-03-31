from aiogram.dispatcher.filters.state import StatesGroup, State


class ProductsIdState(StatesGroup):
    product_id = State()


class ProductsAmountState(StatesGroup):
    product_amount = State()