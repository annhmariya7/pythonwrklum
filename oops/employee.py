class Employee:
    id:int
    name:str
    department:str
    gender:str

    def create(self,id,name,dept,gender):
        self.id=id
        self.name=name
        self.department=dept
        self.gender=gender

    def display_emp(self):
        print(self.id,self.name,self.department,self.gender)

obj=Employee()
obj.create(100,"ann","hr","female")
obj.display_emp()
        