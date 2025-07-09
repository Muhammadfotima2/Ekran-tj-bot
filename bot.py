import telebot
from telebot import types

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
WEBAPP_CATALOG_URL = 'https://ekran-tj-bot-production-XXXXX.up.railway.app'
WEBAPP_ADMIN_URL = 'https://ekran-tj-admin-production-XXXXX.up.railway.app/admin'

ADMIN_ID = 6172156061  # ← замени на свой Telegram ID

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    catalog_button = types.KeyboardButton("🛒 Каталог", web_app=types.WebAppInfo(url=WEBAPP_CATALOG_URL))
    markup.add(catalog_button)

    # Показываем кнопку админ-панели только админу
    if message.from_user.id == ADMIN_ID:
        admin_button = types.KeyboardButton("🛠 Админ-панель", web_app=types.WebAppInfo(url=WEBAPP_ADMIN_URL))
        markup.add(admin_button)

    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в <b>EKRAN.TJ</b>\n\nВыберите нужный раздел ниже:",
        reply_markup=markup,
        parse_mode='HTML'
    )
