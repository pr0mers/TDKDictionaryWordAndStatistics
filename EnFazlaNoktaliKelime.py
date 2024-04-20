with open('siralanmis_maddeler.txt', 'r', encoding='utf-8') as dosya:
    kelimeler = dosya.read().splitlines()
    
noktasayilari = {}
mx=0
for kelime in kelimeler:
    nokta=0
    for harf in kelime:
        if harf in "çijşğ": # ğ de 1 nokta var diye saydım, zaten maksimumu değiştirmiyor
            nokta=nokta+1
        elif harf in "öü":
            nokta=nokta+2
    mx=max(mx,nokta)
    if nokta not in noktasayilari:
        noktasayilari[nokta] = [kelime]
    else:
        noktasayilari[nokta].append(kelime)

for sayi in noktasayilari:
    print(str(sayi)+ " " + str(len(noktasayilari[sayi])))
