import numpy as np

xmin = 10000000000000000000000
xmax = 0
ymin = 10000000000000000000000
ymax = 0
with open("input.txt", 'r') as file:
    for line in file:
        coord = [int(coord) for coord in line.split(',')]
        xmin = coord[0] if coord[0] < xmin else xmin
        ymin = coord[1] if coord[1] < ymin else ymin
        xmax = coord[0] if coord[0] > xmax else xmax
        ymax = coord[1] if coord[1] > ymax else ymax

print(xmin, ymin, xmax, ymax)
new_array = np.zeros(((xmax-xmin), (ymax-ymin)), dtype=np.bool)
print(new_array)
