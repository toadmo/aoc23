from collections import defaultdict, Counter
import operator

with open("input.txt", "r") as f:
    data = f.readlines()

q1 = 0

numbers = "0987654321"
lowerletters = "abcdefghijklmnopqrstuvwxyz"
upperletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ordering = "AKQJT98765432"[::-1]

all_hands = []
all_weights = {}

for i in range(len(data)):
    line = data[i]
    hand, weight = line.split()
    hand_count = Counter(hand).most_common()
    # hand_count = [[x, y] for x, y in hand_count]
    all_hands.append((hand_count, i, hand))
    all_weights[hand] = int(weight)
    

sorted_hands = sorted(all_hands, key=lambda k: ([elem[1] for elem in k[0]], [ordering.index(elem[0]) for elem in k[2]]))
# print(sorted_hands)


for i in range(len(sorted_hands)):
    hand_count, index, hand = sorted_hands[i]
    # print((i+1)*all_weights[hand])
    q1 += (i+1)*all_weights[hand]


print(q1)

q2 = 0

ordering = "AKQT98765432J"[::-1]


all_hands = []

for i in range(len(data)):
    line = data[i]
    hand, weight = line.split()
    hand_count = Counter(hand).most_common()
    new_hand_count = []
    found_j = False
    # print(hand_count)
    for i in range(len(hand_count)):
        if hand_count[i][0] != "J" or hand == "JJJJJ":
            new_hand_count.append(hand_count[i])
        else:
            found_j = True
            j_count = hand_count[i][1]
    if found_j:
        new_hand_count[0] = (new_hand_count[0][0], new_hand_count[0][1] + j_count)

    all_hands.append((new_hand_count, i, hand))
    
    

sorted_hands = sorted(all_hands, key=lambda k: ([elem[1] for elem in k[0]], [ordering.index(elem[0]) for elem in k[2]]))
# print(sorted_hands)


for i in range(len(sorted_hands)):
    hand_count, index, hand = sorted_hands[i]
    print(hand)
    print((i+1)*all_weights[hand])
    q2 += (i+1)*all_weights[hand]

print(q2)