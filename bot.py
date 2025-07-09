import telebot
from flask import Flask, request
import requests

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
WEBHOOK_URL = 'https://ekran-tj-bot.up.railway.app/'  # Укажи свой актуальный Railway URL

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')
app = Flask(name)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    admin_button = telebot.types.KeyboardButton("🛠 Админ-панель")
    markup.add(admin_button)

    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в <b>EKRAN.TJ</b>\n\n"
        "Нажмите кнопку ниже, чтобы открыть <b>админ-панель</b>:",
        reply_markup=markup
    )

# Обработка WebApp
@bot.message_handler(content_types=['web_app_data'])
def handle_webapp_data(message):
    data = message.web_app_data.data
    bot.send_message(message.chat.id, f"🧾 Получены данные: {data}")

# Обработка Webhook запросов
@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_str = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return '', 200
    else:
        return '', 403

# Установка Webhook при запуске
if name == 'main':
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    app.run(host='0.0.0.0', port=8080)
