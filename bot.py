import telebot

TOKEN = '7861896848:AAHJk1QcelFZ1owB0LO4XXNFflBz-WDZBIE'
bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Привет! Бот работает ✅")

bot.remove_webhook()  # ВАЖНО: отключает Webhook, чтобы polling работал
bot.polling(non_stop=True)
