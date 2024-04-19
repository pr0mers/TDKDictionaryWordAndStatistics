import json

with open('autocomplete.json', 'r', encoding='utf-8') as dosya: 
    veri = json.load(dosya)
    
ezilebitenliste= set()
ezilebitenlistetekkelime=set()

for madde_verisi in veri:
    madde = madde_verisi.get("madde", "").lower()
    if madde.endswith("ez"):
        madde=madde.replace("ez","EZ")
        ezilebitenliste.add(madde)
        if(len(madde.split())==1):
            ezilebitenlistetekkelime.add(madde)
            
with open('EZilebitentekkelime.txt', 'w', encoding='utf-8') as txt_dosyasi: #txtye yazdırıyorum
    txt_dosyasi.write('\n'.join(ezilebitenlistetekkelime))
with open('EZilebitenhepsi.txt', 'w', encoding='utf-8') as txt_dosyasi:
    txt_dosyasi.write('\n'.join(ezilebitenliste))
    
print(f'ez ile biten tek kelimelerinin sayısı : {len(ezilebitenlistetekkelime)}')
print("")
print(f'ez ile biten tek kelimelerinin sayısı : {len(ezilebitenliste)}')

