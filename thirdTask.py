from pprint import pprint
import os

with open('1.txt', encoding='UTF-8') as file_1:
    lines_1 = file_1.readlines()
    len_1 = len(lines_1)

with open('2.txt', encoding='UTF-8') as file_2:
    lines_2 = file_2.readlines()
    len_2 = len(lines_2)

with open('3.txt', encoding='UTF-8') as file_3:
    lines_3 = file_3.readlines()
    len_3 = len(lines_3)


dict_ = {
    len_1: lines_1,
    len_2: lines_2,
    len_3: lines_3
        }

sorted_dict = dict(sorted(dict_.items()))
# needed_text = list(sorted_dict.items())
# text_ = ', '.join(needed_text)
# pprint(needed_text)
pprint(sorted_dict)



