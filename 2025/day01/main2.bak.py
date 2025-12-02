current_position = 50
number_zero = 0
with open("input.txt", 'r') as f:
    for line in f:
        displacement_value = int(line[1:])
        if line[0] == 'R':
            current_position += displacement_value
        else:
            current_position -= displacement_value
        old_position = current_position
        current_position %= 100
        if old_position != current_position:
            number_zero += abs(old_position // 100)

print(number_zero)