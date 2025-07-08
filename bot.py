import telebot
from telebot import types

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    web_app = types.WebAppInfo(url='https://angelic-gratitude-production.up.railway.app')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="📲 Открыть каталог", web_app=web_app))

    bot.send_message(
        message.chat.id,
        "Добро пожаловать в <b>EKRAN.TJ-KBS</b>!\n\n📱 Вы можете выбрать модели и оформить заказ через WebApp-каталог.",
        reply_markup=keyboard
    )

@bot.message_handler(content_types=['web_app_data'])
def handle_webapp(message):
    data = message.web_app_data.data

    # Добавляем иконки банков в сообщение
    html_message = data.replace(
        "🏦",
        "🏦 <img src='https://telegra.ph/file/39f3e25047099ad71f378.png' width='20'/> Alif Bank или <img src='https://telegra.ph/file/7e611e15399039c9179d0.png' width='20'/> Dushanbe-City"
    )

    bot.send_message(message.chat.id, html_message)

bot.polling()
