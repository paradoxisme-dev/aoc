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
        self.record_len = 25

    def check_stat(self, stat: list[int]):
        has_inf = False
        for i in range(self._stat_len):
            if self.jolt_counter[i] > stat[i]:
                has_inf = True
            elif self.jolt_counter[i] < stat[i]:
                return 1
        return -1 if has_inf else 0

    def bigger(self, stat1, stat2) -> int:
        """
        1 = all part stat1 >= stat2
        -1 = all part stat1 <= stat2
        0 = all part stat1 == stat2
        -2 ???
        """
        dif = 0
        for i in range(len(stat1)):
            if stat1[i] > stat2[i]:
                dif = 1 if (dif==0) or (dif==1) else -2
            elif stat1[i] == stat2[i]:
                dif = 0 if dif==0 else dif
            else:
                dif = -1 if (dif==0) or (dif==-1) else -2

    def reduce_stats_size(self):
        bigger_stat = self.stats[0]
        tmp_stats = set()
        for stat in self.stats:
            comparator = self.bigger(bigger_stat, stat)
            if comparator == -1:
                bigger_stat = stat
            if comparator == -2:
                tmp_stats.add(stat)
        new_stats = set([bigger_stat])
        for stat in tmp_stats:
            comparator = self.bigger(bigger_stat, stat)
            if comparator == -2:
                new_stats.add(stat)
        self.stats = new_stats

    def check_all_button(self):
        self.number_step += 1
        new_stats = set()
        bigger_stat = None
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
                    if bigger_stat is None:
                        bigger_stat = new_stat
                    new_stats.add(tuple(new_stat))
        self.stats = new_stats
        if len(self.stats) > self.record_len:
            self.record_len = len(self.stats)
            self.reduce_stats_size
        return True


number_step_for_all = 0
with open("input.txt", 'r') as file:
    machine_number = 0
    for line in file:
        machine_number += 1
        machine = Machine(line)
        while machine.check_all_button():
            print(machine_number, len(machine.stats), machine.number_step)
        number_step_for_all += machine.number_step


print(number_step_for_all)
