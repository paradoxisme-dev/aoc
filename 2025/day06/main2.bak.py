from functools import reduce


total = 0
columns: list[list[str]] = []

with open('input_ex.txt', 'r') as file:
    for line in file:
        line = line[:-1]
        line = line[::-1]
        column_elements = line.split(' ')
        if column_elements.count('+') != 0:
            break
        while True:
            try:
                id_empty_column = column_elements.index('')
                if len(column_elements) > id_empty_column+1 and column_elements[id_empty_column+1] != '':
                    column_elements[id_empty_column+1] = ' ' + column_elements[id_empty_column+1]
                column_elements.remove('')
            except ValueError:
                break
        for num_column, element in enumerate(column_elements):
            if len(columns) <= num_column:
                columns.append([])
            for number_id, character in enumerate(element):
                if len(columns[num_column]) <= number_id:
                    columns[num_column].append('')
                columns[num_column][number_id] += character
    while True:
        try:
            column_elements.remove('')
        except ValueError:
            break
    for col in columns:
        print(col)
    for num_column, operation in enumerate(column_elements):
        num_col = [el.strip() for el in columns[num_column]]
        while True:
            try:
                num_col.remove('')
            except ValueError:
                break
        num_col = [int(el) for el in num_col]
        print(num_col, operation)
        if operation == '+':
            total += sum(num_col)
        elif operation == '*':
            total += reduce(lambda x, y: x*y, num_col)

print(total)
