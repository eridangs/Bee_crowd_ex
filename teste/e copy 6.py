# 6. Matriz Espiral
matriz = [[1,2,3],[4,5,6],[7,8,9]]

linha = 0
coluna = 0
linhaf = len(matriz)
colunaf = len(matriz[0])

for _ in range(len(matriz)):
    for i in range(linha, linhaf):
        for j in range(coluna, colunaf):
            print(matriz[i][j])
        coluna = j

    
    linha = 2
