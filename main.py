import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# ====== التوكن مباشر (غيّره بتوكنك الحقيقي) ======
API_TOKEN = '7550278246:AAH6UUiBxRRomE1QTKiC7xgmCVjPceQOMns'

# ====== إعدادات اللوق ======
logging.basicConfig(level=logging.INFO)

# ====== تعريف البوت والديسباتشر ======
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# ====== رسالة ترحيب ======
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("أهلًا في بوت التوصيات 🔥\nاكتب اسم العملة (ذهب، بيتكوين، يورو، باوند) لتحصل على التوصية.")

# ====== التوصيات للعملات ======
@dp.message_handler()
async def handle_currency(message: types.Message):
    text = message.text.lower()
    if "ذهب" in text or "gold" in text:
        await message.reply("📈 توصية الذهب:\nشراء من 2320\nالهدف: 2340\nالستوب: 2300")
    elif "بيتكوين" in text or "bitcoin" in text:
        await message.reply("📈 توصية البيتكوين:\nشراء من 58200\nالهدف: 59500\nالستوب: 57000")
    elif "يورو" in text or "eur" in text:
        await message.reply("📈 توصية اليورو:\nشراء من 1.0850\nالهدف: 1.0900\nالستوب: 1.0800")
    elif "باوند" in text or "gbp" in text:
        await message.reply("📈 توصية الباوند:\nشراء من 1.2900\nالهدف: 1.2970\nالستوب: 1.2840")
    else:
        await message.reply("❌ العملة غير معروفة. اكتب: ذهب، بيتكوين، يورو، أو باوند")

# ====== تشغيل البوت ======
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
