f = str(input("Iveskite zodi, kad patikrinti ar palidromas: "))
if f == f[::-1]:
    print("Palidrnomas")
else:
    print("Ne palindromas")