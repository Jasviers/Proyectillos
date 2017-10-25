'''
BOT TO THROW A COIN
'''
import telebot #Libreria para comunicar con telegram
import random #Libreria para generar un numero random
import getToken #Proporciona el token del bot
from telebot import types

bot = telebot.TeleBot(getToken.getToken("coin"))

idiom="esp"
idiomsList={
    "esp":{1:"Cara", 2:"Cruz",3:"Canto",4:"Elige tu idioma",5:"Resultado",6:"Elige"},
    "en":{1:"Head", 2:"Tail",3:"Edge",4:"Choose your idiom",5:"Result",6:"Choose"},
    "fr":{1:"Face", 2:"Pile",3:"Bord",4:"Algo en frances",5:"Resultado",6:"Elige"}
}

@bot.inline_handler(func=lambda query: query.query=='coin'or query.query=='moneda')
def coin(query):
    try:
        r = types.InlineQueryResultArticle('1',
                                           idiomsList[idiom][5],
                                           types.InputTextMessageContent(throw()))
        bot.answer_inline_query(query.id, [r])
    except Exception as e:
        print(e)

@bot.message_handler(commands=["moneda","coin",""])
def monedas(message):
        bot.reply_to(message, throw())

@bot.inline_handler(func=lambda query: query.query=='idiom')
def idioma(query):
    keyboard = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton(text="Esp", callback_data="esp")
    btn2 = telebot.types.InlineKeyboardButton(text="Fr", callback_data="fr")
    btn3 = telebot.types.InlineKeyboardButton(text="En", callback_data="en")
    keyboard.add(btn1)
    keyboard.add(btn2)
    keyboard.add(btn3)
    r = telebot.types.InlineQueryResultArticle(
        id="1",
        title=idiomsList[idiom][4],
        input_message_content=telebot.types.InputTextMessageContent(message_text=idiomsList[idiom][6]),
        reply_markup=keyboard
    )
    bot.answer_inline_query(query.id, [r], cache_time=10)

@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    idiom = call.data

def throw():
    num = random.randrange(0,10000)
    if num>5000 and num!=666 :
        return idiomsList[idiom][1]
    elif num == 666:
        return idiomsList[idiom][3]
    else:
        return idiomsList[idiom][2]



print("running...")
bot.polling(True)
