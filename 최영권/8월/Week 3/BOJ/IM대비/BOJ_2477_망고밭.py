mango = int(input())
direction = []
length = []
for i in range(6):
    d, dist = map(int, input().split())
    direction.append(d)
    length.append(dist)


small_square = 0
for i in range(len(direction)):
    if direction[i % 6] == direction[(i + 2) % 6]:
        small_square = length[(i + 1)%6] * length[i%6]


w_idx = max((i for i in range(6) if direction[i] in (1, 2)), key=lambda i: length[i])
h_idx = max((i for i in range(6) if direction[i] in (3, 4)), key=lambda i: length[i])

large = length[w_idx] * length[h_idx]

print(mango*(large-small_square))   

# mango = int(input())
# direction = []
# length = []
# for i in range(6):
#     d, dist = map(int, input().split())
#     direction.append(d)
#     length.append(dist)

# w_idx = max((i for i in range(6) if direction[i] in (1, 2)), key=lambda i: length[i])
# h_idx = max((i for i in range(6) if direction[i] in (3, 4)), key=lambda i: length[i])

# large = length[w_idx] * length[h_idx]
# small = length[(w_idx + 3) % 6] * length[(h_idx + 3) % 6]


# print(mango*(large-small))   