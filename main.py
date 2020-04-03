import telebot
import random
import os

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')


@bot.message_handler(content_types=['text'])
def folder(message):
    path = 'E:\file\file2\file3'
    name = random.randrange(10000, 100000)
    tname = os.path.join(path, str(name))
    os.mkdir(tname)
    tname2 = os.path.join(tname, 'file.txt')
    file = open(tname2, 'w')
    file.write(message.text)
    file.close()
    bot.send_message(message.chat.id, str(name))


bot.polling()
