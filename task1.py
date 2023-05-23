import re
import random
import os
from collections import UserDict


current_dir = os.path.dirname(__file__)
path_to_file = os.path.join(current_dir, 'synonyms.txt')
synonyms = []

with open(path_to_file, 'r', encoding='cp1251') as new_file:
    data = new_file.read()

    formatted_data = data.split('\n')

    for words in formatted_data:
        if words:
            pair = re.findall(r'\b\w*', words)
            result = []
            for word in pair:
                if word:
                    result.append(word.lower())
            synonyms.append(result)

    print(synonyms)

    while True:
        user_input = input("Введите слово, на которое хотите найти синоним: ").lower()

        for wrds in synonyms:
            if user_input in wrds:
                for word in wrds:
                    if word != user_input:
                        print(word)

        user_input2 = input('Нравится? ')

        if (user_input2 == 'Да') or (user_input2 == 'да'):
            print('Отлично')
            break
        else:
            user_input3 = input('Введите свой вариант: ')
            for wrds in synonyms:
                if user_input in wrds:
                    synonyms.remove(wrds)
                    synonyms.append([user_input, user_input3])
            print('Отлично, сохранил!')

