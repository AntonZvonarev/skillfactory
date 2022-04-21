# Задание 17_9_1
# Звонарев Антон, группа QAP-68

# Функция сортировки последовательности пузырьковым методом
def my_sort():
    for i in range(len(my_lst)):
        for j in range(len(my_lst) - i - 1):
            if my_lst[j] > my_lst[j + 1]:
                my_lst[j], my_lst[j + 1] = my_lst[j + 1], my_lst[j]
    return my_lst

# Функция поиска позиции числа в последовательности бинарным методом
def binary_search(mod_lst, my_element, start, end):
    if start > end:
        return False
    middle = (end + start) // 2
    if mod_lst[middle] == my_element:
        return middle
    elif my_element < mod_lst[middle]:
        return binary_search(mod_lst, my_element, start, middle - 1)
    else:
        return binary_search(mod_lst, my_element, middle + 1, end)

# Запрос ввода последовательности чисел
my_str = input("Введите последовательность чисел через пробел: ")

# Преобразование последовательности из строки в список
my_lst = list(map(int, my_str.split()))

# Запрос на ввод числа для поиска в списке
my_element = int(input("Введите любое число:"))

# Определение диапазона поиска бинарным методом
start = 0
end = len(my_lst)

# Создание сортированного списка через вызов функции сортировки
mod_lst = my_sort()
print("Последовательность чисел после сортировки:", mod_lst)

if mod_lst[0] > my_element or mod_lst[-1] < my_element: # Определение того, что введенное число не находится в границах списка
    print("Введённое число находится вне границ последовательности")
elif mod_lst[0] == my_element: # Проверка не является ли нулевой элемент числом для сравнения
    print("Введённое число является нулевым элементом отсортированной последовательности")
else:
    for i in range(len(mod_lst)):    # Определение числа из последовательности
       if mod_lst[i] >= my_element:  # предыдущего введенному или большему чем введенное
          my_element = mod_lst[i-1]  # Определение числа из последовательности для поиска его позиции
          break

print("Позиция предыдущего числа в отсортированной последовательности:", binary_search(mod_lst, my_element, start, end))