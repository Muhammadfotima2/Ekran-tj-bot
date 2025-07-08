import telebot
from telebot import types

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
WEBAPP_URL = 'https://ekran-tj-admin.up.railway.app'  # Адрес WebApp

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    catalog_button = types.KeyboardButton("📦 Каталог", web_app=types.WebAppInfo(url=WEBAPP_URL))
    markup.add(catalog_button)

    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в <b>EKRAN.TJ</b>\n\n"
        "Нажмите кнопку ниже, чтобы открыть админ-панель:",
        reply_markup=markup
    )

bot.polling()
