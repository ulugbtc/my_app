import requests
import json
import logging

from telegram.ext import Updater
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import CommandHandler


updater = Updater(token='592647053:AAFZC8dkqsfybmBvxypViBIV42zTFGOWNYM')# here your telegram bots ip
dispatcher = updater.dispatcher


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


r = requests.get('https://api.coinmarketcap.com/v2/ticker/1027/')
info = r.text
raw_data = json.loads(info)
narx1 = raw_data['data']['quotes']['USD']['price']



r = requests.get('https://api.coinmarketcap.com/v2/ticker/1/')
info = r.text
raw_data = json.loads(info)
narx = raw_data['data']['quotes']['USD']['price']





def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Heloo!!! IF you wont to see  cost the /bitcoin or /ethereum. I am going to show you")
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)



def bitcoin(bot, update):    
    bot.send_message(chat_id=update.message.chat_id, text=narx)

bitcoin_handler = CommandHandler('bitcoin', bitcoin)
dispatcher.add_handler(bitcoin_handler)





def ethereum(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=narx1)

ethereum_handler = CommandHandler('ethereum', ethereum)
dispatcher.add_handler(ethereum_handler)



bot_name = 'https://t.me/coin_costbot'




updater.start_polling()
