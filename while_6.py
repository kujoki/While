
N = int(input('Enter: '))
k = 2
m = 1


if N%2 == 0: # если N - четное
    while not N < 2:
        m*=N
        N = N - k

elif N%2 == 1: # если N - нечетное
    while not N < 1:
        m*=N
        N = N - k
else:
    print ('Ошибка в расчетах')

print (m)

'''
Более простое решение

while not N<=2:
    m*=N
    N = N - 2
print (m)

N == 2?
N = N - k (k = 0)
k+=2
N == 2?
N = N - k
k+=2
N == 2? (с клавиатуры)
N = N - k
k+=2

m*=N (m = 1)
'''
