def percorre(N):
    word = input()
    lista = list(word)

    comprimento = len(lista) # guarda quantia de elementos
    newword = [''] * comprimento

    meio = int(len(lista)/2) - 1 # elemento que equivale a letra no meio da lista
    
    return organiza(newword,meio,lista,comprimento)
        
def organiza(newword:list,meio:int,lista:list,comprimento:int):
    i = 0
    while meio >= 0:
        newword[i] = lista[meio]
        meio -= 1
        i += 1
    while i < len(newword):
        newword[i] = lista[comprimento-1]
        comprimento -= 1
        i += 1
    return ''.join(newword)

def main():
    N = int(input())
    for _ in range(N):
        l = percorre(N)
        print(l)

main()