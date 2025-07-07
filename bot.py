import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(TOKEN)

# Удаляем webhook перед запуском polling
bot.remove_webhook()

# /start — главное меню
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("📦 Original", callback_data="cat_Original"),
        InlineKeyboardButton("💡 OLED", callback_data="cat_Oled"),
        InlineKeyboardButton("🧩 Incell", callback_data="cat_Incell")
    )
    bot.send_message(
        message.chat.id,
        "📱 Добро пожаловать в магазин EKRAN.TJ-KBS!\nВыберите качество экрана:",
        reply_markup=markup
    )

# Категория → список моделей
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
    bot.edit_message_text(
        f"📦 Модели с качеством: {quality}",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )

# Модель → подробности
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
        bot.send_photo(call.message.chat.id, photo=photo_url, caption=text, parse_mode='HTML', reply_markup=markup)

# Заказ
@bot.callback_query_handler(func=lambda call: call.data.startswith("order_"))
def handle_order(call):
    bot.send_message(
        call.message.chat.id,
        "📦 Напишите, пожалуйста, ваше имя, номер телефона и количество товара. Мы скоро с вами свяжемся!"
    )

bot.polling()
