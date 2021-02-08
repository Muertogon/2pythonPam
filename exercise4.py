m = 1
g = []
dalsk = int(input("Skaiciu kurio norite suzinoti daliklius: "))
while m < dalsk:
    if dalsk % m == 0:
      g.append(m)
    m += 1

for i in range(len(g)):
     print(g[i])