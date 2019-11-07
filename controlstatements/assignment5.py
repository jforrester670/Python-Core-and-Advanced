primeFlag = True

n = int(input("Enter a number: "))
i = 2
while i < (n - 1):
    if n % i == 0:
        primeFlag = False
        break
    i += 1

if (primeFlag):
    print("Prime No")
else: 
    print("Not a Prime No")