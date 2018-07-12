# Lesson 02 homework

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

# fruits = ['apple', 'banana', 'kiwi', 'watermelon', 'papaya', 'mango', 'cherry']
# new_fruits = enumerate(fruits)
# for index, fruit in new_fruits:
#     indexed_list = ('{}. {}').format(index + 1, fruit)
#     print(indexed_list)


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

# list_one = [1, 3, 5, 7, 9, 0, 'apple', 'banana', 'kiwi', 'watermelon', 'papaya', 'mango', 'cherry']
# list_two = [1, 2, 3, 4, 'kiwi', 'watermelon', 'cherry']
# list_three = [x for x in list_one if x not in list_two]
# print(list_three)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

# list = [1, 13, 0, 57, 9, 10, 16, 23, 4, 32, 67, 8, 143, 1000, 444]
# new_list= []
# for list_item in list:
#     if list_item % 2 == 0:
#         list_item /= 4
#     else:
#         list_item *= 2
#     new_list.append(list_item)
# print(new_list)

