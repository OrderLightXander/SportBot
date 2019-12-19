import telebot
from Test import Scrapper
from ScrapperInPage import PgScr
from ScrapperInPage import returner
from ScrapperCof import returnerCof
from ScrapperCof import ScrappeCof
bot = telebot.TeleBot('958041868:AAHbY8MawShxUpCLgPYmWm-BXL5C9K5lieM')
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    #elif message.text == '1':
        #bot.send_message(message.chat.id, returner(id_country))
    else:
        id_country = int(message.text)
        if id_country % 2 == 0:
            bot.send_message(message.chat.id, returner(raw_list, id_country) + returnerCof(raw_cof, id_country) + returner(raw_list,id_country+1) + returnerCof(raw_cof, id_country+1))
        else:
            bot.send_message(message.chat.id, returner(raw_list,id_country-1) + returnerCof(raw_cof,id_country-1) + returner(raw_list,id_country)+returnerCof(raw_cof,id_country))


raw_data = Scrapper(1)
raw_list = PgScr(raw_data)
raw_cof = ScrappeCof(raw_data)
bot.polling()