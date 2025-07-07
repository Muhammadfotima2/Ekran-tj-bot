import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(TOKEN)

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
        "📱 Добро пожаловать в магазин <b>EKRAN.TJ-KBS</b>!\n\n"
        "🛍 Нажмите кнопку ниже, чтобы открыть каталог экранов и выбрать нужную модель и качество:",
        reply_markup=markup,
        parse_mode='HTML'
    )

@bot.message_handler(content_types=['web_app_data'])
def handle_web_app(message):
    data = message.web_app_data.data
    bot.send_message(message.chat.id, f"✅ Вы выбрали: <b>{data}</b>", parse_mode='HTML')

bot.infinity_polling()
