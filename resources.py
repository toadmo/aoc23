numbers = "0987654321"
lowerletters = "abcdefghijklmnopqrstuvwxyz"
upperletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# def getNeighborsWithDiag(x, y, x_len, y_len):
#     neigh = []
#     if x > 0:
#         neigh.append((x-1, y))

#     if x < x_len - 2:
#         neigh.append((x+1, y))

#     if y > 0:
#         neigh.append((x, y-1))
    
#     if y < y_len - 2:
#         neigh.append((x, y+1))

#     if x > 0 and y < y_len - 2:
#         neigh.append((x-1, y+1))

#     if x < x_len - 2 and y < y_len - 2:
#         neigh.append((x+1, y+1))

#     if x > 0 and y > 0 :
#         neigh.append((x-1, y-1))

#     if x < x_len - 2 and y > 0:
#         neigh.append((x+1, y-1))

#     return neigh

def getNeighbors(x, y, x_len, y_len):
    neigh = []
    if x > 0:
        neigh.append((x-1, y))

    if x < x_len - 2:
        neigh.append((x+1, y))

    if y > 0:
        neigh.append((x, y-1))
    
    if y < y_len - 2:
        neigh.append((x, y+1))

    return neigh

def getNeighborsWithDiag(x, y, x_len, y_len):
    neigh = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if not i == 0 and not j == 0 and x + i > 0 and x + i < x_len - 2 and y + j > 0 and y + j < y_len - 2 :
                neigh.append(x+i, y+j)

    return neigh

def intersect(a,b,c,d):
    return not (b < c or d < a)