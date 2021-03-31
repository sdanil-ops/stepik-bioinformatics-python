#   --------------------------------------------------------------------------
#   Bioinformatics Institute
#   python programming course solutions
#   Task 2.6.1
#   Напишите программу, которая считывает с консоли числа (по одному в строке) 
#   до тех пор, пока сумма введённых чисел не будет равна 0 и сразу после
#   этого выводит сумму квадратов всех считанных чисел.
#   Copyright (c) 2021. Danil Smirnov
#   Released under GNU Public License (GPL)
#   email zabanen.nu@ya.ru
#   --------------------------------------------------------------------------

numbers = [int(input())]
while sum(numbers) != 0:
    numbers.append(int(input()))

print(sum([x**2 for x in numbers]))
