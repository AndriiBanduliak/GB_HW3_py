'''2. Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
in
4

out
[2, 5, 8, 10]
[20, 40]

in
5

out
[2, 2, 4, 8, 8]
[16, 16, 4]'''

from random import sample as sam


def SumList(List):
    sum = [0]
    for i in range(len(List) // 2):
        sum.append(List[i] * List[len(List) - i - 1])
    if not len(List) % 2 == 0:
        sum.append(List[len(List) - len(List) // 2 - 1])
    sum.remove(0)
    return sum


digits = list(sam(range(10), 10))
print(digits)
print(SumList(digits))