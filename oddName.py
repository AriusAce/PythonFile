"""Tran Trung Hao"""

name = str(input("Enter your name: "))
while name == "":
    print("Please enter something")
    name = str(input("Enter your name: "))
print(name[1])