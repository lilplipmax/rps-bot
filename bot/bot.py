import random
import telebot
from telebot import types



bot = telebot.TeleBot("7127149921:AAHHFtFPLF51qXP6l6Iz1U8trIvhvENn6xs")

game = ["Камень", "Ножницы", "Бумага"]

@bot.message_handler(commands=["start"])
def handle_start(message):
  keyboard = types.ReplyKeyboardMarkup(True)
  button1 = types.KeyboardButton("Камень")
  button2 = types.KeyboardButton("Ножницы")
  button3 = types.KeyboardButton("Бумага")
  keyboard.add(button1, button2, button3)


  bot.send_message(message.chat.id, "Здравствуй, котик)", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_message(message):

  random_object = random.choice(game)

  result = "Заново!!!"
  if random_object == "Камень" and message.text == "Ножницы":
    result = "Антимяу"
  elif random_object == "Бумага" and message.text == "Ножницы":
    result = "МЯУ МЯУ"
  elif random_object == "Ножницы" and message.text == "Ножницы":
    result = "Еще раз("
  elif random_object == "Ножницы" and message.text == "Бумага":
    result = "Кот облезлый"
  elif random_object == "Камень" and message.text == "Бумага":
    result = "ПУШИСТИК!!!!"
  elif random_object == "Бумага" and message.text == "Бумага":
    result = "Ни тебе ни мне"
  elif random_object == "Бумага" and message.text == "Камень":
    result = "Ты кот породы сфинктер"
  elif random_object == "Ножницы" and message.text == "Камень":
    result = "Кот доволен"
  elif random_object == "Камень" and message.text == "Камень":
    result = "пох"

  bot.send_message(message.chat.id, random_object)
  bot.reply_to(message, result)



bot.polling(none_stop=True)