class Parent:

    phone="samsunga17"
    vechicle="bullet"

    def mobile(self):
        print(self.phone)

    def bike(self):
        print(self.vechicle)


class Child(Parent):
    pass
obj=Child()
obj.mobile()
obj.bike()