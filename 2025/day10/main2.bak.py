class Machine(object):
    def __init__(self, description_line):
        line = description_line[:-1]
        line_cut = line.split(' ')
        self.buttons = [
            [int(led) for led in button[1:-1].split(',')]
            for button in line_cut[1:-1]
        ]
        self.jolt_counter = [
            int(value) for value in line_cut[-1][1:-1].split(',')
        ]
        self.number_step = 0
        self._stat_len = len(self.jolt_counter)
        self.stats = set([tuple([0] * self._stat_len)])

    def check_stat(self, stat: list[int]):
        has_inf = False
        for i in range(self._stat_len):
            if self.jolt_counter[i] > stat[i]:
                has_inf = True
            elif self.jolt_counter[i] < stat[i]:
                return 1
        return -1 if has_inf else 0

    def check_all_button(self):
        self.number_step += 1
        new_stats = set()
        for button in self.buttons:
            for stat in self.stats:
                new_stat = list(stat)
                for button_value in button:
                    new_stat[button_value] += 1
                check = self.check_stat(new_stat)
                if check == 0:
                    return False
                if check == 1:
                    continue
                if check == -1:
                    new_stats.add(tuple(new_stat))
        self.stats = new_stats
        return True


number_step_for_all = 0
with open("input.txt", 'r') as file:
    for line in file:
        machine = Machine(line)
        while machine.check_all_button():
            print(len(machine.stats), machine.number_step)
        number_step_for_all += machine.number_step


print(number_step_for_all)
