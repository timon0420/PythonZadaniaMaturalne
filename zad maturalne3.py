plik = open('przyklad.txt', 'r')
def spr(linia):
    for litera1 in linia:
        for litera2 in linia:
            if abs(ord(litera1) - ord(litera2)) > 10:
                return
    print(linia)
for linia in plik:
    spr(linia[:-1])
