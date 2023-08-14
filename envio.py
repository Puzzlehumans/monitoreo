import os
import requests
import emailPuzzle as em
# from mensajePuzzle import bot,chatid
import telebot
import time
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)
# chatid = men.chatid

res = requests.get('http://192.168.100.10:4000/getData/sensores/puz00003')
alarm = res.json()['DI0']
# alarm = 1
if alarm == 1:  
    hora_alerta = time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime())
    # print(hora_alerta)
    em.send_mail("ingenieria@puzzlehumans.com")
    em.send_mail("rpazmino@puzzlehumans.com")
    for user in chatid:
        bot.send_message(user, f'Alarma Activada Sr. Bader. /n/n/r Hora de activacion: {hora_alerta}')
        