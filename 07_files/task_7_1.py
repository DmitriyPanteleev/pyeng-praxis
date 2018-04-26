# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

with open('ospf.txt', 'r') as f:
    for line in f:
        spospf_string = line.strip().split()
        prefix = spospf_string[1]
        admetric = spospf_string[2]
        nexthop = spospf_string[4][:-1]
        lastupdate = spospf_string[5][:-1]
        outboundint = spospf_string[6]
        
        print("Protocol:             OSPF")
        print("Prefix:               "+prefix)
        print("AD/Metric:            "+admetric)
        print("Next-Hop:             "+nexthop)
        print("Last update:          "+lastupdate)
        print("Outbound Interface:   "+outboundint)
        print()
