number_step = 0
with open("input_ex.txt", 'r') as file:
    for line in file:
        line = line[:-1]
        line_cut = line.split(' ')
        goal_value = 0
        goal_rep = line_cut[0][1:-1]
        for id_value, value in enumerate(goal_rep[::-1]):
            if value == '#':
                goal_value += 1 << id_value
        print(goal_value)
        start_set = set()
        for button in line_cut[1:-1]:
            new_button_rep = 0
            button_toggle = [int(led) for led in button[1:-1].split(',')]
            for led_id in button_toggle:
                new_button_rep += 1 << led_id
            start_set.add(new_button_rep)
        all_config = start_set.copy()
        is_ok = goal_rep in all_config
        while not is_ok:
            new_set = set()
            for button in start_set:
                for test_conf in all_config:
                    new_conf = button ^ test_conf
                    if new_conf == goal_value:
                        is_ok = True
                        break
                    new_set.add(new_conf)
                if is_ok:
                    break
            all_config = all_config.union(new_set)
            print(all_config)
            number_step += 1


print(number_step)
