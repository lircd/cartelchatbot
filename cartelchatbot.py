import telebot

bot = telebot.TeleBot('1043393164:AAHArcpd5Lyteh7eORF3W3rlcYLYCw1iT74')

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Привет,бот был создан для чата Cartel')

@bot.message_handler(commands=['rules'])
def rules_message(message):
	bot.send_message(message.chat.id, 'https://telegra.ph/PRAVILA-KARTELYA-12-13')

@bot.message_handler(content_types=['text'])
def sen_text(message):
	if message.text.lower() == 'правила чата':
		bot.send_message(message.chat.id, 'Пропишите "/rules"')		
bot.polling()