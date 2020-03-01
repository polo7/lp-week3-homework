import logging


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# Ссылка на моего бота - http://t.me/LP16UberBot
# !!! С 13 версии хотят отменить подход pass_* и перейти на context

# TO DO
# Добавить таймер для пользователя для ограничения времени ответа, чтобы он мог тоже проиграть
# Сделать посильней проверки и очистку ввода пользователя или поиск города итак с этим справится?
# Попробовать сделать Ростов-на-Дону и Ростов на Дону - чтобы прощать пользователю такие описки.
# Игра с несколькими игроками, если бота посадили в группу.
# Очередность их ходов? Они должны присоединиться к игре, что создать список играющих?
# Сделать выбор кто первым ходит
# Или если начали игру с аргументом и это город, то начал ходить пользователь - /start Воронеж
# Переписать с учетом того, что pas_* будет прекращена поддержка.

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',level=logging.INFO,filename='bot.log')

PROXY = {
    'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}

TOKEN = "1036004253:AAH6OgKQU0xZH7kDUtURSoaJ2Uvpjvvg8Jc"

# user_data = [
#	cities - словарь из загруженных городов
#	now_playing - True/False - игра начата?
#	empty_letter - список из букв, на которые не бывает городов (как там бука ё?)
#	last_city - последний названный город - пока не используется
# 	last_turn - 'user' / 'bot' - кто сделал последний ход - пока не используется
# ]

def load_cities_dict():
	# Словарь городов: ключ - буквы алфавита, значение - список город на эту букву
	cities_dict = {}
	
	# Заполняем ключами от "А" до "Я" с пустыми значениями
	# ! ord('Ё') == 1025 - в этот список она не попадет. Города на Ё игрок должен писать через Е
	for c in range(1040,1072):
		cities_dict[chr(c)] = []
	
	# Загружаем города из КЛАДР и заносим их в соотв-щие их первой букве ключи словаря
	with open('ru_cities.txt', 'r', encoding='utf-8') as f_input:
		for line in f_input:
			c = line[0]
			cities_dict[c].append(line.rstrip('\n'))
	return cities_dict

def valid_city(city, user_data):
	# Проверка есть ли такой город?
	if city[0] in user_data['cities'] and city in user_data['cities'][city[0]]:
		return True
	else:
		return False

def find_last_char(city, user_data):
	# Должны взять последнюю букву для поиска города в ответ.
	# Но надо пропустить те буквы, на которые не бывает городов.
	# i не должна вывалиться за пределы длины слова, т. к. не может быть города,
	# состоящего целиком из букв, на которые нет города :-)
	i = -1
	while city[i] in user_data['empty_letters']:
		i = i - 1
	return city[i]


def pick_city(city_last_char, user_data):
	# Найти и "сказать" город
	if user_data['cities'][city_last_char]:
		return user_data['cities'][city_last_char].pop()
	else:
		# Города на эту букву закончились, выдаем такой код, что городов больше нет.
		return '404'

def init_game(bot, update, user_data):
	user_data['now_playing'] = True
	user_data['cities'] = load_cities_dict()
	tmp_dict = user_data['cities'].copy()
	for i in range(1040, 1072):
		if tmp_dict[chr(i)]:
			del(tmp_dict[chr(i)])
	user_data['empty_letters'] = tmp_dict.keys()
	update.message.reply_text('"Города России". Начата новая игра. Напишите город или завершите игру командой /stop')

def stop_game(bot, update, user_data):
	user_data['now_playing'] = False
	update.message.reply_text('Игра завершена. Спасибо!')

def play_game(bot, update, user_data):
	# Заменить if внизу на 
	# if not user_data.get('now_playing', false) ???
	if not 'now_playing' in user_data.keys() or not user_data['now_playing']:
		update.message.reply_text('Игра не начата. Начните ее командой /start')
	else:
		# play game
		current_city = update.message.text.strip().upper() 
		if valid_city(current_city, user_data):
			# Игрок сказал подходящий город, удалим его из списка на эту букву.
			user_data['cities'][current_city[0]].remove(current_city)
			update.message.reply_text('Такой город есть :)')
			
			ch = find_last_char(current_city, user_data)
			update.message.reply_text('Мне на букву {}'.format(ch))

			city_bot_reply = pick_city(ch, user_data)
			if city_bot_reply != '404':
				# Нашли город в ответ. Говорим.
				update.message.reply_text(city_bot_reply)
				update.message.reply_text('Вам на букву {}'.format(find_last_char(city_bot_reply, user_data)))
				
				# Удалять не надо, при поиске итак идет pop()
				# user_data['cities'][city_bot_reply[0]].remove(city_bot_reply)
			else:
				update.message.reply_text('Города на букву {} закончились. Я проиграл :('.format(ch))
				stop_game(bot, update, user_data)

		else:
			update.message.reply_text('Такого города нет, ошибка в написании (Ё пишите через Е) или его уже называли')

def main():
	updater = Updater(TOKEN, request_kwargs=PROXY)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler('start', init_game, pass_user_data=True))
	dp.add_handler(CommandHandler('stop', stop_game, pass_user_data=True))
	dp.add_handler(MessageHandler(Filters.text, play_game, pass_user_data=True))

	updater.start_polling()
	updater.idle()



if __name__ == "__main__":
    main()