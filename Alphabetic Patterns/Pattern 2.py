""" PRINT=>
A A A A A 
B B B B B 
C C C C C 
D D D D D 
E E E E E"""
for x in range(1, 6):
    for y in range(65, 70):
        print(chr(y), end=" ")
    print()

print("\n\n")
#Alternative
for x in 'ABCDE':
    for y in 'ABCDE':
        print(y,end=" ")
    print()