from collections import defaultdict, Counter

with open("input.txt", "r") as f:
    data = f.readlines()


q1 = 0

nums = "0987654321"

def getNeighbors(x, y):
    neigh = []
    if x > 0:
        neigh.append((x-1, y))

    if x < len(data[0]) - 2:
        neigh.append((x+1, y))

    if y > 0:
        neigh.append((x, y-1))
    
    if y < len(data[0]) - 2:
        neigh.append((x, y+1))

    if x > 0 and y < len(data[0]) - 2:
        neigh.append((x-1, y+1))

    if x < len(data) - 2 and y < len(data[0]) - 2:
        neigh.append((x+1, y+1))

    if x > 0 and y > 0 :
        neigh.append((x-1, y-1))

    if x < len(data) - 2 and y > 0:
        neigh.append((x+1, y-1))


    return neigh

for i in range(len(data)):
    index = 0
    line = data[i]
    while index < len(line):
        if line[index] in nums:
            numcoords = [(i, index)]
            numchars = line[index]

            index += 1
            
            while line[index] in nums:
                numcoords.append((i, index))
                numchars += line[index]
                index += 1
        
            for y, x in numcoords:
                neighbs = getNeighbors(x,y)
                seen = False
                for x, y in neighbs:
                    if data[y][x] not in nums and data[y][x] != ".":
                        q1 += int(numchars)
                        seen = True
                        break
                if seen:
                    break
        
        
        index += 1

print(q1)

q2 = 0

for i in range(len(data)):
    starcoords = []
    for j in range(len(data[i])):

        if data[i][j] == "*":
            starcoords.append((j, i))
        
    for x, y in starcoords:
        numslist = []
        neighbs = getNeighbors(x, y)

        seenset = set()

        for x1, y1 in neighbs:
            if data[y1][x1] in nums and (x1, y1) not in seenset:
                num_str = data[y1][x1]
                new_ind  = x1 + 1

                while data[y1][new_ind] in nums:
                    seenset.add((new_ind, y1))
                    num_str += data[y1][new_ind]
                    new_ind += 1
                    
                new_ind = x1 - 1
                while data[y1][new_ind] in nums:
                    seenset.add((new_ind, y1))
                    num_str = data[y1][new_ind] + num_str
                    new_ind -= 1
                
                numslist.append(int(num_str))
    
        if len(numslist) == 2:
            q2 += numslist[0] * numslist[1]

print(q2)                
                


