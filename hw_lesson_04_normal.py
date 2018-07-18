# Эти задачи необходимо решить используя регулярные выражения!
 
# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры,
# потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.

# import re
#
# user_name = input('Your name: ')
# user_surname = input('Your surname: ')
# user_mail = input('Your mail address: ')
#
# names_pattern = '^[A-Z][a-z]+'
# surnames_pattern = '^[A-Z][a-z]+'
# mail_pattern = '^[a-z_0-9]+@[a-z0-9]+\.(ru|org|com)$'
#
# search_name = re.search(names_pattern, user_name)
# search_surname = re.search(surnames_pattern, user_surname)
# search_mail = re.search(mail_pattern, user_mail)
#
# if search_name == None:
#     print('Name not correct, should begin with capital letter and contain only letters')
# else:
#     print('Name correct')
# if search_surname == None:
#     print('Surname not correct, should begin with capital letter and contain only letters')
# else:
#     print('Surname correct')
# if search_mail == None:
#     print('Mail not correct, letters, numbers, one dot, @ are allowed, should not contain other special symbols')
#     print('also allowed domains ru, com, org only')
# else:
#     print('Mail correct')


# Задача - 2:
# Вам дан текст:
 
some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''
 
# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!

import re

# search_string = '[\.][\.][\.]'  # first variant
search_string = "\.{3}"  # but this one i like more
search_result = re.search(search_string, some_str)

if search_result == None:
     print('sequence of ... not found')
else:
     print('there is sequence of ... in that text')