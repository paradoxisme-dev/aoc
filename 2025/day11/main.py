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
    def nb_connect(cls, start: str, end: str):
        nb_path = 0
        id_end_machine: int = Machine.machines[end].id_machine
        start_machine: Self = Machine.machines[start]
        chemins: list[list[int]] = [
            [machine.id_machine] for machine in start_machine.output
        ]
        while len(chemins) > 0:
            new_chemins: list[list[int]] = []
            for list_id_machine in chemins:
                current_machine = Machine.machines_from_id[list_id_machine[-1]]
                for output_machine in current_machine.output:
                    id_output_machine = output_machine.id_machine
                    if id_output_machine == id_end_machine:
                        nb_path += 1
                        continue
                    if id_output_machine in list_id_machine:
                        continue
                    new_path = list_id_machine.copy()
                    new_path.append(id_output_machine)
                    new_chemins.append(new_path)
            chemins = new_chemins
        return nb_path

    def __str__(self):
        return self.name


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


print(Machine.nb_connect('you', 'out'))
