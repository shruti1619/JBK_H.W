class book:
    def __init__(self,n,p):
        self.name=n
        self.price=p
        
    def __add__(self,other):
        return self.price + other.price     # we can also do multiplication, subtraction etc by defining respective dunder methods
    def __sub__(self,other):
        return self.price - other.price
    def __add__(self,s):
        return self.name+" "+s.name
        
b1=book("python",200)
b2=book("oooo",500)
print(b1+b2)                   
print(b1.__add__(b2))          
print(b1.__add__(b2))      # All three will call most recent constructor which is 3rd one and give concatenated string as output b/c python #                            is dynamic typed language it does not support method overloading statically typed language do.

def m1():
    print("no argument")
    
def m1(a):
    print("one argument:",a)
    
def m1(a,b):
    print("two argument:",a,b)
    
# m1()      # This will give error b/c python does not support method overloading
# m1(10)    # This will give error b/c python does not support method overloading
m1(10,20)   # This will work and give output b/c this is the most recent defined method
