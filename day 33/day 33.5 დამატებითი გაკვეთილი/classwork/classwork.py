#https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python:
def maskify(cc):
    return '#' * (len(cc) - 4) + cc[-4:] if len(cc) > 4 else cc

#https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d:
def solution(text, ending):
    return text.endswith(ending)

#https://www.codewars.com/kata/539ee3b6757843632d00026b:
def capitals(word):
    return [index for index, char in enumerate(word) if char.isupper()]


#https://www.codewars.com/kata/59a8570b570190d313000037/train/python:
def sum_cubes(n):
    return sum(i**3 for i in range(1, n + 1))


#https://www.codewars.com/kata/5174a4c0f2769dd8b1000003/train/python:
def solution(nums):
    if nums == 0:
        return []
    else:
        return sorted(nums)
