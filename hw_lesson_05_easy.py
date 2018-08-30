# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# import os
# user_dir = os.getcwd() # just defining our current directory path
# print('your current directory is: ', user_dir)

def make_folders():
    '''Make folders with names dir_1 to dir_9 in current folder'''
    import os
    dir_name = 'dir'
    for dir in range(0,9):
            new_dir = "{}_{}".format(dir_name, str(dir + 1))
            os.mkdir(new_dir)
make_folders()

def remove_folders():
    '''Deletes folder with names dir_1 to dir_9 from current folder'''
    import os
    dir_name = 'dir'
    for dir in range(0, 9):
        new_dir = "{}_{}".format(dir_name, str(dir + 1))
        os.rmdir(new_dir)
remove_folders()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def view_current_directory():
    '''View sorted content of current folder'''
    import os
    content_list = sorted(os.listdir(os.curdir))
    for items in content_list:
        print(items.format(dir))
view_current_directory()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def file_copy():
    '''Makes copy of a file from which this function runs'''
    import os
    file_name = os.path.basename(__file__)
    print (__file__)
    os.system("cp {} {}".format(file_name, file_name + '_copy'))
file_copy()

# function for hw_lesson_05_normal
def make_folder():
    '''Make single folder in current folder'''
    try:
        import os
        dir_name = str(input('New folder name: '))
        os.mkdir(dir_name)
        print('Folder created', dir_name)
    except ImportError:
        print('Module to import not found')
    except OSError:
        print('System error, try to contact system administrator')
    except IOError:
        print('I/O error, try to contact system administrator')

# function for hw_lesson_05_normal
def remove_folder():
    '''Deletes single folder in current folder'''
    try:
        import os
        dir_name = str(input('Folder name to delete: '))
        os.rmdir(dir_name)
        print('Folder removed', dir_name)
    except ImportError:
        print('Module to import not found')
    except OSError:
        print('System error, try to contact system administrator')
    except IOError:
        print('I/O error, try to contact system administrator')

# function for hw_lesson_05_normal
# def change_folder():
#     '''Change directory by user input'''
#     import os
#     current_dir = os.getcwd()
#     print('Current directory is: ', current_dir)
#     changed_dir = str(input('Directory to go: '))
#     os.chdir(changed_dir)
#     print('Changed directory to', changed_dir)
# change_folder()
# почему-то не работает из этого файла, пришлось вставить в normal напрямую