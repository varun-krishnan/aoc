from prob1 import generate_tower_instructions
from pprint import pprint

def tower_moves(towers, instructions):
    for ins in instructions:
        num, fro, to = ins
        temp = list()
        for i in range(num):
            temp.append(towers[fro-1].pop())
        for i in range(num):
            towers[to-1].append(temp.pop())

    # pprint(towers)
    output = ""
    for tower in towers:
        output = output+tower[-1]
    print(output)

if __name__ == "__main__":
    with open("input.txt", 'r') as fp:
        lines = fp.readlines()

    towers, instructions = generate_tower_instructions(lines)
    tower_moves(towers, instructions)