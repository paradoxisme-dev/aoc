coord_red_tiles: list[list[int]] = []
with open("input.txt", 'r') as file:
    for line in file:
        coord_red_tiles.append([int(coord) for coord in line.split(',')])

surfaces: list[int] = []
for tile_id1 in range(len(coord_red_tiles)):
    for tile_id2 in range(tile_id1 + 1, len(coord_red_tiles)):
        coord1 = coord_red_tiles[tile_id1]
        coord2 = coord_red_tiles[tile_id2]
        surfaces.append((abs(coord1[0]-coord2[0]) + 1) * (abs(coord1[1]-coord2[1]) + 1))

print(max(surfaces))
