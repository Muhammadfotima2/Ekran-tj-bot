import telebot
from flask import Flask, request

API_TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'  # Твой токен сюда
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "📲 Бот успешно работает через Webhook!")

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
