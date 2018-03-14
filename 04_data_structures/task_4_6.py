# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

spospf_string = ospf_route.strip().split()

prefix = spospf_string[1]
admetric = spospf_string[2]
nexthop = spospf_string[4]
lastupdate = spospf_string[5]
outboundint = spospf_string[6]

print("Protocol:             OSPF")
print("Prefix:               "+prefix)
print("AD/Metric:            "+admetric)
print("Next-Hop:             "+nexthop)
print("Last update:          "+lastupdate)
print("Outbound Interface:   "+outboundint)
