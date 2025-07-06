import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '7619246310:AAHloM_NMegAtxdEaYs0ZJncAGwxb74g4so'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton("📱 Samsung A10", callback_data="samsung_a10")
    markup.add(btn)
    bot.send_message(message.chat.id, "Добро пожаловать! Пожалуйста, выберите модель:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "samsung_a10":
        bot.send_message(call.message.chat.id, "📱 *Samsung A10*\n🛠 Качество: Original\n🏷 Бренд: KBS\n💰 Цена: 90 сомонӣ", parse_mode='Markdown')

bot.polling()
