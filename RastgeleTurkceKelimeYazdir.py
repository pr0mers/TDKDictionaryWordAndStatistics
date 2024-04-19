import random

with open('siralanmis_maddeler.txt', 'r', encoding='utf-8') as dosya:
    kelimeler = dosya.read().splitlines()

rastgele_kelime = random.choice(kelimeler)
print("Rastgele Kelime:", rastgele_kelime)
