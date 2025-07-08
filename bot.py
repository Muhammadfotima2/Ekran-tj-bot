import telebot
from telebot import types

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

WEBAPP_URL = 'https://angelic-gratitude-production.up.railway.app'  # <-- твой WebApp

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    webapp_btn = types.KeyboardButton(text="🟢 Оғоз кардан", web_app=types.WebAppInfo(url=WEBAPP_URL))
    markup.add(webapp_btn)

    bot.send_message(
        message.chat.id,
        "📦 <b>Хуш омадед ба EKRAN.TJ-KBS!</b>
"
        "📱 Мо экранҳо барои iPhone, Samsung, Xiaomi ва дигар моделҳо дорем.

"
        "👇 Барои дидани каталог, тугмаи «Оғоз кардан»-ро пахш намоед.",
        reply_markup=markup
    )

@bot.message_handler(content_types=['web_app_data'])
def handle_webapp_data(message):
    data = message.web_app_data.data

    # Иконки барои бонкҳо
    html_message = data.replace(
        "🏦",
        "🏦 <img src='https://telegra.ph/file/39f3e25047099ad71f378.png' width='20'/> Alif Bank ё <img src='https://telegra.ph/file/7e611e15399039c9179d0.png' width='20'/> Dushanbe-City"
    )

    bot.send_message(message.chat.id, html_message)

bot.polling()
