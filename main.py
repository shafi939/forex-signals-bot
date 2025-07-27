import logging
import asyncio
from aiogram import Bot, Dispatcher, types

# توكن بوت تيليجرام
TOKEN = "7550278246:AAH6UUiBxRRomE1QTKiC7xgmCVjPceQOMns"

# إنشاء البوت والموزع
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# أمر /start و /help
@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.reply("مرحباً بك في بوت توصيات الفوركس والذهب 💰\nتابعنا يوميًا لأقوى التحليلات!")

# أي رسالة عادية
@dp.message_handler()
async def handle_message(message: types.Message):
    await message.reply("🔔 قريبًا سيتم إرسال التوصيات بشكل تلقائي هنا!")

# تشغيل البوت
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
