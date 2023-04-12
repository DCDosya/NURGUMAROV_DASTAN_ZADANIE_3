#!/usr/bin/env python3
# coding=utf-8

import random


# функция для получения массива случайных чисел
def random_array(n, m=8, max_value=21):
    array = []  # основной массив
    for i in range(0, n):
        sub_array = []  # подмассив с числами
        for j in range(m):
            # от минимального числа (-10) до максимального -1 (max_value - 1 = 20) с шагом (1)
            number = random.randrange(-10, max_value, 1)
            sub_array.append(number)  # добавление случайного числа в подмассив
        array.append(sub_array)  # добавление подмассива в массив
    return array  # возвращается массив с подмассивами внутри


# функция для вывода массива
def print_array(array):
    print()
    for i in array:  # перебор по подмассивам(строкам)
        for j in i:  # перебор по элементам строк
            print("%5.1f\t" % j, end='')
        print()


# функция для нахождения элементов условия (в этом случае максимум и минимум,
# может быть количество нулей, количество отрицательных числе и т.д.)
def counting(array):
    print()
    # как начальное значение для макс берется первый элемент массива
    max_value = array[1][0]
    for j in range(5):
        e = array[1][j]
        if e > max_value:
            max_value = e
    print("Максимум: %d" % (max_value))
    print()
    return max_value

def nado(array):   #нужен чтобы узнать позицию максимального чилса второй строки
    max_value = array[1][0]
    nad = 0
    for j in range(5):
        e = array[1][j]
        if e > max_value:
            max_value = e
            nad = j
    return nad

def main():
    rowCount = 4
    colCount = 5
    # вызов функции рандома массива, которая возвращает полученный массив
    array = random_array(rowCount, colCount)  # можно изменить размер
    print("Условие задания:\n"
          "Найти максимальный элемент второй строки. \n"
          "Если он больше первого элемента третьей строки,\n"
          "то поменять элементы местами")
    # вызов функции вывода массива
    print_array(array)
    # вызов функции массива по условию, который возвращает элементы для проверки условия
    max_value = counting(array)
    maxposition = nado(array)
    while True:
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        key = input('Введите команду (1, 2 или 3): ')
        if key == '1':  # рандом, вывод и новые значения по условию нового массива
            array = random_array(rowCount, colCount)
            max_value = counting(array)
            maxposition = nado(array)
            print_array(array)
        elif key == '2':
            # проверка выполнения условия
            if max_value < array[2][0]:
                print("Максимальное число второй строки меньше первого элемента третьей строки (%d)" % (max_value))
                print("Задание не будет выполнено.")
            else:
                print("Максимальное число второй строки больше первого элемента третьей строки (%d)" % (max_value))
                # выполнения результата совпадения условия,
                # в данном случае меняем элементы местами
                adc = 0
                adc = array[2][0]
                array[2][0] = max_value
                array[1][maxposition] = adc
                print_array(array)
                break  # выход из цикла

        elif key == '3':
            exit(0)  # выход из программы
if __name__ == '__main__':
    main()
