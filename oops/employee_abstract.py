class Employee:
    data=[
        {"id":1,"name":"jhon","dept":"hr","salary":34000},
        {"id":2,"name":"hari","dept":"it","salary":24000},
        {"id":3,"name":"ravi","dept":"qa","salary":64000},
        {"id":4,"name":"vijay","dept":"hr","salary":74000},
        {"id":5,"name":"tom","dept":"it","salary":24000},
        {"id":6,"name":"vipin","dept":"qa","salary":14000},
        
    ]

    #return all employee records  (list)
    def get(self,*args,**kwargs):       #get is used to list ,*args & **kwargs used to pass unlimited parameters
        return self.data
    

    #employee detail              (detail)
    def retrieve(self,*args,**kwargs):
        id=kwargs.get("id")
        record=[emp for emp in self.data if emp.get("id")==id]     #[list comprehension]
        return record
    
    #add employee                 (create)
    def create(self,*args,**kwargs):         #self must used inside the class
        self.data.append(kwargs)             #kwargs used to display in dictonary format


    
    #delete
    def destroy(self,*args,**kwargs):
        id=kwargs.get("id")
        obj=[e for e in self.data if e.get("id")==id].pop()
        self.data.remove(obj)


    #update
    def update(self,id=None,*args,**kwargs):
        id=id
        obj=[emp for emp in self.data if emp.get("id")==id][0]      #[0] to remove list[]
        obj.update(kwargs)
        print("employee object updated")

   
obj=Employee()
# print(obj.get())

# print(obj.retrieve(id=4))

# obj.create(id=7,name="ann",dept="hr",salary=24000)
# print(obj.get())        #get(get method is in only dictionary) to view all list to know weather id:7 appended to the list or not

# obj.destroy(id=4)
# print(obj.get())  

obj.update(id=4,name="hani",salary=60000)
print(obj.retrieve(id=4))  