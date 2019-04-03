# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например,
192.168.100.1-10.

Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

IP-адреса могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазон
а включая последний.

Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последни
й октет адреса.

Функция возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задачи можно воспользоваться функцией check_ip_addresses из задания 12.1
'''
import subprocess
from datetime import date
from netaddr import iter_iprange

def ping_ip(ip_address = '127.0.0.1', count = 3):
    reply = subprocess.run('ping -c {count} -n {ip}'.format(count=count, ip=ip_address),
                           shell = True,
                           stdout = subprocess.PIPE,
                           stderr = subprocess.PIPE)
    if reply.returncode == 0:
        return True, reply.stdout
    else:
        return False, reply.stdout + reply.stderr

with open('check_ip_list', 'r') as chkList, \
     open('{}_avlb_ip'.format(str(date.today())), 'w') as avIP, \
     open('{}_unlb_ip'.format(str(date.today())), 'w') as unIP:
     
    for ipStr in chkList:
        if ipStr.find('-') != -1 :
            ipbeg = ipStr[:(ipStr.find('-'))]
            ipend = ipStr[(ipStr.find('-'))+1:]
            iprange = iter_iprange(ipbeg, ipend, step=1)
            for ip in iprange:
                answer = ping_ip(str(ip))
                if answer[0]: avIP.write(str(ip)+'\n')
                else: unIP.write(str(ip)+'\n')
            continue
        ip = ipStr
        answer = ping_ip(ip)
        if answer[0]: avIP.write(ip)
        else: unIP.write(ip)
        continue
            