# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv

# Get address string and CIDR string from user input
# userNetwork = input('Input network (like 10.1.1.0/24): ')
(addrString, cidrString) = argv[1].split('/')

# Split address into octets and turn CIDR into int
addr = addrString.split('.')
cidr = int(cidrString)

# Initialize the netmask and calculate based on CIDR mask
mask = [0, 0, 0, 0]
for i in range(cidr):
	mask[int(i/8)] = mask[int(i/8)] + (1 << (7 - i % 8))

# Initialize net and binary and netmask with addr to get network
net = []
for i in range(4):
	net.append(int(addr[i]) & mask[i])

# Print information
print('Network: ')
print('{:10} {:10} {:10} {:10}'.format(net[0], net[1], net[2], net[3]))
print('{:010b} {:010b} {:010b} {:010b}'.format(int(net[0]), int(net[1]), int(net[2]), int(net[3])))

print('Mask: ')
print('{:10} {:10} {:10} {:10}'.format(mask[0], mask[1], mask[2], mask[3]))
print('{:010b} {:010b} {:010b} {:010b}'.format(int(mask[0]), int(mask[1]), int(mask[2]), int(mask[3])))
