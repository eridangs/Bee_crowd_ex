binario = int(input())

decimal = 0

expoente = 0

while binario !=0:
    testes = binario % 10
    binario //= 10
    
    decimal += (testes*2**expoente)
    
    expoente += 1
print(decimal)