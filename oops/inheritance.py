class parent:
    phone="samsung17"
    vehicle="passionpro"

    def mobile(self):
        print(self.phone)

    def bike(self):
        print(self.vehicle)

class child(parent):
    pass           #if the block is empty then use pass for no error

obj=child()
obj.mobile()
obj.bike()