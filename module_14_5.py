from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import *

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

keyb = ReplyKeyboardMarkup()
keyb_2 = InlineKeyboardMarkup()
butt = KeyboardButton(text='Расчитать')
butt_2 = KeyboardButton(text='Информация')
butt_5 = KeyboardButton(text='Купить')
butt_6 = KeyboardButton(text='Регистрация')
butt_3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
butt_4 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
keyb_2.add(butt_3)
keyb_2.add(butt_4)
keyb.add(butt)
keyb.add(butt_2)
keyb.add(butt_5)
keyb.add(butt_5)
start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Расчитать'), KeyboardButton(text='Купить')],
        [KeyboardButton(text='Информация'), KeyboardButton(text='Регистрация')]
    ], resize_keyboard=True
)

inline_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Я - Худею", callback_data="product_buying")],
        [InlineKeyboardButton(text="Минус Жир", callback_data="product_buying")],
        [InlineKeyboardButton(text="Тонус Лайт", callback_data="product_buying")],
        [InlineKeyboardButton(text="FitnessPlus", callback_data="product_buying")]
    ], resize_keyboard=True
)

initiate_db()

def add_product(product_id, title, description, price):
    connection = sqlite3.connect('initiate.bd')
    c = connection.cursor()
    c.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
              (product_id, title, description, price))
    connection.commit()
    connection.close()

products = [
    (1, 'Я - Худею', 'Худеем за 70 дней', 1000),
    (2, 'Минус Жир', 'Худеем за 50 дней', 2000),
    (3, 'Тонус Лайт', 'Худеем за 30 дней', 5000),
    (4, 'FitnessPlus', 'Худеем за 10 дней', 50000)

]
for product in products:
    add_product(*product)

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000

@dp.message_handler(text="Регистрация")
async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if is_included(message.text):
        await message.answer("Пользователь существует, введите другое имя")
        await RegistrationState.username.set()
    else:
        await state.update_data(usnam=message.text)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(em=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(ag=message.text)
    data = await state.get_data()
    add_user(data['usnam'], data['em'], data['ag'])
    await state.finish()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products()
    image = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']
    captions = []
    for product in products:
        captions.append(f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}')
    for i in range(len(image)):
        with open(image[i], 'rb') as img:
            await message.answer_photo(img, caption=captions[i], parse_mode='Markdown')
    await message.answer('Выберите продукт для покупки:', reply_markup=inline_menu)
    # get_all_products(f"Название: {title} | Описание: {description} | Цена: {price}")
    # with open('files/1.jpg', 'rb') as img1:
    #     await message.answer_photo(img1, f'Название: Я - Худею | Описание: Худеем за 70 дней | Цена: 1000₽')
    # with open('files/2.jpg', 'rb') as img2:
    #     await message.answer_photo(img2, f'Название: Минус Жир | Описание: Худеем за 50 дней | Цена: 2000₽')
    # with open('files/3.jpg', 'rb') as img3:
    #     await message.answer_photo(img3, f'Название: Тонус Лайт | Описание: Худеем за 30 дней | Цена: 5000₽')
    # with open('files/4.jpg', 'rb') as img4:
    #     await message.answer_photo(img4, f'Название: FitnessPlus | Описание: Худеем за 10 дней | Цена: 50000₽')
    # await message.answer('Выберите продукт:', reply_markup=inline_menu)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')


@dp.message_handler(text='Расчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=keyb_2)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()


@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=start_menu)


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age1=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth2=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight3=message.text)
    data = await state.get_data()
    formula = int(10 * int(data['weight3']) + 6.25 * int(data['growth2']) - 5 * int(data['age1']) - 161)
    await message.answer(f'Ваша норма каллорий: {formula} ккал в день')
    await state.finish()


@dp.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)