import re
from pprint import pprint

def tower_moves(towers, instructions):
    for ins in instructions:
        num, fro, to = ins
        for i in range(num):
            towers[to-1].append(towers[fro-1].pop())

    # pprint(towers)
    output = ""
    for tower in towers:
        output = output+tower[-1]
    print(output)

def generate_tower_instructions(lines):
    tower_input = list()
    instructions = list()
    read_tower = True
    towers = list()
    for line in lines:
        if re.match("\s*\d[\s\d]*", line):
            read_tower = False
        else:
            ins = re.match("move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)\n?", line)
            if ins:
                instructions.append([int(ins.group(1)), int(ins.group(2)), int(ins.group(3))])
            elif read_tower:
                tower_input.append(line)
    
    num_towers = int(len(tower_input[0])/4)

    for i in range(int(num_towers)):
        towers.append(list())

    for line in tower_input:
        tower_chars = [line[x*4:(x*4)+4] for x in range(num_towers)]
        for idx in range(num_towers):
            tile = re.match("\[(\w)\]", tower_chars[idx])
            if tile:
                towers[idx].append(tile.group(1))

    for tower in towers:
        tower.reverse()

    return towers, instructions

if __name__ == "__main__":
    with open("input.txt", 'r') as fp:
        lines = fp.readlines()

    towers, instructions = generate_tower_instructions(lines)
    tower_moves(towers, instructions)

