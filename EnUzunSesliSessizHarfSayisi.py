
sesli_harfler = "aâeıiîoöuüû"
sessiz_harfler = "bcçdfgğhjklmnprsştvyz"


with open('siralanmis_maddeler.txt', 'r', encoding='utf-8') as dosya:
    kelimeler = dosya.read().splitlines()


ardisiksesliliste = {}
ardisiksessizliste = {}
kelimemxsesliliste = {}
kelimemxsessizliste = {}

mxsesli=0
mxsessiz=0
kelimemxsesli=0
kelimemxsessiz=0

for kelime in kelimeler:
    sesliuzunluk=0
    ardisiksesli=0
    sessizuzunluk=0
    ardisiksessiz=0
    toplamsessiz=0
    toplamsesli=0
    
    for harf in kelime:
        if harf in sesli_harfler:
            toplamsesli+=1
            ardisiksesli+=1
            if ardisiksesli>sesliuzunluk:
                sesliuzunluk=ardisiksesli
        else:
            ardisiksesli=0
        if harf in sessiz_harfler:
            toplamsessiz+=1
            ardisiksessiz+=1
            if ardisiksessiz>sessizuzunluk:
                sessizuzunluk=ardisiksessiz
        else:
            ardisiksessiz=0

    mxsesli=max(mxsesli,sesliuzunluk)
    kelimemxsesli=max(kelimemxsesli,toplamsesli)
    
    if sesliuzunluk not in ardisiksesliliste:
        ardisiksesliliste[sesliuzunluk]=[kelime]
    else:
        ardisiksesliliste[sesliuzunluk].append(kelime)

    if toplamsesli not in kelimemxsesliliste:
        kelimemxsesliliste[toplamsesli]=[kelime]
    else:
         kelimemxsesliliste[toplamsesli].append(kelime)
    
    mxsessiz=max(mxsessiz,sessizuzunluk)
    kelimemxsessiz=max(kelimemxsessiz,toplamsessiz)
    if sessizuzunluk not in ardisiksessizliste:
        ardisiksessizliste[sessizuzunluk]=[kelime]
    else:
        ardisiksessizliste[sessizuzunluk].append(kelime)

    if toplamsessiz not in kelimemxsessizliste:
        kelimemxsessizliste[toplamsessiz]=[kelime]
    else:
         kelimemxsessizliste[toplamsessiz].append(kelime)
    

print(f'Bir kelimedeki maksimum ardışık sesli harf sayısı {mxsesli} ve kelimeler : ')
for i in ardisiksesliliste[mxsesli]:
    print(i)
print("")
print(f'Bir kelimedeki maksimum sesli harf sayısı {kelimemxsesli} ve kelimeler : ')

for i in kelimemxsesliliste[kelimemxsesli]:
    print(i)
print("")
print(f'Bir kelimedeki maksimum ardışık sessiz harf sayısı {mxsessiz-1} ve kelimeler : ') # Maksimum aslında 6 ama kelime dzfgdf yani gerçek kelime olmadığından 1 eksiği
for i in ardisiksessizliste[mxsessiz-1]:
    print(i)
print("")
print(f'Bir kelimedeki maksimum sessiz harf sayısı {kelimemxsessiz} ve kelimeler : ')
for i in kelimemxsessizliste[kelimemxsessiz]:
    print(i)
    
 

