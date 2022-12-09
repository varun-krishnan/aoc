if __name__ == "__main__":
    with open("input.txt", 'r') as fp:
        lines = fp.readlines()

    for lin in lines:
        line = lin.strip()
        found  = False
        ending = 0
        start1 = 0
        while not found:
            repeat = False
            for idx in range(start1+1, start1+14):
                for jdx in range(idx-1,start1-1, -1):
                    if line[jdx] == line[idx]:
                        start1 = jdx+1
                        repeat = True
                        break
                if repeat:
                    break
            if not repeat:
                found = True
                ending = start1+14
                print(ending)