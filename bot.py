import telebot
from telebot import types

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
WEBAPP_ADMIN_URL = 'https://worker-production-7d99.up.railway.app'  # Новый рабочий адрес

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    admin_button = types.KeyboardButton("🛠 Админ-панель", web_app=types.WebAppInfo(url=WEBAPP_ADMIN_URL))
    markup.add(admin_button)

    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в <b>EKRAN.TJ</b>\n\n"
        "Нажмите кнопку ниже, чтобы открыть <b>админ-панель</b>:",
        reply_markup=markup
    )

@bot.message_handler(content_types=['web_app_data'])
def handle_webapp_data(message):
    data = message.web_app_data.data
    bot.send_message(message.chat.id, f"Вы отправили данные из WebApp: {data}")

bot.infinity_polling()
