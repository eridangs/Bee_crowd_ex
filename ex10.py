x = float(input())
k = int(input())
cos = 1
operacao = False
i = 1
while i <= k:
    if k == 0:
        fatorial = 1
        cos -= (x**0)/fatorial
    elif i >= 2 and i % 2 == 0:
        fatorial = 1
        for n in range(i+1):
            if n > 0:
                fatorial *= n
        print("fatorial",fatorial)
        print("i quando começa as operacoes",i)
        if operacao == False:
            cos -= (x**i)/fatorial
            operacao = True
        else:
            cos += (x**i)/fatorial
            operacao = False
        print("cos",cos)
    i+=1
print(f'{cos:.4f}')