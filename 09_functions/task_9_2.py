# -*- coding: utf-8 -*-
'''
Задание 9.2

Создать функцию, которая генерирует конфигурацию для trunk-портов.

Параметр trunk - это словарь trunk-портов.

Словарь trunk имеет такой формат (тестовый словарь trunk_dict уже создан):
    { 'FastEthernet0/1':[10,20],
      'FastEthernet0/2':[11,30],
      'FastEthernet0/4':[17] }

Функция должна возвращать список команд с конфигурацией
на основе указанных портов и шаблона trunk_template.
В конце строк в списке не должно быть символа перевода строки.

Проверить работу функции на примере словаря trunk_dict.


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def generate_trunk_config(trunk):
    '''
    trunk - словарь trunk-портов, для которых необходимо сгенерировать конфигурацию

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    '''
    trunk_template = [
        'switchport trunk encapsulation dot1q', 'switchport mode trunk',
        'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
    ]
    result_list = []

    for key in trunk.keys():
        result_list.append('interface {}'.format(key))
        result_list.append('switchport trunk encapsulation dot1q')
        result_list.append('switchport mode trunk')
        result_list.append('switchport trunk native vlan 999')
        istr = ''
        for i in trunk[key]: istr = istr + str(i) + ' '
        result_list.append('switchport trunk allowed vlan {}'.format(istr))
    return result_list

trunk_dict = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}
# Основное тело программы

result = generate_trunk_config(trunk_dict)

for item in result:
    print(item)
