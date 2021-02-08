import random

list1 = random.sample(range(1,100), 20)
print("Firstlist: "+ str(list1))
#pirmas masyvas
list2 = random.sample(range(1,100), 20)
print("Seclist: "+ str(list2))
#antras masyvas
panas_el2 = [n for n in list1 if n in list2]
#list
print("panasus el: "+str(panas_el2))