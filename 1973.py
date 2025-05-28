N = int(input())
Ncarneiros = list(map(int,input().split()))
caminho = True
total = 0
carneirosroubados = 0
fazendasroubadas = 0

for n in range(N):
    total += Ncarneiros[n]

for i in range(N):
    if Ncarneiros[i] % 2 != 0:
        fazendasroubadas += 1
    else:
        fazendasroubadas += 1
        for j in range(len(Ncarneiros)-1,-1,-1):
            print(Ncarneiros[j])
        break
print(fazendasroubadas, '',total-carneirosroubados)