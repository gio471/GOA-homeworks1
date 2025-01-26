# https://www.codewars.com/kata/555086d53eac039a2a000083/train/python:
def lovefunc( flower1, flower2 ):
    return (flower1 % 2) != (flower2 % 2)

# https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd/train/python:
def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    return n * m

# https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python:
def find_needle(haystack):
    position = haystack.index("needle")
    return f"found the needle at position {position}"

# https://www.codewars.com/kata/57e76bc428d6fbc2d500036d/train/python:
def string_to_array(s):
    if s == "":
        return [""]
    
    return s.split()

# https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python:
def zero_fuel(distance_to_pump, mpg, fuel_left):
    max_distance = mpg * fuel_left
    return max_distance >= distance_to_pump

# https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python:
def bmi(weight, height):
    bmi_value = weight / (height ** 2)
    
    if bmi_value <= 18.5:
        return "Underweight"
    elif bmi_value <= 25.0:
        return "Normal"
    elif bmi_value <= 30.0:
        return "Overweight"
    else:
        return "Obese"

# https://www.codewars.com/kata/5556282156230d0e5e000089/train/python:
def dna_to_rna(dna):
    return dna.replace('T', 'U')

# https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/python:
def check(seq, elem):
    return elem in seq     #in ოპერატორი ამაოწმებს იმას თუ seq-ში არის elem

# https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/python:
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock") or (p1 == "rock" and p2 == "scissors"):
        return "Player 1 won!"
    else:
        return "Player 2 won!"