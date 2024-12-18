import csv

total = 0
count = 0

with open('spotify.csv', mode='r') as file:
    reader = csv.reader(file)
    
    next(reader)

    for row in reader:
        try:
            total += float(row[4])
            count += 1
        except ValueError:
            continue

if count > 0:
    average = total / count
    print(average)
else:
    print("failure")