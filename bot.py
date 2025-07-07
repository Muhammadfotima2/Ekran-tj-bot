import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    webapp_url = 'https://muhammadfotima2.github.io/ekran-webapp/ekran_webapp_index.html'
    markup.add(
        InlineKeyboardButton("📱 Открыть каталог EKRAN.TJ", web_app=WebAppInfo(url=webapp_url))
    )
    bot.send_message(
        message.chat.id,
        "<b>📦 ХУШ ОМАДЕД БА EKRAN.TJ-KBS</b>\n\n👉 Барои дидани каталог, тугмаро зер кунед:",
        reply_markup=markup,
        parse_mode="HTML"
    )

@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    data = message.web_app_data.data  # Пример: "Samsung / OLED"
    model, quality = data.split(' / ')
    bot.send_message(
        message.chat.id,
        f"✅ Шумо интихоб кардед:\n\n📱 Модел: <b>{model}</b>\n💡 Сифат: <b>{quality}</b>",
        parse_mode="HTML"
    )

bot.infinity_polling()
