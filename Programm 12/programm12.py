import random
run = True
while run:
    x = input("Roll a dice [[y]/n]: ")
    if x == 'n':
        run = False
    else:
        print(random.randint(1, 7))