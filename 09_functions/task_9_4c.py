# -*- coding: utf-8 -*-
'''
Задание 9.4

Создать функцию, которая обрабатывает конфигурационный файл коммутатора
и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки можно оставлять).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration', 'version', '!']
RealConfigFile = 'config_sw1.txt'
print(RealConfigFile)

def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return not any(word in command for word in ignore)

def get_command_map(filename, ignore):
    ResultDict = {}
    with open(filename, 'r') as f:
        Trigger = False
        ConfigCommandList = []
        for line in f:
            if line.find(' ') != 0 :
                Trigger = True
                ConfigCommand = line.strip('\n')
                ConfigCommandList = []
                continue
            if line.find('!') != -1 :
                if Trigger:
                    ResultDict.update({ConfigCommand:ConfigCommandList})
                    ConfigCommandList = []
                Trigger = False
                continue
            ConfigCommandList.append(line.strip('\n'))
    return ResultDict

# Основная программа

RealResult = get_command_map(RealConfigFile, ignore)

for InterfaceName in RealResult.keys():
    print(InterfaceName)
    for Command in RealResult[InterfaceName]:
        print(Command)
