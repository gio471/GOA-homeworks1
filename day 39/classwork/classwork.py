# https://www.codewars.com/kata/55eca815d0d20962e1000106:
def generate_range(start, stop, step):
    if step == 0:
        raise ValueError("Step must not be zero.")
    if (stop - start) * step < 0:
        return [] 

    return list(range(start, stop + (1 if step > 0 else -1), step))

# https://www.codewars.com/kata/557a2c136b19113912000010:
def reverse_it(data):
    if type(data) in [int, str, float]:
        return type(data)(str(data)[::-1])
    return data
# https://www.codewars.com/kata/576b93db1129fcf2200001e6:
def sum_array(arr):
    if not arr or len(arr) <= 2:
        return 0  
    
    return sum(arr) - max(arr) - min(arr)
# https://www.codewars.com/kata/5513795bd3fafb56c200049e:
def count_by(x, n):
    arr = []
    for num in range(1, n+1):
        result = x * num
        arr.append(result)
    return arr