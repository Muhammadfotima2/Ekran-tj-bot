import telebot
from telebot import types

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
WEBAPP_URL = 'https://ekran-webapp-production-2297.up.railway.app'
WEBAPP_ADMIN_URL = 'https://ekran-tj-admin-production-df198f.up.railway.app/admin'

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    catalog_btn = types.KeyboardButton("🛍 Каталог", web_app=types.WebAppInfo(url=WEBAPP_URL))
    admin_btn = types.KeyboardButton("🛠 Админ-панель", web_app=types.WebAppInfo(url=WEBAPP_ADMIN_URL))
    markup.add(catalog_btn, admin_btn)

    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в <b>EKRAN.TJ</b>\n\n"
        "Нажмите кнопку ниже, чтобы открыть каталог товаров или админ-панель:",
        reply_markup=markup
    )

bot.infinity_polling()
