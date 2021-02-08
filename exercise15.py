heh = input("Iveskite ilga sakini: ")
def splitW(w):
    kek = w.split()
    done = kek[::-1]
    print(w)
    print(" ".join(done))

splitW(heh)