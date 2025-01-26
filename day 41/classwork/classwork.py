# https://www.codewars.com/kata/55a70521798b14d4750000a4/train/python:
def greet(name):
    final = "Hello," + " " + name + " " + "how are you doing today?"
    return final

# https://www.codewars.com/kata/555a67db74814aa4ee0001b5/train/python:
def is_even(n): 
    return n % 2 == 0

# https://www.codewars.com/kata/53ee5429ba190077850011d4/train/python:
def double_integer(i):
    return i * 2

# https://www.codewars.com/kata/53dc54212259ed3d4f00071c/train/python:
def sum_array(a):
    if a == []:
        return 0
    else:
        return sum(a)
    
# https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python:
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    
# https://www.codewars.com/kata/577a98a6ae28071780000989/train/python:
def minimum(arr):
    return min(arr)
def maximum(arr):
    return max(arr)

# https://www.codewars.com/kata/56d49587df52101de70011e4/train/python:
def leo(oscar):
    if oscar == 88:
        return "Leo finally won the oscar! Leo is happy"
    elif oscar == 86:
        return "Not even for Wolf of wallstreet?!"
    elif oscar < 88:
        return "When will you give Leo an Oscar?"
    else:
        return "Leo got one already!"
    
