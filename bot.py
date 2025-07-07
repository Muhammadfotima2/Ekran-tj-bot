import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from datetime import datetime

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
        "📱 Добро пожаловать в магазин <b>EKRAN.TJ-KBS</b>!

"
        "🛍 Нажмите кнопку ниже, чтобы открыть каталог экранов и выбрать нужные модели:",
        reply_markup=markup,
        parse_mode='HTML'
    )

# 🛒 Обработка множественного заказа
@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    data = message.web_app_data.data.strip()
    try:
        lines = data.split('\n')
        order_lines = []
        total_sum = 0
        for line in lines:
            parts = line.strip().split('|')
            if len(parts) == 4:
                model, quality, price_text, qty_text = map(str.strip, parts)
                qty = int(qty_text.replace('Кол-во:', '').strip())
                price = int(''.join(filter(str.isdigit, price_text)))
                subtotal = qty * price
                total_sum += subtotal
                order_lines.append(f"📱 <b>{model}</b> | 🛠 {quality} | 💰 {price_text} | 🔢 {qty} шт. — 🧾 {subtotal} сом.")

        result_msg = "\n".join(order_lines)
        result_msg += f"\n\n<b>Общая сумма:</b> {total_sum} сомонӣ"

        # Клиенту
        bot.send_message(message.chat.id, f"✅ <b>Ваш заказ:</b>\n\n{result_msg}", parse_mode="HTML")

        # Админу
        admin_msg = f"""
📥 <b>Новый заказ</b>

👤 Имя: {message.from_user.first_name}
🔗 Username: @{message.from_user.username or '—'}
🆔 ID: <code>{message.from_user.id}</code>
🕓 Дата: {datetime.now().strftime('%d.%m.%Y %H:%M')}

{result_msg}
"""
        bot.send_message(ADMIN_ID, admin_msg, parse_mode="HTML")

    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Ошибка при обработке заказа: {e}")

# 🔁 Старт бота
bot.infinity_polling()
