# Задача №1 лекция «Открытие и чтение файла, запись в файл»
from pprint import pprint
cook_book = {}
with open('files/book1.txt', "r", encoding='utf-8') as file:
      for string in file:
         ingradient = file.readline()
         menu_list = []
         for i in range(int(ingradient)):
           x = file.readline().rstrip('\n').split(" | ")#читаем строку в список
           consistent = {'ingridient_name':x[0],'quantity':int(x[1]), 'measure':x[2]}# собираем в словарь
           menu_list.append(consistent)
         file.readline()# читаем пустую строчку
         cook_book[string.strip()] = menu_list# Склеиваем в словарь название меню и состав
      print('cook_book = ')
      pprint(cook_book, sort_dicts=None)
