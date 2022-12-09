from prob1 import get_cal_list_from_file

def get_sorted_sums(net_cal_list):
    sum_list = [sum(per_person_list) for per_person_list in net_cal_list]
    sum_list.sort(reverse=True)
    return sum_list

if __name__ == "__main__":
    cal_list = get_cal_list_from_file("input")
    sum_list = get_sorted_sums(cal_list)
    print(sum(sum_list[:3]))
