import telebot
from telebot import types

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
WEBAPP_CATALOG_URL = 'https://ekran-webapp-production.up.railway.app'
WEBAPP_ADMIN_URL = "https://web-production-48d37.up.railway.app"  # Админ-панель
ADMIN_ID = 6172156061  # Замени на свой Telegram ID

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    catalog_button = types.KeyboardButton("🛒 Каталог", web_app=types.WebAppInfo(url=WEBAPP_CATALOG_URL))
    markup.add(catalog_button)

    # Кнопка админ-панели показывается только админу
    if message.from_user.id == ADMIN_ID:
        admin_button = types.KeyboardButton("🛠 Админ-панель", web_app=types.WebAppInfo(url=WEBAPP_ADMIN_URL))
        markup.add(admin_button)

    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в <b>EKRAN.TJ</b>\n\nВыберите нужный раздел ниже:",
        reply_markup=markup
    )

@bot.message_handler(content_types=['web_app_data'])
def handle_webapp_data(message):
    data = message.web_app_data.data
    bot.send_message(message.chat.id, f"📩 Получены данные: {data}")

bot.infinity_polling()
