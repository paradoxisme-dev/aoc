import numpy as np

xmax = 0
ymax = 0
ymin = 100000000000000
coord_red_tiles: list[list[int]] = []
with open("input.txt", 'r') as file:
    for line in file:
        coord = [int(coord) for coord in line.split(',')]
        coord_red_tiles.append(coord)
        xmax = coord[0] if coord[0] > xmax else xmax
        ymax = coord[1] if coord[1] > ymax else ymax
        ymin = coord[1] if coord[1] < ymin else ymin

print(xmax, ymax)
new_array = np.zeros((xmax+1, ymax+1), dtype=np.bool)

red_tile_col: dict[int, list[int]] = {}
red_tile_line: dict[int, list[int]] = {}
for coord in coord_red_tiles:
    if coord[0] not in red_tile_line:
        red_tile_line[coord[0]] = []
    red_tile_line[coord[0]].append(coord[1])
    if coord[1] not in red_tile_col:
        red_tile_col[coord[1]] = []
    red_tile_col[coord[1]].append(coord[0])
    new_array[coord[0], coord[1]] = True

for line_id in red_tile_line:
    min_in_line = min(red_tile_line[line_id])
    max_in_line = max(red_tile_line[line_id])
    new_array[line_id, min_in_line:max_in_line] = True

for col_id in red_tile_col:
    min_in_col = min(red_tile_col[col_id])
    max_in_col = max(red_tile_col[col_id])
    new_array[min_in_col:max_in_col, col_id] = True

print("make surface")

for id_line, line in enumerate(new_array):
    if id_line < ymin:
        continue
    all_indices = np.where(line == True)[0]
    if all_indices.size > 1:
        min_x = all_indices[0]
        max_x = all_indices[-1]
        new_array[id_line, min_x:max_x] = new_array[id_line, min_x:max_x]|new_array[id_line-1, min_x:max_x]

print("calculate surfaces")

surfaces: list[int] = []
nb_calc = 0
for tile_id1 in range(len(coord_red_tiles)):
    for tile_id2 in range(tile_id1 + 1, len(coord_red_tiles)):
        nb_calc += 1
        if nb_calc  % 100 == 0:
            print(nb_calc)
        coord1 = coord_red_tiles[tile_id1]
        coord2 = coord_red_tiles[tile_id2]
        max_x = coord1[0] if coord1[0] > coord2[0] else coord2[0]
        max_y = coord1[1] if coord1[1] > coord2[1] else coord2[1]
        min_x = coord1[0] if coord1[0] < coord2[0] else coord2[0]
        min_y = coord1[1] if coord1[1] < coord2[1] else coord2[1]
        if np.all(new_array[min_x:max_x, min_y:max_y]):
            surfaces.append((abs(coord1[0]-coord2[0]) + 1) * (abs(coord1[1]-coord2[1]) + 1))

print(max(surfaces))
