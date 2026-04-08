# 1. Número Primo Otimizado

n = int(input())
primo = True
if n <= 1:
    primo = False
if n == 2:
    primo = True
if n % 2 == 0:
    primo = False
i = 3
while i < n:
    if n % i == 0:
        primo = False
    i += 2

if primo == True:
    print("É primo")
else:
    print("Não é primo")