cities = []
with open('rus_cities_abc.txt', 'r', encoding='utf-8') as f_input:
    for line in f_input:
        #line = line.rstrip('\n')
        if (not line in cities) and (not line.rstrip('\n')[-1].isdigit()) :
            cities.append(line)

with open('ru_cities.txt', 'w', encoding='utf-8') as f_output:
    for t in cities:
        f_output.write(t.upper())

# Generates CSV with letter;city
#with open('rus_cities.csv', 'w', encoding='utf-8') as f_output:
#    for t in cities:
#        s = t[0].lower()
#        line = s + ';' + t
#        f_output.write(line)