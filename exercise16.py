import random

pss = str(input("Kokio stiprumo norite slaptazodzio?('1' - silpnas, '2' - stiprus): "))
def weakPass():
    skList = [random.randint(1, 9999999999)]
    with open("wordlist.txt") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
    print(random.choice(words) + str(skList[0]))

def strongPass():
    v = ["a", "b", "c", "d",
         "e", "f", "g", "j",
         "i", "j", "k", "l",
         "m", "n", "o", "p",
         "r", "s", "t", "U",
         "v", "w", "x", "y",
         "z", "@", "#", "$",
         "%", "^", "&", "*",
         "+", "-", "_", "<",
         ">", "?", "/", "~"]
    leng = str(input("Ilgis? '1'- iki 20 zenklu, '2'- iki 40 zenklu: "))
    if leng == "1":
        lns = random.randint(14, 20)
    elif leng == "2":
        lns = random.randint(21, 40)
    else:
        print("no")
    i = 0
    ps = ""
    while i < lns:
        ps += v[random.randint(0, 39)]
        i += 1

    print(ps)

if pss == "1":
    print("Pasirinkote silpna slaptazodi")
    weakPass()
elif pss == "2":
    print("Pasirinkote stipru slaptazodi")
    strongPass()
else:
    print("no")