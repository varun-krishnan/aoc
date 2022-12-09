from pprint import pprint

def get_string_value(input_str):
    value = 0
    for i in input_str:
        if i.islower():
            value |= 1 << (ord(i)-ord('a'))
        else:
            value  |= 1 << (26 + (ord(i)-ord('A')))
    return value

def get_common_element_value(str1, str2, str3):
    common_value = get_string_value(str1) & get_string_value(str2) & get_string_value(str3)
    i = 1

    while common_value > 0:
        if common_value % 2:
            print(i)
            return i
        common_value = common_value/2
        i += 1


if __name__ == "__main__":
    fp = open('input.txt', 'r')
    sum = 0
    lines = fp.readlines()
    line_groups = [lines[x:x+3] for x in range(0, len(lines), 3)]
    for line_group in line_groups:
        sum += get_common_element_value(
            line_group[0].strip(),
            line_group[1].strip(),
            line_group[2].strip(),)

    print("sum is ", sum)