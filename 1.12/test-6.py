#   ------------------------------------------------------------------------------
#   Bioinformatics Institute
#   Task 1.12.6
#   Напишите программу, считывающую с пользовательского ввода целое число n n n 
#   (неотрицательное), выводящее это число в консоль вместе с правильным образом 
#   изменённым словом "программист", для того, чтобы робот мог нормально общаться
#   с людьми, например: 1 программист, 2 программиста, 5 программистов.
#   a program that calculates the area of a triangle by three sides
#   Copyright (c) 2021. Danil Smirnov
#   Released under GNU Public License (GPL)
#   email zabanen.nu@ya.ru
#   ------------------------------------------------------------------------------

def get_end_by_count(count, word):
    endings = {
        'plural_genitive':  'ов',
        'nominative':       '',
        'genitive':         'а'
    }
    result = str(count) + ' ' + word
    if 11 <= count % 100 <= 19 or count % 10 > 4:
        result += endings['plural_genitive']
    elif count % 10 == 1:
        result += endings['nominative']
    elif 2 <= count % 10 <= 4:
        result += endings['genitive']
    elif count == 0 or count % 10 == 0:
        result += endings['plural_genitive']

    return result
    
print(get_end_by_count(int(input()), 'программист'))
