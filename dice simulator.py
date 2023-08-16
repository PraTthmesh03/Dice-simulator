import random
while True:
    print('Roll The dice')
    print('''1.Yes 2.No''')
    user = int(input("What do you want to do : "))
    if user == 1:
        numbers = random.randint(1,6)
        print(numbers)
    else:
        break