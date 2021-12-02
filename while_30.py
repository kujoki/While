



A = int(input('Enter A: '))
B = int(input('Enter B: '))
C = int(input('Enter C: '))
k = 0
#n = 0

#while not B<C or A<C:
while  B>=C and A>=C:
    B = B - C
    A = A - C
    k+=1
'''
while not A<C:
    A = A - C
    n+=1

if k>=n:
    print ('Число квадратов: ', n)
else:
'''
print ('Число квадратов: ', k)

## i = 0
## while i<A:
##     j = 0
##     while j<B:
##         k += 1
##         j += C
##     i += C
## print(k)
