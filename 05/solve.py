from collections import defaultdict, Counter

with open("input.txt", "r") as f:
    data = f.read()

q1 = 0

numbers = "0987654321"
lowerletters = "abcdefghijklmnopqrstuvwxyz"
upperletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

data = data.split('\n\n')

seeds = [int(seed) for seed in data[0].split()[1:]]

def intersect(a,b,c,d):
    return not (b < c or d < a)

for i in range(1, len(data)):
    curr_map = {}

    for seed in seeds:
        curr_map[seed] = seed

    curr_data = data[i].split('\n')
    for line in curr_data[1:]:
        mappings = [int(mapping) for mapping in line.split(' ')]
        dest = mappings[0]
        source = mappings[1]
        range_len = mappings[2]
        for seed in seeds:
            if seed in range(source, source+range_len):
                diff = (source+range_len) - seed
                curr_map[seed] = (dest+range_len) - diff
        
            
    seeds = curr_map.values()

q1 = min(seeds)

print(q1)

seeds = [int(seed) for seed in data[0].split()[1:]]

bounds = [(seeds[i], seeds[i] + seeds[i+1]-1) for i in range(0, len(seeds), 2)]

for i in range(1, len(data)):

    curr_data = data[i].split('\n')
    new_bounds = []

    while len(bounds) > 0:
        x, y = bounds.pop()

        mapped = False

        for line in curr_data[1:]:
            mappings = [int(mapping) for mapping in line.split(' ')]

            dest = mappings[0]
            source = mappings[1]
            range_len = mappings[2]-1

            if intersect(x, y, source, source+range_len):

                new_x = max(source, x) - source + dest
                new_y = min(source+range_len, y) - source + dest

                new_bounds.append((new_x, new_y))

                if max(source, x) > x:
                    bounds.append([x, max(source, x)-1])
                if min(source+range_len, y) < y:
                    bounds.append((min(source+range_len, y)+1, y))
                mapped = True
                break

        if not mapped:
            new_bounds.append((x,y))
                

    bounds = new_bounds
    
q2 = min(bounds)[0]

print(q2)
