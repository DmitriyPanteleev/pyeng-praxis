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

# Duplicate net into broad array, gather host bits, and generate broadcast
broad = list(net)
brange = 32 - cidr
for i in range(brange):
	broad[int(3 - i/8)] = broad[int(3 - i/8)] + (1 << (i % 8))

# Print information, mapping integer lists to strings for easy printing
print ("Address:   " , addrString)
print ("Netmask:   " , ".".join(map(str, mask)))
print ("Network:   " , ".".join(map(str, net)))
print ("Broadcast: " , ".".join(map(str, broad)))
