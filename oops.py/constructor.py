class Student: 
    def __init__(self,fullname,marks):
         self.name = fullname
         self.marks= marks
s1= Student("kartik",12)
print(s1.name,s1.marks)