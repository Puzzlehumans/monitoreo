import os
from dotenv import load_dotenv
import telebot
from threading import Thread
import time 
from telebot import types
from models.chat import chat

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

BOT_INTERVAL = 3
BOT_TIMEOUT = 10
chatid = []
bot = 0

def bot_polling():
    global bot
    print("Starting bot polling now")
    while True:
        try:
            print("New bot instance started")
            bot = telebot.TeleBot(BOT_TOKEN) #Generate new bot instance
            botactions() #If bot is used as a global variable, remove bot as an input param
            bot.polling(none_stop=True, interval=BOT_INTERVAL, timeout=BOT_TIMEOUT)
        except Exception as ex: #Error in polling
            print("Bot polling failed, restarting in {}sec. Error:\n{}".format(BOT_TIMEOUT, ex))
            bot.stop_polling()
            time.sleep(BOT_TIMEOUT)
        else: #Clean exit
            bot.stop_polling()
            print("Bot polling loop finished")
            break #End loop

def botactions():

    @bot.message_handler(commands=['start', 'hello'])
    def send_welcome(message):
        global chatid
        chatid.append(message.chat.id)
        bot.reply_to(message, "Bienvenido al Bot de Alertas de PuzzleHumans")


    @bot.message_handler(func=lambda msg: True)
    def echo_all(message):
        bot.reply_to(message, message.text)


t = Thread(target=bot_polling)
t.start()