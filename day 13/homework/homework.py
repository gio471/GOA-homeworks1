for i in range(11):
    print(i)
for i in range(50,101):
    print(i)
for i in range(200,500,2):
    print(i)
for i in range(1,50,2):
    print(i)

surname = input("Enter surname:")
for i in surname:
    print(i)


#for loops გამოიყენება იმისათვის რომ გაიმეოროს ის დავალება რასაც მივცემთ და რამდენჯერაც მივუთითებთ იმდენჯერ

num = 10
while num < 16:
    print(num)
    num = num + 1

num1 = 50
while num1 > 0:
    print(num1)
    num1 = num1 - 1


#while loop შეიძლება გამოიყენებოდეს მაშინ როდესაც არ იცი რამდენი იტერაცია დაგჭირდება
i = 10
while i < 70:
    print(i)
    print(i = i + 2)