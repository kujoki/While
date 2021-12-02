

k = 0
fin = 1000
p = (int(input('Enter p: ')))/100

while not fin>1100:
    fin += fin*p
    k+=1

print ('Сумма вклада: ', fin)
print ('Число месяцев: ', k)
