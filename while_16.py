




'''
s>200?
k = k * p
s = s + k
k_d = k_d + 1

s>200?
k = k * p
s = s + k
k_d = k_d + 1

s>200?
k = k * p
#не подойдет
s = s + k
k_d = k_d + 1


10 + 1.5*10 + 1.5*1.5*10 + ...
'''
s = 10
p = (float(input('Enter: ')))/100 + 1
print (p)
k_d = 1
k = 10

# если я комментирую %1 и %2, то все ломается
while not s>200:
    k*=p
    print (k)# %1
    s+=k
    print ('пробег: ',s) # %2
    k_d+=1
print ('Количество дней: ',k_d)
print ('Пробег: ',s)
