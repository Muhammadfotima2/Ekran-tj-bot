import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

# ✅ Токен бота
TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(TOKEN)

# 🔹 Команда /start — отправка кнопки WebApp
@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    webapp_button = KeyboardButton(
        text='📲 Открыть каталог',
        web_app=WebAppInfo(url='https://muhammadfotima2.github.io/ekran-webapp/')
    )
    markup.add(webapp_button)
    bot.send_message(
        message.chat.id,
        "📱 Добро пожаловать в магазин <b>EKRAN.TJ-KBS</b>!\n\n"
        "🛍 Нажмите кнопку ниже, чтобы открыть каталог экранов и выбрать нужную модель и качество:",
        reply_markup=markup,
        parse_mode='HTML'
    )

# ✅ Обработка данных из WebApp
@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    data = message.web_app_data.data.strip()
    try:
        model, quality, price = [part.strip() for part in data.split('|')]

        response = f"""
✅ <b>Заказ получен!</b>

📱 <b>Модель:</b> {model}
🛠 <b>Качество:</b> {quality}
💰 <b>Цена:</b> {price}

📲 Скоро с Вами свяжемся!
        """
    except Exception as e:
        response = f"⚠️ Ошибка при обработке заказа: {e}"

    bot.send_message(message.chat.id, response, parse_mode="HTML")

# 🔁 Запуск бота
bot.infinity_polling()
