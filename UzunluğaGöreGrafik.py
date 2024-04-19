import matplotlib.pyplot as plt

uzunluk = [0]*26 # TDK'deki maksimum uzunluktaki kelime 25 harftir.

dosya_adi = 'siralanmis_maddeler.txt'


with open(dosya_adi, 'r', encoding='utf-8') as dosya:
    for satir in dosya:
        kelimeler = satir.split()
        for kelime in kelimeler:
            harf_sayisi = len(kelime)
            uzunluk[harf_sayisi] += 1


plt.figure(figsize=(15, 9))
bars = plt.bar(list(range(1, len(uzunluk))), uzunluk[1:] , color='skyblue')
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='center', ha='center')

plt.xlabel('Kelime Uzunluğu')
plt.ylabel('')
plt.title('Hangi Uzunkluktaki Kelimelerden Kaçar Tane Var')
plt.yticks(range(0, max(uzunluk[1:]), 500))
plt.xticks(range(1, 26))
plt.tight_layout()
plt.show()
