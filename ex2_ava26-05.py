def realcoeficiente(coeficientes:list):
    n = 0
    while n < len(coeficientes):
        for a in coeficientes:
            if n <= 1:
                a = a * (1 ** n)
            else:
                a = a * n
            
            coeficientes[n] = a

            n += 1

def main():
    coeficientes = list(map(float,input().split()))
    realcoeficiente(coeficientes)
    for i in range(1,len(coeficientes)):
        print(f'{coeficientes[i]:.4f}')

main()
