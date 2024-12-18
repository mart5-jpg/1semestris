cont = [['jānis', 93264], ['pēteris', 349676]]

while True:
    res = int(input("ko vēlaties darīt?  1:pievienot, 2:izvadīt, 3:izdzēst, 0:iziet  "))
    print(res)

    if res == 0:
        break
    elif res == 1:
        name = input('ievadi vārdu  ')
        num = int(input('ievadi nummuru  '))
        cont.append([name, num])
    elif res == 2:
        for num in cont:
            print(f"{num[0]} {num[1]}")
    elif res == 3:
        named = input("ievadiet vārdu kura kontaktu vēlaties izdzēst  ")
        for num in cont:
            if named == num[0]:
                cont.pop(cont[num])
    else:
        print('not valid nummber. try again')