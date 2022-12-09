def find_max_sum(net_cal_list):
    max_sum = 0
    for per_person_list in net_cal_list:
        current_sum = sum(per_person_list)
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

def get_cal_list_from_file(file_name):
    cal_list = list()
    with open(file_name, 'r') as fp:
        per_person_list = list()
        lines = fp.readlines()
        for line in lines:
            if line == "\n":
                cal_list.append(per_person_list)
                per_person_list = list()
            else:
                per_person_list.append(int(line))

    return cal_list

if __name__ == "__main__":
    cal_list = get_cal_list_from_file("input")
    print(find_max_sum(cal_list))
