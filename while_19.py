

# счетчик
N = int(input('Enter: '))
A = N
k = 0 # счетчик цифр

while A>0: # находим количество цифр
    A = A//10
    k+=1

d = 1

while k>0: 
    d*=10
    k-=1
    
d = d/10 # соответствует числу !наибольшему порядку! разрядов  
s = 0

while N>0:
    f = N%10
    #print (f,end = " ")
    s+=f*d
    d = d/10
    N = N//10

print (s)


## N = int(input('Enter: '))
## A = N
## B = 0
## 
## while A>0: 
##     B = B*10 + A%10
##     A = A//10
## print(B)

