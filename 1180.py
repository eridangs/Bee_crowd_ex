def DescobreMenor(N:int,l:list):
    menor = l[0]
    posicao = 0
    for i in range(N):
        if l[i] < menor:
            menor = l[i]
            posicao = i
    return menor, posicao

def Main():
    N = int(input())
    l = list(map(int,input().split()))
    menor,posicao = DescobreMenor(N,l)
    print(f"Menor valor: {menor}\nPosicao: {posicao}")

Main()