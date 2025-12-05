class RangeFreshID(object):
    def __init__(self, start: int, finish: int):
        self._start = start
        self._finish = finish

    def in_range(self, tested_id):
        return tested_id >= self._start and tested_id <= self._finish

range_list = []
creating_range = True
number_fresh = 0
with open("input.txt", 'r') as file:
    for line in file:
        line = line[:-1]
        if line == "":
            creating_range = False
            continue
        if creating_range:
            range_values = line.split('-')
            range_list.append(RangeFreshID(int(range_values[0]), int(range_values[1])))
        else:
            tested_id = int(line)
            for current_range in range_list:
                if current_range.in_range(tested_id):
                    number_fresh += 1
                    break

print(number_fresh)
