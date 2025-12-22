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
current_position = 50
number_zero = 0
with open("input.txt", 'r') as f:
    for line_nb, line in enumerate(f):
        displacement_value = int(line[1:])
        if line[0] == 'R':
            current_position += displacement_value
            for _ in range(displacement_value):
                rotor.rigth()
        else:
            for _ in range(displacement_value):
                rotor.left()
            current_position -= displacement_value
        old_number_zero = number_zero
        if current_position < 0:
            number_zero += abs(current_position // 100)-1
        else:
            number_zero += current_position // 100
        current_position %= 100
        if current_position == 0:
            number_zero += 1
        if number_zero != rotor.zero_count:
            print('old_number_zero', old_number_zero)
            print(current_position)
            print('current_position : ', current_position)
            print('rotor.current : ', rotor.current)
            print('line : ', line[:-1], line_nb)
            print('number_zero != rotor.zero_count', number_zero, rotor.zero_count)            

print(rotor.zero_count)
