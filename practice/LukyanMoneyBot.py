import telebot

TOKEN = "5903676340:AAF1ndqShmx0AO6CBKG2NO66mueQCeifhcI"

bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(filters)
# def function_name(massege):
#     bot.reply_to(massege, 'This is a message handler')


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    bot.reply_to(message,f'Привет, {message.chat.username}')

bot.polling(none_stop=True)

@bot.message_handler(content_types=['photo', ])
def say_foto(message: telebot.types.Message):
    bot.reply_to(message, 'Крутая картинка)')

bot.polling(none_stop=True)
