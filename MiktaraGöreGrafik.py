import matplotlib.pyplot as plt

turkce_alfabe = "aâbcçdefgğhıiîjklmnoöprsştuüûvyz"

with open("KelimeSubstrleri.txt", "r", encoding="utf-8") as dosya: # Dosyadan "a" : kullanılma miktarı, "b" : kullanılma miktarı, gibi çekiyorum
    satirhepsi = dosya.readlines()

liste = {}
birinci = []
ikinci = []
for satir in satirhepsi:
    kelime, sayi = satir.strip().split(":") # Kelime ve miktarı diye ayırıyorum
    liste[kelime] = int(sayi)
    if kelime in turkce_alfabe and len(kelime)==1:
        birinci.append(kelime)
        ikinci.append(int(sayi))


plt.figure(figsize=(15, 9)) # Sütun grafiği ayarlıyorum
bars = plt.bar(birinci, ikinci, color='skyblue')


for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), fontsize=8 , va='center', ha='center') # Sayı ve harflerin kaymaması için ortalıyorum ve fontu küçültüyorum


plt.xlabel('Harf')
plt.ylabel('Miktar')
plt.title('Harflerin Kullanılma Miktarlarının Sütun Grafiği')
plt.yticks(range(0, max(ikinci), 3000)) # Y eksenindeki sayıların 3000er artmasını istiyorum
plt.tight_layout()
plt.show()
