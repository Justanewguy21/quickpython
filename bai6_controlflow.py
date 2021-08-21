# ------------------------------------------------------
# By    Tao Thanh
# Date  21 Aug 2021
# Todo  Work with if then else for 
#  ------------------------------------------------------ 
# if, else sample
a = int(input('put the numbers here: '))
print (a)
if a % 2 == 0:
    print('it is an even number')
else:
    print('it is an odd number')
# if elif elif else
#  Nham vao mot so m neu la so chan > 10 thi in ra Chan > 10, In Chan <10, le le >10, le <10
is_even = a % 2
if is_even == 0 and a > 10 :
    print('chan > 10') 
elif is_even ==0 and a < 10:
    print('chan < 10')
elif is_even != 0 and a > 10:
    print('le > 10')
else:
    print('le < 10')

friends = ['Benja','Nguyen', 'Khoi', 'Minh', 'Quang', 'Anh','Duc', 'Thanh', 'Tran', 'Dac']
i = 0
for name in friends:
    i += 1
    print(f'Ban thu {i} la {name}')


for i,name in enumerate(friends): 
    print(f'Ban thu {i} la {name}')
# while
i = 0
while i < len(friends):
    print(f'BAN THU {i + 1} la {friends[i]}')
    i += 1