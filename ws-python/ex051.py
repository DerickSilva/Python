n = int(input('Primeiro termo: '))
r = int(input('Razao: '))
decimo = n + (10 - 1) * r
for c in range(n , decimo + r, r):
    print(c)
