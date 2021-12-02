'''
Дано целое число. Если число является простым (делители n и 1) True.
'''

N = int(input('Enter: '))
A = N - 1
k = 0
'''
N/2 - целое?
print (True)
N/3 - целое?

проверка на целое
'''

## Переписать
while A>1:
    if N%A == 0:
        k += 1
    else:
        None
    print (A,'',N/A)
    A-=1

print (k == 0)
'''
if k == 0:
    print (True)
else:
    print (False)
'''
