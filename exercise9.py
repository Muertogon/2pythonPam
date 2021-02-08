import random

randnmb = random.randint(1, 9)
print("secret nombre: " + str(randnmb))
spsk = 1
while 0 < True:
    atsp = int(input("Bandykit atspeti skaiciu nuo 1 iki 9: "))
    if atsp < randnmb:
        print("Per zemai")
        spsk += 1
    elif atsp > randnmb:
        print("Per aukstai")
        spsk += 1
    else:
        print("ATSPEJOOOOT!! ir tik su "+ str(spsk) +" bandymu/ais")
        break