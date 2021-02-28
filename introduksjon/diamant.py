#Diamant
#   *
#  * *
# *   *
#  * *
#   *

storrelse = int(input("Diamantstørrelse: "))
count = storrelse
for tall_rad in range(storrelse):

    for tall in range(1, storrelse+1):
        if tall == count:
            print("*", end="")
        else:
            print(" ", end="")
    for tall in range(storrelse-1, 0, -1):
        if tall == count:
            print("*", end="")
        else:
            print(" ", end="")
    if count == 1:
        count = storrelse
    else:
        count-=1
    print()

count = 2
for tall_rad in range(storrelse-1):
    for tall in range(1, storrelse+1):
        if tall == count:
            print("*", end="")
        else:
            print(" ", end="")
    for tall in range(storrelse-1, 0, -1):
        if tall == count:
            print("*", end="")
        else:
            print(" ", end="")
    count+=1
    print()

