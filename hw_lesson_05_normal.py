# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

from hw_lesson_05_easy import view_current_directory
from hw_lesson_05_easy import make_folder
from hw_lesson_05_easy import remove_folder

while True:
    try:
        choice = int(input('Make your choice:\n'
                           '---------------------\n'
                           '1. Change directory\n'
                           '2. View directory content\n'
                           '3. Make new directory\n'
                           '4. Delete directory\n'
                           '5. Quit\n'
                           '---------------------\n'
                           'Your choice:'))
        if choice == 1:
            def change_folder():
                '''Change directory by user input'''
                import os
                current_dir = os.getcwd()
                print('Current directory is: ', current_dir)
                try:
                    changed_dir = str(input('Directory to go: '))
                    os.chdir(changed_dir)
                    print('Changed directory to', changed_dir)
                except FileNotFoundError:
                    print('File or directory not exist')
                except NotADirectoryError:
                    print('Must be a directory')
            change_folder()
        elif choice == 2:
            view_current_directory()
        elif choice == 3:
            make_folder()
        elif choice == 4:
            remove_folder()
        elif choice == 5:
            break
        else:
            print('Please make your choice according to options given')
    except ValueError:
        print('Please insert number')
    # except KeyboardInterrupt:                     # не уверен, что нужно
    #     print('Aborted by user: CTRL+C interrupt')
