#   -----------------------------------------------------------
#   Bioinformatics Institute
#   python programming course solutions
#   Task 1.12.4
#   calculate triangle's area by Heron's formula
#   Copyright (c) 2021. Danil Smirnov
#   Released under GNU Public License (GPL)
#   email zabanen.nu@ya.ru
#   -----------------------------------------------------------


def get_triangle_area(a: int, b: int, c: int):
    """ calculates the area of triangle using Heron's formula by the sides a, b, c"""
    semi_perimeter = (a + b + c) / 2
    triangle_area = (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5
    return triangle_area


print(get_triangle_area(
    int(input()), int(input()), int(input())))
