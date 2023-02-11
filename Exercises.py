# 2. Добавить слово в конец списка так, чтобы каждая буква стала отдельным элементом списка
# l = [1, 2, 3]
# a = 'abc'
# result = [1, 2, 3, 'a', 'b', 'c']

#Цикл.
# l = [1, 2, 3]
# b = 'abc'
# for i in b:
#     l.append(i)
# print(l)


# Variant A.
# l = [1, 2, 3]
# a = 'abc'
# result = l + list(a)
# print(result)

# Variant B.
# l = [1, 2, 3]
# a = 'abc'
# a = list(a)
# l.append(a)
# print(l)

# Variant C.
# l = [1, 2, 3]
# a = 'abc'
# a = list(a)
# l.extend(a)
# print(l)

# Variant D.
# l = [1, 2, 3]
# a = 'abc'
# l.extend(list(a))
# print(l)

# Variant E.
# l = [1, 2, 3]
# a = 'abc'
# l.append(list(a))
# print(l)

# Variant F.
# l = [1, 2, 3]
# b = 'abc'
# l += b
# print(l)


# 3. Все чётные числа вывести в другой список
# l = [1,3,4,5,8,9,10,44,22,50,79,54,28,91]
# c = []
# for i in l:
#     if i % 2 == 0:
#         c.append(i)
# print(c)

# 4. Все emails у которых есть слово test вывести в другой список
# l = ['webtest1@gmail.com',
#      'alex_dr5@gmail.com',
#      'elena_viktorovna@gmail.com',
#      'infotest@gmail.com',
#      'sigmatesst@gmail.com',
#      'planet.dollsatest@gmail.com',
#      'loadtestsinfo@gmail.com',
#      'straightwaytest@gmail.com',
#      'test.of.tests@gmail.com',
#      'bigmac@gmail.com',
#      'bigmactest@gmail.com',
#      'kfc_test_supply@gmail.com',
#      'cyberdesk@gmail.com',
#      'supportonlinetest@gmail.com'
#      ]
# f = []
# for i in range(len(l)):
#     if l[i].find('test') != -1:
#          f.append(l[i])
# for j in f:
#      print(j)


# Variant B.
# f = []
# for i in range(len(l)):
#     if 'test' in l[i]:
#         f.append(l[i])
# print(f)

# Variant C.
# f = []
# for i in l:
#     if 'test' in i:
#         f.append(i)
# print(f)

# найти самое маленькое число в списке
# l = [3,0,4,5,8,9,10,44,22,50,-1,79,54,-28,91]

# Variant A.
# min = l[0]
# for i in range(-1, len(l)):
#     if l[i] < min:
#         min = l[i]
# print(min)

# Variant B.
# min = l[0]
# for i in l:
#     if i < min:
#         min = i
# print(min)

# Variant C.
# print('min', min(l))

# 6. Сравнить 2 строки без учёта регистра
# ==============================

# s1 = 'alexander'
# s2 = 'aleXaNdEr'
# if s1.lower() == s2.lower():
#      print(True)
# else:
#      print(False)

# Variant B.
# s1 = 'alexander'
# s2 = 'aleXaNdEr'
# print(s1.lower() == s2.lower())

# 7. Проверить является ли массив подмножеством другого массива
# l1 = [1,4,6]
# l2 = [9,5,1,10,4,33,2,6,0,8]
# c = 0
# for i in l1:
#      if i in l2:
#           c +=1
# if c == len(l1):
#      print(True)
# else:
#      print(False)


# 8. Напишите функцию, которая принимает строку и
# возвращает количество букв английского алфавита,
# которые встречаются больше чем 1 раз.
# l = 'attachment and results'
# abc = 'Aabcdefghjklmnopqrstuxwvz'
# for i in abc:
#      count = 0
#      for j in l:
#         if j == i:
#             count += 1
#      if count > 1:
#         print(i,'встречается', count, 'раз')

# 9. Напишите функцию, которая принимает строки.
# Она должна вернуть False, если в строке содержится две одинаковые буквы,
# а если таких слов нет — True.

# no_duplicate_letters("Здравствуйте, Александра") ➞ False
# Две в в «Здравствуйте», три a в «Александра».

# no_duplicate_letters("Всегда дожимай до конца") ➞ True
# Две в в «Здравствуйте», три a в «Александра».
# l = ("Здравствуйте, Александра")
# p = ("Всегда дожимай до конца")
# def foo(string):
#     return len(set(string)) == len(string)
# print(foo('test'))
# print('tes')

#10. Напишите функцию, которая проверяет сложность пароля. Функция проверяет ряд условий и оценивает сложность пароля. За каждое выполненое условие пароль получает бал.
#
# Если выполняется одно условие - функция возвращает 1, если выполненяется 5 условий - функция вернет 5.
#
# Условия которые нужно проверить:
#
# длина пароля не меньше 6 символов,
# пароль содержит хотя бы 1 цифру,
# пароль содержит хотя бы одну заглавную букву,
# пароль содержит хотя бы одну строчную букву,
# пароль содержит хотя бы один из специальных символов: !@#$%^&*()-+
#
# Типы символов, которые будут содержаться в пароле во время тестирования:

# numbers = "0123456789"
# lower_case = "abcdefghijklmnopqrstuvwxyz"
# upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# special_characters = "!@#$%^&*()-+"

# Пароль не должен содержать кириллических символов

# def check_password(password):
#     scores = 0
#     count_digit = 0
#     count_upper = 0
#     count_lower = 0
#     count_spec = 0
#     for s in password:
#         if s.isdigit():
#             count_digit += 1
#
#         if s.isupper():
#             count_upper += 1
#
#         if s.islower():
#             count_lower += 1
#
#         if s in "!@#$%^&*()-+":
#             count_spec += 1
#     if count_digit>=1 and count_upper>0 and count_lower>0 and count_spec>0 \
#         and len(password)>=6:
#
#         print("Strong password")
#     elif count_digit<1 and count_upper>0 and count_lower>0 and count_spec>0 \
#          and len(password)>=6:
#          print('No numbers')
#     elif count_digit>=1 and count_upper==0 and count_lower>0 and count_spec>0 \
#          and len(password)>=6:
#          print('No uppercase letter')
#     elif count_digit<1 and count_upper>0 and count_lower==0 and count_spec>0 \
#          and len(password)>=6:
#          print('No lowercase letter')
#     elif count_digit>= 1 and count_upper>0 and count_lower>0 and count_spec==0 \
#          and len(password)>=6:
#          print('No symbol')
#
# check_password('Qqwe1qwa!')


# password = input('Enter password: ')
# scores = 0
#
# digit = 0
# upper = 0
# lower = 0
# symbol = 0
#
# if len(password) >= 6:
#    scores += 1
# else:
#     print('Password too short')
#     for i in password:
#         if i.isdigit():
#             digit += 1
#         if i.isupper():
#             upper += 1
#         if i.islower():
#             lower += 1
#         if i in "!@#$%^&*()_+=-":
#             symbol += 1
# if digit > 0:
#     scores += 1
# if upper > 0:
#     scores += 1
# if lower > 0:
#
#     scores += 1
# if symbol > 0:
#     scores += 1
# print(scores)


# def check_items(password):
#     if set(password).intersection('а-яёА-ЯЁ'):
#         return('wrong letters')
#
#     score = 1 if len(password) >= 6 else 0
#     check_item_list = ['0123456789', 'ASDFGHJKLQWERTYUIOPZXCVBNM', 'qwertyuiopasdfghjklzxcvbnm', '!@#$%^&*()_+{}|\][:",./?><']
#
#     for item in check_item_list:
#         if set(password).intersection(item):
#          score += 1
#          return score


def check_password(password):
    # password = input('Введите пароль:')
    digits = '1234567890'
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    symbols = '!@#$%^&*()-+'
    acceptable = digits + upper_letters + lower_letters + symbols

    passwd = set(password)
    if any(char not in acceptable for char in passwd):
        print('Ошибка. Запрещенный спецсимвол')
    else:
        recommendations = []
        if len(password) < 12:
            recommendations.append(f'увеличить число символов - {12 - len(password)}')
        for what, message in ((digits, 'цифру'),
                              (symbols, 'спецсимвол'),
                              (upper_letters, 'заглавную букву'),
                              (lower_letters, 'строчную букву')):
            if all(char not in what for char in passwd):
                recommendations.append(f'добавить 1 {message}')

        if recommendations:
            print("Слабый пароль. Рекомендации:", ", ".join(recommendations))
        else:
            print('Сильный пароль.')


# tests
for test in ("qwety", "Qwert_Y", "Q123wer123tY", "A^B@C*D", "@PowerRangers123@"):
    print("Password:", test)
    check_password(test)
    print(test)