# -*- coding: utf-8 -*-
'''
Задание 9.1a

Сделать копию скрипта задания 9.1.

Дополнить скрипт:
* ввести дополнительный параметр, который контролирует будет ли настроен port-security
 * имя параметра 'psecurity'
 * по умолчанию значение False

Проверить работу функции на примере словаря access_dict,
с генерацией конфигурации port-security и без.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

# Функции и начальные данные

def generate_access_config(access, psecurity = False):
    '''
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17 }

    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    '''

    access_template = [
        'switchport mode access', 'switchport access vlan',
        'switchport nonegotiate', 'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]

    port_security = [
        'switchport port-security maximum 2',
        'switchport port-security violation restrict',
        'switchport port-security'
    ]
    result_list = []

    for key in access.keys():
        result_list.append('interface {}'.format(key))
        result_list.append('switchport mode access')
        result_list.append('switchport access vlan {}'.format(access[key]))
        result_list.append('switchport nonegotiate')
        result_list.append('spanning-tree portfast')
        result_list.append('spanning-tree bpduguard enable')
        if psecurity :
            for item in port_security:
                result_list.append(item)

    return result_list

access_dict = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17,
    'FastEthernet0/17': 150
}

# Основное тело программы

result = generate_access_config(access_dict, True)

for item in result:
    print(item)
