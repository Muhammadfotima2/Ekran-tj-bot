import telebot
from telebot import types

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

WEBAPP_URL = 'https://angelic-gratitude-production.up.railway.app'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    web_app = types.WebAppInfo(url=WEBAPP_URL)
    keyboard.add(types.KeyboardButton("📦 Каталог", web_app=web_app))

    bot.send_message(
        message.chat.id,
        "📦 Добро пожаловать в <b>EKRAN.TJ-KBS</b>!\n"
        "Лутфан, тугмаи <b>«Оғоз кардан»</b>-ро пахш намоед, то каталоги мо кушода шавад.",
        reply_markup=keyboard
    )

@bot.message_handler(content_types=['web_app_data'])
def handle_webapp(message):
    data = message.web_app_data.data

    html_message = data.replace(
        "🏦",
        "🏦 <img src='https://telegra.ph/file/39f3e25047099ad71f378.png' width='20'/> Alif Bank "
        "ё <img src='https://telegra.ph/file/7e611e15399039c9179d0.png' width='20'/> Dushanbe-City"
    )

    bot.send_message(message.chat.id, html_message)

bot.polling()

