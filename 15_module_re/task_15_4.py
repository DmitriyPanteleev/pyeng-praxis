# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'up', 'up')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br_2.txt.

'''

import re
from pprint import pprint

def parse_intrf_brf(inputFile):
    matchList = []
    cregex = re.compile('(\S+) +(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}|unassigned).+(up|down).+(up|down)')
    with open(inputFile, 'r') as inf:
        for line in inf.readlines():
            if re.search(cregex,line):
                matchList.append(re.search(cregex,line).groups())
    return matchList

if __name__ == '__main__':
    
    pprint(parse_intrf_brf('sh_ip_int_br_2.txt'))
