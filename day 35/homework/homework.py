# https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python:
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

# https://www.codewars.com/kata/586f6741c66d18c22800010a/train/python:
def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    return sum(range(begin_number, end_number + 1, step))


# https://www.codewars.com/kata/56a946cd7bd95ccab2000055:
def lowercase_count(strng):
    return sum(1 for char in strng if char.islower())

# https://www.codewars.com/kata/5601409514fc93442500010b/train/python:
def better_than_average(class_points, your_points):
    class_point = sum(class_points) / len(class_points)
    if class_point < your_points:
        return True
    else:
        return False

# https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python:
def grow(arr):
    multiplied = 1
    for num in arr:
        multiplied *= num
    return multiplied

# https://www.codewars.com/kata/53dc23c68a0c93699800041d/train/python:
def smash(words):
    return ' '.join(words)