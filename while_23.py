'''
Найти НОД чисел используя алгоритм.
B != 0, НОД (A,B) = НОД (B,A mod(%) B)
B = 0, НОД (A,B) = A
'''

'''
Сравнить числа между собой и наибольшее из них заменить на
разность (?) наибольшего и наименьшего - так пишут в интернетах
в задаче- остаток от деления - ок ок ок ок ок
повторять пока числа не станут равны
'''
A = int(input('Enter: '))
B = int(input('Enter: '))

while not (A == B):
    A, B = B, A%B
print ('НОД: ', A)