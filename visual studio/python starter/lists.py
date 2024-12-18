names = ['Jānis', 'Andris', 'Kārlis', 'Anna', 'Alise']
ages = [35, 46, 57, 68, 90]
School = [True, False, True, True, False]
weight = 6
num =['0','1','2','3','4','5']
height =3
persondata = [
    ['Jānis', 35, True],
    ['Andris', 46, False],
    ['Kārlis', 57, True],
    ['Anna', 68, True],
    ['Alise', 90, False]
]
#(len)
for i in (names):
    if i == "Anna" or i == 'Alise':
        print(f'Labdien {i}')
    else:
        print(f'Sveiks {i}')

#personal_data = [
#    ['Jacob Nguyen', 28, False, 'charlesmiller@gmail.com'],
#    ['Madison Jones', 35, True, 'marymiller@hotmail.com'],
#    ['Jonathan Lopez', 22, False, 'cameronfoster@gmail.com'],
#    ['Michael Moore', 30, True, 'johnsonmichael@yahoo.com']
#]

#name = input('Enter your name: ')
#age = int(input('Enter your age: '))
#university = input('Are you in university? (yes/no): ').lower() == 'yes'
#email = input('Enter your email: ')

#new_data = [name, age, university, email]
#personal_data.append(new_data)