# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
config1 = command1.split()
vlans1 = config1[-1].split(',')

config2 = command2.split()
vlans2 = config2[-1].split(',')
set1 = set(vlans1)
set2 = set(vlans2)
set3 = ((set1.intersection(set2)))
list1 = list(set3)
print(list1)
