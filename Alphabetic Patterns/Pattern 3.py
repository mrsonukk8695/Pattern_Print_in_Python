""" PRINT=>
E E E E E 
D D D D D
C C C C C
B B B B B
A A A A A  """
for x in range(69, 64, -1):
    for y in range(1, 6):
        print(chr(x), end=" ")
    print()

print("\n\n")
#Alternative
for x in 'EDCBA':
    for y in 'EDCBA':
        print(x,end=" ")
    print()
