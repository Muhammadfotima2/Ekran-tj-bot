import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

# 🔐 Токен Telegram-бота
TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(TOKEN)

# 🚀 /start — Кнопка WebApp
@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(
        text='📲 Открыть каталог',
        web_app=WebAppInfo(url='https://muhammadfotima2.github.io/ekran-webapp/')
    ))
    bot.send_message(
        message.chat.id,
        "📱 Добро пожаловать в магазин <b>EKRAN.TJ-KBS</b>!\n\n"
        "🛍 Нажмите кнопку ниже, чтобы открыть каталог экранов и выбрать нужную модель и качество:",
        reply_markup=markup,
        parse_mode='HTML'
    )

# 📦 Обработка заказа из WebApp
@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    data = message.web_app_data.data.strip()
    try:
        model, quality, price = [part.strip() for part in data.split('|')]
        text = (
            "✅ <b>Заказ получен!</b>\n\n"
            f"📱 <b>Модель:</b> {model}\n"
            f"🛠 <b>Качество:</b> {quality}\n"
            f"💰 <b>Цена:</b> {price}\n\n"
            "📲 Мы с Вами скоро свяжемся!"
        )
    except Exception as e:
        text = f"⚠️ Ошибка при обработке заказа: {e}"

    bot.send_message(message.chat.id, text, parse_mode='HTML')

# 🔁 Запуск бота
bot.infinity_polling()
