# -*- coding: utf-8 -*-
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

# Get address string and CIDR string from user input
userNetwork = input('Input network (like 10.1.1.0/24): ')
(addrString, cidrString) = userNetwork.split('/')

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
