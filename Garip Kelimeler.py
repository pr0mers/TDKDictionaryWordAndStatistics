import json
import time
import requests
import os
start_time = time.time()

###############################
'''
#Gerçekten Garip Olanlar Sadece /// Bir kaç tanesi eksik olabilir hepsi gittiği için

turkce_alfabe = "aâbcçdefgğhıiîjklmnoöprsştuüûvyz /()-,'?.:;!\"’…"
turkce_alfabe+="̇" //// BURASI BOŞ DEĞIL CC87 HEX KODLU BIR KARAKTER VAR BU KARAKTER GORUNTULENEMEDIĞI ICIN TDK DA "islam" KELIMESINI ARATIRSANIZ ONERI ÇIKMAZ AMA ENTER'A BASARSANIZ KELIME KARŞINIZA GELIR
'''
###############################

#Turkce alfabesinde olmayan harfleri içeren kelimeler :
turkce_alfabe = "aâbcçdefgğhıiîjklmnoöprsştuüûvyz "

with open('autocomplete.json', 'r', encoding='utf-8') as dosya: # Burada autocomplete.json dosyasının içeriğini okuyorum
    veri = json.load(dosya)


garipkelimeler = set()
garipharfler = set()
for madde_verisi in veri: # Tüm kelimeleri gezip eğer kelimeler turkce alfabesinde yoksa set'e ekliyorum
    madde = madde_verisi.get("madde", "").lower()
    for harf in madde:
        if harf not in turkce_alfabe:
            garipkelimeler.add(madde)
            garipharfler.add(harf)


with open('garipkelimeler.txt', 'w', encoding='utf-8') as txt_dosyasi: #txtye yazdırıyorum
    txt_dosyasi.write('\n'.join(garipkelimeler))
with open('garipharfler.txt', 'w', encoding='utf-8') as txt_dosyasi:
    txt_dosyasi.write('\n'.join(garipharfler))


end_time = time.time()
print(f"İşlem süresi: {-start_time+end_time} saniye")
