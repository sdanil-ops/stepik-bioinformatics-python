#   --------------------------------------------------------------------------
#
#   Write a program that takes an integer as input that outputs True or False
#   if the passed value  is in the set of numbers (−15,12]∪(14,17)∪[19,+∞)
#
#   Copyright (c) 2021. Danil Smirnov
#   Released under GNU Public License (GPL)
#   email zabanen.nu@ya.ru
#   --------------------------------------------------------------------------

def is_in_area(number: int) -> bool:
    """returns True or False if the passed value  is in the set of numbers"""
    if -15 < number <= 12 or 14 < number < 17 or number >= 19:
        return True


def test_is_in_area(test):
    print('Testing: ', test.__doc__)

    print('Testcase #1: ', end='')
    print('Passed' if test(20) else 'Failed')

    print('Testcase #2: ', end='')
    print('Passed' if not test(-20) else 'Failed')


test_is_in_area(is_in_area)
