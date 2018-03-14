# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
# Input values
IntMode = input('Enter interface mode (access/trunk): ')
IntNumber = input('Enter interface type and number: ')
if IntMode == 'access':
  VlanSet = input('Enter vlan (ex: 10): ')
else:
  VlanSet = input('Enter vlans(ex: 2,3,4,5): ')

# Output config
print('interface ' + IntNumber)
if IntMode == 'access':
  print(access_template[0])
  print(access_template[1].format(VlanSet))
  print(access_template[2])
  print(access_template[3])
  print(access_template[4])
else:
  print(trunk_template[0])
  print(trunk_template[1])
  print(trunk_template[2].format(VlanSet))
