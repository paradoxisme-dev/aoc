from typing import Self


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

    def fusion_if_ok(self, other_range: Self):
        if self.start <= other_range.finish or self.finish >= other_range.start:
            self._start = self.start if self.start < other_range.start else other_range.start
            self._finish = self.finish if self.finish > other_range.finish else other_range.finish
            return True
        return False

range_list = []
number_fresh = 0
with open("input.txt", 'r') as file:
    for line in file:
        is_in_a_range = False
        line = line[:-1]
        if line == "":
            break
        range_values = line.split('-')
        new_range = RangeFreshID(int(range_values[0]), int(range_values[1]))
        for current_range in range_list:
            if current_range.fusion_if_ok(new_range):
                is_in_a_range = True
                break
        if not is_in_a_range:
            range_list.append(new_range)

has_in_a_range = True
while has_in_a_range:
    has_in_a_range = False
    new_range_list = []
    for currently_tested_range in range_list:
        is_in_a_range = False
        for current_range in range_list:
            if current_range.fusion_if_ok(currently_tested_range):
                is_in_a_range = True
                has_in_a_range = True
                new_range_list.append(currently_tested_range)
                break
        if not is_in_a_range:
            new_range_list.append(new_range)
    if has_in_a_range:
        range_list = new_range_list

for current_range in range_list:
    number_fresh += len(current_range)

print(number_fresh)
