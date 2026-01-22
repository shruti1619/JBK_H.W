class book:
    def __init__(self,n,p):
        self.name=n
        self.price=p
        
    def __add__(self,other):
        return self.price + other.price     # we can also do multiplication, subtraction etc by defining respective dunder methods
    def __sub__(self,other):
        return self.price - other.price
    def __addstr__(self,s):
        return self.name+" "+s.name
        
b1=book("python",200)
b2=book("oooo",500)
print(b1+b2)                   # This will internally call __add__ method and will give error if not defined __add__ in class
print(b1.__add__(b2))          # This will internally call __add__ method still give error if not defined __add__ in class
print(b1 -b2)                   # This will internally call __sub__ method and will give error if not defined __sub__ in class
print(b1.__sub__(b2))          # This will internally call __sub__ method still give error if not defined __sub__ in class
print(b1.__addstr__(b2))       # This will internally call __addstr__ and give output as you wrote constructor logic
