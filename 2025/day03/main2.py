total_joltage = 0
all_val = []

with open('input.txt', 'r') as file:
    for line in file:
        string_value = ""
        index_value = 0
        for num_char in range(12, 0,-1):
            for current_value in ["9", "8", "7", "6", "5", "4", "3", "2", "1"]:
                try:
                    test_to = line[index_value:len(line)-num_char]
                    index_value += test_to.index(current_value) + 1
                    string_value += current_value
                    break
                except:
                    pass
        total_joltage += int(string_value)

print(total_joltage)
