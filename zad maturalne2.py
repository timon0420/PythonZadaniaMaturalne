txt = open('sygnaly.txt', 'r').read().strip('\n')
slowa = []
slowa = txt.split('\n')
szukana = max(slowa,key = lambda x: len(set(x)))
print(szukana, len(set(szukana)))

