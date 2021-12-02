'''
Дано вещественное число.
Последовательность
1, 2, (1 + 2*2)/3...
Найти(наим)порядковый номер, для которого разность между текущим и
предшествующим больше вещественного числа
Вывести порядковый номер, предшествующее и текущее число
'''

a = 1 #- предшеств 
b = 2  #- текущее 
k = 2 #- порядковый номер = 3
c = (a + 2*b)/3
N = float(input('Enter: '))

while not (abs(c-b) < N):
    a = b
    print ('a: ',a)
    b = c
    print ('b: ',b)
    c = (a + 2*b)/3
    print ('c: ',c)
    k+=1

print ('Порядковый номер: ',k)
print ('Текущее значение: ',b)
print ('Предшествующее значение: ',a)