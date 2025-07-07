import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from datetime import datetime
import json

# ✅ Ваш токен
TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(TOKEN)

# 🔐 Telegram ID администратора
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
        """📱 Добро пожаловать в магазин <b>EKRAN.TJ-KBS</b>!

🛍 Нажмите кнопку ниже, чтобы открыть каталог экранов и выбрать нужную модель и качество:""",
        reply_markup=markup,
        parse_mode='HTML'
    )

# 🛒 Обработка множественного заказа
@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    data = message.web_app_data.data.strip()
    try:
        orders = json.loads(data)

        total = 0
        items_text = ""
        for item in orders:
            name = item["name"]
            quality = item["quality"]
            price = int(item["price"].split()[0])
            qty = int(item["quantity"])
            item_total = price * qty
            total += item_total
            items_text += f"📦 {name} | {quality} | {price} x {qty} = {item_total} сомонӣ\n"

        user_msg = f"✅ <b>Ваш заказ принят!</b>\n\n{items_text}\n💵 <b>Общая сумма: {total} сомонӣ</b>\n📲 Мы скоро свяжемся!"
        bot.send_message(message.chat.id, user_msg, parse_mode="HTML")

        admin_msg = f"""📥 <b>Новый заказ</b>

👤 Имя: {message.from_user.first_name}
🔗 Username: @{message.from_user.username or '—'}
🆔 ID: <code>{message.from_user.id}</code>
🕓 Дата: {datetime.now().strftime('%d.%m.%Y %H:%M')}

{items_text}
💵 <b>Общая сумма:</b> {total} сомонӣ
"""
        bot.send_message(ADMIN_ID, admin_msg, parse_mode="HTML")

    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Ошибка при обработке: {e}")

# 🔁 Старт бота
bot.infinity_polling()
