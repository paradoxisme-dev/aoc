with open('input.txt', 'r') as file:
    for line in file:
        line = line[:-1]
        line_element = line.split('-')
        if len(line_element) == 2:
            min_interval = int(line_element[0])
            max_interval = int(line_element[1])
            print(min_interval, max_interval)
        else:
            if line_element[0] == '':
                continue
            else:
                element = int(line_element[0])
            print(element)
