import logging
from aiogram import types, Bot, Dispatcher, executor
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton


API_TOKEN = '6646323098:AAHcLovTWt83NWns67zaKST1yOC4IDFI18Y'
bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def message(message : types.Message):
    buttons = [[KeyboardButton("Menu", web_app = WebAppInfo(url = "https://core.telegram.org/bots/webapps"))]]
    await message.answer(message.text, reply_markup = ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True))



if __name__ == '__main__':
    executor.start_polling(dp)