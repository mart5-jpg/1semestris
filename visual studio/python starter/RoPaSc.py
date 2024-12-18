import random
turn = ["rock","paper","scissors"]
while True:
    game = input("1, 2 or 3 players?")

    if game == "exit":
        print("exiting...")
        break

    if game == "1":
        player1 = input('choose rock, paper or scissors: ')
        player2 = random.choice(turn)
    elif game == "2":
        player1 = input('player1 choose rock, paper or scissors: ')
        player2 = input('player2 choose rock, paper or scissors: ')
    elif game == "3":
        player1 = input('player1 choose rock, paper or scissors: ')
        player2 = input('player2 choose rock, paper or scissors: ')
        player3 = input('player3 choose rock, paper or scissors: ')
    if (game == "1") or (game == "2"):
        print(player1, "vs" ,player2)
        if player1 == player2:
            print("draw")
        elif(player1 == "rock" and player2 == "scissors") or \
        (player1 == "scissors" and player2 == "paper") or \
        (player1 == "paper" and player2 == "rock"):
            print("player1 wins")
        else:
            print("player2 wins")
    else:
        print(player1, "vs" ,player2, "vs", player3)
        if (player1 == player2 == player3) or \
        (player1 == "rock" and player2 == "paper" and player3 == "scissors") or \
        (player1 == "paper" and player2 == "scissors" and player3 == "rock") or \
        (player1 == "scissors" and player2 == "rock" and player3 == "paper"):
            print("draw")
        elif(player1 == "rock" and player2 == "scissors" and player3 == "scissors") or \
            (player1 == "paper" and player2 == "rock" and player3 == "rock") or \
            (player1 == "scissors" and player2 == "paper" and player3 == "paper"):
            print("player1 wins")
        elif(player2 == "rock" and player1 == "scissors" and player3 == "scissors") or \
            (player2 == "paper" and player1 == "rock" and player3 == "rock") or \
            (player2 == "scissors" and player1 == "paper" and player3 == "paper"):
            print("player2 wins")
        else:
            print("player3 wins")