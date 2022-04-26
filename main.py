import telebot
from telebot import types

bot = telebot.TeleBot("5399560251:AAHssP-oCzcddgvceNBIwKilAZC-le-9p-s", parse_mode=None)

user1_chat_id = "705106646"
user2_chat_id = "1109711152"


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    mess = f'Чё как, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.reply_to(message, mess, parse_mode='html')


@bot.message_handler()
def messanger(message):
    if int(message.chat.id) == int(user1_chat_id):
        bot.send_message(user2_chat_id, message.text)
    else:
        bot.send_message(user1_chat_id, message.text)


bot.infinity_polling()
