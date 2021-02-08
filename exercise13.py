def fibonacci():
    sk = int(input("Kiek skaiciu norite savo fibonnaci sekoje : "))
    i = 1
    if sk == 0:
        seka = []
    elif sk == 1:
        seka = [1]
    elif sk == 2:
        seka = [1,1]
    elif sk > 2:
        seka = [1,1]
        while i < (sk - 1):
            seka.append(seka[i] + seka[i-1])
            i += 1
    return seka
print (fibonacci())
input()
#visur tas pats sprendimas, o paciam buvo per sunku sugalvot