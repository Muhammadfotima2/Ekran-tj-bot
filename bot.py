import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📦 Каталог", callback_data='catalog'))
    bot.send_message(message.chat.id, "Добро пожаловать в EKRAN.TJ-KBS!\n\nНажмите кнопку ниже, чтобы открыть каталог и оформить заказ:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == 'catalog':
        bot.send_message(call.message.chat.id, "🛒 Каталог:\n\n📱 iPhone XR\nКачество: Incell\nЦена: 240 сомонӣ\n\n📱 Samsung A13\nКачество: Original\nЦена: 100 сомонӣ")

bot.polling()
