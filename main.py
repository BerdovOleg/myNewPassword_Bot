import telebot
import datetime
import random
import logging

from telebot import types
let = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
       "w", "x", "y", "z"]
LET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
       "W", "X", "Y", "Z"]
numb = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbol = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "|", "{", "}", ":", "<", ">", "?", "\"", "№",
          ";", "%", ":", "/", "-", "=", "\\", ".", "`", "[", "]", ";", "'", ","]
def GetMePassword(Lengh,Uppercase, Numbers, MinNumbers, Symbols, MinSymbols):
    pswd = ""
    num  = ""
    symb = ""

    if Numbers & Symbols:
        lengh = Lengh - MinNumbers - MinSymbols

    if Numbers:
        for i in range(MinNumbers):
            rnd = random.randint(0, len(numb) - 1)
            num += numb[rnd]

    if Symbols:
        for i in range(MinSymbols):
            rnd = random.randint(0, len(symbol) - 1)
            symb += symbol[rnd]

    for i in range(lengh):
        rnd = random.randint(0,len(let)-1)

        if Uppercase:
            r = random.randint(0,2)
            if r > 1:
                pswd += (LET[rnd])
            else:
                pswd += (let[rnd])
        else:
            pswd += (let[rnd])

    pswd += num + symb
    l = list(pswd)
    random.shuffle(l)
    """ времинно пишим в файл, для публичного использования УДАЛИТЬ ДВЕ НИЖНИЕ СТЬРОЧКИ"""
    f = open('logs\log.txt', 'a')
    f.write(''.join(l)+ '\n')
    f.close()
    """====================================="""
    return ''.join(l)

f = open('key\API_KEY.txt', 'r')
API_KEY = f.read()
bot = telebot.TeleBot(API_KEY)

def start(command, id, first_name, last_name):
    d = datetime.datetime.now()
    s = 'Command: ' + command + ', Chat id: '+ str(id) + ', User F_name: ' + str(first_name) + ', User L_name: ' + str(last_name) + ', DateTime:' + str(d)
    print(s)
    f = open('logs\login.txt','a')
    f.write(s + '\n')
    f.close()


@bot.message_handler(commands=['website'])
def open_website(message):
    start(message.text, message.chat.id, message.from_user.first_name, message.from_user.last_name)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="GIT", url="https://github.com/BerdovOleg/myNewPassword_Bot"))
    bot.send_message(message.chat.id, "Отлично просто нажми на кнопку!", parse_mode='html',reply_markup=markup)

@bot.message_handler(commands=['start'])
def strart(message):
    try:
        start(message.text, message.chat.id, message.from_user.first_name, message.from_user.last_name)
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
    send_mess = f"<b> Привет {message.from_user.first_name} {message.from_user.last_name}</b>!" \
                f"\nЭтот бот генерирует для тебя случайные пароли! " \
                f"\nДля получения нового пароля напиши /menu " \
                f"\n<b>Внимание! Генерируемые пароли рекомендуется использовать как временное решение. " \
                f"\nДанный пароль не рекомендуется использовать для авторизации в сервисах с важной для Вас информацией. </b>"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(commands=['help'])
def strart(message):
    start(message.text, message.chat.id, message.from_user.first_name, message.from_user.last_name)
    send_mess = f"<b> /start для начала работы с ботом;" \
         f"\n/getpass генерация стандартного нового пароля;" \
         f"\n/getmediumpass генерация средней сложности пароля нового пароля;" \
         f"\n/getstrongpass генерация сложного пароля;"\
         f"\n/gethardgpass генерация гипер сложного пароля;" \
         f"\n/help для получения помощи;"\
         f"\n/website перейти на сайт проекта</b>"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(commands=['menu'])
def strart(message):
    start(message.text, message.chat.id, message.from_user.first_name, message.from_user.last_name)
    send_mess = f"<b>/getpass генерация стандартного нового пароля;" \
         f"\n/getmediumpass генерация средней сложности пароля нового пароля;" \
         f"\n/getstrongpass генерация сложного пароля;"\
         f"\n/gethardgpass генерация гипер сложного пароля;" \
         f"\n/website перейти на сайт проекта</b>"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(commands=['getpass'])
def strart(message):
    start(message.text, message.chat.id, message.from_user.first_name, message.from_user.last_name)
    s = ""
    try:
        s = GetMePassword(8,0,1,2,1,0)
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
    send_mess = s
    logging.info('This is a debug message getpass')
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(commands=['getmediumpass'])
def strart(message):
    start(message.text, message.chat.id, message.from_user.first_name, message.from_user.last_name)
    s = ""
    try:
        s = GetMePassword(11,1,1,3,1,0)
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
    send_mess = s
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(commands=['getstrongpass'])
def strart(message):
    start(message.text, message.chat.id, message.from_user.first_name, message.from_user.last_name)
    s = ""
    try:
        s = GetMePassword(13,1,1,3,1,3)
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
    send_mess = s
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(commands=['gethardgpass'])
def strart(message):
    start(message.text, message.chat.id, message.from_user.first_name, message.from_user.last_name)
    s = ""
    try:
        s = GetMePassword(16,1,1,3,1,3)
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
    send_mess = s
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    start(message.text, message.chat.id, message.from_user.first_name, message.from_user.last_name)
    bot.reply_to(message, message.text)

bot.polling(none_stop=True)