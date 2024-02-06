txt = open('przyklad.txt', 'r').read().strip('\n')
lista = []
lista = txt.split('\n')
wybrane = [lista[i] for i in range(39, len(lista), 40)]
for i in wybrane:
    print(i[9], end='')