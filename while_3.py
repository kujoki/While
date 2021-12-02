
N = int(input('Enter N: '))
k = int(input('Enter k: '))

s = 0

while not N<k:
    s+=1
    N = N - k

print ('Остаток',N)
print ('Частное',s)
