from typing import Self


class JunctionBox(object):
    def __init__(self, coords: tuple[int]):
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]

    def distance_sq(self, other: Self):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 +   (self.z - other.z) ** 2


class BoxeSet(object):
    def __init__(self):
        self.junction_boxes: list[JunctionBox] = []
        self.distances: list[int] = []
        self.coord_id = []
        self.connections: list[set[int]] = []
        self.connected = []
        self.all_con = False

    def calculate_distance(self):
        for id_box1 in range(len(self.junction_boxes)):
            for id_box2 in range(id_box1+1, len(self.junction_boxes)):
                self.distances.append(self.junction_boxes[id_box1].distance_sq(self.junction_boxes[id_box2]))
                self.coord_id.append((id_box1, id_box2))

    @property
    def circuit_length(self):
        return [len(set(circuit)) for circuit in self.connections]

    def connect(self, id_box1, id_box2):
        if (id_box1 in self.connected) and (id_box2 not in self.connected):
            for circuit in self.connections:
                if id_box1 in circuit:
                    circuit.add(id_box2)
                    self.connected.append(id_box2)
                    return
        if (id_box2 in self.connected) and (id_box1 not in self.connected):
            for circuit in self.connections:
                if id_box2 in circuit:
                    circuit.add(id_box1)
                    self.connected.append(id_box1)
                    return
        if id_box2 in self.connected and id_box1 in self.connected:
            circuit_to_connect = []
            for circuit in self.connections:
                if id_box2 in circuit:
                    circuit_to_connect.append(circuit)
                if id_box1 in circuit:
                    circuit_to_connect.append(circuit)
            self.connections.remove(circuit_to_connect[0])
            try:
                self.connections.remove(circuit_to_connect[1])
            except ValueError:
                pass
            self.connections.append(set(list(circuit_to_connect[0]) + list(circuit_to_connect[1])))
            return
        self.connected.append(id_box1)
        self.connected.append(id_box2)
        self.connections.append(set([id_box1, id_box2]))

    @property
    def not_all_connected(self):
        all_connected = (len(self.connected) == len(self.junction_boxes))
        return (len(self.connections) != 1) or (not all_connected)

    def connect_mins(self):
        ordered_distance = sorted(self.distances)
        num_op = 0
        while self.not_all_connected:
            id_min = self.distances.index(ordered_distance[num_op])
            num_op += 1
            box1_id, box2_id = self.coord_id[id_min]
            self.connect(box1_id, box2_id)
            if num_op % 100 == 0:
                print(num_op, len(self.connections))
        return self.junction_boxes[box1_id].x * self.junction_boxes[box2_id].x


box_set = BoxeSet()
with open('input.txt', 'r') as file:
    for line in file:
        coords = tuple([int(coord) for coord in line.split(',')])
        box_set.junction_boxes.append(JunctionBox(coords))

box_set.calculate_distance()
print(box_set.connect_mins())
