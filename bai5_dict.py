# ------------------------------------------------------
# By    Tao Thanh
# Date  18 Aug 2021
# Todo  Work with dict data type
#   - continue with dict             
# ------------------------------------------------------
#1 declare a dictionary
emails = {
    'thanh': 'taothanh@gmail.com',
    'trung': 'trungvan@gmail.com'
}
print(emails)
print(emails['trung'])


# students dictionary
students = {
    'Son': {
        'email': 'son21@gmail.com',
        'phone': '023513452345234',
        'classroom':'8A'
    },
    "Thanh": {
        'email': 'taothanh2020@gmail.com',
        'phone': '012353453415346',
        'classroom':'8A'
    }
}
print(students)
# print information of Thanh
stu = students['Thanh']
print(stu['email'])
# quick way
print(students['Thanh']['email'])


print(students.keys())
