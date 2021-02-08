c = []
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = int(input("input number: "))
for i in range(len(a)):
    if a[i] < b:
        c.append(a[i])

for i in range(len(c)):
    print(c[i])