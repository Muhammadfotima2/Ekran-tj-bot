import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(TOKEN)
bot.remove_webhook()

# /start — выбор бренда
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("📱 Samsung", callback_data="brand_Samsung"),
        InlineKeyboardButton("📱 iPhone", callback_data="brand_iPhone"),
        InlineKeyboardButton("📱 Redmi", callback_data="brand_Redmi"),
        InlineKeyboardButton("📱 Infinix", callback_data="brand_Infinix")
    )
    bot.send_message(
        message.chat.id,
        "📱 <b>ХУШ ОМАДЕД БА EKRAN.TJ-KBS</b>
👇 <b>Маркаи телефони худро интихоб намоед:</b>",
        reply_markup=markup,
        parse_mode='HTML'
    )

# Выбор качества после бренда
@bot.callback_query_handler(func=lambda call: call.data.startswith("brand_"))
def choose_quality(call):
    brand = call.data.split("_")[1]
    if brand == "Samsung":
        markup = InlineKeyboardMarkup()
        markup.row(
            InlineKeyboardButton("📦 Original", callback_data="cat_Samsung_Original"),
            InlineKeyboardButton("💡 OLED", callback_data="cat_Samsung_Oled"),
            InlineKeyboardButton("🧩 Incell", callback_data="cat_Samsung_Incell")
        )
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="🔧 <b>Мо экранҳои Samsung дорем бо сифатҳои зерин:</b>
Интихоб кунед ⬇️",
            reply_markup=markup,
            parse_mode='HTML'
        )
    else:
        bot.answer_callback_query(call.id, "Ҳоло танҳо Samsung дастрас аст.")

# Показ моделей
@bot.callback_query_handler(func=lambda call: call.data.startswith("cat_Samsung_"))
def show_models(call):
    quality = call.data.split("_")[2]
    conn = sqlite3.connect("telegram_catalog.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, model FROM samsung_catalog WHERE quality=?", (quality,))
    items = cursor.fetchall()
    conn.close()

    markup = InlineKeyboardMarkup()
    for item in items:
        markup.add(InlineKeyboardButton(item[1], callback_data=f"prod_{item[0]}"))
    bot.edit_message_text(
        f"📦 Моделҳои Samsung бо сифати: <b>{quality}</b>",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup,
        parse_mode='HTML'
    )

# Показ информации о модели
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
        text = f"📱 <b>{model}</b>\n🛠 <b>Качество:</b> {quality}\n🏷 <b>Бренд:</b> {brand}\n💰 <b>Цена:</b> {price} сомонӣ"
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
