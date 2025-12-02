def is_invalide(id_to_check):
    id_string = str(id_to_check)
    if len(id_string) % 2 == 0:
        if id_string[:len(id_string)//2] == id_string[len(id_string)//2:]:
            return True
    return False

sum_unvalide_id = 0
with open("input.txt", 'r') as f:
    data = f.read()
    for interval in data.split(','):
        start, end = interval.split('-')
        start, end = int(start), int(end)
        for test_id in range(start, end + 1):
            if is_invalide(test_id):
                sum_unvalide_id += test_id

print(sum_unvalide_id)
