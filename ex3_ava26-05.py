def SomaMaiorConjunto(conjunto:list) -> int:
    soma = 0 #conjunto vazio
    Nconjunto = []
    for i in conjunto: #se tiver qualquer numero positivo soma
        if i > 0:
            soma += i
    return soma

def main():
    conjunto = list(map(int,input().split()))
    soma = SomaMaiorConjunto(conjunto)
    print(soma)

main()