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

RealConfigFile = 'config_sw1.txt'
print(RealConfigFile)

def get_int_vlan_map(filename):
    ResultDictTrunk = {}
    ResultDictAccess = {}
    with open(filename, 'r') as f:
        Trigger = 'Empty'
        VLANsList = []
        for line in f:
            if line.find('interface') != -1 :
                Trigger = 'Interface'
                InterfaceName = line.strip('\n')
                VLANsList = []
                continue
            if line.find('!') != -1 :
                if Trigger == 'Access':
                    ResultDictAccess.update({InterfaceName:VLANsList})
                    VLANsList = []
                if Trigger == 'Trunk':
                    ResultDictTrunk.update({InterfaceName:VLANsList})
                    VLANsList = []
                Trigger = 'Empty'
                continue
            if line.find('access vlan') != -1 :
                VLANsList = [int(s) for s in line.split() if s.isdigit()]
                Trigger = 'Access'
            if line.find('trunk allowed vlan') != -1 :
                line = line.replace(',',' ')
                VLANsList = [int(s) for s in line.split() if s.isdigit()]
                Trigger = 'Trunk'
    return ResultDictAccess, ResultDictTrunk

# Основная программа

RealResultAccess, RealResultTrunk = get_int_vlan_map(RealConfigFile)

print('Access:')
for InterfaceName in RealResultAccess.keys():
    print(InterfaceName+': ', end = '')
    print(RealResultAccess[InterfaceName])

print('Trunk:')
for InterfaceName in RealResultTrunk.keys():
    print(InterfaceName+': ', end = '')
    print(RealResultTrunk[InterfaceName])
