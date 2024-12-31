#                                   CODEWARS:
#https://www.codewars.com/kata/53ee5429ba190077850011d4:
def double_integer(i):
    return i * 2

#https://www.codewars.com/kata/55b42574ff091733d900002f:
def friend(x):
    return [name for name in x if len(name) == 4]

# https://www.codewars.com/kata/57f780909f7e8e3183000078:
def grow(arr):
    multiplied = 1
    for num in arr:
        multiplied *= num
    return multiplied

# https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python:
def find_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)  

# https://www.codewars.com/kata/55f73be6e12baaa5900000d4:     Ronaldo>>Messi :)
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

# https://www.codewars.com/kata/56b1f01c247c01db92000076:
def double_char(s):
    st = ""
    for i in s:
        st += i * 2
    return st

# https://www.codewars.com/kata/51f2b4448cadf20ed0000386:
def remove_url_anchor(url):
    return url.split('#')[0]

# https://www.codewars.com/kata/59a8570b570190d313000037:
def sum_cubes(n):
    return sum(i**3 for i in range(1, n + 1))

#                            HOMEWORK

list = [1,2,3,4,5]
list.pop(2)
list.insert(0,3)
print(list)

def giorgi(num1,num2):
    return num1 ** num2
print(giorgi(3,4))



def random(list):
    if len(list) % 2 == 0:
        return "list length is even"
    else:
        return "List length is odd"
print(random(list))