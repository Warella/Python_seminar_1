"""
Задача 8: Требуется определить, 
можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).
*Пример:*
3 2 4 -> yes
3 2 1 -> no
"""
print('Введите длину шоколадки: ')
n = int(input())
print('Введите ширину шоколадки: ')
m = int(input())
print('Введите количество долек: ')
k = int(input())
# Количество долек будет равно одному из чисел m и n, либо m*x, где х<=n, либо n*x, где х<=m
if k < m * n and ((k % m == 0) or (k % n == 0)):
    print(f"{n} {m} {k} -> yes")
else:
    print(f"{n} {m} {k} -> no")