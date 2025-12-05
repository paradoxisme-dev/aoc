class RangeFreshID(object):
    def __init__(self, start: int, finish: int):
        self._start = start
        self._finish = finish

    @property
    def start(self):
        return self._start
    
    @property
    def finish(self):
        return self._finish

    def in_range(self, tested_id):
        return tested_id >= self._start and tested_id <= self._finish

    def __len__(self):
        return self._finish - self._start + 1
    
    def __repr__(self):
        return f'[{self._start}-{self._finish}]'

class RangeList(object):
    def __init__(self):
        self._range_list: list[RangeFreshID] = []

    def insert_new_range(self, new_range: RangeFreshID):
        to_remove: list[RangeFreshID] = []
        for current_range in self._range_list:
            if new_range.finish < current_range.start or new_range.start < current_range.finish:
                to_remove.append(current_range)
        for removed_range in to_remove:
            self._range_list.remove(removed_range)
        print(new_range, to_remove)
        to_remove.append(new_range)
        new_start = min([current_range.start for current_range in to_remove])
        new_finish = max([current_range.finish for current_range in to_remove])
        self._range_list.append(RangeFreshID(new_start, new_finish))

    @property
    def total_size(self):
        number_fresh = 0
        print(self._range_list)
        for current_range in self._range_list:
            number_fresh += len(current_range)
        return number_fresh

range_list = RangeList()
number_fresh = 0
with open("input.txt", 'r') as file:
    for line in file:
        is_in_a_range = False
        line = line[:-1]
        if line == "":
            break
        range_values = line.split('-')
        range_list.insert_new_range(RangeFreshID(int(range_values[0]), int(range_values[1])))

print(range_list.total_size)
