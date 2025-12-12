from functools import lru_cache


machine_connexion = {}

@lru_cache(maxsize=None)
def get_paths_number(a, b, previous=None):
    outputs = machine_connexion[a]
    if previous is None:
        previous = tuple(a)
    else:
        previous = tuple(list(previous) + [a])
    if b in outputs:
        return sum([get_paths_number(output, b, previous) if output != b else 1 for output in outputs if output != 'out'])
    else:
        return sum([get_paths_number(output, b, previous) for output in outputs if output != 'out'])

with open('input.txt', 'r') as file:
    for line in file:
        line = line[:-1]
        key_machines = line.split(':')
        machine_connexion[key_machines[0]] = [
            machine
            for machine in key_machines[1].split(' ')
            if machine != ''
        ]


nb_total = get_paths_number('svr', 'dac')
nb_total += get_paths_number('dac', 'fft')
nb_total += get_paths_number('fft', 'out')
nb_total += get_paths_number('svr', 'fft')
nb_total += get_paths_number('fft', 'dac')
nb_total += get_paths_number('dac', 'out')

print(nb_total)
