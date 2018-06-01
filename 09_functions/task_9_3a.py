# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
RealConfigFile = 'config_sw2.txt'
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
                    if VLANsList == []:
                        ResultDictAccess.update({InterfaceName:[1]})
                    else:
                        ResultDictAccess.update({InterfaceName:VLANsList})
                    VLANsList = []
                if Trigger == 'Trunk':
                    ResultDictTrunk.update({InterfaceName:VLANsList})
                    VLANsList = []
                Trigger = 'Empty'
                continue
            if line.find('mode access') != -1 :
                Trigger = 'Access'
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
