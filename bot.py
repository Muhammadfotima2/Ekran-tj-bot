import telebot
from telebot import types

# Токен бота
TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'

# Адрес WebApp (каталог)
WEBAPP_URL = 'https://ekran-webapp-production-2297.up.railway.app'

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    catalog_btn = types.WebAppInfo(url=WEBAPP_URL)
    button = types.KeyboardButton("🛍 Каталог", web_app=catalog_btn)
    markup.add(button)

    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в <b>EKRAN.TJ</b>\n\n"
        "Нажмите кнопку ниже, чтобы открыть каталог товаров:",
        reply_markup=markup
    )

# Для polling
bot.infinity_polling()
