with open('referat.txt', 'r', encoding='utf-8') as input_file:
	text = input_file.read()

# Длину строки считаем именно по видимым символам, поэтому убираем переводы строки.
print('Длина полученной строки:{}'.format(len(text.replace('\n', ''))))

words_count = text.split()
print(f'Количество слов в тексте: {len(words_count)}')

text = text.replace('.', '!')

with open('referat2.txt', 'w', encoding='utf-8') as output_file:
	output_file.write(text)
print('Точки в тексте заменены на восклицательные знаки.')