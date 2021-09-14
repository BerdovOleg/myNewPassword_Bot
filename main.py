import telebot
from telebot import types

bot = telebot.TeleBot('API_KEY')

@bot.message_handler(commands=['website'])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="Bberdov.Studio", url="https://berdov.studio/"))
    bot.send_message(message.chat.id, "Отлично просто нажми на кнопку!", parse_mode='html',reply_markup=markup)

@bot.message_handler(commands=['start'])
def strart(message):
     send_mess = f"<b> Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nЗнаешь что? \nДля продолжение напиши /send"
     bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(commands=['send'])
def strart(message):
     send_mess = f"<b> =================================</b> /website"
     bot.send_message(message.chat.id, send_mess, parse_mode='html')


bot.polling(none_stop=True)