# -*- coding: utf-8 -*-
'''
Задание 9.2a

Сделать копию скрипта задания 9.2

Изменить скрипт таким образом, чтобы функция возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе

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
    result_dict = {}

    for key in trunk.keys():
        result_list = []
        # result_list.append('interface {}'.format(key))
        result_list.append('switchport trunk encapsulation dot1q')
        result_list.append('switchport mode trunk')
        result_list.append('switchport trunk native vlan 999')
        istr = ''
        for i in trunk[key]: istr = istr + str(i) + ' '
        result_list.append('switchport trunk allowed vlan {}'.format(istr))
        result_dict.update({key:result_list})
    
    return result_dict

trunk_dict = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}
# Основное тело программы

result = generate_trunk_config(trunk_dict)

print(result)
