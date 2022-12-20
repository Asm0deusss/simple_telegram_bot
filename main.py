TOKEN = '5979443692:AAH_fNju_q_YRX55-rYRIwGqgN8ygMNz-Oo'

from aiogram import Bot, types, utils
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


def fib(numb):
    left = 0
    right = 1
    for i in range(numb):
        tmp = left
        left = right
        right += tmp
    return right


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Привет!\n"
                        "Я бот\n"
                        "Вот мои команды:\n"
                        "/film – получить топ-5 фильмов\n"
                        "/song – получить топ-5 песен\n"
                        "/game – получить топ-5 игр\n"
                        "/fib n – вычислить n-ое число Фибоначчи\n"
                        "/pon – получить рандомный стикер Пона\n")


@dp.message_handler(commands=['film'])
async def get_films(message: types.Message):

    await message.reply("Вот ТОП-5 фильмов:\n"
                        "1. Зеленая миля, 1999\n"
                        "2. Список Шиндлера, 1993\n"
                        "3. Побег из Шоушенка, 1994\n"
                        "4. Форест Гамп, 1994\n"
                        "5. Властелин Колец: Возвращение короля, 2003\n")


@dp.message_handler(commands=['song'])
async def get_songs(message: types.Message):

    await message.reply("Вот ТОП-5 песен:\n"
                        "1. BOHEMIAN RHAPSODY - QUEEN\n"
                        "2. IMAGINE - JOHN LENNON\n"
                        "3. SMELLS LIKE TEEN SPIRIT - NIRVANA\n"
                        "4. LOSE YOURSELF - EMINEM\n"
                        "5. BILLIE JEAN - MICHAEL JACKSON\n")


@dp.message_handler(commands=['game'])
async def get_game(message: types.Message):

    await message.reply("Вот ТОП-5 игр:\n"
                        "1. The Witcher 3: Wild Hunt\n"
                        "2. The Elder Scrolls V: Skyrim\n"
                        "3. Grand Theft Auto 5\n"
                        "4. Minecraft\n"
                        "5. Red Dead Redemption 2\n")


@dp.message_handler(commands=['fib'])
async def get_fib(message: types.Message):

    mes = message.get_args()
    if len(mes) == 0:
        await message.answer("Ты не ввел число!\n")
        return

    arguments = mes.split(' ')

    if len(arguments) != 1:
        await message.answer("Ты ввел много аргументов!\n")
        return

    numb = int(arguments[0])
    if numb > 1000:
        await message.answer("Ты ввел большое число!\n")
        return

    await message.answer("Твое число Фибоначии: " + str(fib(numb)))


@dp.message_handler(commands=['pon'])
async def get_fib(message: types.Message):

    pons = ['грустный', 'веселый', 'агрессивный', 'злой', 'непонимающий',
            'чучуть понял', 'волшебный', 'линал', 'матан', 'чооо', 'ахахаха']

    cur_pon = random.choice(pons)

    await message.answer("Сегодня ты " + cur_pon + ' пон')

executor.start_polling(dp, skip_updates=True)
