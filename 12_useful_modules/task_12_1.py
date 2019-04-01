# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

import subprocess

def ping_ip(ip_address = '127.0.0.1', count = 3):
    reply = subprocess.run('ping -c {count} -n {ip}'.format(count=count, ip=ip_address),
                           shell = True,
                           stdout = subprocess.PIPE,
                           stderr = subprocess.PIPE,
                           encoding = 'utf-8')
    if reply.returncode == 0:
        return True, reply.stdout
    else:
        return False, reply.stdout + reply.stderr

curDate = subprocess.run('date',
                      shell = True,
                      stdout = subprocess.PIPE,
                      stderr = subprocess.PIPE,
                      encoding = 'utf-8')

with open('check_ip_list', r) as chkList, \
     open('{date}_avlb_ip'.format(date=curDate.stdout), w) as avIP, \
     open('{date}_unlb_ip'.format(date=curDate.stdout), w) as unIP:
     for ip in chkList:
         answer = ping_ip(ip)
         if answer[0]: avIP.write(ip)
         else: unIP.write(ip)
            