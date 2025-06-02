def somapolinomio(coeficientes: list) -> float:
    n = 0
    p = 0
    x = float(input())
    while n < len(coeficientes):
        a = coeficientes[n]
        p += a * (x ** n)
        n += 1
    return p

def main():
    coeficientes = list(map(float,input().split()))
    k = int(input())
    for _ in range(k):
        p = somapolinomio(coeficientes)
        print(f'{p:.4f}')

main()