# Задача №1 лекция «Открытие и чтение файла, запись в файл»
from pprint import pprint

templ = ['ingridient_name', 'quantity', 'measure']
cook_book = {}
def new_func(cook_book):
    return cook_book

with open('files/book1.txt', "r", encoding='utf-8') as file:
      for string in file:
         ingradient = file.readline()
         menu_list = []
         for i in range(int(ingradient)):
            consistent = dict(zip(templ, file.readline().rstrip('\n').split(" | ")))# склеить 2 списка в словарь
            menu_list.append(consistent)
         file.readline()# читаем пустую строчку
         cook_book[string.strip()] = menu_list# Склеиваем в словарь название меню и состав
      print('cook_book = ')
      pprint(cook_book, sort_dicts=None)