#import telebot

#bot = telebot.TeleBot('7252428794:AAGGAT1LvBnH7jbJk2TerIG-l9CBsXFOM5I')

#from telebot import types



#@bot.message_handler(commands=['start'])
#def startBot(message):
# first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nХочешь расскажу немного о наших сотрудниках?"
# markup = types.InlineKeyboardMarkup()
#  button_yes = types.InlineKeyboardButton('Да', callback_data='yes')
#  markup.add(button_yes)
#  bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)



#@bot.callback_query_handler(func=lambda call:True)
#def response(function_call):
#  if function_call.message:
#     if function_call.data == "yes":
#        second_mess = "Первого сотрудника зовут Максим. Он преподаватель языка Python. Какую оценку вы хотите ему поставить?"
#        markup = types.InlineKeyboardMarkup()
#        markup.add(types.InlineKeyboardButton("Теперь поставьте лайк или диздайк", callback_data='123'))
#        bot.send_photo(message.chat.id, open("maxim.png"))
#        bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
#        bot.answer_callback_query(function_call.id)



#print('Сервер запущен.')
#bot.polling(non_stop=True, interval=1)

import telebot
from telebot import types

bot = telebot.TeleBot('7252428794:AAGGAT1LvBnH7jbJk2TerIG-l9CBsXFOM5I')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("? Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот для твоей статьи для habr.com".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "? Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
    elif(message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
    elif(message.text == "Как меня зовут?"):
        bot.send_message(message.chat.id, "У меня нет имени..")
    
    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Поздороваться с читателями")
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("? Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

print('Сервер запущен.')
bot.polling(none_stop=True)


