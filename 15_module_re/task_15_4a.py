# -*- coding: utf-8 -*-
'''
Задание 15.4a

Создать функцию convert_to_dict, которая ожидает два аргумента:
* список с названиями полей
* список кортежей с результатами отработки функции parse_sh_ip_int_br из задания 15.4

Функция возвращает результат в виде списка словарей (порядок полей может быть другой):
[{'interface': 'FastEthernet0/0', 'status': 'up', 'protocol': 'up', 'address': '10.0.1.1'},
 {'interface': 'FastEthernet0/1', 'status': 'up', 'protocol': 'up', 'address': '10.0.2.1'}]

Проверить работу функции на примере файла sh_ip_int_br_2.txt:
* первый аргумент - список headers
* второй аргумент - результат, который возвращает функции parse_show из прошлого задания.

Функцию parse_sh_ip_int_br не нужно копировать.
Надо импортировать или саму функцию, и использовать то же регулярное выражение,
что и в задании 15.4, или импортировать результат выполнения функции parse_show.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

headers = ['interface', 'address', 'status', 'protocol']
interfaces = [('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
              ('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
              ('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
              ('FastEthernet0/3', 'unassigned', 'down', 'down'),
              ('Loopback0', '10.1.1.1', 'up', 'up'),
              ('Loopback100', '100.0.0.1', 'up', 'up')]
result_list = []

for interface in interfaces:
    elem_dic = dict(zip(headers,list(interface)))
    relult_list = result_list.append(elem_dic)

print(result_list)
