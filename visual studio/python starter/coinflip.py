import random
import time

flips = 0

while True:
    sides = ["heads","tails",]
    if random.randint(1,100) <= 1:
        coin = "edge!?"
    else:
        coin = random.choice(sides)
    print("fliping")
    time.sleep(1)
    print("fliping")
    time.sleep(1)
    print("fliping")
    time.sleep(1)
    print("it landed on")
    time.sleep(2)
    print(coin)
    flips += 1
    if coin == "edge!?":
        print(f"the coin fliped {flips} times")
        break
    else:
        print()
        time.sleep(4)