import telebot
from telebot import types

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardRemove()
    bot.send_message(
        message.chat.id,
        "Добро пожаловать в EKRAN.TJ-KBS!\n\n"
        "Оформите заказ через WebApp и вы получите расчёт.",
        reply_markup=markup
    )

@bot.message_handler(content_types=['web_app_data'])
def handle_webapp(message):
    data = message.web_app_data.data

    # Добавляем иконки в сообщение
    html_message = data.replace(
        "🏦",
        "🏦 <img src='https://telegra.ph/file/39f3e25047099ad71f378.png' width='20'/> Alif Bank или <img src='https://telegra.ph/file/7e611e15399039c9179d0.png' width='20'/> Dushanbe-City"
    )

    bot.send_message(message.chat.id, html_message)

bot.polling()
