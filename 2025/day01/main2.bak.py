current_position = 50
number_zero = 0
with open("input.txt", 'r') as f:
    old_zero = False
    for line in f:
        displacement_value = int(line[1:])
        if line[0] == 'R':
            current_position += displacement_value
        else:
            current_position -= displacement_value
        if current_position < 0:
            number_zero += abs(current_position // 100)
            if old_zero:
                number_zero -= 1
            old_zero = False
            if current_position % 100 == 0:
                number_zero += 1
                old_zero = True
        elif current_position % 100 == 0:
            old_zero = True
            if current_position > 100:
                number_zero += current_position // 100
            else:
                number_zero += 1
        else:
            number_zero += current_position // 100
            old_zero = False
        current_position %= 100

print(number_zero)