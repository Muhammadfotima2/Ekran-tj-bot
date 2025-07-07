
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
import sqlite3

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(TOKEN)

# Старт
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("📦 Original", callback_data="cat_Original"),
        InlineKeyboardButton("💡 OLED", callback_data="cat_Oled"),
        InlineKeyboardButton("🧩 Incell", callback_data="cat_Incell")
    )
    bot.send_message(message.chat.id, "📱 Добро пожаловать в каталог Samsung!
Выберите качество экрана:", reply_markup=markup)

# Обработка выбора категории
@bot.callback_query_handler(func=lambda call: call.data.startswith("cat_"))
def show_models(call):
    quality = call.data.split("_")[1]
    conn = sqlite3.connect("telegram_catalog.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, model FROM samsung_catalog WHERE quality=?", (quality,))
    items = cursor.fetchall()
    conn.close()

    markup = InlineKeyboardMarkup()
    for item in items:
        markup.add(InlineKeyboardButton(item[1], callback_data=f"prod_{item[0]}"))
    bot.edit_message_text(f"🔍 Модели с качеством: {quality}", call.message.chat.id, call.message.message_id, reply_markup=markup)

# Обработка выбора модели
@bot.callback_query_handler(func=lambda call: call.data.startswith("prod_"))
def show_product(call):
    prod_id = call.data.split("_")[1]
    conn = sqlite3.connect("telegram_catalog.db")
    cursor = conn.cursor()
    cursor.execute("SELECT model, quality, brand, price, photo_url FROM samsung_catalog WHERE id=?", (prod_id,))
    result = cursor.fetchone()
    conn.close()

    if result:
        model, quality, brand, price, photo_url = result
        text = f"📱 <b>{model}</b>\n🛠 Качество: {quality}\n🏷 Бренд: {brand}\n💰 Цена: {price} сомонӣ"
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🛒 Заказать", callback_data=f"order_{prod_id}"))
        with open(photo_url, 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=text, parse_mode='HTML', reply_markup=markup)

# Обработка заказа
@bot.callback_query_handler(func=lambda call: call.data.startswith("order_"))
def handle_order(call):
    bot.send_message(call.message.chat.id, "📦 Напишите, пожалуйста, ваше имя, телефон и количество товара:")

bot.polling
