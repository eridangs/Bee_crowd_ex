N = int(input())
for _ in range(N):
    num = int(input())
    string = str(num)
    leds = 0
    for caracter in string:
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
    print(leds)

def main():
    