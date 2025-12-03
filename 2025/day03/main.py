total_joltage = 0

with open('input.txt', 'r') as file:
    for line in file:
        for current_value in ["9", "8", "7", "6", "5", "4", "3", "2", "1"]:
            try:
                index_value = line[:len(line)-2].index(current_value)
                string_value = current_value
                break
            except:
                pass
        for current_value in ["9", "8", "7", "6", "5", "4", "3", "2", "1"]:
            try:
                line[index_value+1:].index(current_value)
                string_value += current_value
                break
            except:
                pass
        total_joltage += int(string_value)

print(total_joltage)
