# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

spconfig1 = command1.strip().split()
spconfig2 = command2.strip().split()

lvlans1 = spconfig1[-1].split(',')
lvlans2 = spconfig2[-1].split(',')

svlans1 = set(lvlans1)
svlans2 = set(lvlans2)

resultvlans = svlans1.intersection(svlans2)

print (resultvlans)

