x = int(input("Enter a number: "))
y = 0

while y < x and y < 100:
    y += 1
    if y % 10 == 0:
        continue
    print(y)
