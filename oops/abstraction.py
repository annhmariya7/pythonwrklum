from abc import ABC,abstractmethod

class Car(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

class Swift(Car):

    
   
    def start(self):
        print("Starts")
        

    
    def stop(self):
        print("Stops")

    
    def accelerate(self):
        print("accelerate")

obj=Swift()
obj.start()
obj.stop()
obj.accelerate()
    