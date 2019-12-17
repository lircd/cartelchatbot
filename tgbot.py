import telebot

bot = telebot.TeleBot('1029207023:AAE3puWzo6tuF_XnEW6R2DjyOcVixEWYfz0') 
#Переменная с токеном

#Клавиатура
keybord1 = telebot.types.ReplyKeyboardMarkup(True, True) # 1 true(уменьшает кнопки) 2 true (скрывает кнопки после нажатия)
keybord1.row('Привет', 'Пока', 'Кто такой блэйн?') #row ряд

@bot.message_handler(commands=['start'])
#Реагирование на команду
def start_message(message):
	bot.send_message(message.chat.id, 'Привет,пошел нахуй отсюда', reply_markup=keybord1) 
	#Для ответа на команды
	#reply_markup=keybord1 вызов клавиатуры
@bot.message_handler(commands=['help'])
def help_message(message):
	bot.send_message(message.chat.id, 'Вам ничем уже не поможешь!')

@bot.message_handler(content_types=['text']) #текстовые команды
def sen_text(message):
	if message.text.lower() == 'привет': 
		bot.send_message(message.chat.id, 'Привет,создатель')
	elif message.text.lower() == 'пока':
		bot.send_message(message.chat.id, 'Пока,создатель')
	elif message.text.lower() == 'хуй':
		bot.send_message(message.chat.id, 'пизда')
	elif message.text.lower() == 'кто такой блэйн?':
		bot.send_message(message.chat.id, 'Онямэ')
	
	#bot.send_message(-395094915, '@'+message.from_user.username)	#пересыл телеграм линка в беседу
	bot.forward_message(-395094915, message.chat.id, message.message_id)	#пересыл сообщений








bot.polling()
#для того что бы бот не отключался
