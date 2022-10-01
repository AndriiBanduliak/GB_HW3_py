'''5. ** Задайте число. Составьте список чисел Фибоначчи, 
в том числе для отрицательных индексов (Негафибоначчи)

in
8
out
-21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

in
5
out
5 -3 2 -1 1 0 1 1 2 3 5'''


def negaFib(n):

    if n == 0 or n == 1:
        return n
    if n == -1:
        return -n
    if n < 0:
        return round(negaFib(abs(n)) * (-1)**(n + 1))
    else:
        return negaFib(n - 1) + negaFib(n - 2)


n = int(input('Enter the number: '))
for i in range(-n, n + 1):
    print(negaFib(i), end=' ')
