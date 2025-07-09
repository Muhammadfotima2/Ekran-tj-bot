import telebot
from telebot import types

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(TOKEN)

# URL WebApp для каталога товаров
WEBAPP_CATALOG_URL = "https://ekran-webapp-production-2297.up.railway.app"

# URL WebApp для админ-панели
WEBAPP_ADMIN_URL = "https://web-production-48d37.up.railway.app"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Кнопка для каталога
    catalog_btn = types.KeyboardButton(
        "📱 Каталог",
        web_app=types.WebAppInfo(url=WEBAPP_CATALOG_URL)
    )

    # Кнопка для админ-панели
    admin_btn = types.KeyboardButton(
        "🛠 Админ-панель",
        web_app=types.WebAppInfo(url=WEBAPP_ADMIN_URL)
    )

    # Добавляем обе кнопки в клавиатуру
    markup.add(catalog_btn, admin_btn)

    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать! Выберите действие:",
        reply_markup=markup
    )

bot.infinity_polling()
