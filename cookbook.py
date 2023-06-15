# Задача №1 лекция «Открытие и чтение файла, запись в файл»
from pprint import pprint

cook_book = {}
with open('files/book1.txt', "r", encoding='utf-8') as file:
  for string in file:
    ingradient = file.readline()
    menu_list = []
    for i in range(int(ingradient)):
      x = file.readline().rstrip('\n').split(" | ")  #читаем строку в список
      consistent = {
        'ingridient_name': x[0],
        'quantity': int(x[1]),
        'measure': x[2]
      }  # собираем в словарь
      menu_list.append(consistent)
    file.readline()  # читаем пустую строчку
    cook_book[
      string.strip()] = menu_list  # Склеиваем в словарь название меню и состав
  print('cook_book = ')
  pprint(cook_book, sort_dicts=None)
  

# Задача №2
print('************************ Задача №2 **************************')
def get_shop_list_by_dishes(dishes, person_count):
  zakaz = []
  final = {}
  #ing_var = {}
  for i in dishes:
    zakaz += cook_book[i]
  # pprint(zakaz)
  # print('**************************')
  for i in zakaz:
    j = 0
    if i['ingridient_name'] not in final.keys():
      final.update({
        i['ingridient_name']: {
          'measure': i['measure'],
          'quantity': i['quantity'] * person_count
        }
      })
    else:  # вычисляем сколько раз встретился инградиент и перемножаем
      j += 1
      ing_var = {i['ingridient_name']: j}
      #print(ing_var,'')
      final.update({
        i['ingridient_name']: {
          'measure': i['measure'],
          'quantity': (i['quantity'] * j) * person_count
        }
      })
  #print(ing_var,'\n', ing_var.keys(),'\n', ing_var.values())
  #final_sort = sorted(final.items())
  #final_sort=sorted(final.values())
  return pprint(final)
  #return pprint(final_sort)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'],2)  #Запеченный картофель Фахитос Утка по-пекински
