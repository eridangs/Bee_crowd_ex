# 7. Contagem de Palavras Únicas

entrada = input()
entrada = list(entrada.split(" "))
palavrasunicas = []

for palavra in range(len(entrada)):
    palavranova = entrada[palavra].lower()
    if palavranova not in palavrasunicas:
        palavrasunicas.append(palavranova)

print(len(palavrasunicas))