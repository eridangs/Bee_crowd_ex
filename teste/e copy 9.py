# 9. Anagrama

p1 = input()
p2 = input()
p1 = list(p1)
p2 = list(p2)
anagrama = True

if len(p1) != len(p2):
    anagrama = False

if p1[0] != p2[-1]:
    anagrama = False

tamanhop2 = len(p2) - 1
tamanhop1 = 0

while anagrama != False and tamanhop1 < len(p1):
    if p1[tamanhop1] != p2[tamanhop2]:
        anagrama = False

    tamanhop1 += 1
    tamanhop2 -= 1

if anagrama != True:
    print("Não é anagrama")
else: print("É anagrama")