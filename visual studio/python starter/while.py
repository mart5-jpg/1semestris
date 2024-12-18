import random

number = random.randint(1, 100)
loops = 0
cloops =0

maxnum = 100 
minnum = 1

while True:
    computer = random.randint(minnum, maxnum)
    cloops += 1
    if computer > number:
        maxnum = computer - 1
        computer = random.randint(minnum, computer)
    elif computer < number:
        minnum = computer + 1
        computer = random.randint(computer, maxnum)
    elif computer == number:
        print("computer attempted", cloops )
        break 

while True:  
    loops += 1
    if loops == 10:
        print("10 guesses already.")
    if loops == 20:
        print("20 guesses already. the computer already beat you probobly.")
    if loops == 50:
        print("50 guesses!? you have guessed more than half of the numbers already!")
    if loops == 100:
        print("a 100 guesses!?! you have guessed all of the numbers and jet you havent gotten the corect nummber. guess the number dosent exist, unless you guessed the same nubre all the time")
    player = int(input("choose a number from 1 to 100 "))
    if player > number:
        print("guess lower")
    elif player < number:
        print("guess higher")
    elif player == number:
        print("correct? the number was", number)
        print(f"you tried {loops} times" )
        print()
        if loops > cloops:
            print("you lost to the computer!")
        elif loops < cloops:
            print("you beat the computer! you get a cepums!")
        elif loops == cloops:
            print("you tied with the computer!")
        break