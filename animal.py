filo = input()
subclasse = input()
habito = input()

if filo == "vertebrado":
    if subclasse == 'ave':
        if habito == 'carnivoro':
            animal = 'aguia'
        else:
            animal = 'pomba'
    else:
        if habito == 'onivoro':
            animal = 'homem' 
        else:
            animal = 'vaca'       
else:
    if subclasse == "inseto":
        if habito == 'hematofago':
            animal = 'pulga'
        else:
            animal = 'lagarta'
    else:
        if habito == 'hematofago':
            animal = 'sanguessuga'
        else:
            animal = 'minhoca'

print(animal)