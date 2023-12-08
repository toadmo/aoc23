from collections import defaultdict, Counter

with open("input.txt", "r") as f:
    data = f.readlines()

q1 = 1

numbers = "0987654321"
lowerletters = "abcdefghijklmnopqrstuvwxyz"
upperletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

times = data[0].split()[1:]
distances = data[1].split()[1:]

print(times, distances)

records = []

for i in range(len(times)):
    time, distance = int(times[i]),  int(distances[i])
    record_count = 0
    for j in range(time + 1):
        if (time - j) * j > distance:
            record_count += 1
    records.append(record_count)

for record in records:
    q1= q1 *record

print(q1)

time = int("".join(times))
distance = int("".join(distances))

q2 = 0
for j in range(time + 1):
    if (time - j) * j > distance:
        record_count += 1
q2 = record_count
print(q2)
