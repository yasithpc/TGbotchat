import os
import telebot


bot = telebot.TeleBot("1914396081:AAHNFA2409oexT-JMVr5eOnkFMaXb__3xkg")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm BST Community Chat Bot")


@bot.message_handler(commands=["botcreator"])
def send_message(message):
  bot.reply_to(message, "yasith")
  
@bot.message_handler(commands=["monitor"])
def send_message(message):
  bot.reply_to(message, "Namindu and Uppla. They are our Class leader")



bot.polling()
