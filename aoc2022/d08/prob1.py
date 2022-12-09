if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        lines = fp.readlines()

    grid = list()

    for line in lines:
        line = line.strip()
        row = [int(x) for x in  line]
        grid.append(row)

    num_cols = int(len(grid[0]))
    num_rows = int(len(grid))

    num_trees = 0

    for i in range (1, num_rows-1):
        for j in range (1, num_cols-1):
            elm = grid[i][j]
            is_candidate = False
            for k in range(0, j):
                if elm <= grid[i][k]:
                    is_candidate = True
                    break
            if not is_candidate:
                continue
            is_candidate = False
            for k in range(j+1, num_cols):
                if elm <= grid[i][k]:
                    is_candidate = True
                    break
            if not is_candidate:
                continue
            is_candidate = False
            for k in range(0, i):
                if elm <= grid[k][j]:
                    is_candidate = True
                    break
            if not is_candidate:
                continue
            is_candidate = False
            for k in range(i+1, num_rows):
                if elm <= grid[k][j]:
                    is_candidate = True
                    break
            if not is_candidate:
                continue
            if is_candidate:
                print("{} {}".format(i, j))
                num_trees += 1


    num_trees = (((num_rows-2)*(num_cols-2)) -num_trees) + 2*num_rows + 2*(num_cols-2)
    print(num_trees)