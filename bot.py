import telebot
from telebot import types

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
WEBAPP_URL = 'https://ekran-webapp-production-2297.up.railway.app'

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    webapp_btn = types.KeyboardButton("🛍 Каталог", web_app=types.WebAppInfo(url=WEBAPP_URL))
    markup.add(webapp_btn)

    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в <b>EKRAN.TJ</b>\n\nНажмите кнопку ниже, чтобы открыть каталог товаров:",
        reply_markup=markup
    )

bot.infinity_polling()
