# ------------------------------------------------------
# By    Tao Thanh
# Date  25 Aug 2021
# Todo  Work with class
# ------------------------------------------------------
number_of_classes = 2
class Player:
    def __init__(self, name, year, club):
        self.name = name
        self.year = year
        self.club = club
    def introduce_me(self):
        print(f'my name is {self.name}, plays for {self.club} {self.year} years')

p1 = Player('Ronaldo', 9, 'MU')
p2 = Player('Messi', 22, 'Barca')
p3 = Player('Haaland', 3, 'Dortmund')

p1.introduce_me()
p2.introduce_me()
p3.introduce_me()

class Student:
    def __init__(self, name, math, literature, english):
        self.name = name
        self.math = math
        self.literature = literature
        self.english = english
    def final_exam(self):
        average = (self.math + self.literature + self.english) / 3
        if average < 5:
            print('TRUOT')
        elif average >=5 and average <= 7:
            print('do binh thuong')
        else:
            print('kha')
s1 = Student('Son', 8, 6, 10)
s2 = Student('Duc', 6, 6, 7)
s3 = Student('Luu', 5, 7, 6)
s1.final_exam()
s2.final_exam()
s3.final_exam()


  


    
