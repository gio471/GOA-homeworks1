#https://www.codewars.com/kata/58261acb22be6e2ed800003a/train/python:
def get_volume_of_cuboid(length, width, height):
    return length * width * height

#https://www.codewars.com/kata/55d277882e139d0b6000005d/train/python:
def find_average(nums):
    return sum(nums) / len(nums)

#https://www.codewars.com/kata/570a6a46455d08ff8d001002/train/python:
def no_boring_zeros(n):
    if n == 0:
        return 0
    while n % 10 == 0:
        n //= 10
    return n

#https://www.codewars.com/kata/5ad0d8356165e63c140014d4/train/python:
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0
    
#https://www.codewars.com/kata/57f781872e3d8ca2a000007e/train/python:
def maps(a):
    return [x * 2 for x in a]

#https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python:
def xo(s):
    s = s.lower()  
    return s.count('x') == s.count('o')

#https://www.codewars.com/kata/59ca8246d751df55cc00014c/train/python:
def hero(bullets, dragons):
    return bullets >= dragons * 2