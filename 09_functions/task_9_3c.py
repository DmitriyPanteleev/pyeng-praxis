# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

from sys import argv

# filename = str(argv[1:]).strip('[]')[1:-1]

RealConfigFile = 'config_sw1.txt'
print(RealConfigFile)

def get_int_vlan_map(filename):
    ResultDict = {}
    with open(filename, 'r') as f:
        Trigger = False
        InterfaceConfigList = []
        for line in f:
            if line.find('interface') != -1 :
                Trigger = True
                InterfaceName = line.strip('\n')
                InterfaceConfigList = []
                continue
            if line.find('!') != -1 :
                if Trigger:
                    ResultDict.update({InterfaceName:InterfaceConfigList})
                    InterfaceConfigList = []
                Trigger = False
                continue
            InterfaceConfigList.append(line.strip('\n'))
    return ResultDict

# Основная программа

RealResult = get_int_vlan_map(RealConfigFile)

for InterfaceName in RealResult.keys():
    print(InterfaceName)
    for Command in RealResult[InterfaceName]:
        print(Command)
