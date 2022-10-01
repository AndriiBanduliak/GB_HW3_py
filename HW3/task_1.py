'''1. Задайте список, состоящий из произвольных чисел, 
количество задаёт пользователь.
Напишите программу, которая найдёт сумму элементов списка, 
стоящих на нечётных позициях(не индексах).

in
5

out
[10, 2, 3, 8, 9]
22

in
4

out
[4, 2, 4, 9]
8
'''

from random import sample


def random_list(size):
    if size < 0:
        size = -size
    result = sample(range(size), size)
    print(result)
    return result


def el_list_sum(list):
    sum = 0
    for i in range(len(list)):
        if i % 2 == 0:
            sum += list[i]
    return sum


print(el_list_sum(random_list(int(input('Enter size of the list: ')))))