# 3

matrix = [
    [1, 2],
    [3, 4]
]

even = []
odd = []

flat = []

for row in matrix:
    for val in row:
        flat.append(val)

for i in range(len(flat)):
    if i % 2 == 0:
        even.append(flat[i])
    else:
        odd.append(flat[i])

even.sort()
odd.sort()

print(even[-2] + odd[-2])