array = [int(x) for x in input("Введите последовательность чисел через пробел:").split()]
print(array)

import random

def qsort_random(array, left, right):
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:

            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)

    return array

left = 0
right = int(len(array)-1)

print(qsort_random(array, left, right))

def binary_search(array, element, left, right):

    middle = (right + left) // 2
    if element == array[middle]:
        if array[middle - 1] < element and element <= array[middle]:
            return middle
        elif element < array[middle]:

            return binary_search(array, element, left, middle - 1)
    elif element == array[middle - 1]:

            return binary_search(array, element, left, middle - 1)
    else:
            return binary_search(array, element, middle + 1, right)

element = int(input("Введите любое положительное целое число из полученного списка: "))
if element not in array:
    print('Такого числа нет в списке')
if element <= array[0]:
    print('Числа нет в диапазоне')
elif element in array:
    print("Номер позиции элемента, который меньше введенного пользователем числа:",
          binary_search(array, element, 0, len(array) - 1))

array = sorted(array)
left = int(array[0])
right = int(array[-1])












