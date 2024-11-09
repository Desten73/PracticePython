from aiogram import Bot, Dispatcher
from aiogram import F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.storage import memory
from aiogram.fsm.context import FSMContext
from aiogram.types import (Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile)
import crud_functions

crud_functions.initiate_db()
api = open("bot_api.txt", "r").read()
bot = Bot(token=api, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
bot_memory = memory.MemoryStorage()
dp = Dispatcher(storage=bot_memory)

keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Рассчитать"), KeyboardButton(text="Информация")],
    [KeyboardButton(text="Купить")]
], resize_keyboard=True, input_field_placeholder="Выберите один из пунктов меню")

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")],
    [InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")]
])

inline_keyboard_products = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Product1", callback_data="product_buying"),
     InlineKeyboardButton(text="Product2", callback_data="product_buying"),
     InlineKeyboardButton(text="Product3", callback_data="product_buying"),
     InlineKeyboardButton(text="Product4", callback_data="product_buying")],
])


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(CommandStart())
async def start(message: Message):
    print(message)
    print(message.text)
    await message.reply("Привет, я бот помогающий твоему здоровью!",
                        reply_markup=keyboard)


@dp.message(F.text == "Рассчитать")
async def main_menu(message: Message):
    await message.answer("Выберите опцию:", reply_markup=inline_keyboard)


@dp.callback_query(F.data == "formulas")
async def get_formulas(call: CallbackQuery):
    await call.message.edit_text("Используется упрощенный вариант формулы Миффлина-Сан Жеора:\n"
                                 "10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")


@dp.message(F.text == "Купить")
async def get_buying_list(message: Message):
    products = crud_functions.get_all_products()
    for product in products:
        await message.answer_photo(FSInputFile(product[3]), f"Название: {product[1]} | "
                                                            f"Описание: {product[2]} | Цена: {product[4]}")
    await message.answer("Выберите продукт для покупки: ", reply_markup=inline_keyboard_products)


@dp.callback_query(F.data == "product_buying")
async def send_confirm_message(call: CallbackQuery):
    await call.answer("")
    await call.message.answer("Вы успешно приобрели продукт!")


@dp.callback_query(F.data == "calories")
async def start_calories(call: CallbackQuery, state: FSMContext):
    print(call)
    print(call.message.text)
    await state.set_state(UserState.age)
    await call.message.edit_text("Введите свой возраст:")


@dp.message(UserState.age)
async def set_age(message: Message, state: FSMContext):
    print(message)
    print(message.text)
    try:
        int(message.text)
        await state.update_data(age=message.text)
        await state.set_state(UserState.growth)
        await message.answer("Введите свой рост:")
    except:
        await message.reply("Необходимо вводить целочисленное число!")


@dp.message(UserState.growth)
async def set_growth(message: Message, state: FSMContext):
    print(message)
    print(message.text)
    try:
        int(message.text)
        await state.update_data(growth=message.text)
        await state.set_state(UserState.weight)
        await message.answer("Введите свой вес:")
    except:
        await message.reply("Необходимо вводить целочисленное число!")


@dp.message(UserState.weight)
async def set_weight(message: Message, state: FSMContext):
    print(message)
    print(message.text)
    try:
        int(message.text)
        await state.update_data(weight=message.text)
        data = await state.get_data()
        await message.answer(f"Ваша норма калорий: {10 * int(data["weight"]) +
                                                    6.25 * int(data["growth"]) -
                                                    5 * int(data["age"]) + 5}")
        await state.clear()
    except:
        await message.reply("Необходимо вводить целочисленное число!")


@dp.message(F.text)
async def all_massages(message: Message):
    print(message)
    print(message.text)
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    dp.run_polling(bot)
