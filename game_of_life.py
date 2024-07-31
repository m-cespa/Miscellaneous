import numpy as np
import random
import time

height = 10
width = 10

# 1 = alive, 0 = dead

A = np.empty((width,height), dtype='int')

for x in range(width):
    for y in range(height):
        A[x,y] = random.randint(0,1)

while True:
    print(A)
    new_A = np.copy(A)
    for x in range(width):
        for y in range(height):
            neighbours = [
                A[(x-1) %width,y], A[(x+1) %width,y],
                A[(x-1) %width,(y-1) %height], A[(x-1) %width,(y+1) %height],
                A[(x+1) %width,(y-1) %height], A[(x+1) %width,(y+1) %height],
                A[x,(y-1) %height], A[x,(y+1) %height]
            ]
            tot = sum(neighbours)
            if A[x,y] == 1:
                if tot == 2 or tot == 3:
                    new_A[x,y] = 1
                else:
                    new_A[x,y] = 0
            elif A[x,y] == 0:
                if tot == 3:
                    new_A[x,y] = 1
                else:
                    new_A[x,y] = 0
    A = new_A
    print()
    time.sleep(1)