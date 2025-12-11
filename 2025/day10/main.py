class Machine:
    def __init__(self, description_line):
        line = description_line[:-1]
        line_cut = line.split(' ')
        goal_rep = line_cut[0][1:-1]
        self.display_size = len(goal_rep)
        self.goal_conf = 0
        for id_value, value in enumerate(goal_rep[::-1]):
            if value == '#':
                self.goal_conf += 1 << id_value

        self.buttons = []
        for button in line_cut[1:-1]:
            new_button_rep = 0
            button_toggle = [int(led) for led in button[1:-1].split(',')]
            for led_id in button_toggle:
                new_button_rep += 1 << self.display_size - led_id - 1
            self.buttons.append(new_button_rep)

        self.states = set([0])
        self.number_apply_all_button = 0

    def show(self):
        print('affichage démarage : {:0b}'.format(self.goal_conf))
        print('list des boutons :')
        for button in self.buttons:
            print('{:0b}'.format(button))

    def apply_all_button(self):
        new_stats = set()
        for state in self.states:
            for button in self.buttons:
                new_stats.add(state^button)
        self.states = new_stats
        self.number_apply_all_button += 1

    def states_has_goal(self):
        return self.goal_conf in self.states


number_step_for_all = 0
with open("input.txt", 'r') as file:
    for line in file:
        machine = Machine(line)
        while not machine.states_has_goal():
            machine.apply_all_button()
        number_step_for_all += machine.number_apply_all_button



print(number_step_for_all)
