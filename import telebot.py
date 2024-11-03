import telebot

bot = telebot.TeleBot('7252428794:AAGGAT1LvBnH7jbJk2TerIG-l9CBsXFOM5I')

from telebot import types



@bot.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nХочешь расскажу немного о наших сотрудниках?"
  markup = types.InlineKeyboardMarkup()
  button_yes = types.InlineKeyboardButton('Да', callback_data='yes')
  markup.add(button_yes)
  bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)



@bot.callback_query_handler(func=lambda call:True)
def response(function_call):
  if function_call.message:
     if function_call.data == "yes":
        second_mess = "Первого сотрудника зовут Максим. Он преподаватель языка Python. Какую оценку вы хотите ему поставить?"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Теперь поставьте лайк или диздайк", callback_data='123'))
        bot.send_photo(message.chat.id, open("maxim.png"))
        bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        bot.answer_callback_query(function_call.id)



print('Сервер запущен.')
bot.polling(non_stop=True, interval=1)
