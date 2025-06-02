# maiuscula 65-90 minuscula 97-122
def contagem(letras_que_aparecem):
    codM = 65
    while codM <= 90:
        qtde = 0
        for i in letras_que_aparecem:
            if i == codM:
                qtde += 1
        if qtde > 0:
            print(f'{chr(codM)}: {qtde}')
        codM += 1

def alfabeto(frase:list) -> list: # tranforma todas as letras em codigos maiusculos
    letras_que_aparecem = []
    for i in range(len(frase)):
        codnumerico = ord(frase[i])
        if codnumerico >= 65 and codnumerico <= 90 or codnumerico >= 97 and codnumerico <= 122:
            if codnumerico >= 97 and codnumerico <= 122:
                codnumerico -= 32
            letras_que_aparecem.append(codnumerico)

    return letras_que_aparecem

def main():
    frase = list(input())
    codigos = alfabeto(frase)
    contagem(codigos)

main()