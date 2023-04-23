num = int(input("enter number: "))
for i in range(num):
    m = i+1
    for j in range(num-i-1):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    print(end=" ")
    for j in range(i+1):
        print(m, end="")
        m += 1
    print()
for i in range(0, 2*num, 2):
    k = i//2
    for j in range(k):
        print(" ", end="")
    for j in range(num-k):
        print(num-j, end="")
    print(end=" ")
    for j in range(i, 2*num, 2):
        print(j+1, end="")
    print()