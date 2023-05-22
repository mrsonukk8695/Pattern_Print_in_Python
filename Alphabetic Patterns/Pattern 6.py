""" PRINT=>
A 
A B
A B C
A B C D
A B C D E"""
for x in range(65, 70):
    for y in range(65, x + 1):
        print(chr(y), end=" ")
    print()