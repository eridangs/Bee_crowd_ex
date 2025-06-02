def possibilidades(faces:list,N:int) -> list:
    lados = [0] * 14

    for j in faces:
        if j >= 1 and j <= 13: #se o numero estiver dentro do intervalo 1-13
            lados[j] += 1 #adiciona 1 a ele dentro de lados na posição[1-13]

    for i in range(1,len(lados)):
        lados[i] = (lados[i] * 100) / N
    
    return lados
    

def main():
    N = int(input())
    faces = list(map(int,input().split()))
    lados = possibilidades(faces,N)
    for i in range(1,14):
        print(f'Face {i}: {lados[i]:.2f}%')

main()
