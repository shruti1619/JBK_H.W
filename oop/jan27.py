from abc import ABC, abstractmethod

class my_class(ABC):
    @abstractmethod
    def m1(self,a):
        pass
    
    def m2(self):
        print("shruti")
        
#obj=my_class()  # This will raise an error because we cannot instantiate an abstract class

class child_class(my_class):
    def m1(self,a):             # if you can't override the abstract method then also it will give error
        print(a+5)              # overriding is mandatory
        
obj=child_class()
obj.m1(18)
obj.m2()