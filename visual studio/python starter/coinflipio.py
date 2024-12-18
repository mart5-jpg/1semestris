file = open('coin.txt', 'r',)
import random
import time

space = ' \n'
flipping = 'flipping\n'
landing = 'it landed on...\n'
flips = 0
total = f'the coin fliped {flips} times\n'

while True:
    sides = ["heads\n","tails\n",]
    if random.randint(1,100) <= 1:
        coin = "edge!?\n"
    else:
        coin = random.choice(sides)
    file.write(flipping)
    time.sleep(1)
    file.write(flipping)
    time.sleep(1)
    file.write(flipping)
    time.sleep(1)
    file.write(landing)
    time.sleep(2)
    file.write(coin)
    flips += 1
    if coin == "edge!?":
        file.write(total)
        file.close
        break
    else:
        file.write(space)
        time.sleep(4)