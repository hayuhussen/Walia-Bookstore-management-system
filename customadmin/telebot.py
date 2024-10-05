import os
import telebot

BOT_TOKEN = os.environ.get('7486348793:AAEFA0AcY4Iw7oQIuzfCf-bjnTdyBwzptMk')
bot = telebot.TeleBot('7486348793:AAEFA0AcY4Iw7oQIuzfCf-bjnTdyBwzptMk')

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, ''
    '/category : book categories'
                 '')


bot.polling(none_stop = True, interval = 0)
