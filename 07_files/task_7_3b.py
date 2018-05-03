# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ignore = ['address-table', 'Address', '----', '-------------------------------------------']

inputfile = 'CAM_table.txt'
vlan = input('Enter VLAN: ')

with open(inputfile, 'r') as inf:
    for line in sorted(inf.readlines()):
        if not (set(ignore) & set(line.split())):
            if line.find(vlan) != -1 :
                print(line.replace('DYNAMIC     ', ''), end="")
            