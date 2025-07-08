import telebot
from telebot import types

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Кнопка WebApp
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    webapp_button = types.KeyboardButton(
        text="📱 Открыть каталог",
        web_app=types.WebAppInfo(url="https://yourwebapp.railway.app/")  # ЗАМЕНИ на свою ссылку
    )
    markup.add(webapp_button)

    bot.send_message(
        message.chat.id,
        "Добро пожаловать в EKRAN.TJ-KBS!\n\n"
        "Нажмите кнопку ниже, чтобы открыть каталог и оформить заказ:",
        reply_markup=markup
    )

@bot.message_handler(content_types=['web_app_data'])
def handle_webapp(message):
    data = message.web_app_data.data

    html_message = data.replace(
        "🏦",
        "🏦 <img src='https://telegra.ph/file/39f3e25047099ad71f378.png' width='20'/> Alif Bank или <img src='https://telegra.ph/file/7e611e15399039c9179d0.png' width='20'/> Dushanbe-City"
    )

    bot.send_message(message.chat.id, html_message)

bot.polling()
