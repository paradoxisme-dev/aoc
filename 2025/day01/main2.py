class Rotor:
    def __init__(self):
        self.current = 50
        self.zero_count = 0

    def rigth(self):
        self.current += 1
        if self.current == 100:
            self.zero_count += 1
            self.current = 0

    def left(self):
        self.current -= 1
        if self.current == -1:
            self.current = 99
        if self.current == 0:
            self.zero_count += 1

rotor = Rotor()
with open("input.txt", 'r') as f:
    for line in f:
        displacement_value = int(line[1:])
        if line[0] == 'R':
            for _ in range(displacement_value):
                rotor.rigth()
        else:
            for _ in range(displacement_value):
                rotor.left()

print(rotor.zero_count)
