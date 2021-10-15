import random

A = random.randint(0, 2)
B = random.randint(0, 2)

if (A-B == 1):
    print("A ",A," B ",B," A win")
elif (B-A == 1):
    print("A ",A," B ",B," B win")
elif (A-B == 2):
    print("A ",A," B ",B," B win")
elif (B-A == 2):
    print("A ",A," B ",B," A win")
elif (A==B):
    print("A ",A," B ",B," Draw")