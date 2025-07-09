import telebot
from telebot import types

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'

# Ссылки на WebApp
WEBAPP_CATALOG_URL = 'https://ekran-webapp-production-2297.up.railway.app'
WEBAPP_ADMIN_URL = 'https://ekran-webapp-production-2297.up.railway.app/admin.html'

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    admin_btn = types.KeyboardButton("🛠 Админ-панель", web_app=types.WebAppInfo(url=WEBAPP_ADMIN_URL))
    catalog_btn = types.KeyboardButton("📦 Каталог товаров", web_app=types.WebAppInfo(url=WEBAPP_CATALOG_URL))
    
    markup.add(admin_btn, catalog_btn)
    
    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в <b><a href='https://ekran-webapp-production-2297.up.railway.app'>EKRAN.TJ</a></b>\n\nВыберите действие:",
        reply_markup=markup
    )

@bot.message_handler(content_types=['web_app_data'])
def handle_webapp_data(message):
    data = message.web_app_data.data
    bot.send_message(message.chat.id, f"✅ Данные получены: {data}")

bot.infinity_polling()
