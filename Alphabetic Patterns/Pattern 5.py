""" PRINT=>
A 
B B
C C C
D D D D
E E E E E"""

for x in range(65, 70):
    for y in range(65, x + 1):
        print(chr(x), end=" ")
    print()