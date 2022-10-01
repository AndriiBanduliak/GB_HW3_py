'''3. Напишите программу, которая будет преобразовывать 
десятичное число в двоичное.
Без использования встроенной функции преобразования, 
без строк.Без использования встроенной функции преобразования, без строк.
in
88
out
1011000

in
11
out
1011'''


def dec_sys_to_bin(num):
    if num == 0:
        print(num)
        return
    elif num != 1:
        dec_sys_to_bin(num // 2)
    print(num % 2, end='')


dec_sys_to_bin(int(input('Enter the decimal number: ')))
print()
