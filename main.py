import telebot
import config
import os
import random


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет!')


def folder(hash):
    name = random.randrange(10000, 100000)
    os.mkdir(str(name))
    txt = open(str(name), 'w')
    txt.write(hash)
    return str(name)


@bot.message_handler(content_types=['text'])
def answer(message):
    bot.send_message(message.chat.id, folder(message.text))
