# https://www.codewars.com/kata/5265326f5fda8eb1160004c8/train/python:
def number_to_string(num):
    return str(num)

# https://www.codewars.com/kata/57eae20f5500ad98e50002c5/train/python:
def no_space(x):
    return x.replace(" ", "")

# https://www.codewars.com/kata/55a70521798b14d4750000a4/train/python:
def greet(name):
    final = "Hello," + " " + name + " " + "how are you doing today?"
    return final

#https://www.codewars.com/kata/57356c55867b9b7a60000bd7/solutions/python:
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        if value2 == 0:
            raise ValueError("Cannot divide by zero")
        return value1 / value2
    

#https://www.codewars.com/kata/582cb0224e56e068d800003c/train/python:
def litres(time):
    return int(time * 0.5)