def is_invalide(id_to_check):
    id_string = str(id_to_check)
    len_id = len(id_string)
    for len_try in range(1, len_id//2+1):
        if len_id % len_try != 0:
            continue
        all_repeat = True
        for interval in range(1, len_id//len_try):
            if id_string[:len_try] != id_string[len_try*interval: len_try*(interval+1)]:
                all_repeat = False
                continue
        if all_repeat:
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
