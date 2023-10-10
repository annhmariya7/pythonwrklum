class student:
    id:int
    name:str
    age:int
    course:str
#__init__ is a constructor name in python & constructor duty is to initialize instance variables

    def __init__(self,id,name,age,course):     #self to call current object
        self.id=id
        self.name=name
        self.age=age
        self.course=course

    def display_student(self):
        print(self.name,self.course)

    def __str__(self):
        return self.name      #now only print the name as objects string representation

obj1=student(100,"ann",21,"bca")
# obj1.display_student()

print(obj1)

