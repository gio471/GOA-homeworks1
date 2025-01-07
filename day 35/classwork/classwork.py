#https://www.codewars.com/kata/5aba780a6a176b029800041c/train/python:
def max_multiple(divisor, bound):
    return bound - (bound % divisor) 

#https://www.codewars.com/kata/52f3149496de55aded000410/train/python:
def sum_digits(number):
    number = abs(number)
    return sum(int(digit) for digit in str(number))

#https://www.codewars.com/kata/5813d19765d81c592200001a/train/python:
def dont_give_me_five(start,end):
    return sum('5' not in str(number) for number in range(start, end + 1))

#https://www.codewars.com/kata/5300901726d12b80e8000498/train/python:

def fizzbuzz(n):
    result = []
    
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    
    return result

#https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python:
def invert(lst):
    return [-a for a in lst]

#https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python:
def sum_array(arr):
    if not arr or len(arr) <= 2:
        return 0  
    
    return sum(arr) - max(arr) - min(arr)