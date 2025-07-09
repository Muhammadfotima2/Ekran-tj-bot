import telebot
import flask

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
WEBHOOK_URL = 'https://worker-production-7d99.up.railway.app'  # Укажи твой Railway адрес

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')
server = flask.Flask(name)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "👋 Хуш омадед ба <b>EKRAN.TJ</b>!")

@server.route('/', methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        update = telebot.types.Update.de_json(flask.request.stream.read().decode("utf-8"))
        bot.process_new_updates([update])
        return '', 200
    else:
        return '', 403

if name == 'main':
    server.run(host='0.0.0.0', port=8080)
