
#   -----------------------------------------------------------------------
#   Bioinformatics Institute
#   python programming course solutions
#   Task 1.12.5
#   Напишите программу, которая получает на вход три целых числа,
#   по одному числу в строке, и выводит на консоль в три строки 
#   сначала максимальное, потом минимальное, после чего оставшееся число.
#   Copyright (c) 2021. Danil Smirnov
#   Released under GNU Public License (GPL)
#   email zabanen.nu@ya.ru
#   -----------------------------------------------------------------------

def getMinMaxMiddle(unsorted_list):
    sorted_list = sorted(unsorted_list)
    return sorted_list[2], sorted_list[0], sorted_list[1]


for number in getMinMaxMiddle(int(input()) for i in range(3)):
    print(number)
