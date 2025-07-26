import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

API_TOKEN = '7550278246:AAH6UUiBxRRomE1QTKiC7xgmCVjPceQOMns'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("مرحبًا! اكتب 'صفقة' للحصول على توصية قوية.")

@dp.message_handler(lambda message: message.text.lower() == 'صفقة')
async def send_signal(message: types.Message):
    recommendation = """
📊 توصية اليوم:

✅ العملة: بيتكوين
🔼 صفقة: شراء
🎯 الهدف: 61200
🛑 وقف الخسارة: 58900

⚠️ الفريم: 15 دقيقة
📉 التحليل: كسر كاذب + سيولة + شمعة ابتلاع صاعدة

بالتوفيق 🌟
"""
    await message.reply(recommendation, parse_mode=ParseMode.MARKDOWN)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
