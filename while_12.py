
N = int(input('Enter: '))
k = 1
s = 0



while s<N or s == N:
    s = s + k
    k+=1
    #print ('Число слагаемых: ',k)
    #print ('Сумма: ',s)

k-=1
s-=k # те же действия в обратном порядке для отката
k-=1 # когда условия перестают меня-ся откат на 3 действия
print ('Сумма: ',s)
print ('Число слагаемых: ',k)


'''
k+=1
s+=k
s<N?

k+=1
s+=k
s<N?

k+=1
s+=k
s<N?


s = 0 #1
k = 1 #2
s<N?
s+=k
k+=1

'''