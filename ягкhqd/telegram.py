import telebot
bot = telebot.TeleBot('6879959992:AAFrc0yiTNdes6edvHrtzqoC35jJWwSE0UU') 
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message)
    bot.send_message(message.chat.id, 'Привет выбери какая у тебя группа? ')

    bot.polling (none_stop=True)
