def dancar(frase:str) -> str:
    l = list(frase)

    maiuscula = True
    for i in range(len(l)):
        if l[i] != " ":
            cod = ord(l[i])
            if maiuscula:
                if cod >=97 and cod <= 122:
                    l[i] = chr(cod - 32)
                maiuscula = False
            else:
                if cod >= 65 and cod <= 90:
                    l[i] = chr(cod + 32)
                maiuscula = True

    return "".join(l)

def main():
    while True:
        try:
            frase = input()
            d = dancar(frase)
            print(d)
        except EOFError:
            break
main()