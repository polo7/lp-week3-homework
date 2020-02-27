cities = []
with open('rus_cities_abc.txt', 'r', encoding='utf-8') as f_input:
    for line in f_input:
        #line = line.rstrip('\n')
        if not line in cities:
            cities.append(line)

test_dict = {}

for t in cities:
    c = t[0].lower()
    if c in test_dict:
        test_dict[c].append(t.rstrip('\n'))
    else:
        #test_dict[c] = list(t.rstrip('\n'))
        test_dict.update({c:list(t)})

print(test_dict)

with open('rus_cities.csv', 'w', encoding='utf-8') as f_output:
    for t in cities:
        s = t[0].lower()
        line = s + ';' + t
        f_output.write(line)