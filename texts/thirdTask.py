import os

files = os.listdir()
final_list = []
for filename in files:
    if not filename.endswith(".txt"):
        continue
    with open(filename, encoding='UTF-8') as f:
        text = f.readlines()
        length = len(text)
        my_list = [length, filename, text]
    final_list.append(my_list)

sorted_file_data = sorted(final_list)

with open('thirdTask.txt', 'a', encoding='UTF-8') as result_file:
    for line in sorted_file_data:
        result_file.write(f'Файл {line[1]}\n')
        for indx, raw in enumerate(line[2], 1):
            result_file.write(f"Строка {indx} {raw}")
        result_file.write("\n")