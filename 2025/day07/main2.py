with open('input.txt', 'r') as file:
    for line in file:
        line = line[:-1]
        if line.count('S') != 0:
            beams = [0] * len(line)
            beams[line.index('S')] = 1
        if line.count('^') != 0:
            while True:
                try:
                    index_spliter = line.index('^')
                    if beams[index_spliter] != 0:
                        if index_spliter - 1 > 0:
                            beams[index_spliter - 1] += beams[index_spliter]
                        if index_spliter + 1 < len(beams):
                            beams[index_spliter + 1] += beams[index_spliter]
                    beams[index_spliter] = 0
                    line = line[:index_spliter] + '.' + line[index_spliter+1:]
                except:
                    break

print(sum(beams)+1)
