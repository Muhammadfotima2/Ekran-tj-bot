import telebot
from telebot import types
from flask import Flask, request

API_TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# Каталог товаров (пример)
catalog = {
    "Samsung": ["Samsung A10", "Samsung A20", "Samsung A30"],
    "iPhone": ["iPhone 11", "iPhone 12", "iPhone 13"]
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('📱 Samsung')
    btn2 = types.KeyboardButton('🍎 iPhone')
    markup.add(btn1, btn2)
    welcome_text = "Хуш омадед ба Магазини EKRAN.TJ-KBS! \nЛутфан категорияро интихоб кунед:"
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    if text in catalog:
        items = catalog[text]
        response = f"Категория: {text}\nМаҳсулотҳо:\n" + "\n".join(items)
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, "Лутфан категорияро интихоб кунед ё /start фармонро истифода баред.")

@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return '', 200
    return 'Unsupported content type', 403

@app.route('/', methods=['GET'])
def index():
    return '✅ Webhook приложение работает!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
