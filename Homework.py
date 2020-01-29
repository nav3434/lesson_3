
# 1) методами строк очистить текст от знаков препинания;
text = open('/Users/andrejnemov/Downloads/text.txt', 'r')
text = text.read()

text = text.replace('.', ' ')
text = text.replace('!', ' ')
text = text.replace('—', ' ')
text = text.replace(',', ' ')
text = text.replace('«', ' ')
text = text.replace('»', ' ')
text = text.replace('?', ' ')
print(text)


# 3) привести все слова к нижнему регистру (map);
text_low = text.lower()
print(text_low)

# 2) сформировать list со словами (split);
text_list = text_low.split()
print(text_list)


# 3) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;

text_dict = {}
for j in range (len(text_list)):
    many = 0
    word = text_list[j]
    for i in range(len(text_list)):
        if word == text_list[i]:
            many = many + 1
    text_dict[word] = many
print(text_dict)

# 4) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).

text_val = list(text_dict.values())
text_val.sort()
print('количество разных слов в тексте: ', len(text_val))
print('Наиболее часто встречающиеся слова: ')
for i in range(5):
    y = int(len(text_val))-1-i
    z = text_val[y]
    # print(text_val[y])
    # print(y,z)
    for key, value in text_dict.items():
        if value == z:
            print('слово: ', key, ' встречается ', value, 'раз')



