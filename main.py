import telebot
from const import tokenTele, token
import vk_api
import time
bot = telebot.TeleBot(tokenTele, 0)
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

tools = vk_api.VkTools(vk_session)
friends = tools.get_all('friends.search', 90)


def log(message):
    from datetime import datetime
    print(datetime.now())
    print(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), message.text)


@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('А токен на гитхаб не залил?', 'а что еще?')
    user_markup.row('oh shit. I am sorry!', '/help')
    user_markup.row('Загрузить моих друзей из VK')
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
    elif message.text == 'Загрузить моих друзей из VK':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        item = telebot.types.KeyboardButton('Назад')
        user_markup.add(item)
        for i in range(len(friends['items'])):
            item = telebot.types.KeyboardButton(friends['items'][i]['first_name'] + ' ' +
                                                friends['items'][i]['last_name'])
            user_markup.add(item)
        bot.send_message(message.from_user.id, "Выберите друга!", reply_markup=user_markup)
    elif message == message:
        markup = telebot.types.ForceReply(selective=False)
        for q in range(len(friends['items'])):
            if message.text == friends['items'][q]['first_name'] + ' ' + friends['items'][q]['last_name']:
                bot.send_message(message.from_user.id, 'Введите сообщение:', reply_markup=markup)
                vk.messages.send(user_id=friends['items'][q]['id'], message=message.text)


# ождиание ввода + отправка сообщение по айди
# определение айди стикера по ласт упд
bot.polling(none_stop=True, interval=0)
