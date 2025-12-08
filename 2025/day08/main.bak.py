from typing import Self


class JunctionBox(object):
    def __init__(self, coords: tuple[int]):
        self.coords: tuple[int] = coords
        self.connected: list[Self] = [self]

    @property
    def x(self):
        return self.coords[0]

    @property
    def y(self):
        return self.coords[1]

    @property
    def z(self):
        return self.coords[2]

    @property
    def circuit(self):
        return (box.coords for box in self.connected)

    def distance_sq(self, other: Self):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 +   (self.z - other.z) ** 2

    def connect(self, other: Self):
        for box in self.connected:
            if other not in box.connected:
                box.connected.append(other)
            if box not in other.connected:
                other.connected.append(box)

    def __repr__(self):
        return str(self.coords)


class BoxeSet(object):
    def __init__(self):
        self.junction_boxes: list[JunctionBox] = []
        self.distances: list[int] = []
        self.coord_id = []

    def calculate_distance(self):
        for id_box1 in range(len(self.junction_boxes)):
            for id_box2 in range(id_box1+1, len(self.junction_boxes)):
                self.distances.append(self.junction_boxes[id_box1].distance_sq(self.junction_boxes[id_box2]))
                self.coord_id.append((id_box1, id_box2))

    def boxes_from_index(self, index):
        return self.coord_id[index]

    @property
    def all_connected(self):
        for box in self.junction_boxes:
            if len(box.connected) <= 1:
                return False
        return True

    def connect_mins(self):
        max_value = max(self.distances) + 1
        while not self.all_connected:
            min_value = min(self.distances)
            id_min = self.distances.index(min_value)
            self.distances[id_min] = max_value
            box1_id, box2_id = self.boxes_from_index(id_min)
            self.junction_boxes[box1_id].connect(self.junction_boxes[box2_id])


box_set = BoxeSet()
with open('input_ex.txt', 'r') as file:
    for line in file:
        coords = tuple([int(coord) for coord in line.split(',')])
        box_set.junction_boxes.append(JunctionBox(coords))

box_set.calculate_distance()
box_set.connect_mins()
