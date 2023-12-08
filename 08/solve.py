from collections import defaultdict, Counter
import operator
import math

with open("input.txt", "r") as f:
    data = f.read()

q1 = 0

numbers = "0987654321"
lowerletters = "abcdefghijklmnopqrstuvwxyz"
upperletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


directions, instructions = data.split('\n\n')

instructions_dict = {}

for instruction in instructions.split('\n'):
    key, valtup = instruction.strip().split(' = ')
    valtup = valtup[1:-1].split(', ')
    instructions_dict[key] = valtup


curr = "AAA"

index = 0

while curr != "ZZZ":
    if directions[index] == "R":
        curr = instructions_dict[curr][1]
    else:
        curr = instructions_dict[curr][0]

    q1 += 1
    index += 1

    if index == len(directions):
        index = 0

print(q1)

starters = []

index = 0

for starter in instructions_dict.keys():
    if starter[-1] == "A":
        starters.append(starter)

def default():
    return 0

z_indices = defaultdict(default)


while True:
    if directions[index % len(directions)] == "R":
        starters = [instructions_dict[curr][1] for curr in starters]
    else:
        starters = [instructions_dict[curr][0] for curr in starters]

    for starter in starters:
        if starter[-1] == "Z":
            z_indices[starter] = index + 1

    if sum([1 for val in z_indices.values()]) == len(starters):
        break

    index += 1


q2 = 1
for i in z_indices.values():
    q2 = q2*i//math.gcd(q2, i)

print(q2)
