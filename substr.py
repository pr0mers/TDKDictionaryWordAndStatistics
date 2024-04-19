from collections import defaultdict

import time

start_time = time.time()
substrs = defaultdict(int)

def generate_substrs(text):
    words = text.strip()
    for n in range(1, len(text) + 1): # kelimenin uzunluğu mesela "abd" için 1 2 3 uzunluğundaki substringlerini buluyorum, substring abc = {a,b,c,ab,bc,abc}
        for i in range(len(text) - n + 1):
            substr = text[i:i+n]
            substrs[substr] += 1
    return substrs


with open("siralanmis_maddeler.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip() 
        result = generate_substrs(line)


sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

with open("KelimeSubstrleri.txt", "w", encoding="utf-8") as file:
    for substring, count in sorted_result:
        file.write(f"{substring}:{count}\n")

end_time = time.time()
print(f"İşlem süresi: {-start_time+end_time} saniye")
