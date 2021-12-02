

k = 0
fin = 1000
p = (int(input('Enter p: ')))/100 + 1

while not fin>1100:
    fin*=p
    k+=1

print ('Сумма вклада: ', fin)
print ('Число месяцев: ', k)
