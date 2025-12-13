import numpy as np
from enum import Enum


class IsPackable(Enum):
    YES = 1
    NO = 2
    PROBABLY = 3
    PROBABLY_NOT = 4
    UNDESCIDE = 5


class Gift:
    def __init__(self, lines):
        self.shape = np.array([[False]*3]*3)
        for id_line, line in enumerate(lines):
            for id_char, char in enumerate(line):
                self.shape[id_line, id_char] = True if char == '#' else False
        self.shapes = []
        new_shape = self.shape
        for _ in range(4):
            new_shape = np.rot90(new_shape, k=-1)
            self.shapes.append(new_shape)
        new_shape = np.fliplr(self.shape)
        for _ in range(4):
            new_shape = np.rot90(new_shape, k=-1)
            self.shapes.append(new_shape)

    @property
    def min_size(self):
        return self.shape.sum()

class Box:
    def __init__(
            self,
            length,
            height,
            gifts: list[Gift],
            quantities: list[int]
        ):
        self.box_size = (length, height)
        self.gifts = gifts
        self.quantities = quantities

    @property
    def max_size(self):
        return self.box_size[0] * self.box_size[1]

    @property
    def is_packable(self):
        full_gift_size = sum([
            quantity * gift.min_size
            for quantity, gift in zip(self.quantities, self.gifts)
        ])
        if full_gift_size > self.max_size:
            return IsPackable.NO
        if sum([
            quantity * 9
            for quantity in self.quantities
        ]) < self.max_size:
            return IsPackable.YES
        return IsPackable.UNDESCIDE


shapes: list[Gift] = []
boxes: list[Box] = []
min_nb_packable = 0
max_nb_packable = 0
with open('input.txt', 'r') as file:
    new_shape = None
    for line in file:
        line = line[:-1]
        if new_shape is not None:
            new_shape.append(line)
            if len(new_shape) == 3:
                shapes.append(Gift(new_shape))
                new_shape = None
        line_el = line.split(':')
        if len(line_el) == 2:
            if line_el[-1] == '':
                new_shape = []
            else:
                quantities = [
                    int(value)
                    for value in line_el[-1].split(' ')
                    if value != ''
                ]
                bax_shape = line_el[0].split('x')
                boxes.append(Box(
                    int(bax_shape[0]),
                    int(bax_shape[1]),
                    gifts=shapes,
                    quantities=quantities
                ))
    for box in boxes:
        is_packable = box.is_packable
        if is_packable == IsPackable.YES:
            min_nb_packable += 1
        if is_packable != IsPackable.NO:
            max_nb_packable += 1

print('[' + str(min_nb_packable) + ', ' + str(max_nb_packable) + ']')
