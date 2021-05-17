# dict1 = {'besh_barmak': '130som'}
# print("Стоимость: ", dict1['besh_barmak'])


# dict2 = {'lagman': '120som'}
# print('Лагман - Старая цена: ', dict2['lagman'])
# dict2['lagman'] = '135som'
# print("Новая цена: ", dict2['lagman'])	

# dict3 = {'borsh': 'Исключенно из меню'}
# print("Борщ - ", dict3['borsh'])
# dict3.pop('borsh')


menu = {'manty': 200, 'plov': 150, 'lagman': 130, 'borsh': 100}
menu['besh_barmak'] = 130
print(menu)
cd1 = {'lagman': 135, 'hleb': 1000}
menu.update(cd1)
print(menu)
del menu['borsh']
print(menu)