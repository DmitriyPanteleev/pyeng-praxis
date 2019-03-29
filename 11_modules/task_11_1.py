# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

# parcing CDP function
def parse_cdp_neighbors(filename):
    with open(filename, 'r') as f:
        tableTrigger = False
        resultDict = {}
        for line in f:
            if line.find('show cdp neighbors') != -1:
                # get name current device
                curDevice = line[:(line.find('show cdp neighbors'))-1]
                continue
            if line.find('Device ID') != -1:
                # found table
                tableTrigger = True
                continue
            if tableTrigger:
                # parcing string and creating element of result table
                destDevice = line[:line.find(' ')]
                curInterf = line[line.find('Eth'):(line.find('Eth') + 7)]
                destInterf = line[line.rfind('Eth'):(line.rfind('Eth') + 7)]
                resultDict.update({(curDevice, curInterf):(destDevice, destInterf)})
                continue
    return resultDict

# Main programm

if __name__ == '__main__':

    print(parse_cdp_neighbors('sw1_sh_cdp_neighbors.txt'))
