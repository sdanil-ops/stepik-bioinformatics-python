#   -----------------------------------------------------------
#   Simple calculator
#  #
#   Copyright (c) 2021. Danil Smirnov
#   Released under GNU Public License (GPL)
#   email zabanen.nu@ya.ru
#   -----------------------------------------------------------


def calculate(first_number, second_number, operator):
    """calculates operations +, -, /, *, mod, pow, div"""
    try:
        result = 0

        if operator == '+':
            result = first_number + second_number
        elif operator == '-':
            result = first_number - second_number
        elif operator == '*':
            result = first_number * second_number
        elif operator == 'pow':
            result = first_number ** second_number
        elif operator == '/':
            result = first_number / second_number
        elif operator == 'mod':
            result = first_number % second_number
        elif operator == 'div':
            result = first_number // second_number

        return result
    except ZeroDivisionError:
        return 'Деление на ноль!'



def test_calculate(test):
    """preventive testing"""
    print('Testing: ', test.__doc__)
    print('Testcase #1: ', end='')
    if test(7, 0, '/') == 'Деление на ноль!' and test(7, 7, '*') == 49:
        print('Passed')
    else:
        print('Failed')
    print('Testcase #2: ', end='')
    if (test(47, 7, 'mod') == 5 and test(47, 7, 'div') == 6 and
        test(2, 6, 'pow') == 64):
        print('Passed')
    else:
        print('Failed')
    print('Testcase #3: ', end='')
    if test(421, 123, '+') == 544 and test(2342, 1832, '-') == 510:
        print('Passed')
    else:
        print('Failed')



test_calculate(calculate)