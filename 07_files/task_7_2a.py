# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

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
            