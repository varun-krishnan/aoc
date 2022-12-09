from copy import deepcopy

def find_move(H, T):
    new_T = deepcopy(T)
    if abs(H[0]-T[0]) <=1 and abs(H[1]-T[1]) <=1:
        return T
    else:
        if T[0] != H[0]:
            new_T[0] = T[0]+int((H[0]-T[0])/abs(H[0]-T[0]))
        if T[1] != H[1]:
            new_T[1] = T[1]+int((H[1]-T[1])/abs(H[1]-T[1]))
        return new_T

def calculate_positions(lines, num_knots):
    H_index = [0,0]
    T_indices = list()
    for i in range(num_knots):
        T_indices.append([0]*2)
    T_set = set()

    T_set.add(tuple(T_indices[num_knots-1]))

    grid = {'R': [1,0],
            'L': [-1,0],
            'U': [0,1],
            'D': [0,-1]}

    for line in lines:
        line = line.strip()
        act, cnt = line.split(' ')
        for i in  range(int(cnt)):
            H_index[0] += grid[act][0]
            H_index[1] += grid[act][1]
            for i in range(len(T_indices)):
                if i == 0:
                    T_indices[0] = find_move(H_index, T_indices[0])
                else:
                    T_indices[i] = find_move(T_indices[i-1], T_indices[i])
            # print(T_indices)
            # print("H_index {} T_index {}".format(H_index, T_index))
            T_set.add(tuple(T_indices[num_knots-1]))

    return (len(T_set))

if __name__ == "__main__":
    with open("input.txt", 'r') as fp:
        lines = fp.readlines()

    num_knots=1
    num_positions = calculate_positions(lines, num_knots)
    print(num_positions)