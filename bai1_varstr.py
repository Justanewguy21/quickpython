# ------------------------------------------------------
# By    Tao Thanh
# Date  12 Aug 2021
# Todo  Work with var and string data type
# 12/8/2021
#   - continue with string             
# ------------------------------------------------------
# declair a string variable 
s = "start learning python"
print(s)
# command concatenation
name_21 = "Ben"
print("welcome " + name_21)
name_21 = 68149
print("welcome " + str(name_21))
# str basic functions
name_21 = "Learning python is quite interesting"
print("length of name_21 is " + str(len(name_21)))
#  variable.find(str that need to find) -> If it find out, it will return a int >= 0
print(name_21.find("Python"))
# upper and lower // isupper and islower
if name_21.islower():
    print('1')
    print(name_21.upper())
else:
    print('2')
    print (name_21.upper())
name_21 = "Bee"
age = 6
print(f'{name_21} is {age}')