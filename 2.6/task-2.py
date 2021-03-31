#   -----------------------------------------------------------
#   Bioinformatics Institute
#   python programming course solutions
#   Task 2.6.2
#   Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... 
#   (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное 
#   целое число n — столько элементов последовательности должна отобразить программа. 
#   На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
#   Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
#   Copyright (c) 2021. Danil Smirnov
#   Released under GNU Public License (GPL)
#   email zabanen.nu@ya.ru
#   -----------------------------------------------------------

def get_increasing_sequence(length: int)-> str:
    sequence = []
    for i in range(1, length + 1):
        for j in range(i):
            sequence.append(i)
            if len(sequence) == length:
                break
        else:
            continue
        break

    return sequence

for number in get_increasing_sequence(int(input())):
    print(number, end=' ')
