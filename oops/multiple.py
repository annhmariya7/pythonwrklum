class p1:
    def m1(self):
        print("inside p1 class m1 method")

class p2:
    def m2(self):
        print("inside p2 class m2 method")

class p3:
    def m3(self):
        print("inside p3 class m3 method")

class child(p2,p1):
    def m1(self):
        print("inside child class m3 method")
    
ch=child()
ch.m2()

ch.m1()

#inheritance
    # =>single inheritance
    #   =>multiple inheritance