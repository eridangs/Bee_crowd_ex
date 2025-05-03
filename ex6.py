n = int(input())
if n < 0:
    n *= (-1)
subnumero = 0
expoente = 1
tem_par = False

while n > 0:
    digitos = n%10
    n = n//10

    if digitos % 2 == 0:
        subnumero += digitos * expoente
        expoente*= 10
        tem_par = True

if tem_par == True:
    print(subnumero)
else:
    print(0)

# print(f'digitos',digitos)
# print(f'numero individual a ser analisado',digitos)
# print(f'numero que sera somado no prox loop', subnumero)
    # print(f'resultado com a quantidade de casas igual a quantidade de numeros pares', subnumero)