from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram import F
from aiogram.fsm.storage import memory

api = open("bot_api.txt", "r").read()
bot = Bot(token=api, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
bot_memory = memory.MemoryStorage()
dp = Dispatcher(storage=bot_memory)


@dp.message(CommandStart())
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")


@dp.message(F.text)
async def all_massages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == "__main__":
    dp.run_polling(bot)


