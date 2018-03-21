# -*- coding: utf-8 -*-
'''
Задание 6.1b

Сделать копию скрипта задания 6.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

CorrectInput = True

while CorrectInput :    
    ipAddress = input('Enter IP Address: ')
    octets = ipAddress.split('.')
    # Test ip for correct input
    if len(octets) != 4 :
        print('Incorrect IPv4 address')
        continue
    for octet in octets :
        try:
            if int(octet) < 0 or int(octet) > 255 :
                print('Incorrect IPv4 address')
                continue
        except ValueError:
            print('Incorrect IPv4 address')
            continue
        if int(octet) < 0 or int(octet) > 255 :
            print('Incorrect IPv4 address')
            continue
    CorrectInput = False

# Categorized
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
