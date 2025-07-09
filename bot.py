from flask import Flask, request
import telebot
from telebot import types

# Токен бота и ссылка на WebApp
TOKEN = '7619246310:AAHloM_NMegAtxdEaYs0ZJncAGwxb74g4so'
WEBAPP_URL = 'https://web-production-3878b.up.railway.app'

# Инициализация бота и Flask
bot = telebot.TeleBot(TOKEN, parse_mode='HTML')
app = Flask(name)

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

# Обработка данных от WebApp
@bot.message_handler(content_types=['web_app_data'])
def handle_webapp_data(message):
    data = message.web_app_data.data
    bot.send_message(message.chat.id, f"📩 Получены данные из WebApp:\n{data}")

# Webhook для Telegram
@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
    return 'ok', 200

# Запуск Flask-сервера на Railway
if name == 'main':
    app.run(host='0.0.0.0', port=8080)
