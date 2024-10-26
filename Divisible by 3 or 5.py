x = int(input("Enter an integer: "))

for i in range(1,x+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")