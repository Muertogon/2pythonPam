import random
import sys
# # Python3 implementation of
# # above approach
#
# # Function to count the number
# # of carry operations
# def count_carry(a, b):
#     # Initialise the value of
#     # carry to 0
#     carry = 0;
#
#     # Counts the number of carry
#     # operations
#     count = 0;
#
#     # Initialise len_a and len_b
#     # with the sizes of strings
#     len_a = len(a);
#     len_b = len(b);
#
#     while (len_a != 0 or len_b != 0):
#
#         # Assigning the ascii value
#         # of the character
#         x = 0;
#         y = 0;
#         if (len_a > 0):
#             x = int(a[len_a - 1]) + int('0');
#             len_a -= 1;
#
#         if (len_b > 0):
#             y = int(b[len_b - 1]) + int('0');
#             len_b -= 1;
#
#             # Add both numbers/digits
#         sum = x + y + carry;
#
#         # If sum > 0, icrement count
#         # and set carry to 1
#         if (sum >= 10):
#             carry = 1;
#             count += 1;
#
#             # Else, set carry to 0
#         else:
#             carry = 0;
#
#     return count;
#
#
# # Driver code
# a = "955847895";
# b = "556545";
#
# count = count_carry(a, b);
# if (count == 0):
#     print("0");
# elif (count == 1):
#     print("1");
# else:
#     print(count);
#
# print(count_carry(a,b))
#exercise 1
name = input("Iveskite savo varda: ")
ag = int(input("Iveskite savo metus: "))
thg = 100 - ag
thg = str(thg)
print(name+" sukaks 100 metų už "+thg+ " metų")

#exercise 2
num = int(input("inter number: "))
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")
check = int(input("inter number: "))
if num % check == 0:
    print("skaicius graziai issidalina is kito duoto")
else:
    print("nop")
#exercise 3
c = []
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = int(input("input number: "))
for i in range(len(a)):
    if a[i] < b:
        c.append(a[i])

for i in range(len(c)):
    print(c[i])


#exercise 4
#neuzbaigta
dalsk = int(input("skaiciu kurio norite suzinoti daliklius"))
while dalsk > i:
    if dalsk % i== 0:
        print(str((i))+("=dalinasi"))
    else:
        print(str((i))+("=nesidalina"))
    i -= 1

#exercise 5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

panas_el = [e for e in a if e in b]
#list
print(panas_el)

#exercise 6

f = str(input("Iveskite zodi, kad patikrinti ar palidromas: "))
if f == f[::-1]:
    print("Palidrnomas")
else:
    print("Ne palindromas")

#exercise 7

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

lygus = [x for x in a if x % 2 == 0]
print(lygus)

#exercise 8

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

#exercise 9

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

#exercise 10

list1 = random.sample(range(1,100), 20)
print("Firstlist: "+ str(list1))
#pirmas masyvas
list2 = random.sample(range(1,100), 20)
print("Seclist: "+ str(list2))
#antras masyvas
panas_el2 = [n for n in list1 if n in list2]
#list
print("panasus el: "+str(panas_el2))

#exercise 11

