from aiogram import Bot, Dispatcher, executor, types
import logging
import os

API_TOKEN = os.getenv("BOT_TOKEN")  # توكن البوت من المتغيرات البيئية

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("أهلًا بك! هذا البوت يعمل ✅")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
