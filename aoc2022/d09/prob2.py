from prob1 import calculate_positions, find_move
if __name__ == "__main__":
    with open("input.txt", 'r') as fp:
        lines = fp.readlines()

    num_knots=9
    num_positions = calculate_positions(lines, num_knots)
    print(num_positions)