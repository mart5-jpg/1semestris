import csv

total = 0
count = 0

eksameni = []
summas = []
skaits = []

with open('vps_ce_rezultati_vsk_2022_2023.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    
    next(reader)

    for row in reader:
        try:
            if row[1] not in eksameni:
                eksameni.append(row[1])
                summas.append(total)
                skaits.append(count)
            else:
                index = eksameni.index(row[1])
                summas[index] += float(row[9])
                skaits[index] += 1
        except ValueError:
            continue

for i in range(0, len(eksameni)):
        print(f'{eksameni[i]} {summas[i] / skaits[i]}')


