'''
Найти первое число Фибоначчи больше N
F_1 = 1
F_2 = 1
F_3 = F_1 + F_2
F_4 = F_2 + F_3
1 1 2 3 5 8 13 21 34 55 89...
'''
a = 1
b = 1
c = 2 #оговорка 0 и 1 тоже числа Фибоначчи, их нужно вставить в конец
N = int (input('Enter: '))
while c < N:
    a = b
    b = c
    c = a + b

a = b
b = c
c = a + b

print (c)
