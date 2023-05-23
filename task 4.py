import re
import os


path_to_dir = os.path.dirname(__file__)
path_to_file = os.path.join(path_to_dir, 'Export(к доп задаче 4).txt')
path_to_new_file = os.path.join(path_to_dir, 'new_file.txt')
prehistory = []

with open(path_to_file, 'r', encoding='utf-16') as file:
    data = file.read()
    formatted_data = data.split('\n')

    for line in formatted_data:
        if 'Name space' in line:
            prehistory.append(line)
            string = '\n'.join(prehistory)
            start_index = formatted_data.index(line)

            with open(path_to_new_file, 'w+', encoding='utf-16') as new_file:
                new_file.write(string)
                new_file.write(formatted_data[start_index], )

        else:
            prehistory.append(line)

    for line in formatted_data[start_index + 1:]:
        details_data = line.split()
        new_line = []
        for index, word in enumerate(details_data):
            if 'Word' in details_data:
                if word == 'Word':
                    new_address = ''
                    number = int(details_data[index - 2])
                    if (number >= 8) and (number <= 15):
                        new_number = number - 8
                        address = details_data[index + 1]
                        new_address = address[:2] + str(int(address[2:5])*2) + address[5]

                    elif (number >= 0) and (number <= 8):
                        new_number = number
                        address = details_data[index + 1]
                        new_address = address[:2] + str(int(address[2:5])*2 + 1) + address[5]

                    if address[6:8] == 'DW':
                        new_address += 'DBW'
                    elif address[6:8] == 'DD':
                        new_address += 'DBD'
                    new_address = new_address + address[8:] + f'.{new_number}'

                    new_line = new_line[:-2]
                    new_line.append(new_address)
                    break
                else:
                    new_line.append(word)

            else:
                if word.startswith('DB'):
                    new_address = ''
                    new_address += word[:6]
                    if word[6:8] == 'DW':
                        new_address += 'DBW'
                    elif word[6:8] == 'DD':
                        new_address += 'DBD'
                    new_address += word[8:]
                    new_line.append(new_address)
                else:
                    new_line.append(word)

        new_line.append('\n')
        with open(path_to_new_file, 'a', encoding='utf-16') as new_file:
            new_file.write(' '.join(new_line))




    # for line in data.split('\t'):
    #     print(line)