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
    max_value = 0
    max_index = [0,0]

    for i in range (1, num_rows-1):
        for j in range (1, num_cols-1):
            elm = grid[i][j]
            l1 = 0
            for k in range(j-1, -1, -1):
                if elm > grid[i][k]:
                    l1 += 1
                else:
                    l1 += 1
                    break
            l2 = 0
            for k in range(j+1, num_cols):
                if elm > grid[i][k]:
                    l2 += 1
                else:
                    l2 += 1
                    break
            l3 = 0
            for k in range(i-1, -1, -1):
                if elm > grid[k][j]:
                    l3 += 1
                else:
                    l3 += 1
                    break
            l4 = 0
            for k in range(i+1, num_rows):
                if elm > grid[k][j]:
                    l4 += 1
                else:
                    l4 += 1
                    break
            net_calc = l1*l2*l3*l4
            print("{} value {} ind {}".format([i,j], net_calc, [l1,l2,l3,l4]))
            if net_calc > max_value:
                max_value = net_calc
                max_index = [i,j]
                # print("{} value {}".format(max_index, max_value))

    print(max_value)