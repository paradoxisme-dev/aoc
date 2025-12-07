number_split = 0
with open('input.txt', 'r') as file:
    for line in file:
        line = line[:-1]
        if line.count('S') != 0:
            beams = list(line.replace('S', '|'))
        if line.count('^') != 0:
            new_beam = beams
            while True:
                try:
                    index_spliter = line.index('^')
                    if beams[index_spliter] == '|':
                        new_beam[index_spliter] = '.'
                        if index_spliter - 1 > 0:
                            new_beam[index_spliter-1] = '|'
                        if index_spliter + 1 < len(new_beam):
                            new_beam[index_spliter + 1] = '|'
                        number_split += 1
                    line = line[:index_spliter] + '.' + line[index_spliter+1:]
                except:
                    break
            beams = new_beam


print(number_split)
