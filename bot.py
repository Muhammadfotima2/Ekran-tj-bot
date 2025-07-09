import telebot
from telebot import types

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
WEBAPP_CATALOG_URL = 'https://ekran-tj-catalog-production.up.railway.app/'  # Вставь адрес каталога

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    catalog_button = types.KeyboardButton("📦 Каталог товаров", web_app=types.WebAppInfo(url=WEBAPP_CATALOG_URL))
    markup.add(catalog_button)

    bot.send_message(
        message.chat.id,
        "👋 <b>Хуш омадед ба мағозаи EKRAN.TJ-KBS!</b>\n\n"
        "📲 Барои дидани <b>каталоги экранҳо</b> кнопкаро пахш кунед:",
        reply_markup=markup
    )

bot.polling(non_stop=True)
