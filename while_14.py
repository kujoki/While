

N = int(input('Enter: '))
k = 1
s = 0

while not s>N:
    s+=1/k
    k+=1

k-=1
s-=1/k
k-=1

print ('Сумма: ', s)
print ('Число слагаемых: ', k)
