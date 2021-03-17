#   -----------------------------------------------------------
#   Bioinformatics Institute
#   python programming course solutions
#   Task 1.12.1
#   a program that calculates the area of a triangle by three sides
#   Copyright (c) 2021. Danil Smirnov
#   Released under GNU Public License (GPL)
#   email zabanen.nu@ya.ru
#   -----------------------------------------------------------


def get_triangle_area(a: float, b: float, c: float):
    """calculates the area of a triangle using Heron's formula by the sides a, b, c """
    semi_perimeter = (a + b + c) / 2
    triangle_area = (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5
    return triangle_area


def test_get_triangle_area(test):
    print('Testing:', test.__doc__)
    test = test(3, 4, 5)
    print('Testcase: ', end="")
    print('Passed' if test == 6.0 else 'Failed')


test_get_triangle_area(get_triangle_area)

