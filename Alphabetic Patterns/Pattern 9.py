""" PRINT =>
E E E E E 
D D D D
C C C
B B
A       """
for x in range(5, 0, -1):
    for y in range(0, x):
        print(chr(x + 64), end=" ")
    print()