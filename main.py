import logging
import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, types, executor

# 🔑 توكن البوت الخاص بك
API_TOKEN = '7550278246:AAH6UUiBxRRomE1QTKiC7xgmCVjPceQOMns'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# العملات المطلوبة مع رموز التوحّد
symbols = {
    "ذهب": "XAU",
    "بيتكوين": "BTC",
    "يورو": "EUR",
    "باوند": "GBP"
}

# دالة سؤال أسعار لايف من exchangerate.host
async def get_live_price(symbol: str) -> float | None:
    url = f"https://api.exchangerate.host/latest?base={symbol}&symbols=USD"
    try:
        async with aiohttp.ClientSession() as session:
            r = await session.get(url)
            data = await r.json()
            return data['rates']['USD']
    except:
        return None

# توليد توصية بسيطة
def generate_signal(price: float) -> str:
    tp = round(price * 1.01, 4)
    sl = round(price * 0.995, 4)
    action = "شراء" if price < tp else "بيع"
    return f"السعر: {price}\nنوع الصفقة: {action}\nالهدف: {tp}\nالستوب: {sl}"

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("أهلاً بك! أرسل اسم عملة (ذهب، بيتكوين، يورو، باوند) لتحصل على توصية لايف.")

@dp.message_handler(lambda m: m.text in symbols)
async def cmd_signal(message: types.Message):
    sym = message.text
    code = symbols[sym]
    price = await get_live_price(code)
    if price is None:
        return await message.reply("❌ تعذر جلب السعر.")
    signal = generate_signal(price)
    await message.reply(f"📊 توصية {sym}:\n{signal}")

async def on_startup(_):
    pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
