import telebot
from telebot import types

bot = telebot.TeleBot('7252428794:AAGGAT1LvBnH7jbJk2TerIG-l9CBsXFOM5I')

@bot.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nХочешь расскажу немного о наших сотрудниках?"
  markup = types.InlineKeyboardMarkup()
  button_yes = types.InlineKeyboardButton('❓ Перейти к оценке преподавателей', callback_data='yes')
  button_yess = types.InlineKeyboardButton('Поздороваться!', callback_data='yess')
  markup.add(button_yes)
  markup.add(button_yess)
  bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def handle_callback(callback):
    if callback.data == 'yes':
        photo_url = 'maxim.png'
        bot.send_photo(callback.message.chat.id, photo_url)
        bot.answer_callback_query(callback.id, 'фото отправлено')
    else:
        bot.send_message(callback.message.chat.id, "Приятно познокомиться")
        
    
@bot.message_handler(content_types=['text'])
# second_mess = "Первого сотрудника зовут Максим. Он преподаватель языка Python. Какую оценку вы хотите ему поставить?"

def func(message):
    bot.send_photo(message.chat.id, open("maxim.png"))
    if(message.text == "? поставить лайк"):
        bot.send_message(message.chat.id, text="Спасибо большое!!!)")
    elif(message.text == "Почемууу"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Что вам не понравилось?")
        btn2 = types.KeyboardButton("Запускай бот по-новой и ставь лайк!?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
    elif(message.text == "Что вам не понравилось?"):
        bot.send_message(message.chat.id, "Не хочу об этом говорить")
    
    elif message.text == "Запускай бот по-новой и ставь лайк!?":
        bot.send_message(message.chat.id, text="хорошо")
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("? Поздороваться")
        button2 = types.KeyboardButton("❓ Перейти к оценке преподавателей")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

print('Сервер запущен.')
bot.polling(none_stop=True, interval = 1)


