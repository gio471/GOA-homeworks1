surname = input("Enter your surname:  ")
if surname[0] == surname[0].upper():
    print("Hello")
else:
    print("bye")

name = input("Enter your name:  ")
letter = input("Enter letter:  ")
if name.find == -1:
    print("can'find it")
else:
    print(" find it",name.find(letter))

ask = input("How to change surname letter:  ")
if ask == "upper":
    print(surname.upper())
elif ask == "lower":
    print(surname.lower())
elif ask == "capitalaze":
    print(surname.capitalize())


#lower() - ასოებს აპატარავებს upper() - ზდის ასოებს .capitalize() - პირველ ასოს ადიდებს .find() - ასოებს პოულობს რომელიც რომელ ინდექსზეა
