with open('zadania maturalne\instrukcje.txt', 'r') as f:
    lines = [x.rstrip() for x in f]

txt = []
for i in lines:
    slowo = i.split(' ')
    if slowo[0] == 'DOPISZ':
        txt.append(slowo[1])
    elif slowo[0] == 'ZMIEN':
        txt.pop()
        txt.append(slowo[1])
    elif slowo[0] == 'USUN':
        txt.pop()
    elif slowo[0] == 'PRZESUN':
        if slowo[1] in txt:
            indeks = txt.index(slowo[1])
            if ord(slowo[1]) == 90:
                txt[indeks] = 'A'
            else:
                txt[indeks] = chr(ord(slowo[1])+1)
                
print(txt)
print('zad1 ', len(txt))
 
lista = [x.split()[0] for x in lines]
ciag = [lista[i] for i in range(1,len(lista)-1,+1) if lista[i+1] == lista[i]]
print('zad2 ', ciag[0], len(ciag))
lista1 = [x.split(' ')[1] for x in lines if x.split(' ')[0] == 'DOPISZ']
naj = [lista1.count(i) for i in lista1]
print('zad3 ', sorted(dict(zip(lista1, naj)).items(), key=lambda x: x[1])[-1])
napis = ''
for i in txt:
    napis += i
print('zad4 ', napis)

