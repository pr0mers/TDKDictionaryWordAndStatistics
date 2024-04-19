from collections import Counter

with open('siralanmis_maddeler.txt', 'r', encoding='utf-8') as dosya:
    kelimeler = dosya.read().splitlines()


farkliharflerliste={}
ayniharflerliste={}

maxfarkliharf=0
maxayniharf=0

for kelime in kelimeler:
    farkliharfler = set()
    for harf in kelime:
        farkliharfler.add(harf)
    maxfarkliharf=max(maxfarkliharf,len(farkliharfler))
    if len(farkliharfler) not in farkliharflerliste:
        farkliharflerliste[len(farkliharfler)]=[kelime]
    else:
        farkliharflerliste[len(farkliharfler)].append(kelime)

    harfler=Counter(kelime)
    maxayniharf=max(maxayniharf,max(harfler.values()))
    if max(harfler.values()) not in ayniharflerliste:
        ayniharflerliste[max(harfler.values())]=[kelime]
    else:
        ayniharflerliste[max(harfler.values())].append(kelime)

print(f'Bir kelimedeki maksimum farklı harf sayısı {maxfarkliharf} ve kelimeler : ')
for i in farkliharflerliste[maxfarkliharf]:
    print(i)
print("")
print(f'Bir kelimedeki maksimum aynı harf sayısı {maxayniharf} ve kelimeler : ')
for i in ayniharflerliste[maxayniharf]:
    print(i)

