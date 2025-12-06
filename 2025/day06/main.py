from functools import reduce


total = 0
columns: list[list[int]] = []

with open('input.txt', 'r') as file:
    for line in file:
        line = line[:-1]
        column_elements = line.split(' ')
        while True:
            try:
                column_elements.remove('')
            except ValueError:
                break
        if column_elements[0] in ['*', '+']:
            break
        for num_column, element in enumerate(column_elements):
            if len(columns) <= num_column:
                columns.append([])
            columns[num_column].append(int(element))
    for num_column, operation in enumerate(column_elements):
        if operation == '+':
            total += sum(columns[num_column])
        elif operation == '*':
            total += reduce(lambda x, y: x*y, columns[num_column])

print(total)
