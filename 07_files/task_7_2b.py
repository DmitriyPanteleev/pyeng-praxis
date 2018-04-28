# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

inputfile = str(argv[1:]).strip('[]')[1:-1]
outfile = 'oufile_task72a.txt'
print(inputfile)
print(outfile)

with open(inputfile, 'r') as inf:
  with open(outfile, 'a') as outf:
    for line in inf.readlines():
        if not (set(ignore) & set(line.split())):
            outf.write(line)
            print(line, end="")
            