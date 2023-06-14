with open('cook_book.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for dish_name in file:
        ingredient_count = int(file.readline())
        ingredient_list = []
        for i in range(ingredient_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingredient_list.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish_name.strip()] = ingredient_list

print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    ingr_list = []
    for dish in dishes:
        if dish in cook_book:
            for ingr in cook_book[dish]:
                if ingr['ingredient_name'] not in ingr_list:
                    ingr_dict = { 'measure' : ingr['measure'] , 'quantity' : int(ingr['quantity']) * person_count }
                    shop_list[ingr['ingredient_name']] = ingr_dict
                    ingr_list.append(ingr['ingredient_name'])

                else:
                    print('повтор!')
                    print(ingr['ingredient_name'])
                    dublicate_ingr = int(ingr_dict['quantity'])
                    print(dublicate_ingr)
                    ingr_dict = {'measure': ingr['measure'], 'quantity': (int(ingr['quantity'])+dublicate_ingr) * person_count }
                    shop_list[ingr['ingredient_name']] = ingr_dict
                    ingr_list.append(ingr['ingredient_name'])


        else: print('Ошибка в названии блюд!')
    print(shop_list)
#    print(ingr_list)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# for dish in dishes:
#    if dish in cook_book:
#        for ingr in cook_book[dish]:
#            shop_list[ingr['ingredient_name']] = {{'measure': cook_book['measure'],'quantity': (cook_book['quantity'] * person_count)}}
#    else: print('Ошибка в названии блюд!')

#shop_list.append(ingr['ingredient_name'] = {
#        {'measure': ingr['measure'], 'quantity': (ingr['quantity'] * person_count)}})