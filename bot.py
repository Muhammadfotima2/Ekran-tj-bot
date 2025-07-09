import telebot
from telebot import types

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
WEBAPP_CATALOG_URL = 'https://ekran-webapp-production-2297.up.railway.app'

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    catalog_button = types.KeyboardButton("📦 Каталог товаров", web_app=types.WebAppInfo(url=WEBAPP_CATALOG_URL))
    admin_button = types.KeyboardButton("🛠 Админ-панель")
    
    markup.add(catalog_button, admin_button)

    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в <b>EKRAN.TJ</b>\n\n"
        "Выберите нужную опцию ниже:",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == "📦 Каталог товаров")
def open_catalog(message):
    bot.send_message(message.chat.id, "Открываем каталог...")

@bot.message_handler(func=lambda message: message.text == "🛠 Админ-панель")
def admin_panel(message):
    bot.send_message(message.chat.id, "🔐 Админ-панель пока не подключена. (Следующий шаг)")

bot.infinity_polling()
