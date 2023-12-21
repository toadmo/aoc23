from collections import defaultdict, Counter
import operator
import math

with open("test.txt", "r") as f:
    data = f.read()

patterns = data.split('\n\n')

q1 = 0

for pattern in patterns:
    horiz_lines = pattern.split('\n')
    vert_lines = ["".join([horiz_lines[j][i] for j in range(len(horiz_lines))]) for i in range(len(horiz_lines[0]))]

    # check horiz

    for i in range(len(horiz_lines) - 1): 
        indic = True
        if horiz_lines[i] == horiz_lines[i+1]:
            for x, y in zip(horiz_lines[i+1:], horiz_lines[0:i+1][::-1]):
                if x != y:
                    indic = False
                    break

            if indic:
                q1 += 100*len(horiz_lines[0:i+1][::-1])
                break
    
    # check vert

    if indic:
        for i in range(len(vert_lines) - 1): 
            indic = True
            if vert_lines[i] == vert_lines[i+1]:
                for x, y in zip(vert_lines[i+1:], vert_lines[0:i+1][::-1]):
                    
                    if x != y:
                        indic = False
                        break

                if indic:
                    q1 += len(vert_lines[0:i+1][::-1])
                    break

print(q1)

q2 = 0

for pattern in patterns:

    horiz_lines = pattern.split('\n')
    vert_lines = ["".join([horiz_lines[j][i] for j in range(len(horiz_lines))]) for i in range(len(horiz_lines[0]))]


    # check horiz

    for i in range(len(horiz_lines) - 1): 
        indic = True
        count = sum(1 for a, b in zip(horiz_lines[i], horiz_lines[i+1]) if a != b)
        if count < 2:
            for x, y in zip(horiz_lines[i+2:], horiz_lines[0:i][::-1]):
                if x != y:
                    count += sum(1 for a, b in zip(horiz_lines[i], horiz_lines[i+1]) if a != b)
                if count > 1:
                    indic = False
                    break

            if count == 1:
                print(horiz_lines[i+1:], horiz_lines[0:i+1][::-1])
                q2 += 100*len(horiz_lines[0:i+1][::-1])
                break
    
    # check vert

    if not indic:
        for i in range(len(vert_lines) - 1): 
            count = sum(1 for a, b in zip(vert_lines[i], vert_lines[i+1]) if a != b)
            if count < 2:
                for x, y in zip(vert_lines[i+2:], vert_lines[0:i][::-1]):
                    if x != y:
                        count += sum(1 for a, b in zip(vert_lines[i], vert_lines[i+1]) if a != b)
                    if count > 1:
                        break

                if count == 1:
                    print(vert_lines[i+1:], vert_lines[0:i+1][::-1])
                    q2 += len(vert_lines[0:i+1][::-1])
                    break

print(q2)