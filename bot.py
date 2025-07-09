import telebot
from telebot import types

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(TOKEN)

# 🔗 URL WebApp
WEBAPP_CATALOG_URL = 'https://ekran-webapp.up.railway.app'
WEBAPP_ADMIN_URL = 'https://ekran-tj-admin.up.railway.app'

# 👑 Твой Telegram ID
ADMIN_ID = 6172156061

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # 📦 Кнопка каталога — видна всем
    catalog_button = types.KeyboardButton(
        "📦 Каталог",
        web_app=types.WebAppInfo(url=WEBAPP_CATALOG_URL)
    )
    markup.add(catalog_button)

    # 🛠 Кнопка админ-панели — видна только администратору
    if message.from_user.id == ADMIN_ID:
        admin_button = types.KeyboardButton(
            "🛠 Админ-панель",
            web_app=types.WebAppInfo(url=WEBAPP_ADMIN_URL)
        )
        markup.add(admin_button)

    bot.send_message(
        message.chat.id,
        "👋 Хуш омадед ба мағозаи <b>EKRAN.TJ‑KBS</b>!\n\n"
        "📱 Барои дидани каталоги экранҳо кнопкаро пахш кунед:",
        reply_markup=markup,
        parse_mode='HTML'
    )

bot.polling()
