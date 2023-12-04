from collections import defaultdict, Counter

with open("input.txt", "r") as f:
    data = f.readlines()


q1 = 0

numbers = "0987654321"
lowerletters = "abcdefghijklmnopqrstuvwxyz"
upperletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


for line in data:
    line = line.strip()
    cardnums, mynums = line.split(' | ')
    cardnums = cardnums.split(': ')[1].split(' ')

    mynums = mynums.split(' ')

    currpts = 0

    for mynum in mynums:
        if mynum in cardnums and mynum != "":
            currpts+=1

    q1 += pow(2, currpts -1 ) if currpts > 0 else 0

print(q1)

q2 = 0

cardcount = [1 for i in range(len(data))]

def default():
    return []

effects = defaultdict(default)

for i in range(len(data)):
    line = data[i].strip()
    cardnums, mynums = line.split(' | ')
    cardnums = cardnums.split(': ')[1].split(' ')

    mynums = mynums.split(' ')

    currpts = 0

    for mynum in mynums:
        if mynum in cardnums and mynum != "":
            currpts+=1
        

    for j in range(i+1, i+currpts+1):
        effects[i].append(j)

for i in range(len(data)): 
    newcards = effects[i]
    for newcard in newcards:
        cardcount[newcard] += cardcount[i]

q2 = sum(cardcount)

print(q2)
