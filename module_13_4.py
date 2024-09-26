from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

class UserState (StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands='start')
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer ('Привет! Я бот помогающий твоему здоровью. Используйте команду /Calories.')

@dp.message_handler(commands = 'Calories')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age1 = message.text)
    await message.answer ('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def  set_weight(message, state):
    await state.update_data(growth2 = message.text)
    await message.answer ('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def  send_calories(message, state):
    await state.update_data(weight3 = message.text)
    data = await state.get_data()
    formula = int(10 * int(data['weight3']) + 6.25 * int(data['growth2']) - 5 * int(data['age1']) + 5)
    await message.answer (f'Ваша норма каллорий: {formula} ккал')
    await state.finish()

@dp.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer ('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)