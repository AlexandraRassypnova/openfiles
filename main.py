from pprint import pprint

with open('recipes.txt', encoding='UTF-8') as file:
    cook_book = {}
    for line in file:
        name_dish = line.strip()
        number_ingredients = int(file.readline())
        products = []
        for ing in range(number_ingredients):
            product = file.readline().strip()
            ingredient_name, quantity, measure = product.split(' | ')
            products.append({'ingredient': ingredient_name,
                             'quantity': int(quantity),
                             'measure': measure})

        file.readline()
        cook_book[name_dish] = products

# pprint(cook_book)

def get_shop_list_by_dishes(person_count: int, dishes: list):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for ingr in cook_book[dish]:
                if ingr['ingredient'] in result:
                    result[ingr['ingredient']]['quantity'] += ingr['quantity'] * person_count
                else:
                    result[ingr['ingredient']] = {'measure': ingr['measure'],'quantity': (ingr['quantity'] * person_count)}
        else:
            print('Такого блюда нет в книге')
    pprint(result)

get_shop_list_by_dishes(10, ['Запеченный картофель', 'Омлет', 'Фахитос'])

