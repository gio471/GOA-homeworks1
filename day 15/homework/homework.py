name = input("Enter your name:")
if name == "Giorgi":
    print("Hello")
else:
   print("Bye")

favorite_num = 7
fav_num = int(input("Enter your favorite number:"))

if favorite_num == fav_num:
     print("Perfect")

elif favorite_num > fav_num:
    print("More")
else:
    print("Less")


for i in range(0,151,2):
    print("Luwia",i)

name1 = input("Enter your name:")
age = int(input("Enter your age:"))
name2 = "Giorgi"
age1 = 12
if name1 and age == name2 and age1:
   print("Twins")
elif name1 and age != name2 and age1:
    print("Not Twins")


for i in range(0,150,2):
   print("luwia")
for i in range(1,150,2):
   print("kentia")

password = "giorgi"
guess = input("Enter password:")
while guess != password:
   guess1 = input("Try Again:")
print("Acses Granted")