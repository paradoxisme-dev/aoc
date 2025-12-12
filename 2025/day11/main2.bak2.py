from typing import Self


class Machine:
    id_machine = 0
    machines: dict[str, Self] = {}
    machines_from_id: dict[int, Self] = {}
    def __init__(self, name: str):
        self.name = name
        Machine.machines[name] = self
        Machine.id_machine += 1
        self.id_machine = Machine.id_machine
        Machine.machines_from_id[self.id_machine] = self
        self.output = set()

    def add_output(self, new_output: Self):
        self.output.add(new_output)

    @classmethod
    def nb_connect(cls, start: str, end: str, must_visit: list[str] = []):
        nb_path = 0
        id_end_machine: int = Machine.machines[end].id_machine
        start_machine: Self = Machine.machines[start]
        must_visit_ids = set([Machine.machines[machine_name].id_machine for machine_name in must_visit])
        paths: list[list[int]] = set([
            tuple([machine.id_machine]) for machine in start_machine.output
        ])
        iter_nb = 0
        while len(paths) > 0:
            iter_nb += 1
            if iter_nb % 10 == 0:
                print(iter_nb, len(paths), len(paths[0]))
            new_paths: list[list[int]] = []
            for list_id_machine in paths:
                current_machine = Machine.machines_from_id[list_id_machine[-1]]
                intersection = must_visit_ids.intersection(current_machine.output)
                if bool(intersection):
                    new_path = list(list_id_machine)
                    new_path.append(intersection[0])
                    new_paths.append(tuple())
                    continue
                for output_machine in current_machine.output:
                    id_output_machine = output_machine.id_machine
                    if id_output_machine == id_end_machine:
                        print('reach out', [Machine.machines_from_id[id_machine].name for id_machine in list_id_machine])
                        is_invalid = False
                        for must_visit_id in must_visit_ids:
                            if must_visit_id not in list_id_machine:
                                is_invalid = True
                                continue
                        if is_invalid:
                            continue
                        print('selected', [Machine.machines_from_id[id_machine].name for id_machine in list_id_machine])
                        nb_path += 1
                        continue
                    if id_output_machine in list_id_machine:
                        continue
                    new_path = list(list_id_machine)
                    new_path.append(id_output_machine)
                    new_paths.append(tuple(new_path))
            paths = new_paths
        return nb_path


machine_connexion = {}
with open('input.txt', 'r') as file:
    for line in file:
        line = line[:-1]
        key_machines = line.split(':')
        machine_connexion[key_machines[0]] = [
            machine
            for machine in key_machines[1].split(' ')
            if machine != ''
        ]
        for machine_name in machine_connexion:
            if machine_name not in Machine.machines.keys():
                new_machine = Machine(machine_name)
            else:
                new_machine = Machine.machines[machine_name]
            for machine_output_name in machine_connexion[machine_name]:
                if machine_output_name not in Machine.machines.keys():
                    new_machine_output = Machine(machine_output_name)
                else:
                    new_machine_output = Machine.machines[machine_output_name]
                new_machine.add_output(new_machine_output)

srv_dac = Machine.nb_connect('svr', 'dac')
dac_fft = Machine.nb_connect('dac', 'fft')
fft_out = Machine.nb_connect('fft', 'out')


print(Machine.nb_connect('svr', 'out', ['dac', 'fft']))
