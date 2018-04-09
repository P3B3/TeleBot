import telebot
from const import tokenTele, token
import vk_api
bot = telebot.TeleBot(tokenTele)
print(bot.get_me())

vk_session = vk_api.VkApi(token=token)
tools = vk_api.VkTools(vk_session)
wall = tools.get_all('wall.get', 100, {'owner_id': 177047189})
friends = tools.get_all
print('Friends count:', friends)


def log(message):
    from datetime import datetime
    print(datetime.now())
    print(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), message.text)


@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('А токен на гитхаб не залил?', 'а что еще?')
    user_markup.row('oh shit. I am sorry!', '/help')
    user_markup.row('Отправить сообщеине вк')
    user_markup.row('/start', '/stop')
    bot.send_message(message.from_user.id, "Привет!", reply_markup=user_markup)
    log(message)


@bot.message_handler(commands=['stop'])
def handel_text(message):
    hide_markup = telebot.types.ReplyKeyboardRemove(True)
    bot.send_message(message.from_user.id, 'meh', reply_markup=hide_markup)
    log(message)


@bot.message_handler(commands=['help'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    bot.send_message(message.from_user.id, "Привет!", reply_markup=user_markup)
    log(message)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'А токен на гитхаб не залил?':
        bot.send_sticker(message.from_user.id, "CAADBAADVgADgFwlA4KN7F0OMsfZAg")
        log(message)
    elif message.text == 'а что еще?':
        bot.send_message(message.from_user.id, 'Ничего. Я устал')
        log(message)
    elif message.text == 'oh shit. I am sorry!':
        bot.send_sticker(message.from_user.id, "CAADBAADNQMAAkMxogY12wEWrMirqgI")
    elif message.text == 'Отправить сообщеине вк':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        for i in range(0, 5):
            item = telebot.types.KeyboardButton('b')
            user_markup.add(item)
        bot.send_message(message.from_user.id, "Привет!", reply_markup=user_markup)
    elif message == message:
        bot.send_message(message.from_user.id, message.text)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


# определение айди стикера по ласт упд
bot.polling(none_stop=True, interval=0)
