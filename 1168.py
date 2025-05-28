def Somador(N:int,lista:list):
    for i in range(N):
        num = input()
        leds = 0
        for caracter in num:
            if caracter == "1":
                leds += 2
            elif caracter == "7":
                leds += 3
            elif caracter == "4":
                leds += 4
            elif caracter == "8":
                leds += 7
            elif caracter == "2" or caracter == "3" or caracter == "5":
                leds += 5
            elif caracter == "6" or caracter == "9" or caracter == "0":
                leds += 6
        lista[i] = leds

def main():
    N = int(input())
    lista = [0] * N
    Somador(N,lista)
    for i in range(N):
        print(f'{lista[i]} leds')

main()