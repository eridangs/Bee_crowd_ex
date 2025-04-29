decimal = int(input())

binario = 0

base = 0
resto = 0

while decimal != 0:
    resto = decimal % 2
    decimal //= 2
    binario += resto * (10**base)
    base += 1

print(binario)