import telebot
from telebot import types

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
WEBAPP_URL = 'https://web-production-3878b.up.railway.app'  # твоя ссылка

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

# Пример товаров
catalog = [
    {"name": "iPhone XR", "quality": "Incell", "price": "240 сомонӣ"},
    {"name": "Samsung A13", "quality": "Original", "price": "100 сомонӣ"},
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    admin_button = types.KeyboardButton("🛠 Админ-панель", web_app=types.WebAppInfo(url=WEBAPP_URL))
    catalog_button = types.KeyboardButton("📦 Каталог товаров")
    markup.add(admin_button, catalog_button)

    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в <b>EKRAN.TJ</b>\n\nВыберите действие:",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == "📦 Каталог товаров")
def send_catalog(message):
    text = "<b>📦 Каталог товаров:</b>\n\n"
    for item in catalog:
        text += f"📱 <b>{item['name']}</b>\n🛠 Качество: {item['quality']}\n💰 Цена: {item['price']}\n\n"
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['web_app_data'])
def handle_webapp_data(message):
    data = message.web_app_data.data
    bot.send_message(message.chat.id, f"📥 Получены данные из WebApp:\n<code>{data}</code>")

bot.polling(non_stop=True)
