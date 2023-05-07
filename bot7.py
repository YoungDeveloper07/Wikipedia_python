import logging

from aiogram import Bot, Dispatcher,executor, types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from wikipedia import *
from config import BOT_TOKEN
bot_token=BOT_TOKEN
wikipedia.set_lang('uz')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=bot_token)

dp=Dispatcher(bot)
keyboard1 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
keyboard1.add( types.KeyboardButton(text='📚Bot haqida'))
@dp.message_handler(commands=['start'])
async def salom(message: types.Message):
    await message.answer('Salom.Botga xush kelibsiz. Nima haqida bilmoqchisiz?')
    
@dp.message_handler(text='📚Bot haqida')
async def send_bothaqaida(message: types.Message):
    await message.answer(
        text=f"👨🏻‍💻 Loyiha asoschisi — @young_developer_07 va @Ilyosbek_Kv\n"
           
             f"📩 Murojaatlar uchun — @young_developer_07"
    )
@dp.message_handler()
async def wiki(message: types.Message):
    try: 
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola yo'q")

if __name__== '__main__':
    executor.start_polling(dp)
