from aiogram import Bot, Dispatcher, types, executor

# توكن البوت الخاص بك من BotFather
API_TOKEN = '7550278246:AAH6UUiBxRRomE1QTKiC7xgmCVjPceQOMns'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("أهلاً بك في بوت توصيات الفوركس 💰")

@dp.message_handler(commands=['تحليل_الذهب'])
async def gold_analysis(message: types.Message):
    await message.reply("📈 الذهب حالياً عند دعم قوي، الشراء جيد من 2310 مع هدف 2330.")

if __name__ == '__main__':
    executor.start_polling(dp)
