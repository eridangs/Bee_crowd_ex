# 8. Caminho Mínimo em Matriz

n, m = map(int, input().split())

matriz = [[0]*m for _ in range(n)]

linha = 0
coluna = 0

totalpossibilidades = (n + m - 2)

for i in range(n):
    for j in range(m):
        matriz[i][j] = int(input())


for i in range(n):
    for j in range(m):
        print(matriz[i][j], end="   ")
    print("\n")


print(n,"\n", m)