import requests
import random
import json

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' # User Agent : python iken site communication kurmuyor o yüzden bu satıyı ekliyoruz.
}

print("3 karakterini girene kadar soru devam eder")

yanlis_bilinenler = []

while True:
    response = requests.get("https://sozluk.gov.tr/icerik",headers=headers)

    veri=response.json()
    secilen=""
    if yanlis_bilinenler and random.choice([True, False]): # Öğrenilmesi için yanlış bilinenleri de soruyorum
        secilen = random.choice(yanlis_bilinenler)
    else:
        secilen = random.choice(veri["syyd"])

    yanlis_kelime = secilen["yanliskelime"]
    dogru_kelime = secilen["dogrukelime"]

    secenekler = [yanlis_kelime, dogru_kelime]

    random.shuffle(secenekler)

    print("Seçenekler:")
    i=0
    for secenek in secenekler:
        i+=1
        print(f"{i}. {secenek}")

    secim = input("Kelimenin doğru yazılışı hangisidir ")
    if(secim=="3"):
        break
    while secim not in {"1", "2"}:
        secim = input("1 ya da 2 girmelisiniz.")
    if(secenekler[int(secim)-1]==dogru_kelime):
         print("Doğru seçtiniz! Kelimenin doğru yazılışı :",dogru_kelime)
         if secilen in yanlis_bilinenler:  
            yanlis_bilinenler.remove(secilen)
    else:
        print("Yanlış seçtiniz! Doğru kelime:", dogru_kelime)
        yanlis_bilinenler.append(secilen)
