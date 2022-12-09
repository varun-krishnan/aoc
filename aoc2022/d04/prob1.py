from pprint import pprint

def check_overlap(sec1, sec2):
    is_overlap = 0
    if (int(sec1[0]) < int(sec2[0])):
        if (int(sec1[1]) >= int(sec2[1])):
            is_overlap  = 1
    elif (int(sec1[0]) > int(sec2[0])):
        if (int(sec2[1]) >= int(sec1[1])):
            is_overlap  = 1
    elif (int(sec1[0]) == int(sec2[0])) or int(sec1[1]) == int(sec2[1]):
        is_overlap = 1

    return is_overlap

if __name__ == "__main__":
    num_overlap = 0
    with open("input.txt", 'r') as fp:
        lines = fp.readlines()

    input_pairs = [line.strip().split(',') for line in lines]

    formatted_inp_pairs = [[inp_pair[0].split('-'), inp_pair[1].split('-')] for inp_pair in input_pairs]

    print(len(formatted_inp_pairs))
    # pprint(formatted_inp_pairs)

    for entry in formatted_inp_pairs:
        overlap = check_overlap(entry[0], entry[1])
        print("{} {}".format(entry, ("true" if overlap else "false")))
        num_overlap += overlap

    print(num_overlap)
