codigo, quantia = map(int, input().split())
hot_dog = 4.00
x_sal = 4.5
x_bac = 5.00
torrada = 2
refri = 1.50
if codigo == 1:
    valor = hot_dog
    valor *= quantia
elif codigo == 2:
    valor = x_sal
    valor *= quantia
elif codigo == 3:
    valor = x_bac
    valor *= quantia
elif codigo == 4:
    valor = torrada
    valor *= quantia
elif codigo == 5:
    valor = refri
    valor *= quantia
print(f'Total: R$ {valor:.2f}')