storrelse = int(input("Størrelse: "))

for linje in range(storrelse):
    for tall in range(storrelse):
        if tall == storrelse-1-linje:
            print("*", end="")
        else:
            print(" ", end="")
    for tall in range(storrelse-1):
        if tall == linje-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for linje in range(storrelse-2, -1, -1):
    for tall in range(storrelse):
        if tall == storrelse-1-linje:
            print("*", end="")
        else:
            print(" ", end="")
    for tall in range(storrelse-1):
        if tall == linje-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
