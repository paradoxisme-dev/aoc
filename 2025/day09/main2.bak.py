coord_red_tiles: list[list[int]] = []
with open("input_ex.txt", 'r') as file:
    for line in file:
        coord_red_tiles.append([int(coord) for coord in line.split(',')])

red_tile_lines_H: dict[int, list[int]] = {}
for coord in coord_red_tiles:
    if coord[0] not in red_tile_lines_H:
        red_tile_lines_H[coord[0]] = []
    red_tile_lines_H[coord[0]].append(coord[1])
for line_id in red_tile_lines_H:
    red_tile_lines_H[line_id] = sorted(red_tile_lines_H[line_id])

red_tile_lines_V: dict[int, list[int]] = {}
for coord in coord_red_tiles:
    if coord[1] not in red_tile_lines_V:
        red_tile_lines_V[coord[1]] = []
    red_tile_lines_V[coord[1]].append(coord[1])
for line_id in red_tile_lines_V:
    red_tile_lines_H[line_id] = sorted(red_tile_lines_V[line_id])

surfaces: list[int] = []
for tile_id1 in range(len(coord_red_tiles)):
    for tile_id2 in range(tile_id1 + 1, len(coord_red_tiles)):
        coord1 = coord_red_tiles[tile_id1]
        coord2 = coord_red_tiles[tile_id2]
        coord_max_x = max([coord1[0], coord2[0]])
        coord_min_x = min([coord1[0], coord2[0]])
        coord_max_y = max([coord1[1], coord2[1]])
        coord_min_y = min([coord1[1], coord2[1]])
        min_y_possible = min([red_tile_lines_H[coord_min_x][0], red_tile_lines_H[coord_max_x][0]])
        max_y_possible = max([red_tile_lines_H[coord_min_x][-1], red_tile_lines_H[coord_max_x][-1]])
        min_x_possible = min([red_tile_lines_V[coord_min_y][0], red_tile_lines_V[coord_max_y][0]])
        max_x_possible = max([red_tile_lines_V[coord_min_y][-1], red_tile_lines_V[coord_max_y][-1]])
        if min_y_possible < coord_min_y:
            continue
        if max_y_possible > coord_max_y:
            continue
        if max_x_possible > coord_max_x:
            continue
        if min_x_possible < coord_min_x:
            continue
        print(coord1, coord2)
        surfaces.append((abs(coord1[0]-coord2[0]) + 1) * (abs(coord1[1]-coord2[1]) + 1))

print(max(surfaces))
