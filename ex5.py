primo = int(input())
i = 2
r = False
if primo == 2:
    print("Primo")
else:
    while i < primo:
        if primo % i == 0:
            r = True
        i += 1
    if r:
        print("Composto")
    else:
        print("Primo")
