import random

i=0
list3 = []
while i < 25:
    list3.append(random.randint(1,15))
    i += 1
print("Pradinis sarasas: " +str(list3))
print("Elementai: "+str(len(list3)))
he = set(list3)
print("Pabaigos sarasas: " +str(he))
print("Elementai: "+str(len(he)))