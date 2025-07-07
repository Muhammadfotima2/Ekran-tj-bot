import telebot
from flask import Flask, request

API_TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

models = [
    {"model": "iPhone 13 Pro", "quality": "Original", "brand": "KBS", "price": "250 сомонӣ"},
    {"model": "Samsung A12", "quality": "OLED", "brand": "Service Pack", "price": "120 сомонӣ"},
    {"model": "Redmi Note 10", "quality": "Incell", "brand": "KBS", "price": "90 сомонӣ"}
]

@bot.message_handler(commands=['start'])
def start_message(message):
    welcome_text = "Хуш омадед ба Магазини EKRAN.TJ-KBS!\n\n📱 Каталоги экранҳои мобилӣ:\n\n"
    for item in models:
        welcome_text += (f"• {item['model']}\n  Качество: {item['quality']}\n  Бренд: {item['brand']}\n"
                         f"  Цена: {item['price']}\n\n")
    bot.send_message(message.chat.id, welcome_text)

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
