# -*- coding: utf-8 -*-
'''
Задание 15.3b

Проверить работу функции parse_cfg из задания 15.3a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция parse_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Переделайте функцию parse_cfg из задания 15.3a таким образом,
чтобы она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''

import re
from pprint import pprint

def parse_cfg(inputFile):
    matchDict = {}
    cregexIntrf = re.compile('interface (\S+)')
    cregexIP = re.compile('ip address (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}) (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})')
    with open(inputFile, 'r') as inf:
        for line in inf.readlines():
            if re.search(cregexIntrf,line):
                interfName = re.search(cregexIntrf,line).group(1)
                ipList = []
            if re.search(cregexIP,line):
                ipList.append((re.search(cregexIP,line).group(1),re.search(cregexIP,line).group(2)))
                matchDict.update({interfName:ipList})
    return matchDict

if __name__ == '__main__':
    
    pprint(parse_cfg('config_r2.txt'))
