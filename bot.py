import telebot
from telebot import types

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'

# ✅ Укажи ссылки на WebApp
WEBAPP_ADMIN_URL = "https://web-production-48d37.up.railway.app"  # ссылка на админку
WEBAPP_CATALOG_URL = "https://web-production-3878b.up.railway.app"  # ссылка на каталог

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # 📦 Кнопка для Каталога
    catalog_button = types.KeyboardButton("📦 Каталог", web_app=types.WebAppInfo(url=WEBAPP_CATALOG_URL))

    # 🛠 Кнопка для Админ-панели
    admin_button = types.KeyboardButton("🛠 Админ-панель", web_app=types.WebAppInfo(url=WEBAPP_ADMIN_URL))

    # Добавляем обе кнопки
    markup.add(catalog_button, admin_button)

    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в <b>EKRAN.TJ</b>\n\n"
        "Выберите действие ниже:",
        reply_markup=markup
    )

@bot.message_handler(content_types=['web_app_data'])
def handle_webapp_data(message):
    data = message.web_app_data.data
    bot.send_message(message.chat.id, f"✅ Получены данные из WebApp: <code>{data}</code>")

bot.infinity_polling()
