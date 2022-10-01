'''4.* Задайте список из произвольных вещественных чисел, 
количество задаёт пользователь.
Напишите программу, которая найдёт разницу между максимальным 
и минимальным значением дробной части элементов.

in
5
out
[5.16, 8.62, 6.57, 7.92, 9.22]
Min: 0.16, Max: 0.92. Difference: 0.76

in
3
out
[9.26, 8.5, 1.14]
Min: 0.14, Max: 0.5. Difference: 0.36'''
import random


def getList(size):
    if size < 0:
        size = -size
    result = [0.0] * size
    for i in range(size):
        result[i] = round(random.uniform(0, 1000), 4)
    print(result)
    return result


def minMax(List):
    min = List[0] - List[0] // 1
    max = min
    for i in range(len(List)):
        fract = List[i] - List[i] // 1
        if fract > max:
            max = fract
        if fract < min:
            min = fract
    print('Minimum fractional part: ', round(min, 4), 'Maximum fractional part: ', round(max, 4), end=' ')
    return round(max - min, 4)


print('Difference: ',minMax(getList(int(input('Enter the size of the list: ')))))
