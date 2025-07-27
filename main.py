import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# ✅ هذا هو التوكن الخاص بك
API_TOKEN = '7550278246:AAH6UUiBxRRomE1QTKiC7xgmCVjPceQOMns'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("أهلاً بك في بوت توصيات العملات 🔥\nاكتب /توصية للحصول على أقوى صفقة الآن.")

@dp.message_handler(commands=['توصية'])
async def send_signal(message: types.Message):
    توصية = "📊 صفقة اليوم:\n\nالعملة: الذهب\nالدخول: 2320\nالهدف: 2332\nالستوب: 2312"
    await message.reply(توصية)

if __name__ == '__main__':
    asyncio.run(dp.start_polling())
