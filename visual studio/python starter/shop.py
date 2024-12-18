import random
saraksts = []
skaitlis = int(input("cik reizes printesi?"))

while True:
    skaitlis = int(input("cik reizes printesi?"))
    for num in range(skaitlis):
        saraksts.append(random.randint(0,1000))
    break