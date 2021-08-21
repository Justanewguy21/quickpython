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


school = {
    '6A1': {
        'khoi':6,
        'tenlop':'6A1',
        'chunhiem':'Tran Van A',
        'siso':47
    },
    '6A2': {
        'khoi':6,
        'tenlop':'6A2',
        'chunhiem':'Tran Van B',
        'siso':45
    },


}

school2 = {
    'khoi7': {
        'classroom': {
            '7A1': {
                'tenlop': 71,
                'chunhiem': 'Nguyen Van A',
                'siso': 50
            },
            '7A2': {
                'tenlop': 72,
                'chunhiem': 'Nguyen Van B',
                'siso': 46
            }
        }
    }
}       
 
print(school['6A1']['chunhiem'])
print(school2['khoi7']['classroom']['7A1']['chunhiem'])
# comparison between a simple way and a complicated way

