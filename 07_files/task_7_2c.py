# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

inputfile = str(argv[1:2]).strip('[]')[1:-1]
outfile = str(argv[2:]).strip('[]')[1:-1]
print(inputfile)
print(outfile)

with open(inputfile, 'r') as inf:
  with open(outfile, 'a') as outf:
    for line in inf.readlines():
        if not (set(ignore) & set(line.split())):
            outf.write(line)
            print(line, end="")
            