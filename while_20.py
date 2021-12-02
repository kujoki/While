'''
Дано целое число. Определить есть ли в записи числа цифра 2.
Если есть True, если нет False
'''



'''
n%10 == 2?
print (True)
else
n = n // 10

n%10 == 2?
print (True) # k+=1
else
n = n // 10
'''
n = int (input('Enter: '))
## пускай, нет цифры 2
## k = False
k = 0
    
while n>0:
   ## Если все-таки есть хотя бы одна:
   if n%10 == 2:
       ## Значит есть
       ## k = True
       k+=1
   n = n//10

## Что спрашивали, то и выводим
## print(k)
print (k>=1)
'''
if k>=1:
    print (True)
else:
    print (False)
'''
