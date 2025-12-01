current_position = 50
number_pointing_zero = 0
with open("input.txt", 'r') as f:
    for line in f:
        if line[0] == 'R':
            current_position += int(line[1:])
        else:
            current_position -= int(line[1:])
        current_position %= 100
        if current_position == 0:
            number_pointing_zero += 1

print(number_pointing_zero)
