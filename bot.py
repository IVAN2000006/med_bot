import telebot
from telebot import types

from text import *
# Создаем экземпляр бота
bot = telebot.TeleBot('6177327678:AAF4I928IP_TG5L0rUysfmgAYkJOfF5Eln0')


markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard = types.InlineKeyboardMarkup()

def new_button(text):
    # global markup
    # item1=types.KeyboardButton(text.lower())
    # markup.add(item1)
    global keyboard
    butt_astma = types.InlineKeyboardButton(text = text, callback_data=text)
    keyboard.add(butt_astma)


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):

    # new_button("астма")
    # new_button("перелом")

    global keyboard
    butt_astma = types.InlineKeyboardButton(text = "astma", callback_data="astma")
    keyboard.add(butt_astma)

    bot.send_message(m.chat.id, text = '''Я на связи. Напиши что с тобой случилось:''', reply_markup= keyboard)

    


# Получение сообщения о травмах
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     if message.text == "перелом шейных позвонков":
#         bot.send_message(message.chat.id, "Поздравляю, вы мертвы")
#     elif message.text == "ушиб уха":
#         bot.send_message(message.chat.id, "Не пиши сюда больше")
#     # И так далее...
#     else:
#         bot.send_message(message.chat.id, "https://algoritmika.org/ru")



@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text.lower()=="астма":
        bot.send_message(message.chat.id,inj_astma)
    elif message.text.lower()=="перелом":
        bot.send_message(message.chat.id,inj_perelom)
    elif message.text.lower()=="ушиб":
        bot.send_message(message.chat.id,inj_ushib)
    elif message.text.lower()=="сотрясение":
        bot.send_message(message.chat.id,inj_sotryas)
    elif message.text.lower()=="ожог":
        bot.send_message(message.chat.id,inj_burn)
    elif message.text.lower()=="болив животе":
        bot.send_message(message.chat.id,inj_bolivjivote)
    elif message.text.lower()=="отравление":
        bot.send_message(message.chat.id,inj_otravlenie)
    elif message.text.lower()=="ранение":
        bot.send_message(message.chat.id,inj_ranenie)
    elif message.text.lower()=="сердце":
        bot.send_message(message.chat.id,inj_serdce)
    elif message.text.lower()=="апендицит":
        bot.send_message(message.chat.id,inj_apendicit)
    elif message.text.lower()=="гипотония":
        bot.send_message(message.chat.id,inj_gipoton)
    elif message.text.lower()=="гипертония":
        bot.send_message(message.chat.id,inj_giperton)
    elif message.text.lower()=="инсульт":
        bot.send_message(message.chat.id,inj_insult)
    elif message.text.lower()=="растяжение":
        bot.send_message(message.chat.id,inj_rastyajenie)
