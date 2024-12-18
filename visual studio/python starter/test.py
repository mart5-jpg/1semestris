import random

#| | | | X O
#-------
#| | | |
#-------
#| | | |

while True:
    X = int(input('chose spot from 1 to 9 '))
    if X  == 1:
        print("|X| | |")
        print('-------')
        print("| | | |")
        print('-------')
        print("| | | |")
    elif X  == 2:
        print("| |X| |")
        print('-------')
        print("| | | |")
        print('-------')
        print("| | | |")
    elif X  == 3:
        print("| | |X|")
        print('-------')
        print("| | | |")
        print('-------')
        print("| | | |")
    elif X  == 4:
        print("| | | |")
        print('-------')
        print("|X| | |")
        print('-------')
        print("| | | |")
    elif X  == 5:
        print("| | | |")
        print('-------')
        print("| |X| |")
        print('-------')
        print("| | | |")
    elif X  == 6:
        print("| | | |")
        print('-------')
        print("| | |X|")
        print('-------')
        print("| | | |")
    elif X  == 7:
        print("| | | |")
        print('-------')
        print("| | | |")
        print('-------')
        print("|X| | |")
    elif X  == 8:
        print("| | | |")
        print('-------')
        print("| | | |")
        print('-------')
        print("| |X| |")
    elif X  == 9:
        print("| | | |")
        print('-------')
        print("| | | |")
        print('-------')
        print("| | |X|")