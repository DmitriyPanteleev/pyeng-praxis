# -*- coding: utf-8 -*-
'''
Задание 12.3

Создать функцию ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые передавны ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.

'''
from tabulate import tabulate
from datetime import date

# Genarating List of IPs
with open('{}_avlb_ip'.format(str(date.today())), 'r') as avIP, \
     open('{}_unlb_ip'.format(str(date.today())), 'r') as unIP:
     
     listAvIP = avIP.readlines()
     listUnIP = unIP.readlines()
     for i in range(0,max(len(listAvIP),len(listUnIP))) :
         if i > len(listAvIP) : listAvIP.append(' ')
         if i > len(listUnIP) : listUnIP.append(' ')

     mergedList = list(zip(listAvIP,listUnIP))
     
     print(tabulate(mergedList, headers=['Reachable','Unreachable']))
