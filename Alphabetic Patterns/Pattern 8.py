""" PRINT=>
A B C D E 
A B C D
A B C
A B
A       """
for x in range(5, 0, -1):
    for y in range(0, x):
        print(chr(y + 65), end=" ")
    print()