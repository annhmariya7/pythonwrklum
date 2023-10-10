from datetime import datetime
class Bank:
    bank_name:str
    acno:str
    person_name=str
    ac_type:str
    balance:int

    def create(self,b_name,acno,p_name,ac_type,bal):
        self.bank_name=b_name          #self used to access current instance
        self.acno=acno
        self.person_name=p_name
        self.ac_type=ac_type
        self.balance=bal

    def deposit(self,amount):
        self.balance+=amount
        print(f"your {self.bank_name} has been created with {amount} avl balnce is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("transaction failed insufficent balance")
        else:
            self.balance-=amount
            print(f"your {self.bank_name} has been debited with {amount} avl balance is {self.balance}")
        
    def get_balance(self):
        print(f"your {self.bank_name} A/c {self.acno} bal on {datetime.today()} is  ")


obj1=Bank()
obj1.create("sbi","10324","vijay","savings",4000)

obj1.deposit(2000)

obj2=Bank()
obj2.create("sbi","10236","johny","savings",5000)
