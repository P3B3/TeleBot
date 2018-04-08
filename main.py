import telebot
from constants import token

bot = telebot.TeleBot(token)
print(bot.get_me())


def log(message, answer):
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. {id = {2}} \n Текст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(answer)


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, "Помощи нет")


bot.polling(none_stop=True, interval=0)
