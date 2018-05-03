# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ignore = ['address-table', 'Address', '----', '-------------------------------------------']

inputfile = 'CAM_table.txt'

with open(inputfile, 'r') as inf:
    for line in sorted(inf.readlines()):
        if not (set(ignore) & set(line.split())):
            print(line.replace('DYNAMIC     ', ''), end="")
            