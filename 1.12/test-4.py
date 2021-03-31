#   -----------------------------------------------------------
#   Bioinformatics Institute
#   python programming course solutions
#   Task 1.12.4
#   написать программу, на вход которой подаётся тип фигуры комнаты
#   и соответствующие параметры, которая бы выводила площадь получившейся комнаты
#   Copyright (c) 2021. Danil Smirnov
#   Released under GNU Public License (GPL)
#   email zabanen.nu@ya.ru
#   -----------------------------------------------------------


def calculateCircleArea(radius):
    return 3.14 * (radius ** 2)

def calculateRectangleArea(a, b):
    return a * b

def calculateTriangleArea(a, b, c):
    semi_perimeter = (a + b + c) / 2
    return (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5

RoomType = input()

if RoomType == 'круг':
    print(calculateCircleArea(float(input())))
elif RoomType == 'прямоугольник':
    print(calculateRectangleArea(float(input()), float(input())))
elif RoomType == 'треугольник':
    print(calculateTriangleArea(float(input()), float(input()), float(input())))



