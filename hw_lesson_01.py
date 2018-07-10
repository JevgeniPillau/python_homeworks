# Lesson 01 homework

<<<<<<< HEAD
# part 1, EASY level

# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран


=======
# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран

>>>>>>> сделал домашнее задание на уровне easy
# user_name = input('What is your name: ')
# user_age = int(input('How old are you: '))
# user_password = input('Please, insert password: ')
# print('Hello,', user_name, '!')
# print('Well,', user_name, 'your age is:', user_age, 'y')
# print(user_password)


# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

<<<<<<< HEAD

=======
>>>>>>> сделал домашнее задание на уровне easy
# number = int(input('insert number: '))
# number += 2
# print('Well, i think my number is bigger:', number)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

<<<<<<< HEAD

# user_age = int(input('How old are you: '))
#
# if user_age >= 18 >= 90:
#     print('Access granted, enjoy our resource!')
# elif user_age >= 90:
#     answer = input('Are you serious? y/n: ')
#     if answer == 'y':
#         print('Access granted, enjoy our resource!')
#     else:
#         print('Goodbye!')
# else:
#     print('Sorry, only users 18 yo. and above are allowed to view this resource')


# part 2, NORMAL level


# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4


# while True:
#     num = int(input('Please, insert number: '))
#     if 0 < num < 10:
#         num **= 2
#         print(num)
#     else:
#         print('Not a valid number')
#         print('Number should be from 0 to 10')


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;


# var_1 = int(input('Please insert number: '))
# var_2 = int(input('Please insert another number: '))
# print(var_1)
# print(var_2)
# print('***switching***')
# if var_1 == var_2:
#     print('Nothing to switch, numbers are equal')
# else:
#     var_1 = var_1 + var_2   # 3 = 1 + 2
#     var_2 = var_1 - var_2   # 1 = 3 - 2
#     var_1 = var_1 - var_2   # 2 = 1 + 1
#     print(var_1)
#     print(var_2)


# part 3, HARD level

# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

# если возраст заканчивается на 1 - то 'год'
# если на 2, 3, 4 - 'года'
# если на 0,5,6,7,8,9 - 'лет'


print ('Медицинская анкета')
print('Пожалуйста, заполните нашу анкету')
name_first = input('Ваше имя: ')
name_last = input('Ваша фамилия: ')
user_age = int(input('Ваш возраст: '))
user_weight = int(input('Ваш вес: '))
year = 'год'
years = 'лет'

if user_age < 30 and 50 <= user_weight <= 120:
    if str(user_age).endswith('1'):
        print(name_first, name_last + ',', 'возраст: ', user_age, year + ',', 'вес: ', user_weight, ' - хорошее состояние')
    elif str(user_age).endswith('2') or str(user_age).endswith('3') or str(user_age).endswith('4'):
        print(name_first, name_last + ',', 'возраст: ', user_age, year + 'а,', 'вес: ', user_weight, ' - хорошее состояние')
    else:
        print(name_first, name_last +',', 'возраст: ', user_age, years + ',', 'вес: ', user_weight, ' - хорошее состояние')
elif user_age >= 30 and user_age <= 40 and user_weight < 50 or user_weight > 120:
    if str(user_age).endswith('1'):
        print(name_first, name_last + ',', 'возраст: ', user_age, year + ',', 'вес: ', user_weight, ' - начните вести правильный образ жизни')
    elif str(user_age).endswith('2') or str(user_age).endswith('3') or str(user_age).endswith('4'):
        print(name_first, name_last + ',', 'возраст: ', user_age, year + 'а,', 'вес: ', user_weight, ' - начните вести правильный образ жизни')
    else:
        print(name_first, name_last +',', 'возраст: ', user_age, years + ',', 'вес: ', user_weight, ' - начните вести правильный образ жизни')
elif user_age > 40 and user_weight < 50 or user_weight > 120:
    if str(user_age).endswith('1'):
        print(name_first, name_last + ',', 'возраст: ', user_age, year + ',', 'вес: ', user_weight, ' - обратитесь к врачу')
    elif str(user_age).endswith('2') or str(user_age).endswith('3') or str(user_age).endswith('4'):
        print(name_first, name_last + ',', 'возраст: ', user_age, year + 'а,', 'вес: ', user_weight, ' - обратитесь к врачу')
    else:
        print(name_first, name_last + ',', 'возраст: ', user_age, years + ',', 'вес: ', user_weight, ' - обратитесь к врачу')
else:
	pass
=======
user_age = int(input('How old are you: '))

if user_age >= 18 >= 90:
    print('Access granted, enjoy our resource!')
elif user_age >= 90:
    answer = input('Are you serious? y/n: ')
    if answer == 'y':
        print('Access granted, enjoy our resource!')
    else:
        print('Goodbye!')
else:
    print('Sorry, only users 18 yo. and above are allowed to view this resource')
>>>>>>> сделал домашнее задание на уровне easy
