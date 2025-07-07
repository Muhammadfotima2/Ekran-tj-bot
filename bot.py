import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from datetime import datetime

# ✅ Ваш токен
TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(TOKEN)

# 🔐 Telegram ID администратора (замени на свой!)
ADMIN_ID = 6172156061

# 🔹 Кнопка WebApp при /start
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

# 🛒 Обработка заказа
@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    data = message.web_app_data.data.strip()
    try:
        model, quality, price, quantity = [part.strip() for part in data.split('|')]

        # Формируем сообщение для пользователя
        response = f"""
✅ <b>Заказ принят!</b>

📱 <b>Модель:</b> {model}
🛠 <b>Качество:</b> {quality}
💰 <b>Цена:</b> {price}
📦 <b>Количество:</b> {quantity}

📲 Мы с вами скоро свяжемся!
        """
        bot.send_message(message.chat.id, response, parse_mode="HTML")

        # Формируем сообщение для администратора
        admin_msg = f"""
📥 <b>Новый заказ</b>

👤 Имя: {message.from_user.first_name}
🔗 Username: @{message.from_user.username or '—'}
🆔 ID: <code>{message.from_user.id}</code>
🕓 Дата: {datetime.now().strftime('%d.%m.%Y %H:%M')}

📱 Модель: <b>{model}</b>
🛠 Качество: <b>{quality}</b>
💰 Цена: <b>{price}</b>
📦 Количество: <b>{quantity}</b>
        """
        bot.send_message(ADMIN_ID, admin_msg, parse_mode="HTML")

    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Ошибка при обработке: {e}")

# 🔁 Старт бота
bot.infinity_polling()
