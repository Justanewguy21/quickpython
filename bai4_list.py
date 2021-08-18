# ------------------------------------------------------
# By    Tao Thanh
# Date  18 August 2021
# Todo  Work with list
# Refs
#   https://developers.google.com/edu/python/lists
# ------------------------------------------------------
# declair a list
menu = ["pencake", "ramen", "phở", "bun", "com rang"]
print(menu)
#  another way to declair a list
customers = list(["John", "Peter", "Musk"])
number1 = []
print(number1)
#  how to access the list elements
print(menu[0])
print(menu[1])
print(menu[2])
# another way
for m in menu:
    print(m)
# check if a value exists in a list
e = "ramen"
# print("ramen" in menu)
print(e in menu)
e = "RAMEN"
print(e in menu)
# basic functions list in python
number1 = [18, 8, 21, 20, 49, 3, 1, 0]
ret = len(number1)
print(f'Lenth of the list is {ret}')
ret = max(number1)
print(f'the maximum value of the list is  {ret}')
print(min(number1))
number1.sort()
print(number1)
print(number1[1])
number1.reverse()
print(number1)
# find the index of a value in the list
ret = menu.index("pencake")
print (f'the position of pencake is {ret}')
# ret = menu.index("Pencake")
# print("the posisiton of the Pencake is " + str(ret))
try:
    ret = menu.index("P")
except:
    ret = -1
print("the posisiton of the Pencake is " + str(ret))
# add/remove a element
number1 = []
number2 = [50, 80, "a"]
number1.append(2)
number1.insert(0,4)
number1.insert(1,10)
number1.append(12)
print(number1)
# number1.insert(1,number2)
# print(number1)
# number1.append(number2)
# print(number1)
number1.extend(number2)
print(number1)
number1.remove("a")
print(number1)
