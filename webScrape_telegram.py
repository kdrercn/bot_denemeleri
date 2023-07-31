import os
import telebot
import requests
from bs4 import BeautifulSoup
import csv
import re

BOT_TOKEN = ('TELEGRAM TOKEN')

print("Bot is working")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "/injury\n/italian")

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Buradayım")

@bot.message_handler(commands=['injury'])
def injury(message):
    r = requests.get('https://www.cbssports.com/nba/injuries/daily/')
    soup = BeautifulSoup(r.text, 'html.parser')
    category = []
    for item in soup.findAll('table')[0].findAll('tr'):
        category.append(item.get_text(strip=True))
    category.remove("TeamPlayerPositionInjuryInjury Status")
    inj = "\n".join(category)
    bot.reply_to(message, inj)

@bot.message_handler(commands=['italian'])
def italian(message):
    t = requests.get('https://www.bestrandoms.com/random-italian-words')
    soup2 = BeautifulSoup(t.text, 'html.parser')
    category = []
    for item in soup2.findAll('li', {'class': 'col-sm-6'}):
        category.append(item.get_text(strip=True))
    first_word = category[0]
    word = first_word.replace("Meaning", "")
    bot.reply_to(message, word) 
       

bot.infinity_polling()