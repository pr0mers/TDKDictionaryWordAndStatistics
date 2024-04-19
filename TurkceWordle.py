import random

kelime_listeleri = {}

dosya_adi = 'siralanmis_maddeler.txt'


with open(dosya_adi, 'r', encoding='utf-8') as dosya: # TDK'deki kelimeleri çekiyorum
    for satir in dosya:
        kelimeler = satir.split()
        for kelime in kelimeler:
            harf_sayisi = len(kelime)
            if harf_sayisi not in kelime_listeleri: # Kelimeleri harf sayısına göre sıralıyorum
                kelime_listeleri[harf_sayisi] = [kelime]
            else:
                kelime_listeleri[harf_sayisi].append(kelime)
                

while True:
    oyuncu_harf = int(input("Kaç harfli kelimeli wordle oynamak istiyorsunuz? "))
    if oyuncu_harf in kelime_listeleri:
        break
    else :
        print("Belirttiğiniz harfte kelime bulunmamaktadır.")
        
kelime=random.choice(kelime_listeleri[oyuncu_harf]) # Kelimeyi belirtilen harfli kelimelerden rastgele seçiyorum
while True:
    tahmin = input("Tahmininizi girin: ").lower()
    if len(tahmin) != len(kelime):
        print("Tahmininiz", len(kelime), "harfli olmalıdır. Lütfen tekrar deneyin.")
        continue
    
    if tahmin not in kelime_listeleri[oyuncu_harf]:
        print("Girdiğiniz kelime TDK'de yoktur.")
        continue
    
    dogru_indeksler = []
    
    harf_sayilari = {}
    
    for harf in kelime: # Kelimede hangi harften kaç tane olduğunu tutuyorum, örn: mösyö = {'m': 1, 'ö' : 2, 's' : 1 ,'y' : 1}
        if harf in harf_sayilari:
            harf_sayilari[harf] += 1
        else:
            harf_sayilari[harf] = 1

    
    for i in range(len(kelime)): # Önce doğru harflerin hangi harfler olduğunu tutuyorum ve doğru oldukları için harf sayısından çıkarıyorum ki kelime mösyö iken ööööö tahmini yaparsak SYSSY yazmasın da GYGGY yazsın
        if tahmin[i] == kelime[i]:
            dogru_indeksler.append(i)
            harf_sayilari[kelime[i]] -= 1

    sonuc = ['G'] * len(kelime)

    for i in range(len(kelime)):
        if i in dogru_indeksler:    
            sonuc[i] = 'Y'
        elif tahmin[i] in kelime and i not in dogru_indeksler: # Yine aynı sebepten karışıklık olmaması için S yazdıktan sonra azaltıyorum
            if harf_sayilari[tahmin[i]] != 0:
                harf_sayilari[tahmin[i]] -= 1
                sonuc[i] = 'S'

    sonuc = ''.join(sonuc)

    print("Sonuç:", sonuc)

    if sonuc == 'Y' * len(kelime):
        print("Tebrikler! Kelimeyi buldunuz:", kelime)
        break
