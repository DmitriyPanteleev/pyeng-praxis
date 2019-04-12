# -*- coding: utf-8 -*-
'''
Задание 15.3a

Переделать функцию parse_cfg из задания 15.3 таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

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
            if re.search(cregexIP,line):
                matchDict.update({interfName:(re.search(cregexIP,line).group(1),re.search(cregexIP,line).group(2))})
    return matchDict

if __name__ == '__main__':
    
    pprint(parse_cfg('config_r1.txt'))
