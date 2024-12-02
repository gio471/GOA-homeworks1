even = []
for i in range(201):
    if i % 2 == 0:
        even.append(i)

print(even)

food = []
food1 = input("Enter your favorite food:  ")
food2 = input("Enter your favorite food:  ")
food3 = input("Enter your favorite food:  ")
food4 = input("Enter your favorite food:  ")
food5 = input("Enter your favorite food:  ")

for i in range(1):
    food.append(food1)
    food.append(food2)
    food.append(food3)
    food.append(food4)
    food.append(food5)
print(food)



list = [1,2,3,4,5,6,7,8,9,10]
for i in range(10):
    if list[i] % 2 != 0:
        print(list[i])





string = "giorgi"
print(len(string))



elements = [1,2,3,4,5]
input = int(input("Pick a number 0 to 4:  "))
for i in range(5):
    if input == i:
        print(elements.pop(i))


sia = [1,2,3,4,5,6,7,89,11,22]
print(len(sia))