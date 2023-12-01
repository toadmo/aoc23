from collections import defaultdict, Counter

with open("input.txt", "r") as f:
    data = f.readlines()

nums = "012345456789"
q1 = 0

for line in data:
    line  = line.strip()
    for i in range(len(line)):
        if line[i] in nums:
            first = line[i]
            break

    for i in range(len(line) -1, -1, -1):
        if line[i] in nums:
            second = line[i]
            break

    q1 += int(first + second)

words = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

q2 = 0

for line in data:
    line  = line.strip()

    numslist = []
    for i in range(len(line)):
        if line[i] in nums:
            first = line[i]
            firstind = i
            numslist.append((firstind, first))
            break

    for i in range(len(line) -1, -1, -1):
        if line[i] in nums:
            second = line[i]
            secondind = i
            numslist.append((secondind, second))
            break

    for i in range(len(line)):
        new_line = line[i:]
        for word in words.keys():
            if word in new_line:
                numslist.append((new_line.index(word) + i, str(words[word])))

    numslist = sorted(numslist)

    line_num = numslist[0][1] + numslist[-1][1]

    q2 += int(line_num)

print(f"Part 1: {q1}\nPart2: {q2}")