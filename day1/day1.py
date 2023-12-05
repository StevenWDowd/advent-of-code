from functools import reduce
from re import finditer

def get_two_digit_num(line):
    """Gets the first and last digits present in a string and returns a
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

def get_two_digits_with_text(line):
    """Gets first and last numbers in a string, including text forms like
    'one', and returns a two-digit number. """

    # use find(). save tuples of found substring and index, ('one', 5)
    # do the same for digits
    # use only the least and greatest indices

    # found_nums = [None, None]
    nums_and_indices = []
    digit_list = ["0","1","2","3","4","5","6","7","8","9"]
    wordnums = ["zero", "one", "two", "three", "four", "five", "six", "seven",
                "eight", "nine"]
    digit_dict = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4",
                  "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    for digit in digit_list:
        matches = finditer(digit, line)
        for match in matches:
            idx = match.span()[0]
            nums_and_indices.append((digit, idx))
        # idx = line.find(digit)
        # if idx >= 0:
        #     nums_and_indices.append((digit, idx))
    for word in wordnums:
        matches = finditer(word, line)
        for match in matches:
            idx = match.span()[0]
            nums_and_indices.append((word, idx))
        # idx = line.find(word)
        # if idx >= 0:
        #     nums_and_indices.append((word, idx))
    print(nums_and_indices)

    #find min index
    first_num = reduce(lambda tup1, tup2: tup1 if tup1[1] < tup2[1] else tup2, nums_and_indices)
    # def return_min_idx_tuple(list):
    #     """Selects tuple with least index from list of tuples like: (val, idx)"""


    #find max index
    second_num = reduce(lambda tup1, tup2: tup1 if tup1[1] > tup2[1] else tup2, nums_and_indices)
    # def return_max_idx_tuple(list):
    #     """Selects tuple with greatest index from list of tuples like:
    #       (val, idx)"""

    #ensure both numbers are digit strings
    if len(first_num[0]) > 1:
        first_num = (digit_dict.get(first_num[0]), first_num[1])

    if len(second_num[0]) > 1:
        second_num = (digit_dict.get(second_num[0]), second_num[1])

    full_num = first_num[0] + second_num[0]

    return int(full_num)









def extract_nums(file):
    """Reads a file and returns an array of two-digit numbers composed of the
    first and last digit of each line."""

    coord_array = []
    with open(file, encoding="utf-8") as f:
        for line in f:
            print(line)
            coord_array.append(get_two_digit_num(line))

    return coord_array

def extract_nums_text(file):
    """Reads a file and returns an array of two-digit numbers composed of the
    first and last number (digit or text) in each line."""

    coord_array = []
    with open(file, encoding="utf-8") as f:
        for line in f:
            print(line)
            coord_array.append(get_two_digits_with_text(line))

    return coord_array

# not working for repeats of strings, e.g., sixfconesix6three1sixsix should be 66
# but is giving me 61






