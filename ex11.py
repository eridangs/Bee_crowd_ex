x = float(input())
n = int(input())
e = 1
i = 1
while i <= n:
    if n == 0:
        fatorial = 1
        e += (x**0)/fatorial
    else:
        fatorial = 1
        for f in range(i+1):
            if f > 0:
                fatorial *= f
        print("fatorial",fatorial)
        print("i quando começa as operacoes",i)
        e += (x**i)/fatorial
        print(e)
    i+=1
print(f'{e:.4f}')