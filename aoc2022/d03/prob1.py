def get_common_element_value(str1, str2):
    value_str1 = 0
    value_str2 = 0
    for i in str1:
        if i.islower():
            value_str1 |= 1 << (ord(i)-ord('a'))
        else:
            value_str1 |= 1 << (26 + (ord(i)-ord('A')))
    print(str1, bin(value_str1))

    for i in str2:
        if i.islower():
            value_str2 |= 1 << (ord(i)-ord('a'))
        else:
            print(i,26 + (ord(i)-ord('A')))
            value_str2 |= 1 << (26 + (ord(i)-ord('A')))
    
    print(str2, bin(value_str2))

    print(bin(value_str1 & value_str2))

    common_value = value_str1 & value_str2

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
    for line in fp.readlines():
        line = line.strip()
        sum += get_common_element_value(line[:int(len(line)/2)], line[int(len(line)/2):])

    print("sum is ", sum)