def primeFirstFunc():
    for num in range(0, 501):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

def primeSecondFunc():
    for num in range(500, 1001):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

print(primeFirstFunc())
print()
print(primeSecondFunc())