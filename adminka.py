from config import *
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
	print(message.chat.id)
	if message.chat.id == admin_m:
		bot.send_message(admin_m, 'Привет, админ!')
	elif message.chat.id == admin_v:
		bot.send_message(admin_v, 'Привет, админ!')

@bot.message_handler(content_types=['text'])
def send_text(message):
	if message.text.lower() == 'отправить' and message.chat.id == admin_v or message.chat.id == admin_m:
		bot.send_message(message.chat.id, 'Привет, мой создатель')
	elif message.text.lower() == 'изменить' and message.chat.id == admin_v or message.chat.id == admin_m:
		bot.send_message(message.chat.id, 'Прощай, создатель')
bot.polling()