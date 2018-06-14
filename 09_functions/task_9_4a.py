# -*- coding: utf-8 -*-
'''
Задание 9.4a

Задача такая же, как и задании 9.4.
Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
При этом, не привязываясь к конкретным разделам.
Она должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:
* то команды верхнего уровня будут ключами словаря,
* а команды подуровней - списками

Если уровня вложенности три:
* самый вложенный уровень должен быть списком,
* а остальные - словарями.

На примере interface Ethernet0/3.100:

{'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}}


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration', 'version', '!']
RealConfigFile = 'config_r1.txt'
print(RealConfigFile)
print()

def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return not any(word in command for word in ignore)

def get_command_map(filename, ignore):
    ResultDict = {}
    with open(filename, 'r') as f:
        Trigger = False
        ConfigCommand = ''
        ConfigCommandList = []
        for line in f:
            if line.find('!') != -1 :
                if Trigger:
                    ResultDict.update({ConfigCommand:ConfigCommandList})
                    ConfigCommandList = []
                Trigger = False
                continue
            if line.find(' ') != 0 and line.find('!') != 0 :
                Trigger = True
                ConfigCommand = line.strip('\n')
                ConfigCommandList = []
                continue
            if line.find(' ') == 0 :
                ConfigCommandList.append(line.strip('\n'))
    return ResultDict

# Основная программа

RealResult = get_command_map(RealConfigFile, ignore)

for InterfaceName in RealResult.keys():
    print(InterfaceName)
    for Command in RealResult[InterfaceName]:
        print(Command)
