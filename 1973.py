def somacarneiros(N_fazendas: int,carneiros:list):
    if len(carneiros) == 1: # quando só tem 1 fazenda
        total = carneiros[0]
    else:
        total = 0
        i = 0
        while i < N_fazendas:
            total += carneiros[i]
            i += 1
    return total


def roubocarneiros(N_fazendas:int, lista:list):
    if len(lista) == 1: # quando só tem 1 fazenda
        carneirosroubados = 1
        fazendasroubadas = 1
    else: #mais de 1 fazenda e necessita verificação se é impar ou par
        carneirosroubados = 0
        fazendasroubadas = 0
        for i in range(N_fazendas):
            if lista[i] % 2 != 0: #carneiros em numero impar
                fazendasroubadas += 1
                carneirosroubados += 1
            else:  #carneiros em numero par
                fazendasroubadas += 1
                if lista[0] != 1:
                    carneirosroubados += 1
                for j in range(i-1,-1,-1):
                    carneirosroubados += 1
                break
    return fazendasroubadas, carneirosroubados


def main():
    N_fazendas = int(input())
    lista_n_carneiros = list(map(int,input().split()))
    total = somacarneiros(N_fazendas,lista_n_carneiros)
    fazendas, carneiros = roubocarneiros(N_fazendas,lista_n_carneiros)
    print(f'{fazendas} {total-carneiros}')

main()