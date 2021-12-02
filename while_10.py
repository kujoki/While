

N = int(input('Enter: '))
s = 1
k = 0
while s<N:
    k+=1
    s = 3**k 

print (k-1)


'''
переход в конец, поменять начальные условия

x = int(input('Enter: '))
h = int(input('Enter: '))
m = int(input('Enter: '))
h+=x//60
m+=x%60
if m >= 60:
    h+=1
    m-=60
print ('Hours:',h)
print ('Minutes:',m)
'''
