sk = int(input("Skaicius: "))
def isPrime(d):
    for i in range(2, d):
        if d % i == 0:
            return False
    return True

print(isPrime(sk))