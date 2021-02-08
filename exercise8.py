kiek = int(input("Kiek norite zaisti raundu?"))
a = 0
while a < kiek:
    pirmzai = str(input("Pirmasis zaidejau-iveskite sulinys, lapas arba zirkles"))
    antrzai = str(input("Antrasis zaidejau-iveskite sulinys, lapas arba zirkles"))
    if pirmzai == antrzai:
        print("Lygiosios")
    elif pirmzai == "sulinys" and antrzai == "lapas":
        print("Antras Zaidejas laimejo")
    elif pirmzai == "lapas" and antrzai == "zirkles":
        print("Antras Zaidejas laimejo")
    elif pirmzai == "zirkles" and antrzai == "sulinys":
        print("Antras Zaidejas laimejo")
    elif antrzai == "sulinys" and pirmzai == "lapas":
        print("Pirmas Zaidejas laimejo")
    elif antrzai == "lapas" and pirmzai == "zirkles":
        print("Pirmas Zaidejas laimejo")
    elif antrzai == "zirkles" and pirmzai == "sulinys":
        print("Pirmas Zaidejas laimejo")
    else:
        print("Sufeilinot ivedima, veskit per nauja")
    a += 1