if __name__ == "__main__":
    with open("input.txt", 'r') as fp:
        lines = fp.readlines()

    for lin in lines:
        line = lin.strip()
        found  = False
        ending = 0
        start1 = 0
        start2 = 0
        while not found:
            for idx in range(start1+2, int(len(line))):
                if line[idx] != line[idx-1] and line[idx] != line[idx-2] and line[idx-1] != line[idx-2]:
                    start2 = idx
                    break
            # import pdb; pdb.set_trace()
            idx = start2+1
            repeat = False
            # while idx <  int(len(line)):
            jdx = idx -1
            while jdx > idx - 4:
                if line[jdx] == line[idx]:
                    start1 = jdx+1
                    repeat = True
                    break
                jdx -= 1
            if not repeat:
                found = True
                ending = idx+1

        print(ending)

        # print("{} {}".format(line, ending))

