def get_two_digit_num(line):
    """Gets the first and last digits present in a string and return a
    two-digit number."""

    found_nums = [None, None]
    digit_list = ["0","1","2","3","4","5","6","7","8","9"]
    for char in line:
        if char in digit_list:
            if not found_nums[0]:
                found_nums[0] = char
                found_nums[1] = char
            else:
                found_nums[1] = char

    full_num = found_nums[0] + found_nums[1]
    return int(full_num)
    # print(found_nums)

    # return found_nums[0] + found_nums[1]


def extract_nums(file):
    """Reads a file and returns an array of two-digit numbers composed of the
    first and last digit of each line."""

    coord_array = []
    with open(file, encoding="utf-8") as f:
        for line in f:
            print(line)
            coord_array.append(get_two_digit_num(line))

    return coord_array





