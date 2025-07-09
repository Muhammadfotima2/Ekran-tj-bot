from flask import Flask, request
import telebot
from telebot import types

# 🔐 Твой токен и WebApp URL
TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
WEBAPP_URL = 'https://web-production-3878b.up.railway.app'

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')
app = Flask(name)

# Установка webhook
bot.remove_webhook()
bot.set_webhook(url=WEBAPP_URL)

# Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    admin_button = types.KeyboardButton("🛠 Админ-панель", web_app=types.WebAppInfo(url=WEBAPP_URL))
    markup.add(admin_button)
    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в <b>EKRAN.TJ</b>\n\n"
        "Нажмите кнопку ниже, чтобы открыть <b>админ-панель</b>:",
        reply_markup=markup
    )

# Обработка WebApp-данных
@bot.message_handler(content_types=['web_app_data'])
def handle_webapp_data(message):
    data = message.web_app_data.data
    bot.send_message(message.chat.id, f"📩 Получены данные из WebApp:\n{data}")

# Webhook с логами
@app.route('/', methods=['POST'])
def webhook():
    print("🚨 Webhook вызван")
    try:
        json_string = request.get_data().decode('utf-8')
        print("📥 Получен JSON:", json_string)
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
    except Exception as e:
        print("❌ Ошибка:", e)
    return 'ok', 200

# Flask запуск
if name == 'main':
    app.run(host='0.0.0.0', port=8080)
