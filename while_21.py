'''
Целое число. Определить есть ли в записи нечетные цифры.
Есть - True. Нет - False.
'''


n = int (input('Enter: '))
## См while_20
k = 0
    
while n>0:
   if n%2 == 1: #проверка на нечетность
       k+=1
   else:
        None
   n = n//10

print (k>=1)
'''
if k>=1:
    print (True)
else:
    print (False)
'''
