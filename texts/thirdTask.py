import os

for filename in list(os.listdir()):
    my_list = []
    with open(filename, encoding='UTF-8') as f:
        text = f.readlines()
        length = len(text)
        my_list = [length, filename, text]
        print(my_list)