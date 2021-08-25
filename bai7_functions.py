# ------------------------------------------------------
# By    Tao Thanh
# Date  21 Aug 2021
# Todo  Work with functions            
# ------------------------------------------------------
# declair a simple functions
# print('ten cua ban Thanh la Thanh')
# print('chieu cao cua ban thanh la 1.70m')
# print('lop cua ban thanh dang hoc la 8A')
# print('ten cua ban Son la Son')
# print('chieu cao cua ban Son la 1.72m')
# print('lop cua ban son dang hoc la 8B')
# def tenham(thamso):
def introduce_me (ten, chieu_cao, lop_hoc):
    print(f'Chieu cao cua {ten} la {chieu_cao}')
    print(f'ban {ten} hoc {lop_hoc}')
a = introduce_me('Son', 1.75, '8B')
# introduce_me('Thanh', 1.7, '8A')
# introduce_me('Son', 1.75, '8B')
print(a)
# functions return results
def sum (a = 0, b = 1):
    print(f'gia tri cua a {a}, b la {b}')
    x = a + b
    return x
i = sum(1,2)
print(i)
i = sum(b = 1, a  = 2)
i = sum()
print(i)

# variant parameters
def sumall(*numbers):
    x = 0
    for x1 in numbers:
        x += x1
    return x
i = sumall(1,2,3,4,199,200,300,688)
print(i)
i = sumall(1,2,3,4,199,200,300,688, 33423346)
print(i)

# Scope of vaiables: global and local
number = 100#global
def add():
    number = 1 #local
    print(number)
add()
print(number)


number = 100#global
def add1():
    global number
    number = 1 #local
    print(number)
add1()
print(number)