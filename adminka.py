from config import *

def send(lesson):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text = 'Увійти', url = lesson[2])
    markup.add(btn)
    bot.send_message(chat_id = idi, text = lesson[0], reply_markup = markup)
    t.sleep(300)
    bot.send_message(chat_id = idi, text = lesson[1], reply_markup = markup)