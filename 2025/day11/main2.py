from functools import lru_cache


machine_connexion = {}

@lru_cache(maxsize=None)
def get_paths_number(start, dac=False, fft=False):
    if start == 'out':
        return 1 if (dac and fft) else 0
    outputs = machine_connexion[start]
    total = 0
    for output in outputs:
        if output == 'dac':
            new_dac = True
        else:
            new_dac = dac
        if output == 'fft':
            new_fft = True
        else:
            new_fft = fft
        total += get_paths_number(output, new_dac, new_fft)
    return total

with open('input.txt', 'r') as file:
    for line in file:
        line = line[:-1]
        key_machines = line.split(':')
        machine_connexion[key_machines[0]] = [
            machine
            for machine in key_machines[1].split(' ')
            if machine != ''
        ]

print(get_paths_number('svr'))
