
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("📱 Каталог", callback_data="catalog"),
        InlineKeyboardButton("📦 Заказ", callback_data="order")
    )
    bot.send_message(message.chat.id, "Добро пожаловать в EKRAN_TJ_bot!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "catalog":
        bot.send_message(call.message.chat.id, "Каталог товаров скоро будет доступен.")
    elif call.data == "order":
        bot.send_message(call.message.chat.id, "Пожалуйста, отправьте ваш заказ.")

bot.polling()
