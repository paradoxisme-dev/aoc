class Stock:
    def __init__(self, filename='input.txt'):
        self.stock = []
        with open(filename) as file:
            for line in file:
                self.stock.append(line[:-1])

    @property
    def size_x(self):
        return len(self.stock[0])

    @property
    def size_y(self):
        return len(self.stock)

    def is_accessible(self, x: int, y: int):
        adjacent_count = 0
        for delta_x in [-1, 0, 1]:
            for delta_y in [-1, 0, 1]:
                if delta_x == 0 and delta_y == 0:
                    continue
                if y+delta_y < 0 or y + delta_y > self.size_y-1:
                    continue
                if x+delta_x < 0 or x + delta_x > self.size_x-1:
                    continue
                if self.stock[y+delta_y][x+delta_x] == '@':
                    adjacent_count += 1
        if adjacent_count < 4:
            return True
        return False

    @property
    def number_accessible(self):
        total = 0
        for x in range(self.size_x):
            for y in range(self.size_y):
                if self.stock[y][x] != '@':
                    continue
                if self.is_accessible(x, y):
                    total += 1
        return total

    @property
    def total_count(self):
        total_count = 0
        new_accessible = 1
        while new_accessible != 0:
            new_accessible = self.number_accessible
            total_count += new_accessible
            self.remove_accessible()
        return total_count

    def remove_accessible(self):
        virtual_stock = []
        for y in range(self.size_x):
            new_line = ''
            for x in range(self.size_y):
                if self.stock[y][x] == '.':
                    new_line += '.'
                else:
                    new_line += '.' if self.is_accessible(x, y) else '@'
            virtual_stock.append(new_line)
        self.stock = virtual_stock

    def show_accessible(self):
        for y in range(self.size_x):
            new_line = ''
            for x in range(self.size_y):
                if self.is_accessible(x, y):
                    new_line += 'x' if self.stock[y][x] == '@' else '.'
                else:
                    new_line += self.stock[y][x]
            print(new_line)

s = Stock()
print(s.total_count)
