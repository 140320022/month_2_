class Person:
    def __init__(self,fullname,age,is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
    def inroduce_myself(self):
        print(f'fullname is {self.fullname}\n|,I am{self.age} years old.')
        if self.is_married:
             print("I'm married")
        else:
             print("I am not married")

class Student(Person):
    def __init__(self,fullname,age,is_married,**marks):
        super().__init__(fullname,age,is_married)
        self.marks = marks

    def Average(self):
      average = sum(self.marks.values())/len(self.marks.values())
      return f'average:{average}'
class Teacher(Person):
    base_salary = 30000

    def __init__(self,fullname,age,is_married,experience):
        super().__init__(fullname,age,is_married,)
        self.experience = experience

    def __int__(self,fullname,age,is_married,experience):
        super().__int__(fullname,age,is_married)
        self.experience = experience

    def inroduce_myself(self):
        super().inroduce_myself()
        print(f'I have{self.experience} years of experience.')

    def Salary(self):
        bonus = self.base_salary / 100*5
        total_salary = self.base_salary

        if self.experience > 3:
            counter = self.experience - 3
            while counter > 0:
                total_salary += bonus
                counter -= 1
        return  total_salary

Teacher = Teacher ("Akparalieva Aizhamal", 45 , False,5)
Teacher.inroduce_myself()
def create_students():
  first_st = Student ("ASEL",22,True,math = 5,science = 4,history = 3)
  secend_st = Student("Aktilek",18,False, math = 5,science = 5,  history = 4 )
  thrid_st = Student ("Aibek",19,False,math = 5, science = 3, history = 5 )
  student_list = [first_st,secend_st,thrid_st]
  return student_list
student_list = create_students()
for student in student_list:
    student.inroduce_myself()
    print(f"My marks:{student.marks},{student.Average()}\n")
