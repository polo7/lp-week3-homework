from datetime import datetime, timedelta
import locale

current_day = datetime.now()

# Вчера
print(f'Вчера: {(current_day - timedelta(days=1)).strftime("%d.%m.%Y")}')

# Сегодня
print(f'Сегодня: {current_day.strftime("%d.%m.%Y")}')

# Месяц назад
# В общем чате условились, что месяц = 30 дней.
print(f'Месяц назад: {(current_day - timedelta(days=30)).strftime("%d.%m.%Y")}')

# Превратить строку "01/01/17 12:10:03.234567" в объект datetime
input_str = "01/01/17 12:10:03.234567"
print(f'\nПревратить строку "{input_str}" в объект datetime')
dt = datetime.strptime(input_str, '%d/%m/%y %H:%M:%S.%f')
print(dt)