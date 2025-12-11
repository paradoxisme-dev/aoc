from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np


class Machine(object):
    def __init__(self, description_line):
        line = description_line[:-1]
        line_cut = line.split(' ')
        self.buttons = [
            [int(led) for led in button[1:-1].split(',')]
            for button in line_cut[1:-1]
        ]
        self.jolt_counter = np.array([
            int(value) for value in line_cut[-1][1:-1].split(',')
        ])
        self.eq = np.array([
            [1 if i in button else 0 for button in self.buttons] for i in range(len(self.jolt_counter))
        ])
        self.c = np.array([1] * len(self.eq[0]))

    @property
    def number_step(self):
        bounds = Bounds(lb=np.array([0] * len(self.eq[0])), ub=np.array([np.inf] * len(self.eq[0])))
        linear_constraint = LinearConstraint(A=self.eq, lb=self.jolt_counter, ub=self.jolt_counter)
        integrality = np.ones_like(self.c)
        return milp(
            c=self.c,
            constraints=linear_constraint,
            bounds=bounds,
            integrality=integrality,
        )
        


number_step_for_all = 0
with open("input.txt", 'r') as file:
    machine_number = 0
    for line in file:
        machine_number += 1
        machine = Machine(line)
        result = machine.number_step
        if result.success:
            number_step_for_all += int(result.fun)
        else:
            print(f"Message: {result.message}")


print(number_step_for_all)
