from collections import defaultdict, Counter

with open("input.txt", "r") as f:
    data = f.readlines()


q1 = 0



for line in data:
    ind, cube_count = line.split(': ')
    ind = int(ind[5:])

    winnable = True

    cubes = cube_count.split('; ')
    for cube in cubes:
        color_dict = {"red": 0, "green": 0, "blue": 0}

        draws = cube.split(', ')
        for draw in draws:
            num_cubes, color_cube = draw.split(' ')
            color_dict[color_cube.strip()] += int(num_cubes)
        

        if color_dict['red'] > 12 or color_dict['green'] > 13 or color_dict['blue'] > 14:
            winnable = False
            break

    if winnable:
        q1 += ind 
    



print(q1)

q2 = 0

for line in data:
    ind, cube_count = line.split(': ')
    ind = int(ind[5:])

    winnable = True

    cubes = cube_count.split('; ')

    reds = []
    blues = []
    greens = []

    for cube in cubes:
        color_dict = {"red": 0, "green": 0, "blue": 0}

        draws = cube.split(', ')
        for draw in draws:
            num_cubes, color_cube = draw.split(' ')
            color_dict[color_cube.strip()] += int(num_cubes)
            
        

        reds.append(color_dict['red'])
        greens.append(color_dict['green'])
        blues.append(color_dict['blue'])

    q2 += (max(reds) * max(blues) * max(greens))

print(q2)
    