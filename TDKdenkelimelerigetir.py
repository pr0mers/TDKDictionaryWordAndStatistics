import json
import time
import requests
import os
start_time = time.time()

turkce_alfabe = "aâbcçdefgğhıiîjklmnoöprsştuüûvyz"


with open('autocomplete.json', 'r', encoding='utf-8') as dosya: # Burada autocomplete.json dosyasının içeriğini okuyorum
    veri = json.load(dosya)

    
'''

----Dosyayı indirmesem böyle GET kullanarak da kelimeleri çekebilirdim----

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
response = requests.get("https://sozluk.gov.tr/autocomplete.json",headers=headers)
veri=response.json()

'''

siralanmis_kelimeler = set() # Set oluşturuyorum çünkü aynı kelimeler varsa onları tekrar almayalım


for madde_verisi in veri: # JSON dosyasındaki kelimeleri geziyorum
    madde = madde_verisi.get("madde", "").lower()
    if madde and len(madde.split()) == 1 and madde[0] in turkce_alfabe: # Kelime türkçe harfle mi başlıyor diye bakıyorum (-den beri vb. şeyleri eklememek için) ve sadece tek kelimeleri ekliyorum
        siralanmis_kelimeler.add(madde.lower())

    
siralanmis_kelimeler = sorted(siralanmis_kelimeler, key=lambda x: [turkce_alfabe.index(c) for c in x if c in turkce_alfabe]) # kelimeleri türkçe sıralıyorum yoksa ı,ö,ğ gibi harfler dosyanın en sonunda oluyor


with open('siralanmis_maddeler.txt', 'w', encoding='utf-8') as txt_dosyasi:
    txt_dosyasi.write('\n'.join(siralanmis_kelimeler))


end_time = time.time()
print(f"İşlem süresi: {-start_time+end_time} saniye")
