# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ipAddress = input('Enter IP Address: ')
octets = ipAddress.split('.')

# Test ip for correct input

if len(octets) != 4 :
    print('Incorrect IPv4 address')
for octet in octets :
    if int(octet) < 0 or int(octet) > 255 :
        print('Incorrect IPv4 address')
        break
if ipAddress == '0.0.0.0' :
    print('unassigned')
elif ipAddress == '255.255.255.255' :
    print('local broadcast')
elif int(octets[0]) < 224 :
    print('unicast')
elif int(octets[0]) < 239 :
    print('multicast')
else :
    print('unused')
