import telebot
from telebot import types

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
WEBAPP_BASE_URL = 'https://ekran-tj-admin-production.up.railway.app'

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    admin_btn = types.KeyboardButton("🛠 Админ-панель", web_app=types.WebAppInfo(url=WEBAPP_BASE_URL + '/admin.html'))
    catalog_btn = types.KeyboardButton("📦 Каталог товаров", web_app=types.WebAppInfo(url=WEBAPP_BASE_URL + '/catalog.html'))

    markup.add(admin_btn, catalog_btn)

    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в <b>EKRAN.TJ</b>\n\n"
        "Выберите раздел ниже:",
        reply_markup=markup
    )

@bot.message_handler(content_types=['web_app_data'])
def handle_webapp_data(message):
    data = message.web_app_data.data
    bot.send_message(message.chat.id, f"📩 Получены данные: {data}")

bot.infinity_polling()
