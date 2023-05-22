""" PRINT=>
A A A A A 
B B B B
C C C
D D
E           """
for x in range(0, 5):
    for y in range(4, x - 1, -1):
        print(chr(x + 65), end=" ")
    print()