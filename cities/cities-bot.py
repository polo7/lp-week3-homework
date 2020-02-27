# Переписать в виде функции, которая принимает имя файла и возвращает словарь,
# заполненный  а - я и городами в соотв. буквах.

# Убрать города с цифрами

# Установить изначально пустые буквы, чтобы в игре их пропускать и брать другую.

# При этом, если в процессе игры список стал пустым, то это значит проигрыш, т. к. города закончились.

# Инициализируем словарь буквами алфавита и соотв-щими им пустыми списками
test_dict = {}
for c in range(1072,1104):
    test_dict[chr(c)] = []

print(test_dict)

# Загружаем города из КЛАДР и заносим их в соотв-щие их первой букве элементы словаря
with open('ru_cities.txt', 'r', encoding='utf-8') as f_input:
    for line in f_input:
        c = line[0].lower()
        test_dict[c].append(line.rstrip('\n'))

print(test_dict)


# Ссылка на моего бота - http://t.me/LP16UberBot

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',level=logging.INFO,filename='bot.log')

PROXY = {
    'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def play_cities(bot, update):
    pass


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)
 

def main():
    mybot = Updater("1036004253:AAH6OgKQU0xZH7kDUtURSoaJ2Uvpjvvg8Jc", request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("play", play_cities))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()