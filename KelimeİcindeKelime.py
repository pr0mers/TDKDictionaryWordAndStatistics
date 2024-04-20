import time
from collections import defaultdict
kelime_listesi={}
start_time = time.time()
with open("siralanmis_maddeler.txt", 'r', encoding='utf-8') as dosya:
    for satir in dosya:
        kelimeler = satir.split()
        for kelime in kelimeler:
            uzunluk = len(kelime)
            if uzunluk in kelime_listesi:
                kelime_listesi[uzunluk].append(kelime)
            else:
                kelime_listesi[uzunluk] = [kelime]


mx = 0
substr_listesi={}



with open("siralanmis_maddeler.txt", 'r', encoding='utf-8') as dosya:
    
    for satir in dosya:
        kelime = satir.strip()
        substrs= set()
        for n in range(2, len(kelime) + 1):
            for i in range(len(kelime) - n + 1):
                substr=kelime[i:i+n]
                if substr in kelime_listesi[n]:
                    substrs.add(substr)
        if len(substrs) not in substr_listesi:
            substr_listesi[len(substrs)]=[kelime]
        else:
            substr_listesi[len(substrs)].append(kelime)
        mx=max(mx,len(substrs))
        
        
print(mx)
for kelime in substr_listesi[mx]:
        
        substrs=set()
        for n in range(2, len(kelime) + 1):
            for i in range(len(kelime) - n + 1):
                substr=kelime[i:i+n]
                if substr in kelime_listesi[n]:
                    substrs.add(substr)
        print(kelime)
        print(substrs)

end_time = time.time()
print(f"İşlem süresi: {-start_time+end_time} saniye")

