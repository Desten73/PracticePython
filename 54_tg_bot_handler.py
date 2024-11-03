from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram import F
from aiogram.fsm.storage import memory
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from aiogram.types import Message


api = open("bot_api.txt", "r").read()
bot = Bot(token=api, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
bot_memory = memory.MemoryStorage()
dp = Dispatcher(storage=bot_memory)
user_router = Router()


class UserState(StatesGroup):

    age = State()
    growth = State()
    weight = State()


@dp.message(CommandStart())
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")


@dp.message(F.text == "test")
async def all_massages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


@dp.message(F.text == "Calories")
async def all_massages(message, state: FSMContext):
    await state.set_state(UserState.age)
    await message.answer("Введите свой возраст:")


@dp.message(UserState.age)
async def set_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(UserState.growth)
    await message.answer("Введите свой рост:")


@dp.message(UserState.growth)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await state.set_state(UserState.weight)
    await message.answer("Введите свой вес:")


@dp.message(UserState.weight)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(f"Ваша норма калорий: {10 * int(data["weight"]) + 
                                                6.25 * int(data["growth"]) -
                                                5 * int(data["age"]) + 5}")
    await state.clear()


if __name__ == "__main__":
    dp.run_polling(bot)


