import telebot


bot = telebot.TeleBot('')

@bot.message_handler(content_types=['text'])
def repaet_all_messages(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(True)