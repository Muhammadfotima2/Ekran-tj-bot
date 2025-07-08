import telebot
from telebot import types

# 🔐 Твой токен
TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

# 🌐 WebApp-ссылка
WEBAPP_URL = 'https://angelic-gratitude-production.up.railway.app/'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    web_app_btn = types.WebAppInfo(url=WEBAPP_URL)
    markup.add(types.KeyboardButton("📦 Каталог", web_app=web_app_btn))
    
    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в <b>EKRAN.TJ-KBS</b>!\n\n"
        "Оформите заказ через каталог WebApp и получите итоговую сумму прямо здесь.",
        reply_markup=markup
    )

@bot.message_handler(content_types=['web_app_data'])
def handle_webapp_data(message):
    data = message.web_app_data.data

    html_message = data.replace(
        "🏦",
        "🏦 <b><img src='https://telegra.ph/file/39f3e25047099ad71f378.png' width='20'/> Alif Bank</b> или <b><img src='https://telegra.ph/file/7e611e15399039c9179d0.png' width='20'/> Dushanbe-City</b>"
    )

    bot.send_message(message.chat.id, html_message)

# 🔁 Бесконечный опрос
bot.infinity_polling()
