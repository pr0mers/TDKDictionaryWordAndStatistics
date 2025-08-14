import json
import time
import requests
import urllib.parse
import os
import random
start_time = time.time()

turkce_alfabe = "aâbcçdefgğhıiîjklmnoöprsştuüûvyz"
turkce_alfabe2 = "abcçdefghıijklmnoöprsştuüvyz"

with open('autocomplete.json', 'r', encoding='utf-8') as dosya: # Burada autocomplete.json dosyasının içeriğini okuyorum
    veri = json.load(dosya)

headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        }

def oyunbaslat():
    oyun = []
    for harf in turkce_alfabe2:
        oyun.append(random.choice(list(harflere_gore_kelimeler[harf])))
    secim="";
    soru=0;
    while(secim!="bitir"):
        dogru=0
        soru=soru%len(turkce_alfabe2)
        while(oyun[soru]=="-"):
            dogru=dogru+1
            soru=soru+1
        print(oyun[soru])
        kel=urllib.parse.quote(oyun[soru])
        url = f"https://sozluk.gov.tr/gts?ara={kel}"
        response = requests.get(url,headers=headers)
        data = response.json()
        if data:
            anlamlar = data[0].get("anlamlarListe", [])
            for anlam in anlamlar:
                if anlam.get("anlam_sira") == "1":
                    print(anlam.get("anlam"))
                    break
        secim=input()
        if(secim =="pas"):
            soru=soru+1
        elif(secim == oyun[soru]):
            oyun[soru]="-"
            soru=soru+1
        if(dogru==len(turkce_alfabe2)):
            print("KAZANDINN")
            return
    print (oyun)


siralanmis_kelimeler = set() # Set oluşturuyorum çünkü aynı kelimeler varsa onları tekrar almayalım


for madde_verisi in veri: # JSON dosyasındaki kelimeleri geziyorum
    madde = madde_verisi.get("madde", "").lower()
    if madde and len(madde.split()) == 1 and madde[0] in turkce_alfabe: # Kelime türkçe harfle mi başlıyor diye bakıyorum (-den beri vb. şeyleri eklememek için) ve sadece tek kelimeleri ekliyorum
        siralanmis_kelimeler.add(madde.lower())

    
siralanmis_kelimeler = sorted(siralanmis_kelimeler, key=lambda x: [turkce_alfabe.index(c) for c in x if c in turkce_alfabe]) # kelimeleri türkçe sıralıyorum yoksa ı,ö,ğ gibi harfler dosyanın en sonunda oluyor

harflere_gore_kelimeler = {}

for kelime in siralanmis_kelimeler:
    if kelime[0] not in harflere_gore_kelimeler:
        harflere_gore_kelimeler[kelime[0]]=set()
    harflere_gore_kelimeler[kelime[0]].add(kelime)


oyunbaslat()

